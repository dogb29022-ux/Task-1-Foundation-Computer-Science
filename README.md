# Task-1-Foundation-Computer-Science

## Overview
The practical implementation and analysis for Task 1 of the Foundation of Computer Science (ST4015CMD) module may be found in this repository. In order to guarantee safe and effective data transfer, the project investigates how encoding formats like Base64, ASCII, and URL encoding interact with contemporary protocols (HTTPS, TLS, SMTP).

## Learning Outcomes
* Analyze the impact of data storage and processing in computer systems.
* Evaluate the role of cryptography and encoding in keeping data secure.

## Quick Start
```sql
#clone the repo
git clone https://github.com/dogb29022-ux/Task-1-Foundation-Computer-Science.git
cd Task-1-Foundation-Computer-Science
```

## Project Structure
```sql
Task-1-Foundation-Computer-Science/
├── README.md               (The project overview)
├── scripts/
|
├── diagrams/
```

## Live Demonstrations
**Tools used**

1. Base64 one
2. Wireshark

**Procedure**
**Step 1: opening the Base64 one and inserting the data.**
First, we'll launch the Base64 One program. It is a free program that demonstrates how Base64 encoding is used to transform data into ASCII text.

<img src="/Diagrams/base64_one.png" height="300" width="500">

**Step 2: Inserting the data and encoding it int the base64 format.**
We will enter the text and encode it in Base64 format once the tool has been opened.

<img src="/Diagrams/encodded to base64.png" height="300" width="500">

**Step 3: Launch Wireshark in loopback mode, then filter the packets for TCP.**
To begin capturing the packet, we first launch Wireshark in loopback mode. "tcp.port == 1025" must be entered in the filter bar.Next, we press the start button to begin packet capture.

<img src="/Diagrams/wireshark.png" height="300" width="500">

**Step 4: Establishing a testing environment locally**
On our computer, we will set up a localized testing environment. It implies that our gadget will be both the transmitter and the recipient.

Initially, we will use the library aiosmtpd to establish a receiver. We must install the aiosmtpd first because it is not preloaded. Thus, we must launch Powershell and enter this command.

```sql
pip install aiosmtpd
```
We will set up a channel to receive the package after installing aiosmtpd. We will use the command below to accomplish that.
```sql
aiosmtpd -n -l localhost:1025
```
Next, we'll set up a sender in the terminal. The commands listed below must be run in order to accomplish that.
```sql
telnet localhost 1025
EHLO localhost
MAIL FROM:<test@me.com>
RCPT TO:<you@me.com>
DATA
```
This command must then be entered in order to send the SMTP package.
```sql
Subject: Base64 Lab
Content-Type: text/plain; charset="utf-8"
Content-Transfer-Encoding: base64

SGVsbG8gV29ybGQh
.
```

**Step 5: Using Wireshark to capture the packet.**
Once the packets are sent, Wireshark begins to capture them and shows the captured packet.

<img src="/Diagrams/port.png" height="300" width="500">

Next, we must right-click on it, navigate to the Follow section, and hit Ctrl+Alt+Shift+T. The details of the captured packet will be displayed when the new window opens.

<img src="/Diagrams/captured encoding.png" height="300" width="500">

We may observe that the original converted text in the Base64 one tool and the captured packet during transmission have the identical Base64 encoded code.

## Preventive Measures
* Although encoding (Base64, URL, Hex) is necessary for data interoperability, it is frequently abused or exploited. These particular precautions should be recorded in your repository

* Sanitization Prior to Encoding: Never encode user input that hasn't been verified. To get over simple firewalls, malicious scripts (XSS) or SQL instructions can be "hidden" within Base64 strings. Prior to processing, data should always be verified against an allowlist.

* Context-Aware Decoding: Make sure the server-side decoding procedure precisely corresponds to the client-side encoding. Inconsistencies in this area may result in "Double Encoding" attacks, in which an attacker encodes a payload twice in order to evade a security filter that only decodes once.

* Integrity Checks (Hashing): There is no security or integrity provided by encoding. Always couple encoded data with a cryptographic hash (such as SHA-256) or a Message Authentication Code (MAC) to guard against data manipulation during transmission.

* Enforce Secure Protocols (TLS 1.3): Encoding such as Base64 should never be used in place of encryption because it is easily reversible by anybody. To stop interceptors from just decoding the communication, all encoded data should be sent via a secure tunnel using TLS 1.3.

## Further Enhancement 
In order to demonstrate "Critical Analysis," which is necessary for a grade of 70% or higher, suggest the following improvements over simple encoding:

* Switch to Base85 for Efficiency: Base85 (ASCII85) is more efficient, increasing data size by about 25%, whereas Base64 increases it by roughly 33%. Suggest this for programs requiring a lot of bandwidth, such as Git internal storage or Adobe PostScript.

* Implementation of JWT (JSON Web Tokens): It is recommended to use JWTs for session management rather to just Base64 strings. These ensure that the data is both URL-safe and tamper-proof by using Base64URL encoding along with a digital signature.

* Binary-to-Text Optimization in IoT: CBOR (Concise Binary Object Representation) is recommended as an alternative to JSON/Base64 for low-power IoT devices. It improves performance in limited contexts by being made for small code and message sizes.

* Automated Secret Scanning: Include Git-Secrets and TruffleHog in your GitHub workflow. When critical Base64-encoded strings, such as API keys, are inadvertently committed to your repository, these tools automatically identify it.

## License
This project is license under MIT License. See more about [License](https://github.com/dogb29022-ux/Task-1-Foundation-Computer-Science/blob/main/LICENSE) here.

## Author
- **Shreejan Byanju**