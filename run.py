from logic import settings
from logic import bot
from logic import data
import time

last_message_id = 0

while True:
	time.sleep(2)
	updates = bot.get_updates(settings.token)

	if len(updates["result"]) > 0:
		
		last_message = updates["result"][-1]
		last_message_text = last_message["message"]["text"]
		message = {"user": data.user,"text": last_message_text}
		chat_id = last_message["message"]["chat"]["id"]
		message_id = updates["result"][-1]["message"]["message_id"]
		result_message = bot.resulted_eng_sentence(data.sentences,message)
		if message_id > last_message_id:
			bot.send_message(result_message, chat_id, settings.token)
			last_message_id = message_id
	else:
		print("No messages")