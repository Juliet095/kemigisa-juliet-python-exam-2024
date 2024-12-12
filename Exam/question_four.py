## 4.(b)
#class is a group where variables are easily defined
#object is a avarible where data is collected.

## 4.(ii)
sentence = "python exam"
words = sentence.split()
word_count = {}
for word in words:
    word_count[word] = word_count.get(word,0) + 1
    print("Word occurances:")
for word, count in word_count.items():
    print(f"{word}:{count}")


## 4.(iii)
def sum_of_two_numbers(a, b):
     return a + b
a=int(input("Enter the first number:"))
b=int(input("Enter the second number:"))

sum_of_two_numbers(a=3, b=4)
print("Sum is {0}".format(sum_of_two_numbers(a , b)))

## 4.(iv)
class car: 
    def __init__(my_car,brand,name,color):
        my_car.brand = brand
        my_car.name = name
        my_car.color = color
car2 = car("BMW", "JK" ,"White")
print(car2.brand)
print(car2.name)
print(car2.color)

## 4.(v)
class car: 
    def __init__(my_car,brand, name,color):
        my_car.brand = brand
        my_car.name = name
        my_car.color = color
    def start_engine(unbeilievable):
        print(f"The engine of the car has started")
car2 = car("BMW", "JK" ,"White")
car2.start_engine()
