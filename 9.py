class Question:
    def __init__(self, text, choices, correct_choice_index):
        self.text = text
        self.choices = choices
        self.correct_choice_index = correct_choice_index

    def display(self):
        print(self.text)
        for i, choice in enumerate(self.choices):
            print(f"{i + 1}. {choice}")
    
    def check_answer(self, selected_index):
        return selected_index == self.correct_choice_index

def run_quiz(questions):
    score = 0
    for question in questions:
        print("\n------------------------------------")
        question.display()
        selected_index = int(input("Enter your choice (1/2/3/4): ")) - 1
        
        if 0 <= selected_index < len(question.choices):
            if question.check_answer(selected_index):
                print("Correct!")
                score += 1
            else:
                print("Incorrect.")
        else:
            print("Invalid choice.")
    
    return score

def main():
    question1 = Question("What is the capital of Pakistan?",
                         ["Lahour", "Islamabad", "Karachi", "Quetta"],
                         correct_choice_index=1)
    
    question2 = Question("Who was the pervious Prime minister'?",
                         ["Nawaz sharif", "Shehbaz sharif", "Perwaz musharaf", "Imran Khan"],
                         correct_choice_index=3)
    
    question3 = Question("In which year Pakistan became a Republic? '?",
                         ["1966", "1912", "1947", "1877"],
                         correct_choice_index=2)
    
    questions = [question1, question2, question3]
    
    print("Welcome to the Quiz!")
    print("Answer the following questions:")
    
    score = run_quiz(questions)
    total_questions = len(questions)
    
    print("\n------------------------------------")
    print(f"Quiz Finished!\nYour Score: {score}/{total_questions}")

if __name__ == "__main__":
    main()