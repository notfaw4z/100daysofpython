# 🚨 Don't change the code below 👇
student_heights = input("Input a list of student heights ").split()
for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])
# 🚨 Don't change the code above 👆

total_no = 0
total_sum = 0
#Write your code below this row 👇
for height in student_heights:
    total_no += 1
    total_sum = total_sum + height

print(round(total_sum/total_no))
