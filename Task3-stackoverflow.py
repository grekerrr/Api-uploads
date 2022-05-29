import requests
from pprint import pprint
import time


def count_questions(tags):
    today_date = int(time.time())
    delta = 172800
    last_date = today_date - delta
    questions_list = []
    url = f"https://api.stackexchange.com/2.3/questions?&fromdate={last_date}&todate={today_date}&order=desc&sort=activity&tagged={tags}&site=stackoverflow"
    response = requests.get(url)
    for i in response.json()["items"]:
        for j in i:
            questions_list.append(i["link"])
        return f'Количество вопросов с тэгом "{tags}": {len(questions_list)}; ссылки на вопросы: {questions_list}'


pprint(count_questions(str(input("Введите тэг: "))))