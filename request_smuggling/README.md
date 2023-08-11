## Request smuggling
is a vulnerability introduced when reverse-proxies and backend servers are not syncronized in their preference for either the ```Content-Length```
or ```Transfer-Encoding``` headers when processing client requests, allowing an attacker to smuggle malicious inputs past front-end security controls.
