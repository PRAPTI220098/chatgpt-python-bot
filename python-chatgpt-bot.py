import requests
import telebot
from telebot import types

F = '\033[1;32m' #Ø§Ø®Ø¶Ø±
B="\033[1;30m" # Black
R="\033[1;31m" # Red
G="\033[1;32m" # Green
Y="\033[1;33m" # Yellow
Bl="\033[1;34m" # Blue
P="\033[1;35m" # Purple
C="\033[1;36m" # Cyan
W="\033[1;37m" # White
PN="\033[1;35m" #PINK

# Replace 'YOUR_BOT_TOKEN' with your actual Telegram bot token
bot = telebot.TeleBot('6222084445:AAEWvWpWiY7Yec3Ne0HnxauZjM4B9ymR1nE')

# Replace 'your_proxy_address' with the IP address or domain of your proxy server,
# and 'port' with the corresponding port number
proxy = {
    'http': 'http://103.206.208.135:55443',
    'https': 'http://207.180.252.117:2222'
}

custom_headers = {
    'Host': 'gptzaid.zaidbot.repl.co',
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36',
}

def chat_with_gpt(message_text):
    api_url = f'https://gptzaid.zaidbot.repl.co/1/text={message_text}'
    response = requests.get(api_url, headers=custom_headers, proxies=proxy).text
    return response

@bot.message_handler(commands=['start'])
def start(message):
    buttons = types.InlineKeyboardMarkup(row_width=2)
    but1 = types.InlineKeyboardButton(text='👨🏻‍💻 Developer', url='https://t.me/S4NCHIT')
    but2 = types.InlineKeyboardButton(text='📣 Channel', url='https://t.me/+Q5RcaQe268lmYmI9')
    buttons.add(but1, but2)
    
    welcome_message = f"👋 Hi {message.from_user.first_name}!\n\n" \
                      f"😃 Welcome to SanchitGPT BOT!\n\n" \
                      f"💬 I am here to answer your questions and have a conversation with you.\n\n" \
                      f"✨ Just type your message, and I'll do my best to respond.\n\n" \
                      f"👨🏻‍💻 If you need to contact the developer or join the channel, check the buttons below.\n"

    bot.send_message(message.chat.id, text=welcome_message, reply_markup=buttons)

@bot.message_handler(func=lambda message: True)
def handle_message(message):
    user_input = message.text
    if user_input.lower() == 'exit':
        bot.send_message(message.chat.id, "Goodbye!")
        return

    # Display who sends the message and the message itself in the terminal
    print(f"{Y}{message.from_user.first_name}: {C}{user_input}\n\n")

    # Send the 🤔 thinking emoji as part of the response message
    response_text = "🤔 " + chat_with_gpt(user_input)

    bot.send_message(message.chat.id, response_text)

    # Display the bot's response in the terminal
    print(f"{Y}Answer: {C}{response_text}")

def main():
    print(f"{PN}ChatGPT Telegram Bot is running...\n")
    bot.polling()

if __name__ == "__main__":
    main()
