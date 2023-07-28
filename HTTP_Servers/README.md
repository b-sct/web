# http servers
default configuration file paths
### nginx
```
/etc/nginx/nginx.conf
/etc/nginx/sites-available/vhost.example.com
```
### apache2
```
/etc/apache2/apache2.conf
/etc/apache2/sites-available/vhost.example.com.conf
```

Tomcat allows path delimiters like '\', '%2F' and '%5C' in the URI. If a vulnerable version of Tomcat is configured through a proxy like Apache HTTP server with mod_proxy and mod_jk, a malformed HTTP request containing strings like "/\../" may allow attackers to work around the context limitations. 
