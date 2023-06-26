# prototype pollution
is a vulnerability in javascript runtimes that is introduced when calling unsafe recursive functions, that merge object attributes with user controlled input - allowing an attacker to pollute the **__proto__**, which is the highest object in the prototype chain, from which all other objects inherit.
**prototype** is the object used to build __proto__, and can be accessed through constructor funcs

pollution.htb contains the following in one of the endpoints of an express API
```
if(req.body.text){
        const message = {
            user_sent: token.user,
            title: "Message for admins",
        };
        _.merge(message, req.body);
        ... 
```
# lodash/merge.js
```
  baseFor(source, function(srcValue, key) {
    if (isObject(srcValue)) {
      baseMergeDeep(object, source, key, srcIndex, baseMerge, customizer, stack);
    }
    else {
      var newValue = customizer
        ? customizer(object[key], srcValue, (key + ''), object, source, stack)
        : undefined;

      if (newValue === undefined) {
        newValue = srcValue;
      }
      assignMergeValue(object, key, newValue);
    }
  }, keysIn);
}
```
