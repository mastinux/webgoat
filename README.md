# WebGoat

> https://github.com/WebGoat/WebGoat/releases/tag/v8.1.0

## Setup

WebGoat needs Java 11

`# update-alternatives --config java`

Start WebGoat

`$ java -jar webgoat-server-8.1.0.jar [--server.port=8080] [--server.address=localhost]`

Visit

`http://localhost:8080/WebGoat`

username/password = newbie/eibwen

### WebWolf - Setup

Feature supported by WebWolf:

- hosting a file
- receiving email
- landing page for incomping requests

Start WebWolf along with a running WebGoat

`$ java -jar webwolf-8.1.0.jar [--server.port=9090] [--server.address=localhost]`

Visit

`http://localhost:9090`

## Lessons

For each lesson there are three steps:

- explain the vulnerability
- learn by doing
- explain mitigation

Lessons

- [General](./lessons/README-General.md)
- [A1 - Injection](./lessons/README-A1-Injection.md)
- [A2 - Broken Authentication](./lessons/README-A2-Broken-Authentication.md)
- [A3 - Sensitive Data Exposure](./lessons/README-A3-Sensitive-Data-Exposure.md)
- [A4 - XML External Entities](./lessons/README-A4-XML-External-Entities.md)
- [A5 - Broken Access Control](./lessons/README-A5-Broken-Access-Control.md)
- [A7 - Cross-Site Scripting](./lessons/README-A7-Cross-Site-Scripting.md)
- [A8 - Insecure Deserialization](./lessons/README-A8-Insecure-Deserialization.md)
- [A9 - Vulnerable Components](./lessons/README-A9-Vulnerable-Components.md)
- [A8:2013 - Request Forgeries](./lessons/README-A8-2013-Request-Forgeries.md)
- [Client Side](./lessons/Client-side.md)
- [Challenges](./lessons/Challenges.md)

\# TODO complete FIXMEs