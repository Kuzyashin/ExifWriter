PyExifWriter tool

Input - Template with rule, tags data, file   
Output - File

Check example.py

You can overload delimiter (default = "; ")

```
from writer import ExifWriter
example_writer = ExifWriter()
example_writer.delimiter = ", "
```