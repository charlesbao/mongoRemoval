import pymongo

def replace_same(collection,find_arg):
    replace_count = 0
    find_args = {}
    for each in collection.find():
        for arg in find_arg:
            find_args[arg] = each[arg]
        counts = collection.find(find_args).count()
        if counts >1:
            replace_count += 1
        print each[find_arg],counts
        obj = collection.find_one(find_args)
        collection.delete_many(find_args)
        collection.insert_one(obj)
    print collection.find().count(),replace_count
    return replace_count