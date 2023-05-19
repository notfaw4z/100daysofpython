# 🚨 Don't change the code below 👇
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
name = name1.lower() + name2.lower()
t_count = name.count("t")
r_count = name.count("r")
u_count = name.count("u")
e_count = name.count("e")
l_count = name.count("l")
o_count = name.count("o")
v_count = name.count("v")


score1 = t_count+r_count+u_count+e_count
score2 = l_count+o_count+v_count+e_count
total_score = int(str(score1)+str(score2))


if total_score < 10 or total_score > 90:
    print(f"Your score is {total_score}, you go together like coke and mentos.")
elif total_score >= 40 and total_score <= 50:
    print(f"Your score is {total_score}, you are alright together.")
else:
    print(f"Your score is {total_score}.")
