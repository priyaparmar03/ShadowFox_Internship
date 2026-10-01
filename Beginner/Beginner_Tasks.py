# -----Task Level (Beginner)-----
# 1. Variables

# 1)
pi = 22/7
print(type(pi))

# 2)
# for = 4
# print(for)
#
# # for is a keyword in for loop. We cannot use for as a variable.

# 3)
P = 5000
R = 5
T = 3
interest = (P*R*T) / 100

print("Simple Interest:",interest)




# 2. Numbers.

# 1)
def func(a,b):
    return format(a,b)

print(func(145, 'o'))

# In this program, octal representation is used.

# 2)
radius = 84
area = 3.14 * radius * radius
print("Area of circular pond:",area)

water = 1.4 * area
print("Total water in the pond:",int(water),"litres")

# 3)
distance = 490
time = 7 * 60

speed = distance /time
print("Speed:",int(speed),"m/s")




# 3. List

justice_league = ["Superman", "Batman", "Wonder Woman", "Flash", "Aquaman", "Green Lantern"]
#
# # 1)
print("Number of members in the Justice League:",len(justice_league))
#
# # 2)
justice_league.extend(["Batgirl", "Nightwing"])
print(justice_league)
#
# # 3)
justice_league.remove("Wonder Woman")
justice_league.insert(0, "Wonder Woman")
print(justice_league)
#
# # 4)
justice_league.remove("Green Lantern")
justice_league.insert(4, "Green Lantern")
print(justice_league)
#
# # 5)
justice_league = ["Cyborg", "Shazam", "Hawkgirl", "Martian Manhunter", "Green Arrow"]
print("Justice League:",justice_league)
#
# # 6)
justice_league.sort()
print("Sorted Justice League:",justice_league)
print("New Leader:",justice_league[0])


# 4. If Condition.

# 1)
height = float(input("Enter height in metres: "))
weight = float(input("Enter weight in kilograms: "))

BMI = weight / (height * height)
print("BMI:", BMI)

if BMI >= 30:
    print("Obesity")
elif BMI >= 25 and BMI < 30:
    print("Overweight")
elif BMI >= 18.5 and BMI < 25:
    print("Normal")
else:
    print("Underweight")


# 2)
Australia = ["Sydney", "Melbourne", "Brisbane", "Perth"]
UAE = ["Dubai", "Abu Dhabi", "Sharjah", "Ajman"]
India = ["Mumbai", "Bangalore", "Chennai", "Delhi"]

city_name = input("Enter a city name: ")

if city_name in Australia:
    print("The city name is in Australia")
elif city_name in UAE:
    print("The city name is in UAE")
else:
    print("The city name is in India")


# 3)
Australia = ["Sydney", "Melbourne", "Brisbane", "Perth"]
UAE = ["Dubai", "Abu Dhabi", "Sharjah", "Ajman"]
India = ["Mumbai", "Bangalore", "Chennai", "Delhi"]

city1 = input("Enter the first city: ")
city2 = input("Enter the second city: ")

if city1 in Australia and city2 in Australia:
    print("Both cities are in Australia.")
elif city1 in UAE and city2 in UAE:
    print("Both cities are in UAE.")
elif city1 in India and city2 in India:
    print("Both cities are in India.")
else:
    print("They don't belong to the same country.")




# 6. Dictionary.

# 1)
names = ["aayush", "sonal", "vipul", "priya", "akash"]
print("Names:",names)

tuple_len = [(name, len(name)) for name in names]
print("Name and length:",tuple_len)


# 2)
my_expenses = {"Hotel" : 1200, "Food": 800, "Transportation" : 500, "Attractions" : 300, "Miscellaneous" : 200}
partner_expenses = {"Hotel" : 1000, "Food": 900, "Transportation" : 600, "Attractions" : 400, "Miscellaneous" : 150}

print("My expenses:",sum(my_expenses.values()))
print("Partner's expenses:", sum(partner_expenses.values()))

if sum(my_expenses.values()) > sum(partner_expenses.values()):
    print("I have spent more money.")
else:
    print("Partner spent more money.")

category = ""
difference = 0

for key in my_expenses:
    diff = abs(my_expenses[key] - partner_expenses[key])

    if diff > difference:
        difference = diff
        category = key

print("Category:",category)
print("Difference:",difference)









