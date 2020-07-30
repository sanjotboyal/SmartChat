import json
import requests

def getMeetingJson(guid):
    url = "https://use2-2.api.microsoftstream.com/api/videos/" + guid + "/events?$filter=Type%20eq%20%27transcript%27&api-version=1.4-private&hostcorrelationid=undefined"
    headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.89 Safari/537.36 Edg/84.0.522.48',
    'cookie':'Authorization=eyJUb2tlbiI6IkpoYTFaT2VQZ1J3TTdEdGkxR2Vwb202Ukp4NE43ZEQ2MGVRaWFSNHhhdXluMVU1VkUzU1dlczRWWHhtTjBWVE1qdUFZZmxiclRHVTlRaFdrVlA5bm5KV0tzanBYMFBMV3FJenFkNGppTFhMemNBMmJraWtUTnJ5WGk4cE5zN0svT2JWZHFGbUdZQ2pGL05pbm8rZC81MnA4SFZyMzE4Q04vUGpXUHpzWXptbzJUK1VMdUhVNGk3d3R1Y1ZEbkdBTVdYcCs1ZTg5NEYvTzhVQWFpeE1zVWVuQ1RaUWtuZjFpUTFrVFV1cVdYdnNkMVZwbTJKTlkwbDh3c3gxWnh4Zk5MNnNDMldiTy9YNE45NnpGdjFTVW1WWlNMTU1kWXFlZFUwTXhvWk04b1htbXAxM3VQU2tqQW5Wd2lXekE1NitvMExkc2xralZsTS9XQk55TFJ1cTlJM1pnSlpQaEZOM1BFK3VQYjJwTlhGVmZ4V2x4Vk5BSzhaUm80UkFEeERMakI4OEtjaGNXMUdzWjlORCt5UmwxM0E3c3h1QWdEUk5haDdzTFV6RHVRV3JaTTJQY1g3MHUweUFaK293WkZqeXZwaWpNVEplVUVkMVk0aWtPVlMvL1lSNHNkUnVBZDlaTjhML0tYVm1HV0hKZlgxeGp0V3l5K05qVGRuMTUyLzMzVnpuVVFDR2l2R1V3S00zZzFoT2svMjZwTHFIV1dvdnpyUUZSUjM3bGJ2WjVWdnN0V0MzMkNkRGs1SlZEU1B2TWhtVVR3OTRFeEtYb1BUNVA4V2YzYUY2NmllZlRrL0ExMmxMdU1vcjdmRWZnNzdCQ3Y2KzhhSVRZV2k2VnhRUkI2QWtSR2Q3YkNhUWFwK1BmSlcvZjdjSGgzMmozNkxMRU5wZFF3WkJkL0ozd3h5d0VLLzI1UkpxRENaNnhzZEMxbXA5dzdQZC9nZGNVdDRkMXhVY1NiTE41cWh0NGNhcWhNQ1BJSE9qM1BhNENQMVhvQUZaVzFpVnhCbUpTMHU4bmMwbXg3NnpWVzRvcHN1L1prT29zcUlkY2NuZUc5MHd0cHdTZzlmM280Tmx6QkZlMWxhLzIzSDN2VmdKVmRObUhjZmdaMWMvY3YvV2MvbzFpVm9tM1lMRWJOL0NkdXAxeDZiMkczRXRFbERLdndiWkRsSUF5VFlLUENxQkRhd3BkaFQ5MVdOYzRuK0d1NzJjaFFBOGhETjk5S05vRlgwbmx3M0NUMERVRkhMZjY3RmIyNlJwcGF3Tjg4U2JBOG5rUWQzQkdMYnlZbk9DNTFOR3E0OTVSbzIrQWk5QytuTDJLQ1R2M25CUS9tZFpoWEZTTXJQZHV1ZEpGOGFac3BtMndFSUdraWplVG40dGhpQU1INGNHd1JISk1obzFhVk82M250bzdZRUliRE16VTB0elV2WkRSYk96QkhIU2ZiRFdZdmltQnhkanpTTk4vbFc3eFd1TEpWTlJ2cWtCVTFZY2JaOTlFNXZ3UFFKS2EzQStia3YwRGRRT0FXMWxaNzh0VUV1TlhDMHg1eXo3em1VMXRsRFF2TVo5UFZpNmFRWkVHUDAvU2xpT1hpWDJXSW5jNFpnclBsYU9ORjNkYWxtZ0FYUmtWRUgxQlhxSmhMK2RnZmJUL2ZqdjZUMDhOWS82TnVDVER5M0swdG9ZajIvUEh0bVI2YzcwZytzWVJZcG9ZUzl0MFY5OUhQWTBnMzBTTGJBRkFZeE12MmhGZnlzbmtXNklUVG9yaVFzelozOUkzZ3VEbU9WL0tKY2hOcE9JREUvVWVGa3RMOTVKcmZQWTZCelJXaG44Tkk0dG5wN3FYYnZxYkZIN1FWSjNRZDhUK2ZWdWZoTS9wOHFwcnI3TG1kTHZXVURPbVdRUHpQZ3FYTDVxZjRvNk1oZ2t5WFpNZjVkL09YaWdwL3JZUlJhY25PZzZZMit2L05tVTkzeHZPWXRIVUtmSkpQUVpQbXIvTVBPam9ibGpRUG56QTNWcHU1QTR2OEVwcEpJQmIvc3dPUTVmRE1nQ2VpOHIwRE1USUlhcVBWa3Zkemw0UDVGTmNOZENjTnFSYUhyZjJtNkZZZE91MmdJZkQrZTJEVG0rSlJ6L2xUUVdBakhOTi83b1ladVZmQWxQVWppakJWUlZZOE9GWi8yRFVNMXNwM1pDeGxpKzJ5bWh3a0JMei9QOEY1ME5rYTFseXZhbzlDZm8xTEo5T1NhRW51V1N0eWdPZFJJMi9wT0JlSnM4aVFFcCtJcFdIakliNXhkYVNoWlgrYkVVdzdvNCtiZHhNRFEzNzZ5UkY5YXg1WHY5VzRWVkVyVWNPQi9scnhPdWVJMlpka0lNYjU1WFoxSSszQ1hrRFh1WlhiQTNtd3E3ejRZamVYdEdpN1ZIbk02em9wbkVraExVb2RUNnc4a2JGa2FiYXZoamNEdTh3eCs2RWtGMTZHejV2ZW9pN1NRNWNkZ3ZBcGd0ODBtMXJwd05UWXppS2xpQXJLQXpIcXp2eDhoZE5vMzExM21zOW1CY1ErMDZrY25pUzRhNkZKa0lXN1hPNTVNQU8yZm0vdC96RnF5ZWJIcXd6TEQ0SGtGNjFUY1FKMVNLQlZDTWdxOC9QcmI1SHd2MlpDVjNDZDRwRVhsbTBQeWpubFBQcXdqYTRTR3FHdTJBaytBbXdzZjI5dzRGN3ZVNmxhZmhGYW9ZTUxEbEJKeEdiWGdBMWNUdTBEMVczRVFkTkhYMW5xclZsWE85UGtXdG05dW5ZT1pmUnlKUXRDb2M3dDNJM2p0WjN2bitvNG1SL0NjYytsZElXbkorVDRMQU80eGdwQWxoMkhNUmVIaHRNRHloWTBILytuNFBoOUkwNUNrb1IzSVFnN0cxUG5tWlYyV210RmEvZFZMdlBwQk9nVkM4bjhoR3FWQVJ4ZzhMSTBXVHAzcVR2NmZUeXR6QkwxNnFKeWYycmNHOEZZUVF1L3lmSDBXMHRyeEduSWN3S25QR2U3TmcrWE8wT3pnK2I1Wnlhb21ZVWtJeXp1WmFhc3BGaGpOYzZIL2NjbFA1UEl1VnRyc3pRU09lWmFRV0gzdFhYUkZqS0JWVFVqb0VVVFl4NmpIV3c4akFLQ2V0N2ZHMThsZ0k9IiwiVG9rZW5TaWduYXR1cmUiOiJQZXhQeDhvdHkzQUtrT1M1Q2lVRk5WSW1QQUpNSUVXckd2MkF6ZjU4UjRBPSIsIkVuY3J5cHRpb25JdiI6IkhleTQ0c1k2NmpCay8weFEyTEUvc0E9PSIsIkVuY3J5cHRpb25LZXlTaWduYXR1cmUiOiJ5Z2VmZXlKYkhZUWxLMnJlbTZ6a1cwc2xLUFZhaU9YZisvRTk1NnBBczhjPSJ9; Signature=6wguihf6az%252beykkYoGfo2JWfxYUs163FnORKYItqH8o%253d; Authorization_Api=eyJUb2tlbiI6IkpoYTFaT2VQZ1J3TTdEdGkxR2Vwb202Ukp4NE43ZEQ2MGVRaWFSNHhhdXluMVU1VkUzU1dlczRWWHhtTjBWVE1qdUFZZmxiclRHVTlRaFdrVlA5bm5KV0tzanBYMFBMV3FJenFkNGppTFhMemNBMmJraWtUTnJ5WGk4cE5zN0svT2JWZHFGbUdZQ2pGL05pbm8rZC81MnA4SFZyMzE4Q04vUGpXUHpzWXptbzJUK1VMdUhVNGk3d3R1Y1ZEbkdBTVdYcCs1ZTg5NEYvTzhVQWFpeE1zVWVuQ1RaUWtuZjFpUTFrVFV1cVdYdnNkMVZwbTJKTlkwbDh3c3gxWnh4Zk5MNnNDMldiTy9YNE45NnpGdjFTVW1WWlNMTU1kWXFlZFUwTXhvWk04b1htbXAxM3VQU2tqQW5Wd2lXekE1NitvMExkc2xralZsTS9XQk55TFJ1cTlJM1pnSlpQaEZOM1BFK3VQYjJwTlhGVmZ4V2x4Vk5BSzhaUm80UkFEeERMakI4OEtjaGNXMUdzWjlORCt5UmwxM0E3c3h1QWdEUk5haDdzTFV6RHVRV3JaTTJQY1g3MHUweUFaK293WkZqeXZwaWpNVEplVUVkMVk0aWtPVlMvL1lSNHNkUnVBZDlaTjhML0tYVm1HV0hKZlgxeGp0V3l5K05qVGRuMTUyLzMzVnpuVVFDR2l2R1V3S00zZzFoT2svMjZwTHFIV1dvdnpyUUZSUjM3bGJ2WjVWdnN0V0MzMkNkRGs1SlZEU1B2TWhtVVR3OTRFeEtYb1BUNVA4V2YzYUY2NmllZlRrL0ExMmxMdU1vcjdmRWZnNzdCQ3Y2KzhhSVRZV2k2VnhRUkI2QWtSR2Q3YkNhUWFwK1BmSlcvZjdjSGgzMmozNkxMRU5wZFF3WkJkL0ozd3h5d0VLLzI1UkpxRENaNnhzZEMxbXA5dzdQZC9nZGNVdDRkMXhVY1NiTE41cWh0NGNhcWhNQ1BJSE9qM1BhNENQMVhvQUZaVzFpVnhCbUpTMHU4bmMwbXg3NnpWVzRvcHN1L1prT29zcUlkY2NuZUc5MHd0cHdTZzlmM280Tmx6QkZlMWxhLzIzSDN2VmdKVmRObUhjZmdaMWMvY3YvV2MvbzFpVm9tM1lMRWJOL0NkdXAxeDZiMkczRXRFbERLdndiWkRsSUF5VFlLUENxQkRhd3BkaFQ5MVdOYzRuK0d1NzJjaFFBOGhETjk5S05vRlgwbmx3M0NUMERVRkhMZjY3RmIyNlJwcGF3Tjg4U2JBOG5rUWQzQkdMYnlZbk9DNTFOR3E0OTVSbzIrQWk5QytuTDJLQ1R2M25CUS9tZFpoWEZTTXJQZHV1ZEpGOGFac3BtMndFSUdraWplVG40dGhpQU1INGNHd1JISk1obzFhVk82M250bzdZRUliRE16VTB0elV2WkRSYk96QkhIU2ZiRFdZdmltQnhkanpTTk4vbFc3eFd1TEpWTlJ2cWtCVTFZY2JaOTlFNXZ3UFFKS2EzQStia3YwRGRRT0FXMWxaNzh0VUV1TlhDMHg1eXo3em1VMXRsRFF2TVo5UFZpNmFRWkVHUDAvU2xpT1hpWDJXSW5jNFpnclBsYU9ORjNkYWxtZ0FYUmtWRUgxQlhxSmhMK2RnZmJUL2ZqdjZUMDhOWS82TnVDVER5M0swdG9ZajIvUEh0bVI2YzcwZytzWVJZcG9ZUzl0MFY5OUhQWTBnMzBTTGJBRkFZeE12MmhGZnlzbmtXNklUVG9yaVFzelozOUkzZ3VEbU9WL0tKY2hOcE9JREUvVWVGa3RMOTVKcmZQWTZCelJXaG44Tkk0dG5wN3FYYnZxYkZIN1FWSjNRZDhUK2ZWdWZoTS9wOHFwcnI3TG1kTHZXVURPbVdRUHpQZ3FYTDVxZjRvNk1oZ2t5WFpNZjVkL09YaWdwL3JZUlJhY25PZzZZMit2L05tVTkzeHZPWXRIVUtmSkpQUVpQbXIvTVBPam9ibGpRUG56QTNWcHU1QTR2OEVwcEpJQmIvc3dPUTVmRE1nQ2VpOHIwRE1USUlhcVBWa3Zkemw0UDVGTmNOZENjTnFSYUhyZjJtNkZZZE91MmdJZkQrZTJEVG0rSlJ6L2xUUVdBakhOTi83b1ladVZmQWxQVWppakJWUlZZOE9GWi8yRFVNMXNwM1pDeGxpKzJ5bWh3a0JMei9QOEY1ME5rYTFseXZhbzlDZm8xTEo5T1NhRW51V1N0eWdPZFJJMi9wT0JlSnM4aVFFcCtJcFdIakliNXhkYVNoWlgrYkVVdzdvNCtiZHhNRFEzNzZ5UkY5YXg1WHY5VzRWVkVyVWNPQi9scnhPdWVJMlpka0lNYjU1WFoxSSszQ1hrRFh1WlhiQTNtd3E3ejRZamVYdEdpN1ZIbk02em9wbkVraExVb2RUNnc4a2JGa2FiYXZoamNEdTh3eCs2RWtGMTZHejV2ZW9pN1NRNWNkZ3ZBcGd0ODBtMXJwd05UWXppS2xpQXJLQXpIcXp2eDhoZE5vMzExM21zOW1CY1ErMDZrY25pUzRhNkZKa0lXN1hPNTVNQU8yZm0vdC96RnF5ZWJIcXd6TEQ0SGtGNjFUY1FKMVNLQlZDTWdxOC9QcmI1SHd2MlpDVjNDZDRwRVhsbTBQeWpubFBQcXdqYTRTR3FHdTJBaytBbXdzZjI5dzRGN3ZVNmxhZmhGYW9ZTUxEbEJKeEdiWGdBMWNUdTBEMVczRVFkTkhYMW5xclZsWE85UGtXdG05dW5ZT1pmUnlKUXRDb2M3dDNJM2p0WjN2bitvNG1SL0NjYytsZElXbkorVDRMQU80eGdwQWxoMkhNUmVIaHRNRHloWTBILytuNFBoOUkwNUNrb1IzSVFnN0cxUG5tWlYyV210RmEvZFZMdlBwQk9nVkM4bjhoR3FWQVJ4ZzhMSTBXVHAzcVR2NmZUeXR6QkwxNnFKeWYycmNHOEZZUVF1L3lmSDBXMHRyeEduSWN3S25QR2U3TmcrWE8wT3pnK2I1Wnlhb21ZVWtJeXp1WmFhc3BGaGpOYzZIL2NjbFA1UEl1VnRyc3pRU09lWmFRV0gzdFhYUkZqS0JWVFVqb0VVVFl4NmpIV3c4akFLQ2V0N2ZHMThsZ0k9IiwiVG9rZW5TaWduYXR1cmUiOiJQZXhQeDhvdHkzQUtrT1M1Q2lVRk5WSW1QQUpNSUVXckd2MkF6ZjU4UjRBPSIsIkVuY3J5cHRpb25JdiI6IkhleTQ0c1k2NmpCay8weFEyTEUvc0E9PSIsIkVuY3J5cHRpb25LZXlTaWduYXR1cmUiOiJ5Z2VmZXlKYkhZUWxLMnJlbTZ6a1cwc2xLUFZhaU9YZisvRTk1NnBBczhjPSJ9; Signature_Api=6wguihf6az%252beykkYoGfo2JWfxYUs163FnORKYItqH8o%253d; UserSession_Api=signature=aUpO0HNYJH8gXxwIGiCmye7ZozNLYfpUJZgcEOVINx0&payload=eyJFbmNyeXB0ZWRQYXlsb2FkIjoiUThyTllkRWp3NCtCUldxNFFvVS8yZXhJNzlTMEdCWjdKb1BRbWJiSnhCcWxCYTdDL2RlWEFtRFY3ZnVPSHdZWGRRa0w0S0tmYzQweTV3WDFBVy9Vd000aTQ1dVpnd0FnRy9PTUNCRTlxQ3lGV0kzbHAvK29CUnI3S0pyOGxSa2VWc2hxSkhUejVOdVRpZmlHTzJDZU1VQkhPaFIzMGJOU1IxTXU4dVVHSUFJZUNFdk9NemZPOTFMRFFDd0tyU2pIVmtodXRuZVlMWDkrZGE3eElSdU51RTFkS2RrZ2hvY0cxQ25nZmswdU1IZTBpNWI3S0tDNTBKeTZwVTl1dWx4TEkzdHZLdzg4S2lIc0E4bE5mWVg5OTEzaElRQjZ6N3dsWkdNbUN6WUVxTjdxQ0NycjR5ZnpEK1dXRVd1Mit0bm04SlJSaXVQbkdCTVdyM1YzN2R6OUZBPT0iLCJFbmNyeXB0aW9uS2V5SGFzaCI6InlnZWZleUpiSFlRbEsycmVtNnprVzBzbEtQVmFpT1hmKy9FOTU2cEFzOGM9IiwiRW5jcnlwdGlvbktleUhhc2hDb2RlIjoxMjExNzY4MTMzLCJFbmNyeXB0aW9uSXYiOiJFYzJyQ0NJaEhZRWZVcXMwVUtVWFRBPT0ifQ',
    "sec-fetch-site":"none",
    "sec-fetch-mode":"navigate",
    "sec-fetch-user":"?1",
    "sec-fetch-dest":"document",
    "accept-language":"en-US,en;q=0.9",
    "authority":"use2-2.api.microsoftstream.com",
    "cache-control":"max-age=0",
    "upgrade-insecure-requests":"1",
    "accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
    }
    request = requests.get(url, headers=headers)
    #print(request)
    jsonContent = json.loads(request.text)
    textDump = ""
    for item in jsonContent["value"]:
       #print(item)
        textDump = textDump + " " + item['eventData']["text"]
    #print(textDump)
    return textDump
 
# if __name__ == "__main__":
#     getMeetingJson("af32a4ff-0400-a521-b057-f1ead038da96")