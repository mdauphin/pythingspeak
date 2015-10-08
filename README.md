pythingspeak - Python package
======================

This is a python library to communicate with thingspeak cloud service

### Some Samples

**open port, get version**
```python
>>> from pytemperaturectrl import julabo
>>> j = julabo.Julabo()
>>> j.open('COM4')
>>> j.getVersion()
'JULABO CORIO CD - 200F 230V 50Hz Version 2.4.1'
```

**close port**
```python
>>> j.close()
```
