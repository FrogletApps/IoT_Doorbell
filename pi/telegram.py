import secret
import os
import requests

bot_message = "Bleep bloop I'm a bot c:"
send_text = 'https://api.telegram.org/bot' + secret.tgBotKey() + '/sendMessage?chat_id=' + secret.tgChatID() + '&parse_mode=Markdown&text=' + bot_message

response = requests.get(send_text)

print (response.json())