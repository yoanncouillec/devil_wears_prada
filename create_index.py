import os
import sys
import json
import time
import inspect
import html
import math

def convert_size(size_bytes):
   if size_bytes == 0:
       return "0B"
   size_name = ("B", "KB", "MB", "GB", "TB", "PB", "EB", "ZB", "YB")
   i = int(math.floor(math.log(size_bytes, 1024)))
   p = math.pow(1024, i)
   s = round(size_bytes / p, 2)
   return "%s %s" % (s, size_name[i])

def build_index_of_products_by_id(products):

    """
    Build an index of products using ID as key.
    """

    print ("{:40}".format(inspect.stack()[0][3]), end='', flush=True)
    products_by_id = {}
    for product in products:
        products_by_id[product["id"]] = product
    return products_by_id


def build_index_of_bag_of_words_by_id(products_by_id):

    """
    Build an index of bows using ID as key.
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
    Build an index of IDs using brand as key.
    """

    print ("{:40}".format(inspect.stack()[0][3]), end='', flush=True)
    ids_by_brand = {}
    for id in products_by_id:
        current_brand = products_by_id[id]["brand"].lower()
        if not current_brand in ids_by_brand:
            ids_by_brand[current_brand] = []
        ids_by_brand[current_brand].append(id)
    return ids_by_brand

            
def build_index_of_ids_by_term(bows_by_id):

    """
    Build an index of IDs using term as key.
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
    Build an index of IDs using collocation as key.
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
            
def call_with_monitor_2(func, arg0, arg1):
    begin = time.time()
    ret = func(arg0, arg1)
    end = time.time()
    print(" {:.3f} s".format(end - begin))
    return ret
    
def call_with_monitor_1(func, arg0):
    begin = time.time()
    ret = func(arg0)
    end = time.time()
    print(" {:.3f} s".format(end - begin))
    return ret
    
def call_with_monitor_0(func):
    begin = time.time()
    ret = func()
    end = time.time()
    print(" {:.3f} s".format(end - begin))
    return ret
    
if __name__ == "__main__":

    index = {}
    products = json.load(open("search_dataset.json"))
    index_filename = "index.json"
    
    index["products_by_id"] = call_with_monitor_1(build_index_of_products_by_id,
                                                  products)
    index["bows_by_id"] = call_with_monitor_1(build_index_of_bag_of_words_by_id,
                                              index["products_by_id"])    
    index["ids_by_brand"] = call_with_monitor_1(build_index_of_ids_by_brand,
                                                index["products_by_id"])
    index["ids_by_term"] = call_with_monitor_1(build_index_of_ids_by_term,
                                               index["bows_by_id"])
    index["ids_by_collocation"] = call_with_monitor_2(build_index_of_ids_by_collocation,
                                                      index["ids_by_term"],
                                                      index["bows_by_id"])

    call_with_monitor_2(dump_index, index, index_filename)
    print ("{:40}".format(index_filename), end='', flush=True)
    print(convert_size(os.stat(index_filename).st_size))
