import datetime
import base64


def generate_password(secret_key):
    current_date = datetime.datetime.now().strftime("%Y%m%d")
    password = secret_key + current_date
    encoded_message = base64.b64encode(password.encode('utf-8')).decode('utf-8')
    return encoded_message


def get_key():
    secret_key = ["bsbflsgxh..", "Jin13389791067"]
    today = datetime.datetime.now().date()
    day = today.day
    if day % 2 == 0:
        key = secret_key[0]
    else:
        key = secret_key[1]
    current_password = generate_password(key)
    return current_password
