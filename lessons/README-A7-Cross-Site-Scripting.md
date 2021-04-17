<!-- START doctoc generated TOC please keep comment here to allow auto update -->
<!-- DON'T EDIT THIS SECTION, INSTEAD RE-RUN doctoc TO UPDATE -->
**Table of Contents**  *generated with [DocToc](https://github.com/thlorenz/doctoc)*

- [A7 - Cross-Site Scripting](#a7---cross-site-scripting)
  - [Cross-Site Scripting](#cross-site-scripting)

<!-- END doctoc generated TOC please keep comment here to allow auto update -->

# A7 - Cross-Site Scripting

## Cross-Site Scripting

### 1. Concept

### 2. What is XSS?

```javascript
alert("XSS Test");
alert(document.cookie);
```

```html
<script>alert("XSS Test")</script>
```

Cookies on two different tab on the same web app are the same for JSESSIONID value.

### 3. Most common locations

### 4. Why should we care?

### 5. Types of XSS

- Reflected
- DOM-based (technically reflected)
- Stored

### 6. Reflected XSS scenario

1. attacker sends a malicious URL to victim
2. victim clicks on the link that loads malicious web page
3. the malicious script embedded in the URL executes in the victim's browser
4. the script steals sensitive information, like the session id, and release it to the attacker

### 7. Try It! Reflected XSS

Field susceptible to XSS: credit card number

### 8. Self XSS or reflected XSS?

### 9. Reflected and DOM-Based XSS

The difference between DOM and 'traditional' reflected XSS is that, with DOM, the payload will never go to the server.
It will only ever be processed by the client.

1. attacker sends a malicious URL to victim
2. victim clicks on the link
3. that link may load a malicious web page or a web page they use that has a vulnerable route/handler
4. if it's a malicious web page, it may use it's own JavaScript to attack another page/URL with a vulnerable route/handler
5. the vulnerable page renders the payload and executes attack in the user's context on that page/site
6. attacker's malicious script may run commands with the privileges of local account

### 10. Identify potential for DOM-Based XSS

- base route: `start.mvc#lesson/`
- parameters processed by the JavaScript route handler: `CrossSiteScripting.lesson/9`

GoatRouter.js

``` javascript
'lesson/:name': 'lessonRoute',
'lesson/:name/:pageNum': 'lessonPageRoute',
'test/:param': 'testRoute',
```

- test code in production: `start.mvc#test/`

### 11. Try It! DOM-Based XSS

- function to execute: `webgoat.customjs.phoneHome()`

\#FIXME

### 12. Quiz

1. 4
2. 3
3. 1
4. 2
5. 4