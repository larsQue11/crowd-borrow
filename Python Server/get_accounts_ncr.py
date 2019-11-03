import requests
import get_OAuth_Token_ncr
from models.account import Account

def get_account_ncr():
    access_token = get_OAuth_Token_ncr.get_oauth2_token_ncr()
    url = "http://ncrqe-qe.apigee.net/digitalbanking/db-accounts/v1/accounts/rf5ao6Qclwsth9OfOvUb-EeV1m2BfmTzUEALGLQ3ehU"

    querystring = {"hostUserId":"TESTUSER002"}

    headers = {
        'Authorization': "Bearer "+access_token,
        'transactionId': "fdd1542a-bcfd-439b-a6a1-5a064023b0ce",
        'Accept': "application/json",
        'User-Agent': "PostmanRuntime/7.19.0",
        'Cache-Control': "no-cache",
        'Postman-Token': "254a7546-0dff-4c70-b0f2-57afc5f74649,b56d7adc-ecee-4666-8e30-00764ca003c7",
        'Host': "ncrqe-qe.apigee.net",
        'Accept-Encoding': "gzip, deflate",
        'Connection': "keep-alive",
        'cache-control': "no-cache"
        }

    response = requests.request("GET", url, headers=headers, params=querystring)
    data = response.json()
    """account = Account(data["id"], data["institutionUserId"], data["institutionCustomerId"], data["institutionId"],
                      data["description"], data["nickName"], data["hostAccountNumber"], data["accountNumber"], data["category"],
                      data["ownershipType"], data["interestRate"], data["isAccountHybrid"], data["isVisible"], data["isHiddenByFi"],
                      data["micrNumber"], data["type"]["value"], data["availableBalance"]["amount"])"""
    return data

def get_accounts_ncr():
    """
    get all accounts from ncr
    :return:
    """
    url = "http://ncrqe-qe.apigee.net/digitalbanking/db-accounts/v1/accounts"
    access_token = get_OAuth_Token_ncr.get_oauth2_token_ncr()

    querystring = {"hostUserId": "TESTUSER001"}

    headers = {
        'Authorization': "Bearer "+access_token,
        'transactionId': "53bb3e61-a06d-457b-97d7-1d704eacdf4c",
        'Accept': "application/json",
        'User-Agent': "PostmanRuntime/7.19.0",
        'Cache-Control': "no-cache",
        'Postman-Token': "7166b34c-b1f5-4717-a3f4-0d84cc716e47,c7c44af2-fa59-4d7f-8282-49ff1e72e20f",
        'Host': "ncrqe-qe.apigee.net",
        'Accept-Encoding': "gzip, deflate",
        'Connection': "keep-alive",
        'cache-control': "no-cache"
    }

    response = requests.request("GET", url, headers=headers, params=querystring)
    json_response = response.json()
    list_accounts = []
    for data in json_response["accounts"]:
        list_accounts.append(data)
    return list_accounts

if __name__ =="__main__":
   print(get_account_ncr())