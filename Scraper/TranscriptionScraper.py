import json
import requests

def getMeetingJson(guid):
    url = "https://use2-2.api.microsoftstream.com/api/videos/" + guid+"/events?$filter=Type%20eq%20%27transcript%27&api-version=1.4-private&hostcorrelationid=undefined"
    headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.89 Safari/537.36 Edg/84.0.522.48',
    'cookie':'Authorization=eyJUb2tlbiI6IkFHS3MyVkhBRFJKYW9wUGZKTVVVSFlubG15U0daSGM3cHVHbWRSUTFqRlRwWldSeFZ1dlJUVkNibzZsUkQ3ZFZGb1pZTjdpSFJycVJpcCtkWEJhbjBvR1JFK3RmTVNNVnhXSk40U1Z0RlJDME1NL2w4NlpKRjFQRzB3ZnEvYlk3eXIyOC9IU0FiNVkzUWk0V1R1Yjl6eERYVFFLc1NWaDFYcW1xZnMvOFQ0VHB5VExVRmxHTUxwMXBscjZETTNxNW91QzlCZ2ZLYmRrRFRSVEVDTEVzVnh1eXNZYjFvV1RLVm81LytIRm43QWw4b2ZDOHFTV3FFdnc3ZFBuc1VlUE8xK3QvRW02S1Vrbzk5MVFidkRnMVpEb0lINlB0ekgydU03MnVGeEp1a3dpUTIxdHhvb0h1a01XMDhZeVVEUE1DY25BOFFkR0NZVDJaL3ZNdDEya3hQZndRNmIwYkZmL29ZdWN1WVhCa2Y2dVVReWNYb2VLNWU3OVdBM0UvVXdCWTJwWkh5eXBud29vdWRZZzB3b3hKZ2lXVFNSTjFQWFpib2crdVR6bmVUd2JHQjZpa0xHZUk0dXg3YzJVRURFUXorNDZzUTQ2SmljWWNhRTVidTNBQldNVUVaS2N1bE9FSjJ4S1NRQldBYzBTWDBIbyt3bXZoYkhsV3hUazcxVk5QUGk5bFFybWlCQ0VHb2xUWjV2TU16YVJFRndxZ3FOMy9XNlRTTHVoQUFIYUxUOG1CTTVuOHFOb1B4TDR2L0pPM1ZGMFh1SUxYaUtPS05SSHJvMzBGeFc0SlJGWGhSNDUrQkdjTkJpZjRqVEM4UVlUVTE0bkE0a0g3N1lSQkNTemxubWlJS012Snk4NnVhZjNWRG5FemdtOWZObkxuV0ZVTjZIMWdlbTlWS25HSDByV1ZLZEJDcVp0dytKdTYxYU5MWVY2QWpkSWNxR29PL0syTTVpeXZlY253aXErTGFRM05SN0xhTjlLaGR3cVV6MURHK0JseEozZGRzWW9JTTFPS05zaHRxUjdzUm5KUmg1Q3hFUHl6cnY0VHNKL0pTL2svQ1RiVjluZWRFMHhJSFpZbGxEM3ozYkE2NDdBMnE0dTlOcVBaTzdnSnBiRWdiek1tNS80R1NSZU9iQ3ZkNVQ1NGFYQlR5YXRRV2JFTm9hTkl6VmNselhxa3gwV3c5ejhrNiszRStkdk5tenUrejJBS053MXJBeHpMbHc5TklBV25nM2Y0dTFMNlBoNktjK2pPME9Pd0pFQ0xuU2F2bDMvaUFlRWVnTlhKMEVvRjl3ZFhaNjNlclAzQ0hpUlhnWE44czRoS21Mdnh6Y3BmTFFwTEJZa09OUmE1cTdPb0ZFL05SKzVBVTZmWDJWcXdMZWhmSktVTEZoY2FqTGFUZUh6Y0o2c1FUR3JOeTh6T2xkQ241QmFjU3NQK1J5b1ByRlhQRVhxSTlhRWhzSzNYemdyM1VNbzROc0M2QkpERmdnNlB6dHZVenZXbnh2dHdEUGZkVnR0RjhqbStIYTlqU1RkUkx0YlBDaUM3cWFLbzBsZnQxM1FEelRWaUhZYi9STU9jS1ZYT3NQQ2pvTzhjQUF2cVdjR3pFQlFka012NXJvNnhrdE9hL0t4eFZnWHg3VFptTWhJb0gydUZJakZ5Q3FBc0lobW10eTYxNjlUNmtiSmZSQWdMc2xKcWVvMmI1VmVndTdyRXFobmV0Y1o2blRGT1hPekNyY1NzcmlyckFkdEtScXMvOVNaKzMycCtKcnp0c25EVkFrMDRVbHRqWlhTZFVTbk1zYVpRK2hWaDlMSEgzN1NDN0NlUFcwZndFWWdSVGcrUFlSaHozeVJXOGVYODV1ckh4bHF0MWRBQmNWVlNsbGZvNHh4UktseEF4Y2JDNDNYV3pUMjFZbU1YeCtsSkM3ODUzenRWenNucFQ4S2Fha3BjNUJhVGgvVXo5ZTBWNVprZnZvSHRwL0hlK0RaN1FpNjhXOUx6akE3RnMrWWk0elYxbFlrTlZaSHBsdHBOYmVDR1pMTTJSWEV5TEUvcnhZMm0zRnFKYjM2RmlOVFBzTktheWtWYlhJbzBLdXJnS1JUS2tOaGUxY3h5Y1pLeDl0QVJRMVNuQjFLeTJ6N2M0bTh3VFFXSkJuRTZKK1JLdG1OdVFYdWZFM09UenZkNE1tczFOQ2JudE5ybFJwUTNLRll1clJkbFFIYjQzSlZzSU13V004cXo2Z0pGa0QvU0FMdjhSSXJGT2xOYStTWGlMRVpoVEkzQnRvR3FDZnRVbkY5bzdYb3BabFJlRDE0Z1QvVUE2Mll2Rm55aUxNMVVWYkpueDZ6a2VQK0kwcS8rbnZtSytHN1ZWTGRUd0N4NDlFNDBwYllNWFNEdlVxTVhyclNXZkw2MENEQTA5ZjRFaEQ5cHVzVk1vVCs1b3RRY3lTZHJiTUpXWE9XUVN1Yzk2WE5MSzJJb3hNNW1hQm1ueVk2dGRhbWY5YzdPaXQxNzl5anpTZ2RnSVZRVHVRem9rQlgwOU01ZXRIZm9zb09mUndSZEhOV3lQSjRWOHVPamdwangwUTFXeWVyTTBoZTBoMUxlbklGV2F6OHNvcC9NN05WL1pmbi9ZMlpzYmZrOUZvQW1RL2xxVlFhRHFIVDRtOHFRbXFETENmUHM0Y3dQc3BmNW5UT0FiTi9kSUJUdU9YU1hIeGMyTE4xVUFkWkpmSFBmTDVLZlJpZE05enVXSmZ2Rktrb0lWUUh3cHc5ZnRvaGZibkdsNzRzWGJ0WEwxWUJFOVRTVFhYMFVCMmtmbEgwL2l0MzVjRzRKbHJNYklmeHdFVERzV1FyZERpZW5Hdyszc09STXRQNGZodWpoMk8yU1lYMDM3a01nVlY5Q2tIZnBTQWI4OTcrb0hXdHFoWWhmM3diRDVzWk4wTFlSZkRiRkdHTUV0QVA5OGNHeG1LYktXbmdHajhuYTVpZVpzTnJUeFcxeG1UL3BleVhZM090T3lSVXl4V3ZRVmNlWnhUUkNVQUpjREZJN2N4MGQ5UXhadDBpeUVkcVJvMXMrWldMOG5jNTRSc0NkYk03QlpqWi9ENEcyaGhNY2l0cHpaeXA2Ui94eTVnWUpjdDZNRW1rQmxzcndTS3M9IiwiVG9rZW5TaWduYXR1cmUiOiJZOUhybUJjRnZDM0lUbUxiZ2F6aW55WUNITGVCTDV0WklpajgrUHFRY3hvPSIsIkVuY3J5cHRpb25JdiI6IlIwTFdzNEdwbmYrdEl6dUJLMXdwNEE9PSIsIkVuY3J5cHRpb25LZXlTaWduYXR1cmUiOiJ5Z2VmZXlKYkhZUWxLMnJlbTZ6a1cwc2xLUFZhaU9YZisvRTk1NnBBczhjPSJ9; Signature=PhX6OyiuW0C01OebvGcN0ii1fHXfbLpNpA15FNeNAeY%253d; Authorization_Api=eyJUb2tlbiI6IkFHS3MyVkhBRFJKYW9wUGZKTVVVSFlubG15U0daSGM3cHVHbWRSUTFqRlRwWldSeFZ1dlJUVkNibzZsUkQ3ZFZGb1pZTjdpSFJycVJpcCtkWEJhbjBvR1JFK3RmTVNNVnhXSk40U1Z0RlJDME1NL2w4NlpKRjFQRzB3ZnEvYlk3eXIyOC9IU0FiNVkzUWk0V1R1Yjl6eERYVFFLc1NWaDFYcW1xZnMvOFQ0VHB5VExVRmxHTUxwMXBscjZETTNxNW91QzlCZ2ZLYmRrRFRSVEVDTEVzVnh1eXNZYjFvV1RLVm81LytIRm43QWw4b2ZDOHFTV3FFdnc3ZFBuc1VlUE8xK3QvRW02S1Vrbzk5MVFidkRnMVpEb0lINlB0ekgydU03MnVGeEp1a3dpUTIxdHhvb0h1a01XMDhZeVVEUE1DY25BOFFkR0NZVDJaL3ZNdDEya3hQZndRNmIwYkZmL29ZdWN1WVhCa2Y2dVVReWNYb2VLNWU3OVdBM0UvVXdCWTJwWkh5eXBud29vdWRZZzB3b3hKZ2lXVFNSTjFQWFpib2crdVR6bmVUd2JHQjZpa0xHZUk0dXg3YzJVRURFUXorNDZzUTQ2SmljWWNhRTVidTNBQldNVUVaS2N1bE9FSjJ4S1NRQldBYzBTWDBIbyt3bXZoYkhsV3hUazcxVk5QUGk5bFFybWlCQ0VHb2xUWjV2TU16YVJFRndxZ3FOMy9XNlRTTHVoQUFIYUxUOG1CTTVuOHFOb1B4TDR2L0pPM1ZGMFh1SUxYaUtPS05SSHJvMzBGeFc0SlJGWGhSNDUrQkdjTkJpZjRqVEM4UVlUVTE0bkE0a0g3N1lSQkNTemxubWlJS012Snk4NnVhZjNWRG5FemdtOWZObkxuV0ZVTjZIMWdlbTlWS25HSDByV1ZLZEJDcVp0dytKdTYxYU5MWVY2QWpkSWNxR29PL0syTTVpeXZlY253aXErTGFRM05SN0xhTjlLaGR3cVV6MURHK0JseEozZGRzWW9JTTFPS05zaHRxUjdzUm5KUmg1Q3hFUHl6cnY0VHNKL0pTL2svQ1RiVjluZWRFMHhJSFpZbGxEM3ozYkE2NDdBMnE0dTlOcVBaTzdnSnBiRWdiek1tNS80R1NSZU9iQ3ZkNVQ1NGFYQlR5YXRRV2JFTm9hTkl6VmNselhxa3gwV3c5ejhrNiszRStkdk5tenUrejJBS053MXJBeHpMbHc5TklBV25nM2Y0dTFMNlBoNktjK2pPME9Pd0pFQ0xuU2F2bDMvaUFlRWVnTlhKMEVvRjl3ZFhaNjNlclAzQ0hpUlhnWE44czRoS21Mdnh6Y3BmTFFwTEJZa09OUmE1cTdPb0ZFL05SKzVBVTZmWDJWcXdMZWhmSktVTEZoY2FqTGFUZUh6Y0o2c1FUR3JOeTh6T2xkQ241QmFjU3NQK1J5b1ByRlhQRVhxSTlhRWhzSzNYemdyM1VNbzROc0M2QkpERmdnNlB6dHZVenZXbnh2dHdEUGZkVnR0RjhqbStIYTlqU1RkUkx0YlBDaUM3cWFLbzBsZnQxM1FEelRWaUhZYi9STU9jS1ZYT3NQQ2pvTzhjQUF2cVdjR3pFQlFka012NXJvNnhrdE9hL0t4eFZnWHg3VFptTWhJb0gydUZJakZ5Q3FBc0lobW10eTYxNjlUNmtiSmZSQWdMc2xKcWVvMmI1VmVndTdyRXFobmV0Y1o2blRGT1hPekNyY1NzcmlyckFkdEtScXMvOVNaKzMycCtKcnp0c25EVkFrMDRVbHRqWlhTZFVTbk1zYVpRK2hWaDlMSEgzN1NDN0NlUFcwZndFWWdSVGcrUFlSaHozeVJXOGVYODV1ckh4bHF0MWRBQmNWVlNsbGZvNHh4UktseEF4Y2JDNDNYV3pUMjFZbU1YeCtsSkM3ODUzenRWenNucFQ4S2Fha3BjNUJhVGgvVXo5ZTBWNVprZnZvSHRwL0hlK0RaN1FpNjhXOUx6akE3RnMrWWk0elYxbFlrTlZaSHBsdHBOYmVDR1pMTTJSWEV5TEUvcnhZMm0zRnFKYjM2RmlOVFBzTktheWtWYlhJbzBLdXJnS1JUS2tOaGUxY3h5Y1pLeDl0QVJRMVNuQjFLeTJ6N2M0bTh3VFFXSkJuRTZKK1JLdG1OdVFYdWZFM09UenZkNE1tczFOQ2JudE5ybFJwUTNLRll1clJkbFFIYjQzSlZzSU13V004cXo2Z0pGa0QvU0FMdjhSSXJGT2xOYStTWGlMRVpoVEkzQnRvR3FDZnRVbkY5bzdYb3BabFJlRDE0Z1QvVUE2Mll2Rm55aUxNMVVWYkpueDZ6a2VQK0kwcS8rbnZtSytHN1ZWTGRUd0N4NDlFNDBwYllNWFNEdlVxTVhyclNXZkw2MENEQTA5ZjRFaEQ5cHVzVk1vVCs1b3RRY3lTZHJiTUpXWE9XUVN1Yzk2WE5MSzJJb3hNNW1hQm1ueVk2dGRhbWY5YzdPaXQxNzl5anpTZ2RnSVZRVHVRem9rQlgwOU01ZXRIZm9zb09mUndSZEhOV3lQSjRWOHVPamdwangwUTFXeWVyTTBoZTBoMUxlbklGV2F6OHNvcC9NN05WL1pmbi9ZMlpzYmZrOUZvQW1RL2xxVlFhRHFIVDRtOHFRbXFETENmUHM0Y3dQc3BmNW5UT0FiTi9kSUJUdU9YU1hIeGMyTE4xVUFkWkpmSFBmTDVLZlJpZE05enVXSmZ2Rktrb0lWUUh3cHc5ZnRvaGZibkdsNzRzWGJ0WEwxWUJFOVRTVFhYMFVCMmtmbEgwL2l0MzVjRzRKbHJNYklmeHdFVERzV1FyZERpZW5Hdyszc09STXRQNGZodWpoMk8yU1lYMDM3a01nVlY5Q2tIZnBTQWI4OTcrb0hXdHFoWWhmM3diRDVzWk4wTFlSZkRiRkdHTUV0QVA5OGNHeG1LYktXbmdHajhuYTVpZVpzTnJUeFcxeG1UL3BleVhZM090T3lSVXl4V3ZRVmNlWnhUUkNVQUpjREZJN2N4MGQ5UXhadDBpeUVkcVJvMXMrWldMOG5jNTRSc0NkYk03QlpqWi9ENEcyaGhNY2l0cHpaeXA2Ui94eTVnWUpjdDZNRW1rQmxzcndTS3M9IiwiVG9rZW5TaWduYXR1cmUiOiJZOUhybUJjRnZDM0lUbUxiZ2F6aW55WUNITGVCTDV0WklpajgrUHFRY3hvPSIsIkVuY3J5cHRpb25JdiI6IlIwTFdzNEdwbmYrdEl6dUJLMXdwNEE9PSIsIkVuY3J5cHRpb25LZXlTaWduYXR1cmUiOiJ5Z2VmZXlKYkhZUWxLMnJlbTZ6a1cwc2xLUFZhaU9YZisvRTk1NnBBczhjPSJ9; Signature_Api=PhX6OyiuW0C01OebvGcN0ii1fHXfbLpNpA15FNeNAeY%253d; UserSession_Api=signature=iyi97COW_L0BudUZjRFzHLUJ4GjkwWORb_SQ05roB7M&payload=eyJFbmNyeXB0ZWRQYXlsb2FkIjoiZ1pEbnRPREdjZ25pRTZ4bjBWQWhMcjBGTlg4b3VlZW54YkJtK2xCeExrME8yS3pkRHJ1YjFzVGhFUUpML0JGRlhQV1N4NW5USnJNRDk1UDVyYmpFdEJTd2treDQzS1cySFdReG9nOVFUK1d1Z3lZdjE4MFRvWHhTVVRIb09zWEtqUHBxZ2dic1hqWW9LejkzcUVGcUZrN0tjYXlhM1BoWTZtU0s3UGVReGIySkQycFpjQzRVUll1UWx4VlNLTExlTC8xb0FqNkR5ZXhCNVhUbVNXejB0MnhiY3Y1c3FINHY1ZnY1VmZGSGlBZmREYytjbGcwaHB5Z2w5QW5IdWs2UXpMVWNHakRJZmlleXpLbDNoeDROdEtHcE4ycmZuNDZiSmdocURqVEJsT3lkbWtIK2RKNUluVWF6b1JGWWJZSGNlNkh4ekp2YzQwUGY3LzhLb0tjM1V3PT0iLCJFbmNyeXB0aW9uS2V5SGFzaCI6InlnZWZleUpiSFlRbEsycmVtNnprVzBzbEtQVmFpT1hmKy9FOTU2cEFzOGM9IiwiRW5jcnlwdGlvbktleUhhc2hDb2RlIjoxMjExNzY4MTMzLCJFbmNyeXB0aW9uSXYiOiJJWFNIMmdORi8rRFk4eXRySXRUSktnPT0ifQ',
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
    print(request)
    jsonContent = json.loads(request.text)
    textDump = ""
    for item in jsonContent["value"]:
        print(item)
        textDump = textDump + " " + item['eventData']["text"]
    return textDump