# babel

The `babel` command line interface provides a single command for sending *messages* to *endpoints*. Endpoints can (currently) be HTTP addresses, SMS numbers, user defined aliases, or (planned) public keys and hashes.

## Usage

```bash
# Send an SMS
babel 4041234567 'Ohai thar'

# Send a message to a contact
babel bob 'Wazzaap!'

# Make a GET request
babel -r http://ipinfo.io/json

# Make a POST request
babel -r http://ipinfo.io/json somepostdata
```

## Installation

To send SMS messages, you'll first need to set up a [Twilio](https://www.twilio.com) account. Follow the instructions for your platform, then run
```
babel YOUR_PHONE_NUMBER Hello World
```
and edit `~/.babel/sms.toml` with your Twilio account settings. Save it and try again.

### Ubuntu

```
# Install Pip
sudo apt-get install python3-pip

# Install babel-cli
sudo pip3 install babel-cli
```

### Mac OS X

```
# Install Homebrew
sudo ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"

# Install Python 3 from Homebrew
sudo brew install python3
sudo brew link --overwrite python3

# Install babel-cli
sudo pip3 install babel-cli
```

## Configuration

* `~/.babel/aliases.txt` contains contact aliases.
* `~/.babel/sms.toml` contains Twilio settings.

## Contributing

See the [design doc](https://docs.google.com/document/d/1B8_FC-u9iGq4RVdUB0VTxRnriBtdFCxIbqk3bhIdidU/edit#) for long term goals. Drop me a line if you're interested in contributing! :-)
