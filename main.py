from extract import DataExtract
from LI import get_language_ID
from LI import get_word_lid
#from extract import get_station
#from extract import get_language_data
#from WordVector import train_w2v
#from evaluate_w2v import plot_vector
#from evaluate_w2v import get_w2v_data
#from evaluate_w2v import display_closestwords_tsnescatterplot
#from FastTextVector import train_fasttext
#from FastTextVector import fasttext_evaluate
#from Glovevector import train_glove, glove_evaluate
#from LI import get_word_language
#
#from evaluate_fasttext import get_fasttext_data
#from FastTextVector import display_closestwords_tsnescatterplot_fasttext

if __name__ == '__main__':
    run_process = True
    path = 'data/False_Positives_with_words_2019-10-31-2019-11-30_with_ids/'
    csv_file = 'golden_corpus.csv'
    embedding_dimension = 300
    method = 'skipgram'  # skipgram/cbow
    lr = 0.05  # the higher the lr, the faster the model converge to a solution but at risk of overfitting to the dataset  stay in range [0.01,1]
    epoch = 30
    ngram_min = 2
    ngram_max = 5
    word = 'disney'
    word2 = 'car'
    word3 = 'toyota'
    test_sentence = ['car', 'bank', 'nedbank', 'gautrain', 'saa', 'capitec', 'amazon', 'airlines', 'ford', 'investment', 'sasol', 'heineken', 'sandton', 'products', 'deloitte', 'spokesperson']
    word_list = ["green", "blue", "red", "toyota"]
    language = 'Afrikaans'
    langauge_list = ['English', 'Afrikaans', 'Zulu', 'Xhosa', 'Sesotho', 'Venda', 'Sepedi', 'Swati', 'Setswana', 'Hindi']

    if run_process:
        #data = DataExtract(path)  # onttrek al die data na 'n csv file
        #get_language_data(path, langauge_list) #onttrek slegs data van 'n gespesifiseerde taal
        #get_station(path, language) #kry die aantal sinne per stasie per taal
        #get_language_ID(langauge_list)  # pas language ID op al die sinne toe,  skryf die sinne wat as engels
                                        # geidentifiseer is na 'n gesamentlike file -> die is dan die hoof korpus
                                        #skryf ook stats van aantal sinne vir afr en engels wat na GC geskryf word
                                        #TODO: daar kan ook ander tale se sinne gecheck word
        get_word_lid()

        #train_w2v(csv_file, embedding_dimension)
        #get_w2v_data(word, word2, word3, word_list)

        #plot_vector()
        #display_closestwords_tsnescatterplot(test_sentence)
        #evaluate_w2v_plots(embedding_dimension)  # Evaluate word Embeddings

        #train_fasttext()
        #fasttext_evaluate(word, word2, word3, word_list)
        #get_fasttext_data(word, word2, word3)
        #display_closestwords_tsnescatterplot_fasttext(word)

        #train_glove()
        #glove_evaluate(word, word2, word3, word_list)

