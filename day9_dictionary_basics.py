programming_dictionary = {
  "Bug": "An error in a program that prevents the program from running as expected.",
  "Function": "A piece of code that you can easily call over and over again."
}

#Retrieve item from dictionary
print(programming_dictionary["Bug"])

#Adding new item to dict
programming_dictionary["Loop"] = "The action of doing something"
print(programming_dictionary)

#Create empty dict
empty_dict = {}

#Wipe existing dictionary
programming_dictionary = {}

#Edit an item in dict
programming_dictionary["Bug"] = "A moth in your pc"

#Loop through a dict
for key in programming_dictionary:
  print(key)
  print(programming_dictionary[key])
