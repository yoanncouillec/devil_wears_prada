import sys
import json

index = json.load(open("index.json"))
products = json.load(open("search_dataset.json"))

if __name__ == "__main__":
    i = 0
    for key in index["by_name_vocabulary"]:
        if len(key) > 2 and len(index["by_name_vocabulary"][key]) > 100:
            print("{}".format(key, len(index["by_name_vocabulary"][key])))
            i += 1
    #print(i)

