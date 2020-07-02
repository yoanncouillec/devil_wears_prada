from itertools import combinations
import sys
import json
import math

index = json.load(open("index.json"))
products = json.load(open("search_dataset.json"))

if __name__ == "__main__":
    #print(len(index["by_term"]["yellow"]))
    #print(len(index["by_term"]["toywatch"]))
    #print(index["by_term"])
    #print(index["by_brand"])
    #print(index["by_collocation"])
    for t in index["ids_by_collocation"]["ralph"]:
        print("{} => {}".format(t,len(index["ids_by_collocation"]["ralph"][t])))
    print(len(index["ids_by_collocation"]["lauren"]["ralph"]))
