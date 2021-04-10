
def enigma_light():

    keys = "abcdefghijklmnopqrstuvwxyz !"
    values = keys[-1] + keys[0:-1]
    print(keys)
    print(values)

    dict_e = dict(zip(keys, values))
    dict_d = dict(zip(values, keys))

    msg = input("enter your secret message: ")
    mode = input("crypto mode: encode (e) OR decrypt as default: ")

    if mode.lower() == "e":
        new_msg = "".join([dict_e[letter] for letter in msg.lower()])
    else:
        new_msg = "".join([dict_d[letter] for letter in msg.lower()])
    
    return new_msg



print(enigma_light())
