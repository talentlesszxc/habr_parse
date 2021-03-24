import requests
from bs4 import BeautifulSoup

url = 'https://freelance.habr.com/tasks?categories=development_all_inclusive,development_backend,development_frontend,development_prototyping,development_ios,development_android,development_desktop,development_bots,development_games,development_1c_dev,development_scripts,development_voice_interfaces,development_other'
response = requests.get(url)
soup = BeautifulSoup(response.text, 'lxml')

task_titles = soup.find_all('div', class_ = 'task__title')
published_at = soup.find_all('span', class_ = 'params__published-at icon_task_publish_at')
href = soup.find_all('a', class_ = 'href')

#for task in task_titles:
    #print(task.text)

#for pub in published_at:
    #print(pub.text)
    
for i in range(0, len(task_titles)):
    print(task_titles[i].text + " опубликовано " + published_at[i].text + ', ссылка: ' + href.text + '\n')