# Insecure Deserialization

Serialization is the process of encoding and formatting data to a byte sequence which the application can later process.
For example:
```
{
  "id": "3",
  "username": "bob",
  "admin": false
}
```

Would be serialized to:
```
O:4:"User":3:{s:2:"id";s:1:"3";s:8:"username";s:3:"bob";s:5:"admin";b:0;}
```

breaking it down
```
O:4:"User":    # instance of User class, whose name contains 4 characters
3:{  ...  }    # data structure containing 3 key-pairs

s:2:"id";s:1:"3";
s:8:"username";s:3:"bob";
s:5:"admin";b:0;
```

Usually after data is serialized it is assigned to the end-user to be later processed by backend functionlity, for example - session cookies, analytics.
Vulnerabilities in the process of deserialization arise from 2 different misconfigurations
1.  weak encryption - often after serialized data that is key to the funcionality of the application is assigned to the end-user it is encrypted.
    being able to directly modify values in serialized data that is passed for later processing by a variety of functions might introduce all kinds of vulnerabilities.
2.  object instatiation - since serializing and later deserializing data often involves the parsing of text into attribute types of classes,
    an attacker might be able to instantiate arbitrary objects and manipulate their attributes.
