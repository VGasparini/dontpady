import requests
from bs4 import BeautifulSoup

if __name__ == "__main__":
    url = 'http://dontpad.com/'+input('Digite o endereco: ')
    clear = True if ord(input('Deseja zerar? (s ou n): '))%2 else False
    text = input('Digite o texto: ')

    if not clear:
        link = requests.get(url)
        soup = BeautifulSoup(link.text,"html.parser")
        old_text = soup.find('textarea').get_text()
        text = old_text+'\n'+text

    data = {'text':text}
    r = requests.post(url = url, data = data)
    if '200' in str(r):
        print('Deu boa, olha la')
    else:
        print('Deu ruim...')