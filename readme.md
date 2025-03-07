# xorcrypt

Simple "on the go" vanilla scripts used to encrypt and decrypt stuff via a simple XOR encryption enhanced by keys of infinite length.

## Usage:
```
python3 xorcrypt.py <INPUT_FILE> <OUTPUT_FILE> <KEY> [IKG_SCRIPT]
```
### Example:
```
"super secret message here" > message.txt
python3 xorcrypt.py message.txt encrypted.txt SuperSecretKey
python3 xorcrypt.py encrypted.txt decrypted.txt SuperSecretKey
```
---
## Is it safe?

Ask AI, not me, I am not an expert in the crypto field.

As far as I know, if the message is shorter or equal to the key then theoretically the message is undecryptable. If the message is longer, then the key will be reused to encrypt the message. But this kind of usage has its flaws, like a frequency analysis attack/crack.

*So, the message is safe as long as the key is longer or equal to the message. So why can't the key be of infinite length?*

To make that happen, we make use of ***Infinite Key Generator*** that can generate the next chunks of the infinite key based on the key of fixed length. `ikg_sha256.py` is an example of such a tool which uses SHA256 algorithm to generate its chunks.