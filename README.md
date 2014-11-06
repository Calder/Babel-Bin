babel
=====

The `babel` command line interface provides a single command for sending *messages* to *endpoints*. Endpoints can (currently) be HTTP addresses, SMS numbers, user defined aliases, or (planned) public keys and hashes.

Usage
-----

```
babel 4041234567 "Ohai thar"
babel bob "Wazzaap!"
babel -r http://ipinfo.io/json
```

Installation
------------

```
sudo easy_install babel
```

Contributing
------------

See the [design doc](https://docs.google.com/document/d/1B8_FC-u9iGq4RVdUB0VTxRnriBtdFCxIbqk3bhIdidU/edit#) for long term goals. Drop me a line f you're interested in contributing! :-)
