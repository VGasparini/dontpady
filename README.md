# dontpady

A tool for Dontpad's users in Python + requests + bs4

**Warning**: This app isn't a Dontpad official software.

--- 

## Instalation

Install `requests` and `bs4` library

```bash
pip3 install requests bs4
```

## Interface usage

- First input asks for dontpad's address
- Second one means if you want to clear or not actual page ('s'==yes | 'n'==no)
- Third one is finally your text

### Command line usage:

Commands:

- [-h | --help]
- [-i | --input <path> <text>]
- [-o | --ouput <path>]
- [-c | --clear <path>]

Update text erasing actual text

`dontpady.py -i -c test_path 'Testing text'`

Append new text at end of actual text

`dontpady.py -i test_path 'Testing text'`

Input text from file

`dontpady.py -i test_path < file`

Just print actual text

`dontpady.py -o test_path`

Save actual text in file

`dontpady.py -o test_path > file`

Just clear actual text

`dontpady.py -c test_path`