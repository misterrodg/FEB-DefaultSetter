# FEB Default Setter

A simple Python-based vidmap default setter for use with [FE-BUDDY](https://github.com/Nikolai558/FE-BUDDY).

## Requirements

Python3.8 or Later (Tested with Python 3.10.12)

Only imports are JSON, and OS, so it should run on a standard Python implementation.

## Instructions for use

1. Copy or move (the original files will not be overwritten) the files from the `FE-BUDDY_OUTPUT/CRC/vNAS BATCH UPLOAD` directory in to the `feb_source` directory.
2. Run the following command:
   <br/>
   ```
   python3 setdefaults.py
   ```
3. The resulting files will be found in an `output` directory.

### Optional Command Line Arguments

By default, the script looks for the defaults file in the `feb_source` directory, in a file called `vNAS_Defaults.txt`. It will then place all of the processed files in an `output` directory.

Each of these can be overridden by the following command line flags:

1. `--sourcedir` - Sets the source directory path (relative or full).

```
Example:
--sourcedir "/Users/kyle/Downloads"
```

2. `--outputdir` - Sets the output directory path (relative or full). It will create it if it does not currently exist.

```
Example:
--outputdir "/Users/kyle/Documents"
```

3. `--defaultsfile` - Sets the filepath of the defaults file.

```
Example:
--defaultsfile "/Users/kyle/Downloads/vNAS_Defaults.txt"
```

# Contributions

Want to contribute? Check out the [Open Issues](https://github.com/misterrodg/FEB-DefaultSetter/issues), fork, and open a [Pull Request](https://github.com/misterrodg/FEB-DefaultSetter/pulls).

## Additional Contributors

[Nikolai558](https://github.com/Nikolai558) - Compact JSON Formatting

# License

This is licensed under [GPL 3.0](./LICENSE).
