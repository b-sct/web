## Request smuggling
is a vulnerability introduced when reverse-proxies and backend servers are not syncronized in their preference for either the ```Content-Length```
or ```Transfer-Encoding``` header for defining the boundaries of incoming client requests.

This desync allows an attacker to send a request that would overlap with other requests on the stack that are forwarded to the backend 
For example: injecting a POST request that has a body parameter ```smuggling=``` and ```Content-Length: 30``` - 
resulting in the request line of the next request in the stack to be parsed as the content of the variable smuggling, reulting in part
of the request to be interpreted as the start of the next request.


the vuln could be classified as either of the following:

- ```CL.TE``` the front-end server uses the Content-Length header and the back-end server uses the Transfer-Encoding header.
- ```TE.CL``` the front-end server uses the Transfer-Encoding header and the back-end server uses the Content-Length header.
- ```TE.TE``` the front-end and back-end servers both support the Transfer-Encoding header, but one of the servers can be induced not to process it by obfuscating the header in some way.

#### ```CL.TE``` example
```
POST / HTTP/1.1
Host: vulnerable.com
Content-Type: application/x-www-form-urlencoded
Content-Length: 60
Transfer-Encoding: chunked

0

GET /reset?pass=smuggled HTTP/1.1
Host: vulnerable.com
```
in this example, the front-end prefers Content-Length, so 60 bytes are specified (up until the end of the Host header of the smuggled request), while the backend processes using Transfer-Encoding - 
the first chunk is processed (0) which terminates the request. All lines that follow are considered the start of a new request, so the next request's contents will be appended to the smuggled one.


#### ```TE.CL``` example
```
POST / HTTP/1.1
Host: 0a7500c10314fd5a8767681c0018002e.web-security-academy.net
Content-Type: application/x-www-form-urlencoded
Content-Length: 4
Transfer-Encoding: chunked

87
GET /admin/delete?username=carlos HTTP/1.1
Host: localhost
Content-Type: application/x-www-form-urlencoded
Content-Length: 15

x=1
0

```
in this example, the ```Content-Length``` of the injected GET request surpasses the length of ```x=1\r\n0\r\n\r\n```, resulting in the parsing of the next incoming request's line as
the body of the smuggled GET request.
