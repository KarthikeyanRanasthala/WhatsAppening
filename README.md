![](https://img.shields.io/github/license/KarthikeyanRanasthala/WhatsAppening.svg)
![](https://img.shields.io/pypi/pyversions/whatsappening-cli.svg)
![](https://img.shields.io/pypi/v/whatsappening-cli.svg)
![](https://img.shields.io/pypi/format/whatsappening-cli.svg)
![](https://img.shields.io/pypi/status/whatsappening-cli.svg)
![](https://img.shields.io/pypi/dd/whatsappening-cli.svg?label=pypi%20downloads)
![](https://img.shields.io/librariesio/sourcerank/pypi/whatsappening-cli.svg)

# WhatsAppening

## Overview

WhatsAppening tracks a user's Whatsapp activity using Selenium on WhatsApp Web. The tracked data will be displayed in the terminal, written to a CSV file & pushed to Firebase Realtime Database.

[WhatsAppening-Firebase](https://www.github.com/KarthikeyanRanasthala/WhatsAppening-Firebase) contains necessary files to setup Firebase Hosting and Firebase Cloud Messaging for Realtime Push Notifications.

## Requirements

- [Python 3](https://www.python.org/downloads)
- [Firefox Browser](https://www.mozilla.org/firefox)
- [geckodriver](https://github.com/mozilla/geckodriver/releases) (Will be downloaded automatically from v1.3.0+)

## Installation

WhatsAppening is available on PyPI. You can install the latest version using pip.
```
    pip install whatsappening-cli
```

To Install the previous version without Firebase Realtime Database support.
```
    pip install whatsappening-cli==1.1.1
```

## Usage

Make sure you're executing it from the directory containing 'FirebaseAdminSDK.json'.
```
    whatsappening-cli
```

To use the previous versions (1.1.1 and below) without Firebase Realtime Database support, Make sure you're executing it from the directory containing 'geckodriver'.

## Development

```
    git clone https://www.github.com/KarthikeyanRanasthala/WhatsAppening.git
```

## Limitations

- You can track only one target-user at once.
- You need to have an active chat with the target-user. Be a day old or a year old chat. It's a Whatsapp Web limitation.