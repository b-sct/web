# Insecure Deserialization

Serialization is the process of formatting object data to a byte sequence which the application can later process.
For example, consider the following attributes:
```
{
  "id": "3",
  "username": "bob",
  "admin": false
}
```

these serialize to (PHP):
```
O:4:"User":3:{s:2:"id";s:1:"3";s:8:"username";s:3:"bob";s:5:"admin";b:0;}
```

breaking the serialized object down:
```
O:4:"User":    # instance of User class, whose name contains 4 characters
3:{  ...  }    # dictionary structure containing 3 key-pairs (attributes and corresponding values)

s:2:"id";s:1:"3";
s:8:"username";s:3:"bob";
s:5:"admin";b:0;
```

Deserialization is the process of instantiating objects from their serialized reporesentation.
An insecure deserialization is one in which user-supplied input is not properly sanitized, potentially allowing an attacker
the creation of arbitrary PHP objects and manipulating their attributes.

### PHP Type Juggling
is a manipulation that can be made to the types of attributes that takes advantage of loose comparisons made in the backend: 

##### vulnerable backend
```php
<?php
$user = unserialize($_COOKIE['session']);

if ($user['access_token'] == $admin_token) {
    $admin = true;
}
```
payload that makes a string == integer (resulting in true)
```
O:4:"User":2:{s:8:"username";s:7:"lowpriv";s:12:"access_token";i:0;}
```

full type comparison results in PHP can be found in this [PayloadsAllTheThings cheatsheet](https://github.com/swisskyrepo/PayloadsAllTheThings/blob/master/Type%20Juggling/README.md#loose-comparison)
