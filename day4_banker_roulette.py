# Import the random module here
import random
# Split string method
names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")
print(names)
# 🚨 Don't change the code above 👆
num_names = len(names)

#Write your code below this line 👇
random_choice = random.randint(0, num_names-1)
payer = names[random_choice]
print(payer + " is going to buy the meal today!")
