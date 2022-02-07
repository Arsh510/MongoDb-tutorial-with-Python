import pymongo

print("Welcome to pymongo")
connectdb = pymongo.MongoClient("localhost:27017")
print(connectdb)

db = connectdb['pydb']
collection = db['pycollection']

# for create a database and insert one or many data with id

data = ([
    {'name':'ARSH', 'city':'Vadodara'},
    {'name':'XYZ', 'city':'Mumbai'},
    {'name':'ABC', 'city':'Benglore'},
    {'_id':1,'name':'ARSH', 'city':'Vadodara'},
    {'_id':2,'name':'XYZ', 'city':'Mumbai'},
    {'_id':3,'name':'ABC', 'city':'Benglore'}
    ])
collection.insert_many(data)

# for find a data

findany = collection.find_one({'name':'ARSH'})
alldata = collection.find({'name':'ARSH'})
for item in alldata:  #covert in array
    print(item)

#show database and collection

alldatabase = connectdb.list_database_names()
print(alldatabase)

database = connectdb.list_databases()
print(database)

showcollection = connectdb['pydb']
print(showcollection.list_collection_names())

# update one and many
collection.update_one({'name':'XYZ'}, {'$set':{'city': 'Surat'}})
collection.update_one({'name':'XYZ'}, {'$set':{'location': 'Surat'}})
collection.update_many({'name':'ABC'}, {'$set':{'city': 'Surat'}})

# delate one and many
collection.delete_one({'name':'XYZ'})
collection.delete_many({'name':'ABC'})

# find any and update
collection.find_one_and_update({'name':'XYZ'}, {'$set':{'city': 'Lunawada'}})
