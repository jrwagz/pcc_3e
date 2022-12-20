motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)
print(id(motorcycles[0]))
# motorcycles.append('ducati')
motorcycles.insert(0, 'ducati')
del motorcycles[0]
print(motorcycles)
print(id(motorcycles[0]))
print(id(motorcycles[1]))

popped_motorcycle = motorcycles.pop()
print(motorcycles)
print(popped_motorcycle)
motorcycles.remove('yamaha')
print(motorcycles)
