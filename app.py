from flask import Flask, render_template, request, url_for, flash
import dencryptor
import encryptor

app = Flask(__name__)
app.secret_key = "playfair"


@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        tool = request.form['tool']
        key = request.form['key']
        text = request.form['text']

        if tool == "Encrypt":
            cipher = encryptor.cipher_builder(key)
            # encryptor.cipher_table_print(cipher)
            if cipher == -1:
                flash(f"Key error \"{key}\": Key should contains only letters")
                return render_template('index.html')
            try:
                lp = encryptor.letters_pair(text)
                et = encryptor.encryption(cipher, lp)
            except:
                flash(f"Text error: App not support non-Latin characters")
                return render_template('index.html')

            return render_template('solution.html', cipher=cipher, key=key, text=text, etext="".join(et).upper(),
                                   flag=0)
        else:
            cipher = encryptor.cipher_builder(key)
            if cipher == -1:
                flash(f"Key error \"{key}\": Key should contains only letters")
                return render_template('index.html')
            try:
                etext = dencryptor.get_text(text)
                d_text = dencryptor.decryption(cipher, etext)
            except:
                flash(f"Text error: App not support non-Latin characters")
                return render_template('index.html')
            return render_template('solution.html', cipher=cipher, key=key, text=text, etext="".join(d_text), flag=1)

    else:
        return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True)
