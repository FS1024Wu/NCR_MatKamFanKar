from http.client import HTTPSConnection
from base64 import b64encode
import json


c = HTTPSConnection("gateway-staging.ncrcloud.com")


userAndPass = b64encode(b"acct:amzing4@amzing4serviceuser:abcd1234").decode("ascii")

headers = {'Authorization' : 'Basic %s' %  userAndPass,
            'Content-Type': "application/json",
            'accept': "application/json",
            'nep-application-key': "8a00860b6641a0ae016646ecc5e4000a",
            'nep-organization': "ncr-market",
            'nep-service-version': "2.2.0:2",
            }


def get_transaction(id):
    c.request('POST', '/transaction-document/transaction-documents/'+id, headers=headers)
    return c.getresponse()

def post_transaction(id, customer_name, items):
    i_list =""
    for i in range(len(items)):
        i_list += "{\"category\":{\"name\":\"" + items[i] + "\"}},"

        if i is len(items)-1:
            i_list = i_list[:-1]

    payloads = "{\"tlogData\": [{\"id\": \""+id+ "\",\"siteInfo\":{\"id\":\"1\"}, \"transactionNumber\":\"1\", \"dataProviderName\": \"string\", \"dataProviderVersion\":\"string\", \"tlog\":{\"customer\":{\"name\":\""+ customer_name +"\"},\"items\":["+i_list+"]}}]}"


    c.request('POST', '/transaction-document/transaction-documents/', payloads, headers)
    return c.getresponse()

id = "875effbf-03d2-4832-b0a9-0eff80850b63"

res = get_transaction(id)
data = res.read().decode("utf-8")
print(data.modelVersion)



