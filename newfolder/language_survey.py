from survey import AnonymousSurvey
question = 'what was the first language you learned? '
language_survey = AnonymousSurvey(question)
language_survey.show_question()
print("Enter 'q' at any time to quit")
while True:
    response = input("Language: ")
    if response=='q': 
        break
    language_survey.store_response(response)
#show the survey results
print("Thank you for participating in our survey.")
language_survey.show_results()