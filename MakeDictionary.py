from gensim.corpora import Dictionary, HashDictionary, MmCorpus, WikiCorpus
from gensim.models import TfidfModel
from gensim.utils import smart_open, simple_preprocess
from gensim.corpora.wikicorpus import _extract_pages, filter_wiki

# Takes 6Hrs

stop_words = []

sw = file('stop_words.txt', 'r')
for word in sw:
    word = word.strip().strip('\n')
    if word not in stop_words:
        stop_words.append(word)
sw.close()

stop_words = set(stop_words)


def tokenize(text):
	global stop_words 
	return [token for token in simple_preprocess(text) if token not in stop_words]

def iter_wiki(dump_file):
    """Yield each article from the Wikipedia dump, as a `(title, tokens)` 2-tuple."""
    ignore_namespaces = 'Wikipedia Category File Portal Template MediaWiki User Help Book Draft'.split()
    for title, text, pageid in _extract_pages(smart_open(dump_file)):
        text = filter_wiki(text)
        tokens = tokenize(text)
        if len(tokens) < 50 or any(title.startswith(ns + ':') for ns in ignore_namespaces):
            continue  # ignore short articles and various meta-articles
        yield title, tokens


wiki_stream = (tokens for _, tokens in iter_wiki('enwiki-latest-pages-articles.xml.bz2'))

print "making of dictionary started"
wiki_dictionary = Dictionary(wiki_stream)
print "wikipedia dictionary made"

wiki_dictionary.filter_extremes(no_below=10, no_above=0.3, keep_n=200000)

print "...... saving the dictionary"
wiki_dictionary.save('WikiDictionary200k.dict')
print "dictionary saved ........"

# wiki = WikiCorpus('enwiki-latest-pages-articles.xml.bz2')  # make a corpus from wiki dump

# MmCorpus.save_corpus('WikiCorpus.mm', wiki) # Saving the corpus


