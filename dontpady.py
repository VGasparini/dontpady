from sys import argv
from requests import post,get
from bs4 import BeautifulSoup

def pull(path):
    data = get(url=path)
    soup = BeautifulSoup(data.text,"html.parser")
    old_text = soup.find('textarea').get_text()
    return old_text

def push(path, clear, text):
    
    if not clear:
        old_text = pull(path)
        text = old_text+'\n\n'+text

    data = {'text':text}
    
    return True if '200' in str(post(url=path, data=data)) else False

if len(argv) == 1:
    path = 'http://dontpad.com/'+input('dontpad.com/')
    print('\nText on',path,'\n\n'+pull(path),'\n') if ord(input('Print atual text? y/n: '))%2 else False
    clear = True if ord(input('Clear atual text? y/n: '))%2 else False
    text = input('New text to input: ')

    if push(path,clear,text):
        print('Finished')
    else:
        print('Error')

else:
    if argv[1] == '-i' or argv[1] == '--input':
        if '-c' in argv:
            path  = 'http://dontpad.com/'+argv[3]
            clear = True
            text  = input() if len(argv)==4  else argv[4]
        else:
            path  = 'http://dontpad.com/'+argv[2]
            clear = False
            text  = input() if len(argv)==3  else argv[3]
        if push(path,clear,text):
            print('Finished')
        else:
            print('Error')

    elif argv[1] == '-o' or argv[1] == '--output':
        path = 'http://dontpad.com/'+argv[2]
        clear = True if '-c' or '--clear' in argv else False
        print(pull(path))

    elif argv[1] == '-c' or argv[1] == '--clear':
        path  = 'http://dontpad.com/'+argv[2]
        clear = True
        text  = ''
        if push(path,clear,text):
            print('Finished')
        else:
            print('Error')

    elif argv[1] == '-h' or argv[1] == '--help':
        print('usage: dontpady.y [-h | --help] [-i | --input <path> <text>]\n',
            '[-o | --ouput <path>] [-c | --clear <path>]\n')
        print('Common uses:')
        print("Update text erasing atual text")
        print("    dontpady.py -i -c test_path 'Testing text'")
        print("Append new text at end of atual text")
        print("    dontpady.py -i test_path 'Testing text'")
        print("Input text from file")
        print("    dontpady.py -i test_path < file")
        print("Just print atual text")
        print("    dontpady.py -o test_path")
        print("Save atual text in file")
        print("    dontpady.py -o test_path > file")
        print("Just clear atual text")
        print("    dontpady.py -c test_path")

    else:
        print('Unknown option\n\nusage: dontpady.y [-h | --help] [-i | --input <path> <text>]\n',+
            '[-o | --ouput <path>] [-c | --clear <path>]\n\nmade by github.com/vgasparini')