# list of questions
# store the answers
# randmoly pick questions
# ask the questions
# give answer
# see if they are correct 
# keep track of the score
# tell the user their score






import random
questions = {
    "what is 1+1":"2",
    "what is the result of 10//3?":"3",
    "what is force":"pull or push",
    "what symbol is used for comment":"#",
    "what does len() function used for":"length"
}
def python_trivia_game():
    questions_list = list(questions.keys())
    total_qus = 3
    score = 0
    
    selected_questions = random.sample(questions_list,total_qus)
    for idx,question in enumerate(selected_questions):
        print(f"{idx + 1}. {question}")
        user_answer = input("your answer: ").lower().strip()

        correct_answer = questions[question]

        if user_answer == correct_answer.lower():
            print("correct\n")
            score +=1
        else:
            print(f"wrong. The correct answer is {correct_answer}\n ")

 
    print(f"Game Over! your final score is : {score}/ {total_qus}")




python_trivia_game()