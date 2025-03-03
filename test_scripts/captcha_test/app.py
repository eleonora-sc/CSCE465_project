from flask import Flask, render_template, request, session, redirect, url_for
import random
import string

app = Flask(__name__)
app.secret_key = '123'


def generate_captcha(length=6): #generate text based captcha for this
    return ''.join(random.choices(string.ascii_uppercase + string.digits, k=length))


@app.route('/', methods=['GET', 'POST'])
def index():
    if 'captcha' not in session:
        session['captcha'] = generate_captcha()

    message = ''
    if request.method == 'POST':
        user_input = request.form.get('captcha_input', '').strip().upper()
        if user_input == session.get('captcha', ''):
            message = 'Success!'
            session.pop('captcha', None)  #Pop old captcha
            return redirect(url_for('success'))
        else:
            message = 'Wrong captcha u bot :(.' #Case: user enters wrong answer, regenerate captcha.
            session['captcha'] = generate_captcha()

    return render_template('index.html', captcha=session['captcha'], message=message)


@app.route('/success') #route in successful test case
def success():
    return 'Successful validation!'


if __name__ == '__main__':
    app.run(debug=True)
