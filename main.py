import nltk
from nltk.tokenize import PunktSentenceTokenizer

f = open ( 'my-test-file.txt' , 'rU')
raw = f.read()
tokens = nltk.word_tokenize ( raw )
train_text = nltk.Text( tokens )

f2 = open ( 'my-sample-file.txt', 'rU')
raw = f2.read()
tokens = nltk.word_tokenize ( raw )
sample_text = nltk.Text ( tokens )

custom_sent_tokenizer = PunktSentenceTokenizer ( train_text )
tokenized = custom_sent_tokenizer( sample_text )

def process_content():
    try:
        for i in tokenized[:5]:
            words = nltk.word_tokenize( i )
            tagged = nltk.pos_tag( words )
            print( tagged )

    except Exception as e:
        print ( str ( e ))

process_content()

#print superlatives
superlatives = list()
comparatives = list()
adjectives = list()
adj_comparative = list()
adj_superlative = list()
ord_adverbs = list()

def superlatives():
    for tagged_word in tagged:
        for word in tagged_word:
            if ( word [ 1 ] == 'RBS' )
                superlatives.append ( word [1] )

def comparatives():
    for tagged_word in tagged:
        for word in tagged_word:
            if ( word [ 1 ] == 'RBR')
                comparative.append ( word[1] )

def adjectives():
    for tagged_word in tagged:
        for word in tagged_word:
            if ( word [ 1 ] == 'JJ')
                adjectives.append ( word[ 1 ] )

def adj_comparative():
    for tagged_word in tagged:
        for word in tagged_word:
            if ( word[1] == 'JJR')
                adj_comparative.append( word[1])

def adj_superlative():
    for tagged_word in tagged:
        for word in tagged_word:
            if ( word[1] == 'JJS' )
                adj_superlative.append ( word[1] )

def ord_adverbs ():
    for tagged_word in tagged:
        for word in tagged_word:
            if ( word[1] == 'RB' )
                ord_adverbs.append( word[1] )


superlatives() #most, best
comparatives() #better
adjectives() #description before noun
adj_comparative() #better
adj_superlative() #best
ord_adverbs() #very, silently









