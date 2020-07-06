def index_by_brand_vocabulary():
    print ("{:40}".format(inspect.stack()[0][3]), end='', flush=True)
    index["by_brand_vocabulary"] = {}
    for product in products:
        current_brand = product["brand"].lower()
        for piece_of_brand in current_brand.split():
            if not piece_of_brand in index["by_brand_vocabulary"]:
                index["by_brand_vocabulary"][piece_of_brand] = []
            index["by_brand_vocabulary"][piece_of_brand].append(product["id"])

            
def index_by_name():
    print ("{:40}".format(inspect.stack()[0][3]), end='', flush=True)
    index["by_name"] = {}
    for product in products:
        current_name = product["name"].lower()
        if not current_name in index["by_name"]:
            index["by_name"][current_name] = []
        index["by_name"][current_name].append(product["id"])

        
def index_by_name_vocabulary():
    print ("{:40}".format(inspect.stack()[0][3]), end='', flush=True)
    index["by_name_vocabulary"] = {}
    for product in products:
        current_name = product["name"].lower()
        for piece_of_name in current_name.split():
            if not piece_of_name in index["by_name_vocabulary"]:
                index["by_name_vocabulary"][piece_of_name] = []
            index["by_name_vocabulary"][piece_of_name].append(product["id"])

            
def index_by_global_vocabulary():
    print ("{:40}".format(inspect.stack()[0][3]), end='', flush=True)
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

