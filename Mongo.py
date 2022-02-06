import pymongo

print("Welcome to pymongo")
connectdb = pymongo.MongoClient("localhost:27017")
print(connectdb)

db = connectdb['pydb']
collection = db['pycollection']

# for create a database and insert one or many data with id

# data = ([
#     # {'name':'ARSH', 'city':'Vadodara'},
#     # {'name':'XYZ', 'city':'Mumbai'},
#     # {'name':'ABC', 'city':'Benglore'}
#     {'_id':1,'name':'ARSH', 'city':'Vadodara'},
#     {'_id':2,'name':'XYZ', 'city':'Mumbai'},
#     {'_id':3,'name':'ABC', 'city':'Benglore'}
#     ])
# collection.insert_many(data)

# for find a data

# findany = collection.find_one({'name':'ARSH'})
# alldata = collection.find({'name':'ARSH'})
# for item in alldata:  #covert in array
#     print(item)

#show database and collection

# alldatabase = connectdb.list_database_names()
# print(alldatabase)

# database = connectdb.list_databases()
# print(database)

# showcollection = connectdb['pydb']
# print(showcollection.list_collection_names())

collection.update_one({'name':'XYZ'}, {'$set':{'city': 'Surat'}})

