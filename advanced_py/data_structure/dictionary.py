# https://www.programiz.com/python-programming/dictionary
# https://realpython.com/iterate-through-dictionary-python/

dic = {'tianbo': '2cm', 'a': [1,2,3], 'b': {'bb': 100}}

# add item
dic['somebody'] = '18cm'
print(dic)
# lookup
print(dic['tianbo'])
# print(dic['abc'])  # since the key not found, will trigger a key error
print(dic.get('abc'))

# update
dic['tianbo'] = '3cm'
print(dic)
dic['abc'] = '3cm' #  == upsert
print(dic)
# remove
dic.pop('somebody')
print(dic)

print("pop out an item before", dic)
res = dic.popitem()
print("pop out an item after", dic)
print(res[:])

# size
print(len(dic))
# iterate
print("learning iterator 1")
for k in dic:
    print(k, dic[k])
print("learning iterator 2")
for item in dic.items():
    print(item)
    print(type(item))
print("learning iterator 3")
for k, v in dic.items():
    print(k, v)
# get all keys
# get all values
