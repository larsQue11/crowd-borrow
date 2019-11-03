import requests


def get_oauth2_token_ncr():
    url = "http://ncrqe-qe.apigee.net/digitalbanking/oauth2/v1/token"

    payload = "grant_type=password&scopes=accounts%3Aread%2Ctransactions%3Aread%2Ctransfers%3Awrite%2Caccount%3Awrite%2Cinstitution-users%3Aread%2Crecipients%3Aread%2Crecipients%3Awrite%2Crecipients%3Adelete%2Cdisclosures%3Aread%2Cdisclosures%3Awrite&username=HACKATHONUSER001&password=test123"
    headers = {
        'Content-Type': "application/x-www-form-urlencoded",
        'Authorization': "Basic NDAxZGFhYjIyZTNiNDAxNjgwZTY4ZTk0NmNiZWI5YzI6MDgxMDBmYjIyYWYzNDBmZGIwZDBjYmNjZTViMGJjMmU=",
        'transactionId': "f3df8be7-621d-4278-994a-1f3d6a156c1d",
        'institutionId': "DI0516",
        'Accept': "application/json",
        'Date': "Sun, 03 Nov 2019 03:15:08 GMT",
        'User-Agent': "PostmanRuntime/7.19.0",
        'Cache-Control': "no-cache",
        'Postman-Token': "7c7d1a7a-7c19-4b0b-be28-ba5b672618d9,562bd220-7071-4bb4-a1a2-fb6ede262bbe",
        'Host': "ncrqe-qe.apigee.net",
        'Accept-Encoding': "gzip, deflate",
        'Content-Length': "278",
        'Connection': "keep-alive",
        'cache-control': "no-cache"
        }

    response = requests.request("POST", url, data=payload, headers=headers)
    json_response = response.json()
    return json_response["access_token"]