# # ## Excercise 1
# # numbersList = [1,1,2,3,5,8,13,21,34,55]
# # squaredNumList = [number**2 for number in numbersList]
# # print(squaredNumList)
# #
# # #Exercise 2
# #
# # numberList = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
# # evenList = [number for number in numberList if (number % 2 == 0)]
# # print(evenList)
# height = float(input("What is your height : "))
# weight = float(input("What is your weight : "))
#
# if height > 3:
#     raise ValueError("Are You A Godzilla?")
# else:
#     bmi = weight / height ** 2
fruits = ["Apple", "Pear", "Orange"]


def makePie(index):
    try:
        fruit = fruits[index]
        print(fruit + "pie")
    except IndexError:
        print("Fruit Pie")

makePie(4)
