from fbchat import Client
from fbchat.models import Message, MessageReaction


class Messenger:
    def __init__(self, username_or_email, password):
        self.client = Client(username_or_email, password)

    def all_users(self):
        self.users = self.client.fetchAllUsers()

    def top_20_users(self):
        return self.client.fetchThreadList()

    def best_friend(self) -> (object, int):
        self.top_20 = self.top_20_users()
        detailed_users = [list(self.client.fetchThreadInfo(user.uid).values())[0] for user in self.top_20]
        sorted_detailed_users = sorted(detailed_users, key=lambda u: u.message_count, reverse=True)
        return sorted_detailed_users[0], sorted_detailed_users[0].message_count

    def send_message(self, user, text):
        self.client.send(Message(
            text=f"Congratulations {user.name}, you are my best friend with {user.message_count} messages!\n{text}"
        ),
            thread_id=user.uid)

    def logout(self):
        self.client.logout()


if __name__ == '__main__':
    username = "xxx@gmail.com"
    password = "XXXXXXXXX"
    integrate_messenger = Messenger(username_or_email=username, password=password)
    integrate_messenger.all_users()
    integrate_messenger.top_20_users()
    user_obj, messenger_count = integrate_messenger.best_friend()
    integrate_messenger.send_message(user=user_obj,
                                     text="Hay Your My best Friend. this is from analytic with Chatbot.")
