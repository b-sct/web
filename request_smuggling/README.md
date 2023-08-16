## Request smuggling
is a vulnerability introduced when reverse-proxies and backend servers are not syncronized in their preference for either the ```Content-Length```
or ```Transfer-Encoding``` header when parsing client requests, allowing an attacker to include both headers in a single request,
which results in part of the request to be interpreted as the start of the next request.


the vuln could be classified as either of the following:
    * ```CL.TE``` the front-end server uses the Content-Length header and the back-end server uses the Transfer-Encoding header.
    * ```TE.CL``` the front-end server uses the Transfer-Encoding header and the back-end server uses the Content-Length header.
    * ```TE.TE``` the front-end and back-end servers both support the Transfer-Encoding header, but one of the servers can be induced not to process it by obfuscating the header in some way.

#### ```CL.TE``` example
```
POST / HTTP/1.1
Host: vulnerable.com
Connection: keep-alive
Content-Type: application/x-www-form-urlencoded
Content-Length: 6
Transfer-Encoding: chunked

0

GET /reset?pass=smuggled HTTP/1.1
Host: vulnerable.com
```
