import argparse
from sys import argv
from requests import post,get
from bs4 import BeautifulSoup

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
        url =url.replace("dontpad.com", "")
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
        text = input('Enter the text: ')

    return text

# Build the text to be sent
def buildText(inputUser, filePath, clear, url):
    text = getText(inputUser, filePath)
    if(not clear):
        link = get(url)
        soup = BeautifulSoup(link.text,"html.parser")
        old_text = soup.find('textarea').get_text()
        text = old_text + "\n" + text
    return text

def main(args):
    # Validate URL
    url = validateUrl(args.url)

    # Build text
    text = buildText(args.input, args.file, args.clear, url)

    # Send text
    response = push(url, text)

    if str(response.status_code).startswith("20"):
        if(args.output):
            print(pull(url))
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
    parser.add_argument("url", type = str, help = "Dontpad's address")
    args = parser.parse_args()

    main(args)