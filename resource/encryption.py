import base64

def encrypt_message(message):
    encoded_data = base64.b64encode(message).decode(encoding="utf-8")
    return encoded_data

def decrypt_message(encMessage):
        decoded_data = base64.b64decode(encMessage).decode(encoding="utf-8")
        return decoded_data
