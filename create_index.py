import os
import sys
import json
import inspect
import html
import utils # see utils.py

def build_index_of_products_by_id(products):

    """
    Build an index of products using ID as key (ID -> products).
    """

    print ("{:40}".format(inspect.stack()[0][3]), end='', flush=True)
    products_by_id = {}
    for product in products:
        products_by_id[product["id"]] = product
    return products_by_id


def build_index_of_bag_of_words_by_id(products_by_id):

    """
    Build an index of bows using ID as key (ID -> bows).
    """

    print ("{:40}".format(inspect.stack()[0][3]), end='', flush=True)
    bow_by_id = {}
    for id in products_by_id:
        bow_by_id[id] = {}
        product = products_by_id[id]
        split_name = set(html.unescape(product["name"])
                         .replace('"', '').replace("'", '')
                         .lower()
                         .split())
        split_brand = set(html.unescape(product["brand"])
                          .replace('"', '').replace("'", '')
                          .lower()
                          .split())
        bow_by_id[id] = list(split_name.union(split_brand))
    return bow_by_id


def build_index_of_ids_by_brand(products_by_id):

    """
    Build an index of IDs using brand as key (brand -> IDs).
    """

    print ("{:40}".format(inspect.stack()[0][3]), end='', flush=True)
    ids_by_brand = {}
    for id in products_by_id:
        current_brand = products_by_id[id]["brand"].replace("*","").replace("+", "").lower()
        if not current_brand in ids_by_brand:
            ids_by_brand[current_brand] = []
        ids_by_brand[current_brand].append(id)
    return ids_by_brand

            
def build_index_of_ids_by_term(bows_by_id):

    """
    Build an index of IDs using term as key (term -> IDs).
    """

    print ("{:40}".format(inspect.stack()[0][3]), end='', flush=True)
    ids_by_term = {}
    for id in bows_by_id:
        for term in bows_by_id[id]:
            if not term in ids_by_term:
                ids_by_term[term] = []
            ids_by_term[term].append(id)
    return ids_by_term

def build_index_of_ids_by_collocation(ids_by_term, bows_by_id):

    """
    Build an index of IDs using collocation as key (terms -> IDs)
    """

    print ("{:40}".format(inspect.stack()[0][3]), end='', flush=True)
    ids_by_collocation = {}
    for term in ids_by_term:
        ids_by_collocation[term] = {}
        for collocation_id in ids_by_term[term]:
            for collocation_term in bows_by_id[collocation_id]:
                if collocation_term != term:
                    if collocation_term not in ids_by_collocation[term]:
                        ids_by_collocation[term][collocation_term] = []
                    ids_by_collocation[term][collocation_term].append(collocation_id)
    return ids_by_collocation

def dump_index(index, filename):
    print ("{:40}".format(inspect.stack()[0][3]), end='', flush=True)
    index_file = open(filename,"w")
    json.dump(index, index_file)
    index_file.close()
            
if __name__ == "__main__":

    index = {}
    products = json.load(open("search_dataset.json"))
    index_filename = "index.json"
    
    index["products_by_id"] = utils.call_with_monitor_1(
        build_index_of_products_by_id,
        products)
    
    index["bows_by_id"] = utils.call_with_monitor_1(
        build_index_of_bag_of_words_by_id,
        index["products_by_id"])
    
    index["ids_by_brand"] = utils.call_with_monitor_1(
        build_index_of_ids_by_brand,
        index["products_by_id"])
    
    index["ids_by_term"] = utils.call_with_monitor_1(
        build_index_of_ids_by_term,
        index["bows_by_id"])
    
    index["ids_by_collocation"] = utils.call_with_monitor_2(
        build_index_of_ids_by_collocation,
        index["ids_by_term"],
        index["bows_by_id"])

    utils.call_with_monitor_2(dump_index, index, index_filename)
    print ("{:40}".format(index_filename), end='', flush=True)
    print(utils.convert_size(os.stat(index_filename).st_size))
