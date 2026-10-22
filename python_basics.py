name = "Pramod"
experience_years = 7
daily_study_hours = 1.0

print(f"My name is {name}. I have {experience_years} years of IT experience.")
print(f"I study Python for {daily_study_hours} hours per day.")

weekly_study_hours = daily_study_hours * 7
print(f"My weekly study time is {weekly_study_hours} hours.")

if daily_study_hours >= 2:
    print("Good progress! You meet your daily study target.")
elif daily_study_hours >= 1:
    print("You're making progress. Try to reach 2 hours.")
else:
    print("Let's start with at least 1 hour of learning.")

ai_topics = ["Python", "Git", "Azure AI", "RAG", "LLMs"]

print("\nMy AI learning roadmap:")
for index, topic in enumerate(ai_topics, start=1):
    print(f"{index}. {topic}")


def greet(topic):
    print(f"My next learning topic is {topic}.")


def create_message(topic):
    return f"My next learning topic is {topic}."


def create_learning_messages(topics):
    if not topics:
        return []

    messages = []
    for topic in topics:
        messages.append(f"I will learn: {topic}")

    return messages


greet("Python")

message = create_message("RAG")
print(message.upper())

result = create_learning_messages(ai_topics)
print(result)
print(f"Total messages: {len(result)}")

empty_result = create_learning_messages([])
print(empty_result)
print(f"Empty result count: {len(empty_result)}")