import requests
import telebot
from telebot import types

# Replace 'YOUR_BOT_TOKEN' with your actual Telegram bot token
bot = telebot.TeleBot('6222084445:AAEp3MD8bjXN3xTAzm9NVTZU593IHgUtkIY')

def chat_with_gpt(message_text):
    api_url = f'https://gptzaid.zaidbot.repl.co/1/text={message_text}'
    response = requests.get(api_url).text
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
    print(f"Message from {message.from_user.first_name}: {user_input}")

    # Send the 🤔 thinking emoji as part of the response message
    response_text = "🤔 " + chat_with_gpt(user_input)

    # Remove the 🤔 thinking emoji from the response_text
    response_text = response_text.replace("🤔", "").strip()

    # Add like and dislike buttons to the answer
    reply_markup = types.InlineKeyboardMarkup(row_width=2)
    like_button = types.InlineKeyboardButton(text='👍 Like', callback_data='like')
    dislike_button = types.InlineKeyboardButton(text='👎 Dislike', callback_data='dislike')
    reply_markup.add(like_button, dislike_button)

    # Send the response with the like and dislike buttons
    bot.send_message(message.chat.id, response_text, reply_markup=reply_markup)

    # Display the bot's response in the terminal
    print(f"Bot Response: {response_text}")

@bot.callback_query_handler(func=lambda call: True)
def handle_callback(call):
    if call.data == 'like':
        bot.answer_callback_query(call.id, "You liked the answer. Thank you!")
    elif call.data == 'dislike':
        bot.answer_callback_query(call.id, "You disliked the answer. We'll improve!")

def main():
    print("ChatGPT Telegram Bot is running...")
    bot.polling()

if __name__ == "__main__":
    main()
