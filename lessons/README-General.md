<!-- START doctoc generated TOC please keep comment here to allow auto update -->
<!-- DON'T EDIT THIS SECTION, INSTEAD RE-RUN doctoc TO UPDATE -->
**Table of Contents**  *generated with [DocToc](https://github.com/thlorenz/doctoc)*

- [General](#general)
  - [HTTP Basics](#http-basics)
  - [HTTP Proxies](#http-proxies)
  - [Developer Tools](#developer-tools)
  - [CIA Triad](#cia-triad)
  - [Crypto Basics](#crypto-basics)
  - [Writing new lesson](#writing-new-lesson)

<!-- END doctoc generated TOC please keep comment here to allow auto update -->

# General

## HTTP Basics

## HTTP Proxies

## Developer Tools

## CIA Triad

Confidentiality Integirty Availability (CIA)

## Crypto Basics

### Base64 Encoding

```
Authorization: Basic bmV3YmllOnNlY3JldA==
```

```sh
$ echo -n bmV3YmllOnNlY3JldA== | base64 -d
newbie:secret
```

### Other Encoding

```
{xor}Oz4rPj0+LDovPiwsKDAtOw==
```

use any online IBM WebSphere xor decoder in order to find

```
databasepassword
```

### Plain Hashing

```
5f4dcc3b5aa765d61d8327deb882cf99
```

is MD5 hash for

```
password
```

```
8D969EEF6ECAD3C29A3A629280E686CF0C3F5D5A86AFF3CA12020C923ADC6C92
```

is SHA-256 hash for

```
123456
```

### Signatures

Private key (`private.txt`):

```
-----BEGIN PRIVATE KEY-----
MIIEvgIBADANBgkqhkiG9w0BAQEFAASCBKgwggSkAgEAAoIBAQDJCmG1Sg8zj1tmcATLkmLgl2G1EdCVyO7sozuldajQIJytbFrddOvHl4fHSgODEHxojZyf+A8gHF/mG7XrOtX/OP4bk8OK+5D1JPIuCrbQ4IKri6bVkzPKIfE+C8iyWaYF+ulLppUwvb4a2t6v+hjiZIVoaOKD4YeXgSmeuhKdvXEiATQXTguc2y3poQqM4SP/7Rc0RYwduyEGebXK0Z0MB/3g7wOpsyLHMOvHrQ2KcOKL2LRMbC7cAKIADZYyAdS2I842RaolVBAVEaBGZSLK+Y2hgG20faSrnwDQaBNkyGUmnN2kqEdCW+xK1MHsusxj1UAuAvWNjL0vmSlHiA8lAgMBAAECggEAVrlKwviqrBRIWl0yRFrmmnnTJVgFAchHAP+9aDfkVbvruogGfofEejos0VRlRXGkKToFeaB5beGvoMUNaebcj5eXTnAkp1y0AHwqmJ/4kwx2cefxVSqF6clQlvJgZkdz7hp57y9yJi+DxXPrIkCh4W95eTvdkwSECGAogxdDlpVwe1RnO5RMzg8EhSEO/HIbcreKqANwxjoG61fve/61+N5F1z1PpA4UjICDZ3ElaZHemKsdk5atr1I4aIMGdNJPItyyS+qGHmMK+xeyP4brC/hhViIhnsdAv40/EMfbwil3QDQ58LIromTvgAqCvWKmM3xw9uYaFUi99qgO6OupFQKBgQD6dYmZRdR7n5tQqK6cxXuzdAEryo1chRzXRYdsjW9UYYFXpcyzGb02ia++rQQnd94oqsS7ceIegWEk5TjsVP/LoU5QP5vpjOoKBTk1Ge4wbPGUgAYTtUPK+GGCsyeqaXtS3903QONnlgFfuk9MOrBzgpcrN4xMZuUKFNfkBfegkwKBgQDNfPbvIawNBTqNfCdfpe+2t48Jb156UqQzKFcXHqq3gXn5hCdnobhus9i9sG2UTniJcnGqB9u9TLAZMSXcp8iUnJULbXgaLe6yhrv2zZd1de7cOx453F+kYDHjJvD9r6t8g+BGS+YDSEUypX48VOUbWTM/bbqqY1g/NlZCiiw8ZwKBgQDR5mdm+MrWwDBeLMAJysec4X+Jv7sw6q39C9wu8Wl4Ai9v0Rf4kX2tkz6iQkXU/fRFiLhPj2W9wxgy35gRGDs34PvM7UIxPVN3CmGjSxP/qY3csl5lbehe1kKCUrrPao9cKRkwEUWDroeAPpfuftEaPTuLkIYYEbOp+0XjZ8zb2QKBgQCNT8vNJX3ZMmhS1jeJimawY8lE9salHmH3IF3L83X5XlwQYHZsyQU5dAqwYDzrSY+RDhfmkyLlKnDL0kW0WdoRgSDqS+zVLBNDyG5IypfG2kRaRXmC1u8a7mBAUw5Vl1I5/cLk9NsIFNIpgy+ts8Aer5gTnZVKCamtRuPJPJYxLwKBgF3IKY/P5UXrnW5CJXgh0ItoM9rixOA4yZ4WSh+GvpTpc9sn7TRu8AfJB0qnlbCgZNQoMSykVdoYQ84tC8mDvxB+QDSLycFpABknKbm2tGO173on6tArVEBZLu2Xy9JbthOmH7UYuNEslXv1DDiJC2pc/jlgT3jrhqrL/GVWx5a6
-----END PRIVATE KEY-----
```

Determine the modulus as hex string:

```
$ openssl rsa -text -noout -in private.txt -modulus
...
Modulus=C90A61B54A0F338F5B667004CB9262E09761B511D095C8EEECA33BA575A8D0209CAD6C5ADD74EBC79787C74A0383107C688D9C9FF80F201C5FE61BB5EB3AD5FF38FE1B93C38AFB90F524F22E0AB6D0E082AB8BA6D59333CA21F13E0BC8B259A605FAE94BA69530BDBE1ADADEAFFA18E264856868E283E1879781299EBA129DBD71220134174E0B9CDB2DE9A10A8CE123FFED1734458C1DBB210679B5CAD19D0C07FDE0EF03A9B322C730EBC7AD0D8A70E28BD8B44C6C2EDC00A2000D963201D4B623CE3645AA2554101511A0466522CAF98DA1806DB47DA4AB9F00D0681364C865269CDDA4A847425BEC4AD4C1ECBACC63D5402E02F58D8CBD2F992947880F25
...
```

Save the modulus in `modulus.txt`

Calculate the signature for the hex string (modulus) using the private key:

```sh
$ openssl dgst -sha256 -sign private.txt -out signature.txt modulus.txt
$ base64 signature.txt 
```

```
EoaCUIoT1SmkpFz1fnMv5J7oL6FbaE4tc3n8I5Z0LHcV6Ij60j2lIxZrB1s2/BgKHG40IskkD0EbnppfGK72f0hlj3sd4fOiMTLHGoN1r5dNJ8AM7+UI2X8ywzbWW16ij7jh6YbEIVELh/0dxluKZzSNJ2iqb6lKp4sA8bmRebM9+h4nh4UhudacsKc62CeHxVvb/yMIkf+xrqRmIa51hFYYqEWiYUTeltDBcKJf1SqDjIfcBx05Omg0vwTwKXZQdp/YuV6WcxeyAkJTeckcrwt2wHW+8ZCbr3XQBvceZmy6hEgAKkW7Ib2ruF3EabOIGILzAEL+Al90EjEGDoougQ==
```

### Keystore

### Java cacerts

Find the secret inside the following container image

```sh
# docker run -d webgoat/assignments:findthesecret
```

And decrypt the following message

```
U2FsdGVkX199jgh5oANElFdtCxIEvdEvciLi+v+5loE+VCuy6Ii0b+5byb5DXp32RPmT02Ek1pf55ctQN+DHbwCPiVRfFQamDmbHBUpD7as=
```

```sh
# docker exec -it --user root <CONTAINER ID> /bin/bash
root@<CONTAINER ID>:~# cat /root/default_secret 
ThisIsMySecretPassw0rdF0rY0u
root@<CONTAINER ID>:~# echo "U2FsdGVkX199jgh5oANElFdtCxIEvdEvciLi+v+5loE+VCuy6Ii0b+5byb5DXp32RPmT02Ek1pf55ctQN+DHbwCPiVRfFQamDmbHBUpD7as=" | openssl enc -aes-256-cbc -d -a -kfile /root/default_secret
Leaving passwords in docker images is not so secure
```

### Post quantum cryptography

## Writing new lesson