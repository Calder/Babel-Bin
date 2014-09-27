#!/usr/bin/env python3

# Strings (may eventually be shared)
TO_HELP      = "the recipient address"
MESSAGE_HELP = "the message data"
REPLY_HELP   = "wait for and print reply"

import argparse

# Parse command line arguments
parser = argparse.ArgumentParser('babel')
parser.add_argument('TO', help=TO_HELP)
parser.add_argument('MESSAGE', nargs='?', help=MESSAGE_HELP)
parser.add_argument('-r', '--reply', action='store_true', help=REPLY_HELP)
args = parser.parse_args()