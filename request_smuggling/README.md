## Request smuggling
is a vulnerability introduced when reverse-proxies and backend servers are not syncronized in their preference for either the ```Content-Length```
or ```Transfer-Encoding``` header when processing client requests, allowing an attacker to send a single request which would be interpreted as 2 distinct
requests by the backend, thus smuggling malicious inputs past front-end security controls.
