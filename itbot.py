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

                            
    # Fetch the message
    msg = request.form.get('Body')
    phone_number = request.form.get('From')
    resp = MessagingResponse()      
    


    
    # Create reply
    if msg == 'Hello':
        resp.message("Hi I am your Felican University's IT Bot!\n Reply *Menu* to see what I can do for you.")
        return str(resp)
    
    if msg == 'Menu':
        resp.message("Hi I am your Felican University's IT Bot!\n\nIf you forgot your email password reply *Email*\nIf you forgot your email password reply *Webadvisor*\nIf you have problems connecting to wifi reply *Wifi*\nOtherwise please email us at helpdesk@felician.edu or call us at 201-554-0240")
        return str(resp)
    if msg == 'Email':
        resp.message("To reset your email password please follow the guidelines in this article\n https://felician.atlassian.net/servicedesk/customer/portal/2/article/199000077?src=-1977257468")
        return str(resp)
    if msg == 'Webadvisor':
        resp.message("To reset your Webadvisor password please follow the guidelines in this article\n https://felician.atlassian.net/servicedesk/customer/portal/2/article/199098485?src=2008668440")
        return str(resp)
    if msg == 'Wifi':
        resp.message("We are currently experiencing some issues with the server that affected the connectivity of the wifi, please be patient while we work on solving this problem\n Sorry for the inconvenience")
        return str(resp) 	
    
    




if __name__ == "__main__":
    app.run(debug=True)