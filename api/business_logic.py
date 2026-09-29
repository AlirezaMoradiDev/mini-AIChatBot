from .serializres import Chat

class ChatLogic:
    def __init__(self, message):
        self.message = message

    def clean(self):
        # more operator...
        return self.message.lower()

    def answer(self):
        answers = {
            'hello': 'Hi, can I help you?',
        }
        try:
            return answers[self.clean()]
        except KeyError:
            return 'coming soon'