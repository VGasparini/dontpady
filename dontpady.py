import argparse
import sys
from requests import post,get
from bs4 import BeautifulSoup

def calculate(key):
    k = len(key)
    result = k
    for letter in range(k):
        result += (int((bin(ord(key[letter]))[2:]).replace('0','2').replace('1','0').replace('2','1'),2)+letter)
    return result%k

def crypt(key, text):
    new_text = ''
    for letter in range(len(text)):
        new_text += chr(ord(text[letter]) + key + letter)
    
    return new_text

def decrypt(key, text):
    old_text = ''
    for letter in range(len(text)):
        try:
            old_text += chr(ord(text[letter]) - key - letter)
        except ValueError:
            old_text += '\n'
    
    return old_text

def pull(path):
    data = get(url=path)
    soup = BeautifulSoup(data.text,"html.parser")
    old_text = soup.find('textarea').get_text()

    return old_text

def push(path, text):
    data = {'text':text}

    return post(url=path, data=data)

# Some random url validation
def validateUrl(url):
    if(url.startswith("dontpad.com")):
        url = url.replace("dontpad.com/", "")
        url = url.replace("dontpad.com", "")
    if(url.startswith("https://dontpad.com")):
        url = url.replace("https://dontpad.com/", "")
        url = url.replace("https://dontpad.com", "")
    if(url.startswith("http://dontpad.com")):
        url = url.replace("http://dontpad.com/", "")
        url = url.replace("http://dontpad.com", "")

    return 'http://dontpad.com/' + url

# Get text from file or from user input
def getText(inputUser, filePath):
    text = ''
    if(filePath != None):
        try:
            with open(filePath, 'r') as file:
                for line in file:
                    text += line
        except IOError as ex:
            print("I/O error ({}): {}".format(ex.errno, ex.strerror))
            exit()
        except:
            print("Unexpected error: ", sys.exc_info()[0])
            exit()
    elif(inputUser != None):
        text = inputUser

    return text

# Build the text to be sent
def buildText(inputUser, filePath, clear, url, key):
    text = getText(inputUser, filePath)

    text = crypt(key,text) if key != None else text

    if(not clear):
        link = get(url)
        soup = BeautifulSoup(link.text,"html.parser")
        old_text = soup.find('textarea').get_text()
        text = old_text + "\n" + text

    return text

def main(args):
    # Validate URL
    url = validateUrl(args.url)
    key = calculate(args.key) if args.key != None else None

    # Build text
    text = buildText(args.input, args.file, args.clear, url, key)

    # Send text
    response = push(url, text)

    if str(response.status_code).startswith("20"):
        if(args.output):
            output = pull(url)
            if args.key != None:
                key = calculate(args.key)
                output = decrypt(key,output)
            print('Text\n',output)
        else:
            print('Success: {}'.format(url))
    else:
        print('Error')

if __name__ == "__main__":
    # Args parser
    parser = argparse.ArgumentParser()
    parser.add_argument("-f", "--file", help="File path")
    parser.add_argument("-i", "--input", type=str, help="Input text from user")
    parser.add_argument("-c", "--clear", action="store_true", help = "Clear the page before put the new content")
    parser.add_argument("-o", "--output", action="store_true", help = "Print actual text in dontpad address")
    parser.add_argument("-k", "--key", type = str, help = "Key to encrypt/decrypt")
    parser.add_argument("url", type = str, help = "Dontpad's address")
    args = parser.parse_args()

    main(args)