from __future__ import division
import fasttext
import pandas as pd
from pycountry import languages
import re
import csv
from whatlang import WhatLang
import unicodedata

PRETRAINED_MODEL_PATH = '/home/nuette/PycharmProjects/Pre/lid.176.bin'
model = fasttext.load_model(PRETRAINED_MODEL_PATH)

# Kan nie Salid gebruik om die LID te doen nie, want hy vat net sekere grootte sinne, maar ek kan nie agter kom wat die grootte is nie, daar staan niks in die dokumentasie nie. Hy vat ook baie lank.
# fasstex se LID is vinnig, maar identifiseer beina al die sinne as Engels

# Gaan deur die data.csv file (geginereer deur extract.py)
# identifiseer al die Engelse sinne met fasttext lid en save hulle na die golden.csv file saam met die radio stasie se taal.
# Save ook die sinne alleen na golden_sentences.txt


def get_language_ID(language_list):
    # open file for writing
    golden_data = open('golden_corpus.csv', 'w')  # sentences identified as English
    other_data = open('mix_corpus.csv', 'w')  # sentences in other languages
    goldenwriter = csv.writer(golden_data)
    otherwriter = csv.writer(other_data)
    header = ['station_name', 'station_language', 'identified_language', 'confidence_score', 'Sentence']
    goldenwriter.writerow(header)
    otherwriter.writerow(header)
    textFile = open("golden_sentences.txt", "w+")  #save golden sentences - english sentences

    regex = r"\w__(\w\w)"
    #########

    filename = 'data.csv'
    df = pd.read_csv(filename)
    sentences_list = df['Sentence'].tolist()
    station_list = df['station_name'].tolist()
    station_lang = df['Language'].to_list()
    x = 0
    for sentence in sentences_list:
        predictions = model.predict(sentence)
        predicted_lang = predictions[0][0].encode('ascii', 'ignore')
        prediction_score = str(predictions[1][0])
        matches = re.search(regex, predicted_lang)
        if matches:
            language_name = languages.get(alpha_2=matches.group(1)).name
            row_info = [station_list[x], station_lang[x], language_name, prediction_score, sentence]
            if language_name == 'English':
                if prediction_score >= 0.8:
                    # write data to golden corpus file
                    goldenwriter.writerow(row_info)
                    textFile.write(sentence + '\n')
                else:
                    # write data to other file
                    otherwriter.writerow(row_info)
            else:
                #ander tale
                row_info = [station_list[x], station_lang[x], language_name, prediction_score, sentence]
                otherwriter.writerow(row_info)
            x = x + 1
    print('done')


# identify the language of each word in the golden_sentences.txt file


def get_word_lid():
    wl = WhatLang()
    tagged_data = open("lid_tagged_corpus.txt", "w")
    with open('golden_sentences.txt') as f:
        print('identifing the language of words')
        corpus = f.readlines()
        for line in corpus:
            list_tagged = []
            word_list = line.split(' ')
            for w in word_list:
                pred = wl.predict_lang(w)
                if pred != "not_enough_text":
                    if pred == 'UNKNOWN_LANGUAGE':#if the language is unknown
                        lang = 'UNK'
                    else:
                        lang = unicodedata.normalize('NFKD', pred).encode('ascii', 'ignore')
                    tagged_word = w + '_' + lang
                    list_tagged.append(tagged_word)
            tagged_line = ' '.join([str(elem) for elem in list_tagged])
            tagged_data.writelines(tagged_line)
            print("sentence tagged")
