from twilio.rest import Client


def send_sms_alert():

    try:
        # Define your body
        my_body='Yo'
        # define client
        client = Client('SSID GOES HERE XXX ','AUTH TOKEN XX ')
        client.messages.create(to='+ TO XXXX ',
                               from_= '+TWILIO NUMBER XXX',
                               body=my_body)
    except:
        print('Cannot send Sms!')

send_sms_alert()