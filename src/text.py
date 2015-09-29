import urllib2
from time import sleep

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

def send_multiple_texts(phoneNum, textList):
    # Text directions to phone number
    payload = ''
    for text in textList:
        payload = '%28' + str(textList.index(text)) + '%29' + '%20' + text.replace(' ', '%20')
        for i in range(0, len(payload), 160):
            try:
                print send_text(phoneNum, unicode(payload[i:i+160]).encode('utf-8'))
                sleep(5)
            except UnicodeEncodeError, e:
                pass