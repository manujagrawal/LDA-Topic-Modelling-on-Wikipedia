from gensim.corpora import Dictionary, HashDictionary, MmCorpus, WikiCorpus
from gensim.models import TfidfModel
from gensim.utils import smart_open, simple_preprocess
from gensim.corpora.wikicorpus import _extract_pages, filter_wiki
from gensim import corpora

# Takes 6hrs 
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

def iter_wiki(dump_file): # making a wiki token stream
    """Yield each article from the Wikipedia dump, as a `(title, tokens)` 2-tuple."""
    ignore_namespaces = 'Wikipedia Category File Portal Template MediaWiki User Help Book Draft'.split()
    for title, text, pageid in _extract_pages(smart_open(dump_file)):
        text = filter_wiki(text)
        tokens = tokenize(text)
        if len(tokens) < 50 or any(title.startswith(ns + ':') for ns in ignore_namespaces):
            continue  # ignore short articles and various meta-articles
        yield tokens

# wiki_stream = (tokens for _, tokens in iter_wiki('enwiki-latest-pages-articles.xml.bz2'))

def corpus_stream (tokenStream, dictionary):
	i = 0
	for tokens in tokenStream:
		if (i%1000) == 0 :
			print "streamed ", i, " documents "
		i+=1
		yield dictionary.doc2bow(tokens)
	
if __name__ == '__main__':
		
	print ".... loading the dictionary"
	wiki_dict =Dictionary.load('WikiDictionary200k.dict')
	print "dictionary loaded ...."

	print ".... making the serialised corpus "
	corpora.MmCorpus.serialize('Wiki_Corpus.mm', corpus_stream( iter_wiki('enwiki-latest-pages-articles.xml.bz2'), wiki_dict ) )
	print "serialised corpus made ...."
