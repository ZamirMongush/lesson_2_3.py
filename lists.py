#food = ['apple', 'coconut', 'banana']
#print(food[0])
#food[1] = 'peach' - заменить элемент
#print(food)
#food.append(True) - добавить элемент
#food.extend("string") - добавляет из множество элементов
#food.remove("banana") -удаляет элемент
#print("coconut" in food) - проверяет элемент
#print("coconut" not in food) - проверяет отсутствие элемента
food = ["apple", "coconut", "banana"]
food.append(True)
print(food)
food.extend(['string', 2])
print(food)
food.remove("banana")
print(food)
print("coconut" not in food)
print(food[0:3])