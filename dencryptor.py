import encryptor as ec


def get_text(t, data_type=1):
    split_text = []

    if data_type == 0:
        with open('text_file/text_encrypted.txt', 'r', encoding="utf-8") as file:
            text = file.read().lower()
    else:
        text = t.lower().replace(" ", "")

    for i in range(0, len(text), 2):
        split_text.append(text[i: i + 2])

    # print(split_text)
    return split_text


def decryption(c, text):
    for n, t in enumerate(text):

        l0, l1 = ec.letter_position(c, t)

        if l0[0] == l1[0]:
            l0[1] = (l0[1] - 1) % 5
            l1[1] = (l1[1] - 1) % 5
        elif l0[1] == l1[1]:
            l0[0] = (l0[0] - 1) % 5
            l1[0] = (l1[0] - 1) % 5
        else:
            l1[0], l0[0] = l0[0], l1[0]

        text[n] = c[l0[0]][l0[1]] + c[l1[0]][l1[1]]

    with open('text_file/text_decrypted.txt', 'w', encoding="utf-8") as file:
        file.write("".join(text))

    # print("".join(lp))

    return text
