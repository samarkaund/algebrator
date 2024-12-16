class Answers:
    def __init__(self):
        self.ANSWERS = open("answers.txt", encoding="utf-8").readlines()

    def return_answer(self, type, hard, number):
        ur = f"{type}_ur_{hard}{number}"
        for answer in self.ANSWERS:
            if answer[0:answer.index(')')] == ur:
                return answer[answer.index(')') + 2:-1:]
