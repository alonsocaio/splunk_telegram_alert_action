import requests
import sys


class SplunkTelegramAlertAction:
	def __init__(self, **kwargs):
		self.params = [
			"bot_id",
			"summary",
			"message",
			"chat_id"
		]


def send_telegram_message(self, bot_id, payload):
	url = ''
	print(bot_id)


if __name__ == "__main__":
	if len(sys.argv) > 1 and sys.argv[1] == "--execute":
		try:
			splunk_telegram_alert_action = SplunkTelegramAlertAction()
			splunk_telegram_alert_action.execute()
			sys.exit(0)
		except Exception as e:
			print("Unhandled exception: " + str(e), file=sys.stderr)
else:
	print("Unsupported execution mode (expected --execute flag)", file=sys.stderr)
	sys.exit(1)
