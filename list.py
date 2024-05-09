cart = ['pen', 'pencil', 'eraser', 'notebooks']
print(cart[2])

print(cart[1:3])
cart[1] = 'apple'
print(cart)  #lists are mutable
new_cart = cart[0:3]
new_cart[1] = 'Grapes'
print(new_cart)
