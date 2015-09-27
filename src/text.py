import urllib2
# import json

TEXT_API_URL = 'http://69.204.255.92/api/text/send?'
TEXT_API_SEP = '&'
TEXT_API_NEWLINE = '%0A'

def get_text_url(phoneNum, payload):
    return TEXT_API_URL + "to=" + phoneNum + TEXT_API_SEP + "msg=" + payload

def send_text(phoneNum, payload):
    requestURL = get_text_url(phoneNum, payload)
    response = urllib2.urlopen(requestURL).read()
    # json_resp = json.loads(response)
    # return json_resp["type"]
    return response