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
- TODO