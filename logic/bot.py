import requests
import time
from . import settings

def resulted_eng_sentence(sentences_list,message):
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
	url = f"{settings.root_url}{token}/getUpdates"
	res = requests.get(url)
	if res.status_code in settings.ok_codes:
		updates = res.json()
		return updates

def send_message(text_message, chat_id, token):
	url = f"{settings.root_url}{token}/sendMessage"
	res = requests.post(url, data={'chat_id': chat_id, "text": text_message})
	if res.status_code in settings.ok_codes:
		return True
	else:
		return False

if __name__ == "__main__":
	print("labuda")