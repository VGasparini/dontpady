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
- Then asks if you want to see atual content
- Third one means if you want to clear or not atual page
- And last one is finally your new text

### Command line usage:

Commands:

-h, --help                Show this help message and exit
-f FILE, --file FILE      File path
-i INPUT, --input INPUT   Input text from user
-c, --clear               Clear the page before put the new content
-o, --output              Print actual text in dontpad address
-k KEY, --key KEY         Key to encrypt/decrypt


Update text erasing atual text

`dontpady.py -i -c 'Testing text' test_path'`

Append new text at end of atual text

`dontpady.py -i 'Testing text' test_path `

Writing with crypto key

`dontpady.py -i 'Testing text' -k 'testing key' test_path`

Input text from file

`dontpady.py -f /file/path/text.txt test_path`

Just print atual text

`dontpady.py -o test_path`

Decrypt atual text

`dontpady.py -k 'testing key' -o test_path`
