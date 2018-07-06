import os
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.wait import WebDriverWait
from .models import PlayerGoalScore

chrome_bin = os.environ.get('GOOGLE_CHROME_SHIM', 'google-chrome-stable')

url = "https://www.fifa.com/worldcup/statistics/players/goal-scored"

fields = ['rank', 'player_name', 'goals_scored', 'assists', 'minutes_played', 'matches_played', 'penalties_scored',
          'goals_left_foot', 'goals_right_foot', 'headed_goals']


def scrap():
    options = Options()
    options.binary_location = chrome_bin

    # Inicializa webdriver
    yield 'Inicializando Browser<br /><br />'

    driver = webdriver.Chrome(chrome_options=options)
    # Aguarda o browser
    driver.implicitly_wait(30)

    # Entra na URL
    yield f'Entrando na URL: {url}<br />'
    driver.get(url)

    wait = WebDriverWait(driver, 15)

    pagination_base = driver.find_element_by_id('goal-scored_paginate')
    pagination_items = pagination_base.find_elements_by_xpath('.//a')

    goals_table = driver.find_element_by_id('goal-scored')

    goals = []

    for number, page in enumerate(pagination_items):

        yield f'<br /><br />Lendo página {number+1}<br />'

        driver.execute_script("arguments[0].click();", page)
        # page.click()
        driver.implicitly_wait(2)

        rows = goals_table.find_elements_by_tag_name('tr')

        yield f'Itens: '

        for row in rows:
            cols = row.find_elements_by_tag_name('td')
            if cols:
                goal = {}
                for i, field in enumerate(fields):
                    val = cols[i].text
                    try:
                        goal[field] = int(val)
                    except ValueError:
                        goal[field] = val.title()
                goals.append(goal)

                yield f'{goal["rank"]}, '
    driver.close()

    yield '<br /><br />Atualizando banco de dados...'

    PlayerGoalScore.objects.all().delete()
    for goal in goals:
        PlayerGoalScore(**goal).save()

    yield '<br /><br />Finalizado'
