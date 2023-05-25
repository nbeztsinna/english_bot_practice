import requests
import time

# Используя файл с лекции, а так же код с прошлых работ, с котором мы научились создавать на основе входящего сообщения набор из предложений по английскому, 
# сделайте бота, который будет ,в ответ на текст от юзера присылать ему предложения на английском, либо сообщение о том ,что предложений не найдено.
# Для простоты пусть у нас уровень юзера не учитывается. Задайте для всех, например, уровень 1.  Важно, в первую очередь, чтобы вы смогли соединить два скрипта.

# Nadiia's bot Api
token = "6161374725:AAGzmrYzA_SBdztYPn9QysZB03XMBgXzQEw"
root_url = "https://api.telegram.org/bot"

ok_codes = 200, 201, 202, 203, 204
# comment for git
# comment for second_br

sentences = [
	{"text": "When my time comes \n Forget the wrong that I’ve done take.", 
	"level": 1},
	{"text": "In a hole in the ground there lived a hobbit.", 
	"level": 2},
	{"text": "The sky the port was the color of television, tuned to a dead channel take.", 
	"level": 1},
	{"text": "I love the smell of napalm in the morning.", 
	"level": 0},
	{"text": "The man in black fled across the desert, and the gunslinger followed.", 
	"level": 0},
	{"text": "The Consul watched as Kassad raised the death wand.", 
	"level": 1},
	{"text": "If you want to make enemies, try to change something.", 
	"level": 2},
	{"text": "We're not gonna take it. \n Oh no, we ain't gonna take it \nWe're not gonna take it anymore", 
	"level": 1},
	{"text":"I learned very early the difference between knowing the name of something and knowing something.", 
	"level": 2}
]

user = {"username" : "Egor",
		"level" : 1} 


def resulted_eng_sentence(sentences_list):
	result_list = []
	result_message = ''

	for sentence in sentences_list:
		if message.get("text") in sentence.get("text"):
			result_list.append(sentence.get("text"))

	if len(result_list) == 0:
		result_message = "Does not exist"
	if len(result_list) == 1:
		result_message = result_list[0]

	if len(result_list) > 1:
		for result in result_list:
			result_message = result_message + "\n **** \n" + result

	return result_message




def get_updates(token):
	url = f"{root_url}{token}/getUpdates"
	res = requests.get(url)
	if res.status_code in ok_codes:
		updates = res.json()
		return updates

def send_message(text_message, chat_id, token):
	url = f"{root_url}{token}/sendMessage"
	res = requests.post(url, data={'chat_id': chat_id, "text": text_message})
	if res.status_code in ok_codes:
		return True
	else:
		return False


last_message_id = 0

while True:
	time.sleep(2)
	updates = get_updates(token)

	if len(updates["result"]) > 0:
		
		last_message = updates["result"][-1]
		last_message_text = last_message["message"]["text"]
		message = {"user": user,"text": last_message_text}
		chat_id = last_message["message"]["chat"]["id"]
		message_id = updates["result"][-1]["message"]["message_id"]
		result_message = resulted_eng_sentence(sentences)
		if message_id > last_message_id:
			send_message(result_message, chat_id, token)
			last_message_id = message_id
	else:
		print("No messages")