from datetime import datetime

API_KEY = "1768456634:AAFhKt6YzkYkmM5TGE8huUVrQrRQgmFS-yY"


def message_response(user_input):
    user_text = str(user_input).lower()

    if user_text in ('hi', 'hello'):
        return "Hey! How's it going"

    if user_text in ('who are you', 'who are you?'):
        return 'I am RFM bot'

    if user_text in ('time', 'time?'):
        now = datetime.now()
        date_time = now.strftime("%d/%m/%y, %H:%M")

        return str(date_time)

    return "I don't understand what you are saying."
