from deep_translator import GoogleTranslator
import nltk
nltk.download('stopwords')
from textblob import TextBlob, Word, Blobber


def translate(all_text):
       r = []
       for i in range(len(all_text)):
              translated = GoogleTranslator(source='es', target='en').translate(all_text[i])
              r.append(translated)
       return r

def get_polarity(all_text):
       r = []
       for i in range(len(all_text)):
              text = TextBlob(all_text[i])
              r.append(text.sentiment)
       return r

              
