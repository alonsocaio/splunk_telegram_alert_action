import requests
import sys
import json


def send_telegram_message(payload):
	config = payload.get('configuration')
	bot_id = config.get('bot_id')
	chat_id = config.get('chat_id')
	summary = config.get('summary')
	message = config.get('message')

	telegram_message = '<b>%s<b>\n%s' % (summary, message)

	url = 'https://api.telegram.org/bot%s/sendMessage' % bot_id

	r = requests.post(url=url, data={'chat_id': chat_id, 'text': telegram_message, 'parse_mode': 'HTML'}).json()


if __name__ == "__main__":
	if len(sys.argv) > 1 and sys.argv[1] == "--execute":
		payload = json.loads(sys.stdin.read())
		send_telegram_message(payload)

else:
	print("Unsupported execution mode (expected --execute flag)", file=sys.stderr)
	sys.exit(1)
