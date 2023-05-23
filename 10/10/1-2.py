import json

with open('1.json', 'r') as f:
    y = f.read()
s = json.loads(y)
for i in s['products']:
    print("название " + i['name'])
    print("цена " + str(i['price']))
    print("вес " + str(i['weight']))
    if i['available'] == True:
        print('В наличии')
    elif i['available'] == False:
        print('Нет в наличии')
    print(   )
a = input("Впишите через запятую название продукта, цену, вес")
x = a.split(',')
r = {'name': x[0], 'price': x[1], 'available': 'true', 'weight': x[2]}
s['products'].append(r)
with open('1.json', 'w') as e:
    json.dump(s, e, indent=4,ensure_ascii=False)
