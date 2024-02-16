stores = {
    'Магнит': {'молоко', 'соль', 'сахар', 'печенье', 'сыр'},
    'Пятерочка': {'мясо', 'молоко', 'сыр'},
    'Перекресток': {'молоко', 'творог', 'сыр', 'сахар', 'печенье'},
    'Лента': {'печенье', 'молоко', 'сыр'}
}

# нельзя соль
salt = [store for store, products in stores.items() if 'соль' not in products]

# молоко печенье и сыр
Cheese = [store for store, products in stores.items() if {'молоко', 'печенье', 'сыр'}.issubset(products)]

#  мясо и молоко
belock = [store for store, products in stores.items() if {'мясо', 'молоко'}.issubset(products)]

print(salt, "\n", Cheese, "\n", belock)

