# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License.

from typing import List
from botbuilder.core import CardFactory, TurnContext, MessageFactory
from botbuilder.core.teams import TeamsActivityHandler, TeamsInfo
from botbuilder.schema import CardAction, HeroCard, Mention, ConversationParameters
from botbuilder.schema.teams import TeamInfo, TeamsChannelAccount
from botbuilder.schema._connector_client_enums import ActionTypes

from .cognitive_services_pipeline import summarize
from .scraper import TranscriptionScraper

import webbrowser
import json

meetings_list = []
mentioned_members_list = []

class TeamsConversationBot(TeamsActivityHandler):

    def __init__(self, app_id: str, app_password: str):
        self._app_id = app_id
        self._app_password = app_password

    async def on_teams_members_added(  # pylint: disable=unused-argument
        self,
        teams_members_added: [TeamsChannelAccount],
        team_info: TeamInfo,
        turn_context: TurnContext,
    ):
        for member in teams_members_added:
            if member.id != turn_context.activity.recipient.id:
                await turn_context.send_activity(
                    f"Welcome to the team { member.given_name } { member.surname }. "
                )

    async def on_message_activity(self, turn_context: TurnContext):
        TurnContext.remove_recipient_mention(turn_context.activity)
        text = turn_context.activity.text.strip().lower()

        if "summarize" in text:
            await self._summarize(turn_context)
            return

        if "recording" in text:
            await self._openMeetingRecording(turn_context)
            return

        if "last" in text:
            await self._last_meeting(turn_context)
            return

        if "previous" in text:
            await self._previous_meeting(turn_context)
        
            
        

        #await self._send_card(turn_context, False)
        #return

    async def _mention_activity(self, turn_context: TurnContext):
        mention = Mention(
            mentioned=turn_context.activity.from_property,
            text=f"<at>{turn_context.activity.from_property.name}</at>",
            type="mention",
        )

        reply_activity = MessageFactory.text(f"Hello {mention.text}")
        reply_activity.entities = [Mention().deserialize(mention.serialize())]
        await turn_context.send_activity(reply_activity)


    async def _previous_meeting(self, turn_context: TurnContext):
        if (len(meetings_list) > 1): 
            GUID = meetings_list[-2]
            url_required = "https://msit.microsoftstream.com/video/" + GUID

            # TODO: Replace with function call that retrieves JSON
            # Call to retrieve meeting transcript
            #transcription_text = TranscriptionScraper.getMeetingJson(GUID)

            # # temporarily using fake sample file text
            # # read file
            file = open('bots/sample.txt', 'rb')
            transcription_text = file.read()
            
            # TODO: Replace with function call that runs Azure Cognitive API and Summary API
            # Call to Summary and analytics API
            summary_json = json.loads(summarize.summarize(transcription_text))
            file.close()
            await self._send_last_meeting_card(turn_context, url_required, summary_json, GUID)
        else: 
            message = "There was no recorded meetings before this..."
            reply_activity = MessageFactory.text(message)
            await turn_context.send_activity(reply_activity)

    async def _last_meeting(self, turn_context: TurnContext):
        if (len(meetings_list) > 0): 
            GUID = meetings_list[-1]
            url_required = "https://msit.microsoftstream.com/video/" + GUID

            # TODO: Replace with function call that retrieves JSON
            # Call to retrieve meeting transcript
            #transcription_text = TranscriptionScraper.getMeetingJson(GUID)

            # # temporarily using fake sample file text
            # # read file
            file = open('bots/sample.txt', 'rb')
            transcription_text = file.read()
            
            # TODO: Replace with function call that runs Azure Cognitive API and Summary API
            # Call to Summary and analytics API
            summary_json = json.loads(summarize.summarize(transcription_text))
            file.close()
            await self._send_last_meeting_card(turn_context, url_required, summary_json, GUID)

        else: 
            message = "No Past Meetings saved..."
            reply_activity = MessageFactory.text(message)
            await turn_context.send_activity(reply_activity)

    async def _summarize(self, turn_context: TurnContext):
        passed_message = turn_context.activity.text

        if(len(passed_message.split(" ")) == 3):
            url_required = passed_message.split(" ")[2]
            guid_start = url_required.find("video/") + 6
            #guid_end = url_required.find("?")
            GUID = url_required[guid_start:len(url_required)]
            GUID = GUID[:-1]
            # add to meetings list 
            meetings_list.append(GUID)

            # TODO: Replace with function call that retrieves JSON
            # Call to retrieve meeting transcript

            transcription_text = TranscriptionScraper.getMeetingJson(GUID)

            # # temporarily using fake sample file text
            # # read file
            #file = open('bots/sample.txt', 'rb')
            #transcription_text = file.read()
            
            # TODO: Replace with function call that runs Azure Cognitive API and Summary API
            # Call to Summary and analytics API
            summary_json = json.loads(summarize.summarize(transcription_text))
            #file.close()

            # Send summary card to chat
            await self._send_summary_card(turn_context, url_required, summary_json, GUID)

            # Personal Message members of the chat that were mentioned in the meeting
            await self._message_all_members(turn_context, str(transcription_text))

        else: 
            message = "Missing/Invalid Stream URL..."
            reply_activity = MessageFactory.text(message)
            await turn_context.send_activity(reply_activity)
        

    async def _openMeetingRecording(self, turn_context: TurnContext):
        message = "Recording opening..."
        url = turn_context.activity.value["meetingURL"]
        webbrowser.open(url, new=0)
        
        reply_activity = MessageFactory.text(message)
        await turn_context.send_activity(reply_activity)

    async def _send_last_meeting_card(self, turn_context: TurnContext, meeting_url, summary_json, GUID):
        buttons = [
            CardAction(
                type=ActionTypes.message_back, 
                title="See Meeting Recording",
                text="recording", 
                value={"meetingURL": meeting_url}
            )
        ]
        card = HeroCard(
            title="Summary of this Meeting: " + GUID, subtitle= "Meeting Sentiment" + str(summary_json["sentiment"]),text = summary_json["summary_text"], buttons = buttons
        )
        await turn_context.send_activity(
            MessageFactory.attachment(CardFactory.hero_card(card))
        )


    async def _send_summary_card(self, turn_context: TurnContext, meeting_url, summary_json, GUID):
        buttons = [
            CardAction(
                type=ActionTypes.message_back,
                title="Get Previous Meeting Info",
                text="previous",
            ),
            CardAction(
                type=ActionTypes.message_back, 
                title="See This Recording",
                text="recording", 
                value={"meetingURL": meeting_url}
            )
        ]
        card = HeroCard(
            title="Summary of this Meeting: " + GUID, subtitle= "Meeting Sentiment: " + str(summary_json["sentiment"]),text = summary_json["summary_text"], buttons = buttons
        )
        await turn_context.send_activity(
            MessageFactory.attachment(CardFactory.hero_card(card))
        )

    async def _get_member(self, turn_context: TurnContext):
        TeamsChannelAccount: member = None
        try:
            member = await TeamsInfo.get_member(
                turn_context, turn_context.activity.from_property.id
            )
        except Exception as e:
            if "MemberNotFoundInConversation" in e.args[0]:
                await turn_context.send_activity("Member not found.")
            else:
                raise
        else:
            await turn_context.send_activity(f"You are: {member.name}")

    async def _message_all_members(self, turn_context: TurnContext, transcription_text):
        team_members = await self._get_paged_members(turn_context)

        for member in team_members:
            # check if member's name was mentioned in meeting
            member_first_name = member.name.split(" ")[0]
            

            if transcription_text.lower().find(member_first_name.lower()) != -1:
                mentioned_members_list.append(member_first_name)

                # split text into words. Remove punctuation to prevent mistakes in indexing 
                transcription_text = transcription_text.replace(",","")
                transcription_text = transcription_text.replace(".","")
                transcription_text = transcription_text.replace("\\r"," ")
                transcription_text = transcription_text.replace("\\n","")

                transcription_list = transcription_text.lower().split(" ")
                
                # find name placement in transcription list 
                indexFound = transcription_list.index(member_first_name.lower())

                # get range of words around name to get context and form message
                context_threshold_range = 10
                context_message = ""
                
                # compose message with context
                for word in range (indexFound - context_threshold_range, indexFound + context_threshold_range):
                    context_message += transcription_list[word] + " "

                conversation_reference = TurnContext.get_conversation_reference(
                    turn_context.activity
                )

                conversation_parameters = ConversationParameters(
                    is_group=False,
                    bot=turn_context.activity.recipient,
                    members=[member],
                    tenant_id=turn_context.activity.conversation.tenant_id,
                )

                async def get_ref(tc1):
                    conversation_reference_inner = TurnContext.get_conversation_reference(
                        tc1.activity
                    )
                    return await tc1.adapter.continue_conversation(
                        conversation_reference_inner, send_message, self._app_id
                    )

                    

                async def send_message(tc2: TurnContext):
                    return await tc2.send_activity(
                        "Hi you were mentioned in the meeting. Here's some context: " + context_message
                    )  # pylint: disable=cell-var-from-loop

                await turn_context.adapter.create_conversation(
                    conversation_reference, get_ref, conversation_parameters
                )
        mentioned_members = ','.join(mentioned_members_list)

        await turn_context.send_activity(
            MessageFactory.text("All members who's names were mentioned in the meeting were notified with context: " + mentioned_members)
        )
        mentioned_members_list.clear()

    async def _get_paged_members(
        self, turn_context: TurnContext
    ) -> List[TeamsChannelAccount]:
        paged_members = []
        continuation_token = None

        while True:
            current_page = await TeamsInfo.get_paged_members(
                turn_context, continuation_token, 100
            )
            continuation_token = current_page.continuation_token
            paged_members.extend(current_page.members)

            if continuation_token is None:
                break

        return paged_members
