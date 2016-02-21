# mongoRemoval
Dongodb Duplicate removal

```Python
import mongoRemoval

collection = pymongo.MongoClient('127.0.0.1',27017).db.collection
print mongoRemoval.replace_same(collection,['number','name'])
```
