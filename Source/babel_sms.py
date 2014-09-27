#!/usr/bin/env python3

DEFAULT_CONFIG = """\
# Babel uses Twilio (https://www.twilio.com) to send SMS messages.
# If you don't have an account, you can register for one here:
# https://www.twilio.com/try-twilio

# Your Twilio sending number (not your regular phone number)
# Find it here: https://www.twilio.com/user/account/phone-numbers/incoming)
twilio_number = ""

# Your Twilio Account SID and Auth Token
# Find them here: https://www.twilio.com/user/account
twilio_account_sid = ""
twilio_auth_token = \"\""""

from babel_base import *

# Check arguments
if not args.MESSAGE: fail("MESSAGE required by SMS.")
if args.reply: fail("Can't receive SMS replies.")

import os.path
import toml

check_for_config_dir()

# Create config file if it doesn't already exist
if not os.path.isfile(BABEL_DIR+"/sms.toml"):
    open(BABEL_DIR+"/sms.toml", "w").write(DEFAULT_CONFIG)

# Load config file
s = toml.loads(open(BABEL_DIR+"/sms.toml").read())

from twilio.exceptions import TwilioException
from twilio.rest import TwilioRestClient
from twilio.rest.exceptions import TwilioRestException

# Authenticate with Twilio
try:
    client = TwilioRestClient(s['twilio_account_sid'], s['twilio_auth_token'])
except TwilioException as e:
    fail("Twilio error "+e.msg,
         "You may need to edit %s/sms.toml."%BABEL_DIR)

# Send a text
try:
    sms = client.sms.messages.create(body=args.MESSAGE,
                                     to=args.TO, from_=s['twilio_number'])
except TwilioRestException as e:
    fail("Twilio error "+e.msg,
         "You may need to edit %s/sms.toml."%BABEL_DIR)