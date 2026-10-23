import json

learning_plan = {
    "name": "Pramod",
    "goal": "AI Engineer",
    "topics": ["Python", "Git", "Azure AI"]
}

with open("learning_plan_output.json", "w") as file:
    json.dump(learning_plan, file, indent=4)

print("Learning plan saved successfully.")