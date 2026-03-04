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

## Preventive Measures
* Although encoding (Base64, URL, Hex) is necessary for data interoperability, it is frequently abused or exploited. These particular precautions should be recorded in your repository:

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