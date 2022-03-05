
def encode(message, key):
    len_msg = len(message)
    my_string = ""
    for i in range(len_msg):
        msg_num = ord(message[i])
        total = msg_num + key
        revert = chr(total)
        my_string = my_string + revert
    return my_string


def encode_better(message, key):
    len_msg = len(message)
    my_string = ""
    for i in range(len_msg):
        msg_num = ord(message[i]) - 65
        key_num = ord(key[i % len(key)]) - 65
        total = msg_num + key_num
        mod = total % 58
        convert = mod + 65
        revert = chr(convert)
        my_string = my_string + revert
    return my_string

