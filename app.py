from flask import Flask, render_template, request, flash, get_flashed_messages
from random import randint
app = Flask(__name__)
app.secret_key = "secret_key"


@app.route('/')
def users():
    return render_template('new.html')


@app.route('/search')
def courses():
    mes = ['Попробуй еще раз', 'Есть подсказка - первая буква К', 'Есть подсказка - вторая буква с']
    term = request.args.get('term')
    if term.lower() != 'ксюша':
        #flash('This is a message', 'error')
        #messages = get_flashed_messages(with_categories=True)
        return render_template('new.html',
                               messages=mes[randint(0,2)], )
    return render_template('image.html')


if __name__ == '__main__':
    app.run(debug=True)
