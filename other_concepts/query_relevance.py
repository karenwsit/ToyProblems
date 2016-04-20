"""
Equations
TF(term, doc) = # of times a given term appears in a given document
IDF(term, corpus) = log (total # of docs in a corpus/ # of docs that contain that term)
Relevance = (TF(term0)* IDF(term0)) + (TF(term1)* IDF(term1))
"""
import math

def build_dicts(query, corpus):
    tf_dict = {}
    idf_dict = {}
    total_doc_num = 0

    for doc in corpus:
        tf_dict[doc] = tf_dict.get(doc, {})  #builds out nested dic for every doc in corpus
        total_doc_num += 1   #keeps track of # of docs in the corpus
        for term in query:
            in_doc = False
            term_count = 0
            for word in doc:
                if word == term:
                    in_doc = True
                    term_count += 1
            tf_dict[doc][term] = term_count
            if in_doc:
                idf_dict[term] = idf_dict.get(term,0)+1  #number of docs that contain term

    return idf_dict, tf_dict, total_doc_num

def find_rel_score(idf_dict, tf_dict, total_doc_num, query):
    rel_score = None
    for term in query:
        num_doc_with_term = idf_dict[term]
        idf = math.log(total_doc_num/num_doc_with_term)
        for doc, inner_dict in tf_dict.iteritems():
            tf = inner_dict[term] # returns number of times a term appears in that particular doc

