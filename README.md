# Search Challenge

Search Challenge is a challenge finding most relevant products for a user query.

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

# Document Structure

A document contains:
* a unique *id*
* a *name* of the product with common information like color, type of clothes, etc.
* the *brand* of the product

# TF-IDF

To find relevant documents, we compute a score based on TF-IDF.

Recall that TF gives the frequency of a term into a text.

While IDF gives the importance of a term in a corpus of documents.

# Pre-processing

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


# *Magic* Formula

For each word of a query, we add up the tfidf of the word.

<img src="https://render.githubusercontent.com/render/math?math=\sum_{k}^{} tfidf(w_k,d)">

* *w*, k-th word of a query
* *d*, current document

# Example

Let's find "yellow toywatch" as an example

```
python search.py "yellow toywatch"
```

Our algorithm returns

```
Score: 2.660508157504646, {'id': 4838, 'name': 'Jelly Time Only watch yellow', 'brand': 'Toywatch'}
Score: 2.384013737986109, {'id': 49638, 'name': 'Blue Jelly Watch', 'brand': 'Toywatch'}
Score: 2.1423313310278136, {'id': 66641, 'name': 'Sammy', 'brand': 'Yellow Box'}
Score: 2.1423313310278136, {'id': 4083, 'name': 'Ablaze', 'brand': 'Yellow Box'}
Score: 1.6067484982708604, {'id': 1046, 'name': 'Medis Earbuds Yellow', 'brand': 'Urbanears'}
Score: 1.6067484982708604, {'id': 50865, 'name': 'Fossil Yellow Bracelet Watch', 'brand': 'Fossil'}
Score: 1.6067484982708604, {'id': 24758, 'name': 'Yellow Tiered Tee', 'brand': 'Topshop'}
Score: 1.5893424919907393, {'id': 56368, 'name': 'Fluo Time Only watch black/white', 'brand': 'Toywatch'}
Score: 1.5893424919907393, {'id': 56383, 'name': 'Gems pavé set watch white', 'brand': 'Toywatch'}
Score: 1.5893424919907393, {'id': 4833, 'name': 'Jelly Time Only watch black', 'brand': 'Toywatch'}
```

The first document is the only one of the sample containing both words "yellow" and "toywatch".

```
Score: 2.660508157504646, {'id': 4838, 'name': 'Jelly Time Only watch yellow', 'brand': 'Toywatch'}
```

The score logically is relatively high.

By analysing the corpus we see that "yellow" appears into 112 documents while "toywatch" appears into 5 documents. Consequently, "toywatch" has more weight.

```
Score: 2.384013737986109, {'id': 49638, 'name': 'Blue Jelly Watch', 'brand': 'Toywatch'}
Score: 2.1423313310278136, {'id': 66641, 'name': 'Sammy', 'brand': 'Yellow Box'}
Score: 2.1423313310278136, {'id': 4083, 'name': 'Ablaze', 'brand': 'Yellow Box'}
```

By comparing top 2, 3 and 4, we see that even if the document 49638 has 1 more words than the 2 others the weight of "toywatch" gives more importance to the document.

# Indexes

Dealing with huge data may be time and space consuming. We created several indexes to access data in O(1) as much as possible. All indexes are stored into a single Python dictionnary and is saved as a json file.

## By IDs

The first one, stores documents by ids

```
{ 
  12829: {
    'id': 12829,
    'name': 'Teens Jess Military Ponte Roma Shift Dress',
    'brand': 'Boohoo',
    'bag_of_words': ['shift', 'roma', 'dress', 'military', 'ponte', 'teens', 'jess', 'boohoo']
  },
  35115: {
    'id': 35115,
    'name': 'Military S/S Scoop-Neck T-Shirt',
    'brand': 'Splendid',
    'bag_of_words': ['splendid', 'military', 'scoop-neck', 't-shirt', 's/s']
  },
  ...
}
```

This index avoids looking a document into a list which would cause O(n) operations.

## By Terms

The second index gives, for a given word, all documents containing that word.

```
{
  'renoir': [46983, 46304, 14502, 2106, 1727, 19927, 33194, 46989],
  'grandstand': [5863],
  'henderson': [21293, 386],
  'fordham': [21293],
  'splendour': [62603, 10386, 14789],
  'waterlily': [24143, 18737],
  '511': [52212, 44252, 17500, 36804, 17371],
  'classic-fit': [31112, 26397, 7189, 36209],
  ...
}
```

This index helps in computing the IDF efficiently.

# Installation

## Requirements

   - Python 3.6.7
   - Pip 19.2.3
   - Data set of products in a file named `search_dataset.json`

## Install dependencies

First of all, install all needed libraries

```
pip install -r requirements.txt
```

## Create indexes

Then, you create all indexes

```
make index
```

## Launch queries

You can test predefined queries

```
make test
```

## Test with your queries

You are free to call

```
python search.py "your query"
```

Or you can the call to the test Makefile directive

# Further improvements

- Remove brand in queries and make TF-IDF on names and levenstein on brand.