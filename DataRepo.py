import json

import requests as requests


class QuizRepo:

    @staticmethod
    def GetQuizQuestions():
        try:
            response = requests.get("https://opentdb.com/api.php?amount=10&category=9",
                                    params={"type": "boolean", "difficulty": "easy"})
            #
            response_dict = json.loads(response.text)
        except IOError as error:
            print(error)
        return response_dict["results"]
