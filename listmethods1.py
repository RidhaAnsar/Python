basket = ['apple', 'grapes', 'banana', 'watermelon']

#adding
basket.append('Orange')

print(basket)

#inserting
basket.insert(2, 'Mango')
print(basket)

#removing an item by its index,
basket.pop(0)      
print(basket)

#removing an item by its value
basket.remove('grapes')
print(basket)

##clear the basket
basket.clear()
print(basket)
