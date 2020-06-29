# Search Challenge

Search Challenge is a challenge finding most relevant products from a user query.

For instance, 

```
python search.py "prada shirt"
```

would print

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

## TF-IDF Based Score

To find relevant documents, we compute a score based on TF-IDF.

Recall that TF gives the frequency of a term into a text, while IDF gives the importance of a term in a corpus of documents.

A query mixes brand name and product name in a undetermined order, we preprocessed products' documents in a way that brand and name are merged together for each document as a list of words.

For instance,

```
{
  'id': 55451,
  'name': "'Hurric' Jacket",
  'brand': 'K-Way',
  'bag_of_words': ['k-way', 'hurric', 'jacket']
}
```

Note that we cleaned data by lowering entry, removing special characters, and decoding HTML escaped characters.

# Indexes

# Installation

