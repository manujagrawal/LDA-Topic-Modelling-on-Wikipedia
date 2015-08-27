from gensim.corpora import Dictionary, HashDictionary, MmCorpus, WikiCorpus
from gensim.models import TfidfModel, LdaModel
from gensim.utils import smart_open, simple_preprocess
from gensim.corpora.wikicorpus import _extract_pages, filter_wiki
from gensim import corpora


wiki_dict = Dictionary.load('WikiDictionary.dict') # Loading the dictionary
print (".... successfully loaded the dictionary")

wiki_dict.filter_extremes(no_below=5, no_above=0.5, keep_n=200000)

print "successfully filtered the extremes .... ; saving the dictionary"

wiki_dict.save('WikiDictionary200k.dict')

