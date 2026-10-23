user_input = input("Enter a whole number: ")

try:
    number = int(user_input)
    print(f"You entered: {number}")
except ValueError:
    print("Invalid input: please enter a whole number.")
import json

with open("learning_plan.json", "r") as file:
    learning_plan = json.load(file)

for topic in learning_plan["topics"]:
    print(topic)