from flask import Flask, request
from twilio.rest import Client
from twilio.twiml.messaging_response import MessagingResponse
from apscheduler.schedulers.background import BackgroundScheduler
import datetime
import emoji
import os 
app = Flask(__name__)


account = os.environ.get("ACCOUNT_SID")
token = os.environ.get("TOKEN")
client = Client(account, token)

# message = client.messages.create(to=user_number(), from_="whatsapp:+14155238886",
#
@app.route("/")
def Hello():
    return "Hello CS420:Software Engineering"
@app.route("/sms", methods=['POST'])
def sms_reply():
    """Respond to incoming calls with a simple text message.""" 
    #Closing the ticket time
    msg_received = datetime.datetime.now()
    update = msg_received + datetime.timedelta(minutes=1) 

    # Fetch the message
    msg = request.form.get('Body')
    phone_number = request.form.get('From')
    resp = MessagingResponse()      
    
    def ticket_update(message):
        client.messages.create(to=phone_number, from_="whatsapp:+14155238886", body=message)

    # Create reply
    if 'hello' in msg.lower():
        resp.message("Hi I am your Felican University's IT \U0001F916 \n Reply *Menu* to see what I can do for you.")
        return str(resp)
    
    if 'menu' in msg.lower():
        resp.message("Hi I am your Felican University's IT \U0001F916 \n If you forgot your email password reply *Email*\nIf you forgot your email password reply *Webadvisor*\nIf you have problems connecting to wifi reply *Wifi*\nOtherwise please email us at helpdesk@felician.edu or call us at 201-554-0240")
        return str(resp)
    if 'email' in msg.lower():
        resp.message("To reset your email password please follow the guidelines in this article\n https://felician.atlassian.net/servicedesk/customer/portal/2/article/199000077?src=-1977257468")
        return str(resp)
    if 'webadvisor' in msg.lower():
        resp.message("To reset your Webadvisor password please follow the guidelines in this article\n https://felician.atlassian.net/servicedesk/customer/portal/2/article/199098485?src=2008668440")
        return str(resp)
    if 'wifi' in msg.lower():
        resp.message("We are currently experiencing some issues with the server that affected the connectivity of the wifi, please be patient while we work on solving this problem\n Sorry for the inconvenience")
        return str(resp)
    if 'brightspace' in msg.lower():
        resp.message("We do not manage the Brightspace system. Please contact Ansu Mathew at MathewA@felician.edu or Rebecca DeVita at DeVitaR@felician.edu.")
        return str(resp)
    else:
        resp.message("I'm sorry my bot skills are not advanced enough to help you with this issue \N{pensive face} \nPlease contact the helpdesk at helpdesk@felician.edu or call us at 201-554-0240 \n Meanwhile checkout *Menu* for what I can do \N{hugging face} !")
        return str(resp)

if __name__ == "__main__":
    app.run(debug=True)
