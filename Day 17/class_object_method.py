#Defining class
class User:
    
    #initializing
    def __init__(self, user_id, username):
        self.id = user_id
        self.username = username
        self.followers = 0
        self.following = 0
    
    #defining method
    def follow(self, user):
        user.followers += 1
        self.following += 1


#creating objects from the class User
user_1 = User("001", "fawaz")
user_2 = User("002", "jack")


user_1.follow(user_2)

print(user_1.followers)
print(user_1.following)
print(user_2.followers)
print(user_2.following)
