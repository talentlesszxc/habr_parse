import telebot
import requests
from bs4 import BeautifulSoup

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
            return line
    #return info


bot = telebot.TeleBot('')

keyboard1 = telebot.types.ReplyKeyboardMarkup(True)
keyboard1.row('/start', 'Контент', 'Программирование', 'Пока')
@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id, 'Привет, я бот для получения информации о новых заказах с сайта freelance.habr.com. Для начала выберите интересущую тематику. По нажатию на кнопку вы получите информацию о последнем заказе в данной категории', reply_markup = keyboard1)

@bot.message_handler(content_types=['text'])
def send_text(message):
    if message.text.lower() == 'контент':
        #bot.send_message(message.chat.id, 'Начинаю работу. Как только заказ из категорий "Контент" появится, я тут же о нем сообщу')
        bot.send_message(message.chat.id, 'Показываю самое актуальное задание из категории Контент ')
        url = 'https://freelance.habr.com/tasks?categories=content_copywriting,content_rewriting,content_audio,content_article,content_scenarios,content_naming,content_correction,content_management,marketing_smm,marketing_seo,marketing_context,marketing_email,marketing_research,marketing_sales,marketing_pr,marketing_other'
        bot.send_message(message.chat.id, get_all_tasks(get_html(url)))
        
        
    elif message.text.lower() == 'программирование':
        #bot.send_message(message.chat.id, 'Начинаю работу. Как только заказ из категории "Программирование"  появится, я тут же о нем сообщу')
        bot.send_message(message.chat.id, 'Показываю самое актуальное задание из категории Программирование ')
        url = 'https://freelance.habr.com/tasks?categories=development_all_inclusive,development_backend,development_frontend,development_prototyping,development_ios,development_android,development_desktop,development_bots,development_games,development_1c_dev,development_scripts,development_voice_interfaces,development_other'        
        bot.send_message(message.chat.id, get_all_tasks(get_html(url)))
        
    elif message.text.lower() == 'пока':
        bot.send_message(message.chat.id, 'Пока-пока')
        bot.send_sticker(message.chat.id, 'CAACAgIAAxkBAAEBCiZgWyitfQGUal51agJWvV3n9A_A7QAC7QADGB0GD4PCb2ql1faFHgQ')
    
bot.polling()