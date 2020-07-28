#!/usr/bin/env python3
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License.

import os

""" Bot Configuration """


class DefaultConfig:
    """ Bot Configuration """

    PORT = 3978
    APP_ID = os.environ.get("MicrosoftAppId", "b608ddab-f544-469b-9422-49b705219183")
    APP_PASSWORD = os.environ.get("MicrosoftAppPassword", "-IrhN._E26Klp6sPh_7suUZX.PX0E1ahX3")
