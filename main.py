#import csv
from datetime import datetime
import requests
from bs4 import BeautifulSoup

url = 'https://freelance.habr.com/tasks?categories=development_all_inclusive,development_backend,development_frontend,development_prototyping,development_ios,development_android,development_desktop,development_bots,development_games,development_1c_dev,development_scripts,development_voice_interfaces,development_other'
#url = 'https://freelance.habr.com/tasks?categories=content_copywriting,content_rewriting,content_audio,content_article,content_scenarios,content_naming,content_correction,content_management,marketing_smm,marketing_seo,marketing_context,marketing_email,marketing_research,marketing_sales,marketing_pr,marketing_other'

def get_html(url):
    response = requests.get(url)
    return response.text
    
#info = []  
  
def get_all_tasks(html):
    soup = BeautifulSoup(html, 'lxml')
    tasks = soup.find_all('header', class_ = 'task__header')
    #pub_date = soup.find_all('span', class_ = 'params__published-at icon_task_publish_at')    
    links = []
    tasks_list = []
    pubs = []    
    info = []
    for task in tasks:        
        
        l = task.find('a').get('href')
        link = 'freelance.habr.com' + l
        
        tasks_list.append(task.text)
        links.append(link)
        
        line = task.text + link
        if line not in info:
            info.append(line)
            print(line)
            
    #return info
 
def main(): 
    while True:
        print(get_all_tasks(get_html(url)))
    #print(links)
    
if __name__ == '__main__':
    main()