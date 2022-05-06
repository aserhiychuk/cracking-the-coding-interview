from collections import Counter
import unittest


def sparse_similarity(documents):
    '''
    17.26 Sparse Similarity: The similarity of two documents (each with distinct 
    words) is defined to be the size of the intersection divided by the size of 
    the union. For example, if the documents consist of integers, the similarity 
    of {1, 5, 3} and {1, 7, 2, 3} is 0.4, because the intersection has size 2 and 
    the union has size 5.

    We have a long list of documents (with distinct values and each with an associated ID) 
    where the similarity is believed to be "sparse."That is, any two arbitrarily selected 
    documents are very likely to have similarity 0. Design an algorithm that returns a list 
    of pairs of document IDs and the associated similarity.
    
    Print only the pairs with similarity greater than 0, Empty documents should not be 
    printed at all. For simplicity, you may assume each document is represented as an array 
    of distinct integers. 

    EXAMPLE

    Input:
    13: {14, 15, 100, 9, 3}
    16: {32, 1, 9, 3, 5}
    19: {15, 29, 2, 6, 8, 7}
    24: {7, 10}

    Output:
    ID1, ID2 : SIMILARITY
    13, 19   : 0.1
    13, 16   : 0.25
    19, 24   : 0.14285714285714285
    '''
    elements = {}

    for doc_id, document in documents.items():
        for el in document:
            if el not in elements:
                elements[el] = []

            elements[el].append(doc_id)

    n_common = Counter()

    for _, docs in elements.items():
        if len(docs) == 1:
            continue

        for i in range(len(docs)):
            for j in range(i + 1, len(docs)):
                doc1 = docs[i]
                doc2 = docs[j]

                if doc1 > doc2:
                    doc1, doc2 = doc2, doc1

                n_common[(doc1, doc2)] += 1

    result = {}

    for (doc1, doc2), n in n_common.items():
        result[(doc1, doc2)] = n / (len(documents[doc1]) + len(documents[doc2]) - n)

    return result


class SparseSimilarityTest(unittest.TestCase):
    def test_sparse_similarity(self):
        documents = {
            13: [14, 15, 100, 9, 3],
            16: [32, 1, 9, 3, 5],
            19: [15, 29, 2, 6, 8, 7],
            24: [7, 10]
        }

        actual = sparse_similarity(documents)
        expected = {
            (13, 19): 0.1, 
            (13, 16): 0.25, 
            (19, 24): 0.14285714285714285
        }
        self.assertDictEqual(expected, actual)


if __name__ == '__main__':
    unittest.main()
