import numpy as np
import lda
import lda.datasets
X = lda.datasets.load_reuters()
vocab = lda.datasets.load_reuters_vocab()
titles = lda.datasets.load_reuters_titles()
print X.shape

print np.array(vocab).shape
print np.array(titles).shape

print X
print vocab
print titles

print X[0].sum()
print X[1].sum()
print X[2].sum()
print X[3].sum()
print X[4].sum()
print titles[0]
# print X.sum()

# model = lda.LDA(n_topics=20, n_iter=1500, random_state=1)
# model.fit(X)  # model.fit_transform(X) is also available
# topic_word = model.topic_word_  # model.components_ also works
# n_top_words = 8
# for i, topic_dist in enumerate(topic_word):
# 	topic_words = np.array(vocab)[np.argsort(topic_dist)][:-n_top_words:-1]
# 	print('Topic {}: {}'.format(i, ' '.join(topic_words)))