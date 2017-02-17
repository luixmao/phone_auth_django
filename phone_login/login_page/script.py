# /usr/bin/env python
# Download the twilio-python library from http://twilio.com/docs/libraries
from twilio.rest import TwilioRestClient

# Find these values at https://twilio.com/user/account
with open('/etc/parkapp_project/twilio_password.txt') as f:
    twilio_password = f.read().strip()
account_sid = "ACc11c369c8b9d31cca420a9cc233730bb"
auth_token = twilio_password
client = TwilioRestClient(account_sid, auth_token)

message = client.messages.create(to="+12132907861", from_="+18187228353", body="Code")