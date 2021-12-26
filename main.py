from typing import Dict, List
from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel
import random

from starlette.responses import HTMLResponse

app = FastAPI ()
messages = []


class RandomList(BaseModel):
    random_list: List[str]


app.mount("/static", StaticFiles(directory="static"), name="static")


@app.post('/choice-random/')
async def choice_random(random_list: RandomList):
    """"""
    new_random_list = [elem for elem in random_list.random_list if elem]
    return {'choiced': random.choice(new_random_list)}


@app.post('/shake-list/')
async def choice_random(random_list: RandomList):
    """"""
    new_random_list = [elem for elem in random_list.random_list if elem]
    random.shuffle(new_random_list)
    print(new_random_list)
    return [{'shaked': random_elem} for random_elem in new_random_list]


@app.get('/', response_class=HTMLResponse)
async def root():
    return """
        <!DOCTYPE html>
        <html lang="ru">
        <head>
            <meta charset="UTF-8">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <title>Рандомайзер</title>
            <link rel="stylesheet" href="static/style.css">
            <script src="static/script.js" defer></script>
        </head>
        <body>
            <main>
                <form id="form" action="">
                    <input class="random-list-elem" type="text">
                    <button id="add-input" class="add-input">+</button>
                    
                    <div class="form_toggle-item item-1 radio-label">
                    <label class="radio-label" for="radio-1">
                        <input name="radio-1" id="form-radio-1" type="radio" value="select" checked> 
                        <span class='inner-label'>Выбрать случайный элемент</span>
                    </label>
                    </div>
                    <div class="form_toggle-item item-2 radio-label">
                        <label for="radio-1">
                        <input name="radio-1" id="form-radio-2" type="radio" value="on">
                        <span class='inner-label'>Перемешать список</span>
                        </label>
                    </div>
                    <input id="button-ok" type="submit" value="Зарандомить">
                </form>
                <div class="result"></div>
            </main>
        </body>
        </html>
    """
