import nltk
from nltk.stem import PorterStemmer
from nltk.corpus import stopwords

f = open ( "DTStateofUnion2019.txt").read()
tokens = nltk.word_tokenize ( f )
#print ( tokens ) #list of words, each word is a string

tagged_list = list()

#code added on sunday, 10/10

def remove_noise ( tokens ):
    filtered_tokens = list()
    noise_words = set ( stopwords.words ( "english"))
    for w in tokens:
        if w not in noise_words:
            filtered_tokens.append ( w )
    return filtered_tokens

filtered_tokens = list()
filtered_tokens = remove_noise ( tokens )

def stemming ( filtered_tokens ):
    ps = PorterStemmer()
    stemmed_words = list()
    for w in filtered_tokens:
        stemmed_words.append ( ps.stem ( w ) )
    return stemmed_words

filter_and_stem_tokens = list( )
filter_and_stem_tokens = stemming ( filtered_tokens )

def pos_tagger ( filter_and_stem_tokens ):
    pos_tag_list = nltk.pos_tag ( filter_and_stem_tokens )
    return ( pos_tag_list )

tagged_list = pos_tagger( filter_and_stem_tokens )


def add_postag_before_word( tagged_list ):
    tag_first_list = list()
    for pos_tagged_token in tagged_list:
        tag_first_list.append ( pos_tagged_token[ 1 ] + ":" + pos_tagged_token[ 0 ])

    return tag_first_list

def output_to_file ( tag_first_list ):
    #outputs the words as strings into a file so that its somewhat readable
    tagged_text_file = open ( "tagged_file.txt", "w")
    for word in tag_first_list:

        if word == ".:.":
            tagged_text_file.write ( word + "\n\n" )

        else:
            tagged_text_file.write ( word + " ")

output_to_file ( add_postag_before_word ( tagged_list ) )

#reduce words to stem form



















