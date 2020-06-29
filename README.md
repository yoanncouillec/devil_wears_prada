# Search Challenge

Search Challenge is a challenge finding most relevant products from a user query.

For instance

```
python search.py "prada shirt"
```

Prints

```
Score: xxx, {'id': 20636, 'name': 'Plaid Shirt', 'brand': 'Prada'}
Score: xxx, {'id': 20665, 'name': 'Stripe T Shirt', 'brand': 'Prada'}
Score: xxx, {'id': 64955, 'name': 'Bib Detail T Shirt', 'brand': 'Prada'}
Score: xxx, {'id': 44034, 'name': 'Beach Flip-Flop', 'brand': 'Prada'}
Score: xxx, {'id': 31747, 'name': 'Cosmetic Pouch', 'brand': 'Prada'}
Score: xxx, {'id': 31748, 'name': 'Cosmetic Pouch', 'brand': 'Prada'}
Score: xxx, {'id': 31749, 'name': 'Camera Case', 'brand': 'Prada'}
Score: xxx, {'id': 31750, 'name': 'Cosmetic Pouch', 'brand': 'Prada'}
Score: xxx, {'id': 44040, 'name': 'Floral Sneaker', 'brand': 'Prada'}
Score: xxx, {'id': 31753, 'name': 'Shoulder Bag', 'brand': 'Prada'}
```

# Score

For each user query, a list of 10 top results is returned. Each returned document is associated with a score.

## Document Structure

A document contains:
* an unique *id*
* a *name* of the product with common information like color, type of clothes, etc.
* the *brand* of the product

## TF-IDF

To find relevant documents, we compute a score based on TF-IDF.

Recall that TF gives the frequency of a term into a text.

While IDF gives the importance of a term in a corpus of documents.

## Pre-processing

A query mixes brand name and product name in a undetermined order, we pre-processed products' documents in a way that brand and name are merged together for each document as a list of words.

For instance

```
{
  'id': 55451,
  'name': "'Hurric' Jacket",
  'brand': 'K-Way',
  'bag_of_words': ['k-way', 'hurric', 'jacket']
}
```

Note that we clean data by lowering entries and decoding HTML escaped characters. We do the exact same pre-processing for queries.


## *Magic* Formula

For each word of a query, we add up the tfidf of that word related to a given product document.

<img src="https://render.githubusercontent.com/render/math?math=\sum_{k}^{} tfidf(w_k,d)">

* *w*, k-th word of the query
* *d*, current document

# Indexes

# Installation

