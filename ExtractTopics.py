from gensim.corpora import Dictionary, HashDictionary, MmCorpus, WikiCorpus
from gensim.models import TfidfModel, LdaModel
from gensim.utils import smart_open, simple_preprocess
from gensim.corpora.wikicorpus import _extract_pages, filter_wiki
from gensim import corpora
from gensim.models.ldamulticore import LdaMulticore

wiki_corpus = MmCorpus('Wiki_Corpus.mm')   # Loading the corpus 
print (".... successfully loaded the corpus")

wiki_dict = Dictionary.load('WikiDictionary200k.dict') # Loading the dictionary
print (".... successfully loaded the dictionary")

lda = LdaMulticore(corpus=wiki_corpus, id2word=wiki_dict, num_topics=300, chunksize=10000, passes=2)

print ".... successfully extracted the topics; saving the model"
lda.save('WikiLDA_300.lda')

print "finished ...."
