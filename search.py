from itertools import combinations
import sys
import json
import math
import re

index = json.load(open("index.json"))
products = json.load(open("search_dataset.json"))

def find_by_name(query):
    try:
        return index["by_name_vocabulary"][query]
    except:
        return []

def find_by_brand(query):
    try:
        return index["by_brand_vocabulary"][query]
    except:
        return []

def find_by_global_vocabulary(query):
    try:
        return index["by_global_vocabulary"][query]
    except:
        return []

def find_by_term(query):
    try:
        return index["ids_by_term"][query]
    except:
        return []

def find(query):
    search = {}
    for word in query.split():
        search[word] = {}
        #search[word]["name"] = len(set(find_by_name(word)))
        #search[word]["brand"] = len(set(find_by_brand(word)))
        search[word] = set(find_(word))
        #search[word]["union"] = len(set(find_by_name(word)).union(set(find_by_brand(word))))
    return search

def combination(l):
    res = list(combinations(l,1))
    for i in range(2, len(l)+1):
        res += list(combinations(l,i))
    res = list(map(lambda c: list(c), res))
    return res

def tf(term,document):
    i = 0
    for t in document:
        if t == term:
            i += 1
    return i / float(len(document))

def idf(term):
    if len(find_by_term(term)) == 0:
        return 0
    else:
        return(math.log(len(index["products_by_id"])/(len(index["ids_by_term"][term]))))

def tf_idf(term, document):
    return tf(term,document) * idf(term)

def get_brand_indexes_in_query(query, brand):
    return [m.start() for m in re.finditer(brand, query)]

def find_brand_in_query(query):
    res = []
    for brand in index["ids_by_brand"]:
        i = query.find(brand)
        if i != -1:
            q = {
                "brand": brand,
                "query": query,
                "query_without_brand": " ".join(query.replace(brand,"").strip().split()),
                "brand_weight": len(index["ids_by_brand"][brand])
            }
            res.append(q)
    return res

def get_collocation_weight(w1,w2):
    try:
        return len(index["ids_by_collocation"][c[0]][c[1]])
    except:
        return 0

if __name__ == "__main__":

    query = sys.argv[1]
    ids = set()

    print(find_brand_in_query(query))

    words = query.split()
    
    for word in words:
        x = set(find_by_term(word))
        ids = ids.union(x)

    for c in list(combinations(words, 2)):
        weight = get_collocation_weight(c[0], c[1])
        print("{} => {}".format(c, weight))
            
    results = []
        
    for id in ids:
        score = 0
        for w in query.split():
            score += tf_idf(w, index["bows_by_id"][str(id)])
        results.append({"id": id, "score": score})

    results.sort(key=lambda x: x["score"], reverse=True)

    i = 0

    if len(results) == 0:
        print("No matching documents found for query \"{}\"".format(query))
    
    for doc in results:
        print("Score: {}, {}".format(doc["score"],
                                     {
                                         "id":doc["id"],
                                         "name": index["products_by_id"][str(doc["id"])]["name"],
                                         "brand": index["products_by_id"][str(doc["id"])]["brand"]
                                     }))
        i += 1
        if i == 10:
            break;
