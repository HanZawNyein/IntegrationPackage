# Bot Integration

### Telegram

    app = Telegram(__name__)
    app.config['api_key'] = os.getenv("TELEGRAM_API_KEY")
    print(app.get_updates())
    chat_id = os.getenv("CHAT_ID")
    app.send_message(chat_id=chat_id, text='gggg')
    app.get_me()

### Messenger

    username = "xxx@gmail.com"
    password = "XXXXXXXXX"
    integrate_messenger = Messenger(username_or_email=username, password=password)
    integrate_messenger.all_users()
    integrate_messenger.top_20_users()
    user_obj, messenger_count = integrate_messenger.best_friend()
    integrate_messenger.send_message(user=user_obj,
                                     text="Hay Your My best Friend. this is from analytic with Chatbot.")

<!--************************************************-->
<!--           Created By Han Zaw Nyein             -->
<!--                    6/30/2022                   -->
<!--            Junior Odoo Developer               -->
<!--************************************************-->