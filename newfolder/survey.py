class AnonymousSurvey:
    def __init__(self, question):
        self.question = question
        self.responses = []
        
    def show_question(self):
        print(self.question)
    
    def store_response(self, new_response):
        self.responses.append(new_response)

    def show_results(self):
        for response in self.responses:
            print(f" - {response}")