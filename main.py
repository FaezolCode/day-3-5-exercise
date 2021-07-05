# 🚨 Don't change the code below 👇
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
combined_name = name1 + name2
lowercase = combined_name.lower() 

t = lowercase.count("t")
r = lowercase.count("r")
u = lowercase.count("u")
e = lowercase.count("e")

true = t + r + u + e

l = lowercase.count("l")
o = lowercase.count("o")
v = lowercase.count("v")
e = lowercase.count("e")

love = l + o + v + e

love_score = int(str(true) + str(love))


if (love_score < 10) or (love_score > 90):
  print(f"your love score is {love_score}, you go together like coke and mentos")
elif (love_score >= 40) and (love_score <= 50):
  print(f"your love score is {love_score}, you are alright together.")
else:
  print(f"your score is {love_score}")