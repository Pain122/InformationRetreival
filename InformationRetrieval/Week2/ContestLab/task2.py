# Team Ruslan Mihailov and Pavel Tishkin

from docx2python import docx2python as d2p
from bs4 import BeautifulSoup as bs
from bs4.element import Comment
import speech_recognition as sr
import requests
import textract
import re

def get_loot(text):
    m = re.search('L[0|O]{2}T:([a-zA-Z ]*)', text)
    if m:
        return m.group(0)[5:].strip('\n ')
    else:
        return None

def extract_txt(data):
    return get_loot(data.content.decode('utf-8'))

def extract_jpg_pdf(data, extension):
    filename = '{}.{}'.format(extension, extension)
    with open(filename, 'wb+') as f:
        f.write(data.content)
        
    text = textract.process(filename)
    return get_loot(text.decode('utf-8'))

def extract_docx(data, extension):
    filename = '{}.{}'.format(extension, extension)
    with open(filename, 'wb+') as f:
        f.write(data.content)
        
    text = d2p(filename).text
    return get_loot(text)

def tag_visible(element):
    if element.parent.name in ['style', 'script', 'head', 'title', 'meta', '[document]']:
        return False
    if isinstance(element, Comment):
        return False
    return True

def text_from_html(body):
    soup = bs(body, 'html.parser')
    texts = soup.findAll(text = True)
    visible_texts = filter(tag_visible, texts)  
    return "".join(t for t in visible_texts)

def extract_html(data):
    text = text_from_html(data.content)
    return get_loot(text)

def extract_wav(data, extension):
    filename = '{}.{}'.format(extension, extension)
    with open(filename, 'wb+') as f:
        f.write(data.content)
    
    r = sr.Recognizer()
    audio = None
    with sr.AudioFile(filename) as source:
        audio = r.record(source)
        
    text = r.recognize_google(audio, language = 'de')
    return text

with open('input.txt', 'r') as f:
    url = f.read()

data = requests.get(url)
extension = url.split('.')[-1]

if extension == 'txt':
    loot = extract_txt(data)
elif extension in ['jpg', 'pdf']:
    loot = extract_jpg_pdf(data, extension)
elif extension == 'docx':
    loot = extract_docx(data, extension)
elif extension == 'html':
    loot = extract_html(data)
elif extension == 'wav':
    loot = extract_wav(data, extension)
    
with open('output.txt', 'w') as f:
    f.write(loot)