import requests
import get_OAuth_Token
from models.recipient import Recipient


def get_all_recipients_ncr():
    # get Token from NCR platform
    access_token = get_OAuth_Token.get_oauth2_token_ncr()
    url = "http://ncrqe-qe.apigee.net/digitalbanking/db-recipients/v1/recipients"

    querystring = {"hostUserId":"HACKATHONUSER100"}

    headers = {
        'transactionId': "94f5b7f0-7cda-43c0-912e-79c7c8fcc155",
        'Authorization': "Bearer "+access_token,
        'Content-Type': "application/json",
        'User-Agent': "PostmanRuntime/7.19.0",
        'Accept': "*/*",
        'Cache-Control': "no-cache",
        'Postman-Token': "738a3311-5777-44dc-aaf9-f0461a8163d2,7b8fc933-f0b3-4e65-b9d9-970ccd14a937",
        'Host': "ncrqe-qe.apigee.net",
        'Accept-Encoding': "gzip, deflate",
        'Connection': "keep-alive",
        'cache-control': "no-cache"
        }

    response = requests.request("GET", url, headers=headers, params=querystring)
    json_response = response.json()
    list_recipients = []
    for data in json_response["Recipients"]:
        recipient = Recipient(data["id"], data["institutionId"], data["memberNumber"],
                              data["institutionCustomerId"], data["passCode"], data["email"], data["nickName"])
        list_recipients.append(recipient)
    return list_recipients

if __name__=="__main__":
    for i in get_all_recipients_ncr():
        print(i)