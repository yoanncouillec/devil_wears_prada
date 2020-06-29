import sys
import json
import time
import inspect
import html

index = {}
products = json.load(open("search_dataset.json"))

def index_by_id():
    print ("{:30}".format(inspect.stack()[0][3]), end='')
    index["by_id"] = {}
    for product in products:
        split_name = set(html.unescape(product["name"])
                         .replace('"', '').replace("'", '')
                         .lower()
                         .split())
        split_brand = set(html.unescape(product["brand"])
                          .replace('"', '').replace("'", '')
                          .lower()
                          .split())
        product["bag_of_words"] = list(split_name.union(split_brand))
        index["by_id"][product["id"]] = product

def index_by_brand():
    print ("{:30}".format(inspect.stack()[0][3]), end='')
    index["by_brand"] = {}
    for product in products:
        current_brand = product["brand"].lower()
        if not current_brand in index["by_brand"]:
            index["by_brand"][current_brand] = []
        index["by_brand"][current_brand].append(product["id"])

def index_by_brand_vocabulary():
    print ("{:30}".format(inspect.stack()[0][3]), end='')
    index["by_brand_vocabulary"] = {}
    for product in products:
        current_brand = product["brand"].lower()
        for piece_of_brand in current_brand.split():
            if not piece_of_brand in index["by_brand_vocabulary"]:
                index["by_brand_vocabulary"][piece_of_brand] = []
            index["by_brand_vocabulary"][piece_of_brand].append(product["id"])

def index_by_name():
    print ("{:30}".format(inspect.stack()[0][3]), end='')
    index["by_name"] = {}
    for product in products:
        current_name = product["name"].lower()
        if not current_name in index["by_name"]:
            index["by_name"][current_name] = []
        index["by_name"][current_name].append(product["id"])

def index_by_name_vocabulary():
    print ("{:30}".format(inspect.stack()[0][3]), end='')
    index["by_name_vocabulary"] = {}
    for product in products:
        current_name = product["name"].lower()
        for piece_of_name in current_name.split():
            if not piece_of_name in index["by_name_vocabulary"]:
                index["by_name_vocabulary"][piece_of_name] = []
            index["by_name_vocabulary"][piece_of_name].append(product["id"])

def index_by_global_vocabulary():
    print ("{:30}".format(inspect.stack()[0][3]), end='')
    index["by_global_vocabulary"] = {}
    for product in products:
        current_name = product["name"].lower()
        for piece_of_name in current_name.split():
            if not piece_of_name in index["by_global_vocabulary"]:
                index["by_global_vocabulary"][piece_of_name] = []
            index["by_global_vocabulary"][piece_of_name].append(product["id"])
        current_brand = product["brand"].lower()
        for piece_of_brand in current_brand.split():
            if not piece_of_brand in index["by_global_vocabulary"]:
                index["by_global_vocabulary"][piece_of_brand] = []
            index["by_global_vocabulary"][piece_of_brand].append(product["id"])

def index_by_term():
    print ("{:30}".format(inspect.stack()[0][3]), end='')
    index["by_term"] = {}
    for id in index["by_id"]:
        for word in index["by_id"][id]["bag_of_words"]:
            if not word in index["by_term"]:
                index["by_term"][word] = []
            index["by_term"][word].append(id)

def dump_index():
    print ("{:30}".format(inspect.stack()[0][3]), end='')
    index_file = open("index.json","w")
    json.dump(index, index_file)
    index_file.close()
            
def call_with_monitor(func):
    begin = time.time()
    func()
    end = time.time()
    print(" {:.3f} s".format(end - begin))
    
if __name__ == "__main__":
    call_with_monitor(index_by_id)
    call_with_monitor(index_by_brand)
    #call_with_monitor(index_by_brand_vocabulary)
    #call_with_monitor(index_by_name)
    #call_with_monitor(index_by_name_vocabulary)
    #call_with_monitor(index_by_global_vocabulary)
    call_with_monitor(index_by_term)
    call_with_monitor(dump_index)
    print(index["by_id"])
    #print(index["by_brand"])
