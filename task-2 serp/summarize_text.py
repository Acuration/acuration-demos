import requests
import time
import random

def summarize(text):
    url = 'https://www.semrush.com/goodcontent/api/summary-generator/generate-summary/'
    payload = {'text': text, 'format': 'paragraph', 'length_penalty': 10}

    waittime = 15
    print(f'Waiting for {waittime}s...', end=' ')
    time.sleep(waittime)
    print('Sending post request..')
    try:
        resp = requests.post(url, json=payload)

        if resp.status_code == 200:
            data = resp.json()
            return data['summary']
        else:
            return 'Some error in summarizing'
    except:
        print('Some error in doing post request')