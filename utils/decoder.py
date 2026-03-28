def decode_name(name):
    return name.replace("ENC_", "")

def decode_bpm(hex_value):
    return int(hex_value, 16)

def decode_med(text):
    decoded = ""
    for char in text:
        decoded += chr(ord(char)-1)
    return decoded