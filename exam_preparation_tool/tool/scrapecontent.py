import requests

def get_stackoverflow_questions(tag, num_questions=10):
    base_url = "https://api.stackexchange.com/2.2/questions"

    params = {
        "pagesize": num_questions,
        "order": "desc",
        "sort": "creation",
        "tagged": tag,
        "site": "stackoverflow"
    }

    try:
        response = requests.get(base_url, params=params)
        response.raise_for_status()

        data = response.json()
        questions = [item["title"] for item in data["items"]]

        return questions
    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")
        return []

def generatequestion():
    tag = input("Enter a programming language or technology tag (e.g., python, java): ")
    num_questions = int(input("Enter the number of questions to retrieve: "))

    questions = get_stackoverflow_questions(tag, num_questions)

    if questions:
        print("\nStack Overflow questions related to the topic:")
        for i, question in enumerate(questions, 1):
            print(f"{i}. {question}")
    else:
        print("No questions found for the topic.")