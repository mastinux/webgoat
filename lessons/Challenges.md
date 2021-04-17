<!-- START doctoc generated TOC please keep comment here to allow auto update -->
<!-- DON'T EDIT THIS SECTION, INSTEAD RE-RUN doctoc TO UPDATE -->
**Table of Contents**  *generated with [DocToc](https://github.com/thlorenz/doctoc)*

- [Challenges](#challenges)
  - [Admin lost password](#admin-lost-password)
  - [Without password](#without-password)
  - [Admin password reset](#admin-password-reset)
  - [Without account](#without-account)

<!-- END doctoc generated TOC please keep comment here to allow auto update -->

# Challenges

## Admin lost password

### Welcome to the WebGoat challenge (CTF)

Brute forcing is not allowed.

### Login portal

`Reset Password` send a request with POST body `email=admin%40webgoat&token=`

\#FIXME how the lesson has been completed?

## Without password

SQL injection through POST body:

```
username_login=Larry&password_login=alfa'+or+1%3D'1
```

## Admin password reset

\#FIXME challenge completed sending admin@localhost, why?

## Without account

\#FIXME