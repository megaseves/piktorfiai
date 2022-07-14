from flask import Flask, render_template
from data import queries

app = Flask(__name__, static_url_path='/static')


@app.route('/')
def main_page():
    main_cards = queries.index_limit()
    return render_template('index.html', main_cards=main_cards)


@app.route('/galeria/<int:kereso>')
def kereso(kereso):
    cards = queries.connect(kereso)
    return render_template('galeria.html', cards=cards)


@app.route('/contact')
def contact():
    return render_template('contact.html')


@app.route('/about-us')
def about_us():
    return render_template('about_us.html')


if __name__ == "__main__":
    app.run(
        debug=True,
        port=5000
    )
