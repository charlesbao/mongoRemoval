import pymongo

class mongoRemoval:
    _client = None
    _db = None
    _collection = None

    def replace_same(self,find_arg):
        collection = self._collection
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

    def db(self,db,username = None,password = None):
        self._db = self._client.db
        if not username == None:
            self._db.authenticate(username,password)

    def collection(self,db):
        self._collection = self._client.db.collection

    def __init__(self,ip,port):
        self._client = pymongo.MongoClient(ip, port)

def replace_same(self,collection,find_arg):
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
