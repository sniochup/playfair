def table_counter(i, j):
    j = (j + 1) % 5
    if j == 0:
        i += 1
    return i, j


def cipher_table_print(c):
    for i in range(5):
        print(c[i])


def cipher_builder(i_key):
    letter_usage = [0] * 26
    cipher_table = [[None for _ in range(5)] for _ in range(5)]

    i = 0
    j = 0

    key = list(i_key.lower().replace(" ", ""))

    for k in key:
        ak = ord(k) - 97
        if ak == 9:
            ak = 8

        if not 0 <= ak <= 25:
            print(f"Key error \"{i_key}\": Key should contains only letters")
            return -1

        if letter_usage[ak] == 0:
            letter_usage[ak] = 1
            cipher_table[i][j] = chr(ak + 97)
            i, j = table_counter(i, j)

    for n in range(26):
        if n == 9:
            continue

        if letter_usage[n] == 0:
            cipher_table[i][j] = chr(n + 97)
            i, j = table_counter(i, j)

    # cipher_table_print(cipher_table)
    return cipher_table


def letters_pair(name, data_type=1):
    if data_type == 0:
        with open(name, 'r', encoding="utf-8") as file:
            text = file.read().lower()
            text = "".join(filter(str.islower, text))
    else:
        text = "".join(filter(str.islower, name.lower()))

    data = [text[0]]
    lp = []

    x_counter = 0
    for i in range(1, len(text)):
        if data[i - 1 + x_counter] == text[i]:
            data.append('x')
            x_counter += 1

        data.append(text[i])

    if len(data) % 2:
        data.append('x')

    for i in range(0, len(data), 2):
        lp.append(data[i] + data[i + 1])

    # print(lp)
    return lp


def letter_position(c, t):
    l0, l1 = [], []
    find0, find1 = False, False

    for i in range(5):
        for j in range(5):
            if c[i][j] == t[0]:
                l0.extend([i, j])
                find0 = True

            if c[i][j] == t[1]:
                l1.extend([i, j])
                find1 = True

            if find0 and find1:
                break
    return l0, l1


def encryption(c, text):
    for n, t in enumerate(text):
        if t[0] == 'j':
            t = 'i' + t[1]
        if t[1] == 'j':
            t = t[0] + 'i'

        l0, l1 = letter_position(c, t)

        if l0[0] == l1[0]:
            l0[1] = (l0[1] + 1) % 5
            l1[1] = (l1[1] + 1) % 5
        elif l0[1] == l1[1]:
            l0[0] = (l0[0] + 1) % 5
            l1[0] = (l1[0] + 1) % 5
        else:
            l0[0], l1[0] = l1[0], l0[0]

        text[n] = c[l0[0]][l0[1]] + c[l1[0]][l1[1]]

    with open('text_file/text_encrypted.txt', 'w', encoding="utf-8") as file:
        file.write("".join(text).upper())

    # print(text)
    # print("".join(text))

    return text
