import goslate
import nltk
import re
nltk.download('stopwords')
from textblob import TextBlob, Word, Blobber
gs = goslate.Goslate()

def translate(all_text):
       r = []
       for i in range(len(all_text)):         
              translated = gs.translate(all_text[i], 'en')
              r.append(translated)
       return r

def get_polarity(all_text):
       text = TextBlob(all_text)
       return text

def clean_text(text):
    text = re.sub(r'^RT[\s]+','',text)
    text = re.sub(r'https?:\/\/.*[\r\n]*','',text)
    text = re.sub(r'#','',text)
    text = re.sub(r'@[A-Za-z0-9]+','',text)
    return text

              
