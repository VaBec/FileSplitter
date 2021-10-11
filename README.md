# FileSplitter

This script splits a textfile into smaller Files.

## How To

- Install python
- Add your .txt file to the same directory of the FileSplitter.py
- Open cmd (win + "cmd") in the directory of the script. Run the Script with your arguments.

```
python FileSplitter.py test.txt 500000
```

The Splitter reads "test.txt" and generates (overwrites existing) new Files under "./output" with the amount of lines specified (e.g. 500000).