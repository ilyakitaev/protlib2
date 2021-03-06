# protlib2
Fork of http://courtwright.org/protlib/ with additional functionality

## Additional classes and parameters:

### CArrayWO
CArrayWO - Inherited from CArray. Uses global packed size field and offset to count it's own size

Example:

```
class SomeCommand(CStruct):
  pnum = CUChar(always=0x01)
  size = CUShort()
  data = CArrayWO(-3, "size", CUChar()) 
```

### Conditional fields
  
cond and cond_filed are used to include/exclude field from parsing 
  
Example:

```  
class SomeCondCommand(CStruct):
  pnum = CUChar(always=0x02)
  size = CUShort()
  static1 = CUInt()
  static2 = CUShort()
  conditional1 = CUShort(cond=lambda f: f & 0x80000000, cond_field="static1")
  conditional2 = CUChar(cond=lambda f: f & 0x8000, cond_field="static2")
  static2 = CUShort()
  static4 = CUShort()
```

Fields conditional1 and conditional2 will be added to result object only if conditions are true


### Byte Order
Byte Order can be set for an individual field by passing byte_order=LITTLE_ENDIAN or BIG_ENDIAN

Example:

```
class SomeLittleEndianCommand(CStruct):
  pnum = CUChar(always=0x01)
  size = CUShort(byte_order=LITTLE_ENDIAN)
```

Note: You can of course still overwrite global BYTE_ORDER by changing the format-string
    e.g. protlib.BYTE_ORDER=b"<" # Little Endian
            or
         protlib.BYTE_ORDER=LITTLE_ENDIAN