
from nltk.corpus import stopwords
from nltk.stem.snowball import SnowballStemmer
from nltk import RegexpTokenizer

stop_words = set(stopwords.words("spanish"))
stemmer = SnowballStemmer("spanish")

def text_preprocess(text):
    tokenizer = RegexpTokenizer(r'\w+')
    tokens = tokenizer.tokenize(text.lower())
    tokens = [word for word in tokens if word not in stop_words]
    tokens = [stemmer.stem(word) for word in tokens]
    return ' '.join(tokens)
