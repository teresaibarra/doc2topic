from doc2topic import models, corpora
import sys

data = corpora.DocData(sys.argv[1])
model = models.Doc2Topic(data, n_topics=40)

# print(model.get_document_topics(0))
model.print_topic_words()
model.get_document_topics_json()
