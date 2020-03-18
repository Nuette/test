import json
import csv
import os
import gensim
from gensim.models import Word2Vec
from collections import defaultdict
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
nltk.download('punkt')

# extract data from json files and write to one csv file ---> data.csv
# TODO adjust code so that method exept list of file paths and iterate through each folder and append the data to csv file
class DataExtract(object):
    def __init__(self, path):
        csv_data = open('data.csv', 'w')
        csvwriter = csv.writer(csv_data)
        header = ['Keyword', 'Broadcast link', 'station_name', 'Language', 'Reject reason', 'Sentence']
        csvwriter.writerow(header)
        print('open file for writing')
        self.path = path
        for filename in os.listdir(path):  # iterate through directory
            if filename.endswith(".json"):
                # Load JSON file
                with open(path + filename) as f:
                    data = json.load(f)
                    print('writing data to csv file...')
                    for data_i in data:
                        row_info = [data_i['keyword'].encode('ascii', 'ignore').decode('ascii'), data_i['details']['station_detail']['feed_path'], data_i['details']['station_detail']['station_name'], data_i['details']['station_detail']['language'], data_i['details']['reject_reason']]
                        words_temp = []
                        for word_detail in data_i['details']['words']:
                            words_temp.append(word_detail['word'])
                        sentence = ' '.join(words_temp)
                        row_info.append(sentence.encode('ascii', 'ignore').decode('ascii'))
                        csvwriter.writerow(row_info)
        print("data extraction complete")


def get_station(path, language):
    station = defaultdict(int)
    for filename in os.listdir(path):  # iterate through directory
        if filename.endswith(".json"):
            # Load JSON file
            with open(path + filename) as f:
                data = json.load(f)
                for data_i in data:
                    if data_i['details']['station_detail']['language'] == language:
                        station[data_i['details']['station_detail']['station_name']] += 1
    print(sorted(((v, k) for k, v in station.iteritems()), reverse=True))


#organize the data according to the radio station's language
def get_language_data(path, language_list):
    # TODO: tokenize words using ICU tokenizer (that's what fasttext uses)
    stop_words = set(stopwords.words('english'))  # import stopwords for stopword removal
    # open file for writing
    for lang in language_list:
        print('extracting data for ' + lang + ": ")
        filename = lang + '_data.csv'
        csv_data = open(filename, 'w')
        csvwriter = csv.writer(csv_data)
        header = ['Keyword', 'station_name', 'Reject reason', 'Sentence']
        csvwriter.writerow(header)
        for filename in os.listdir(path):  # iterate through directory
            if filename.endswith(".json"):
                # Load JSON file
                with open(path + filename) as f:
                    data = json.load(f)
                    # write data to csv file
                    for data_i in data:
                        if data_i['details']['station_detail']['language'] == lang:
                            row_info = [data_i['keyword'].encode('ascii', 'ignore').decode('ascii'), data_i['details']['station_detail']['station_name'], data_i['details']['reject_reason']]
                            words_temp = []
                            for word_detail in data_i['details']['words']:
                                if word_detail['word'] not in stop_words:  # remove stopwords
                                    words_temp.append(word_detail['word'])
                            sentence = ' '.join(words_temp)
                            row_info.append(sentence.encode('ascii', 'ignore').decode('ascii'))
                            #row_info.append(sentence)
                            csvwriter.writerow(row_info)
    print("Language extraction complete")
