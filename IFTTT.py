import json
import urllib.request
import requests

# Define a function
def iftt():
    # define payload thats a dictionary
    payload={'value1':'hello',
             'value2':11}

    # define Keys
    KEYS='XXXXXYOUR KEY GOES HERE XXX'

    # define URL
    URL='https://maker.ifttt.com/trigger/XXX/with/' # replace XX event name

    # Generate a new Url
    NEW_URL=URL+KEYS

    print(NEW_URL)
    requests.post(NEW_URL,data=payload)


if __name__ == '__main__':
    for x in range(0,10):
        if x==5:
            #Execute function only once
            print(x)
            iftt()
        else:
            pass