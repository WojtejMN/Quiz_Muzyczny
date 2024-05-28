from flask import Flask, render_template, request, session, redirect, url_for
from random import choice, sample

app = Flask(__name__)
app.secret_key = 'your_secret_key'
songs = [
    {'title': 'Song1', 'file': 'song1.mp3'},
    {'title': 'Song2', 'file': 'song2.mp3'},
    {'title': 'Song3', 'file': 'song3.mp3'},
    {'title': 'Song4', 'file': 'song4.mp3'},
    {'title': 'Song5', 'file': 'song5.mp3'}
]

@app.route('/')
def index():
    return render_template('index.html', name='Gość')

@app.route('/templates', methods=['GET', 'POST'])
def podstrona1():
    if 'score' not in session or request.method == 'GET':
        session['score'] = 0
        session['round'] = 0

    if request.method == 'POST':
        selected_option = request.form.get('choice')
        if selected_option == "no_selection" or selected_option != session['correct_answer']:
            is_correct = False
        else:
            session['score'] += 1
            is_correct = True
        session['round'] += 1

        if session['round'] >= 20:
            # Reset the game after 20 rounds
            score = session['score']
            session.clear()
            session['score'] = score
            return redirect(url_for('index'))

    # Always pick a new song and options, regardless of GET or POST
    correct_song = choice(songs)
    options = sample(songs, 4)
    if correct_song not in options:
        options.pop()
        options.append(correct_song)
    options = sample(options, 4)
    session['correct_answer'] = correct_song['title']

    return render_template('podstrona1.html', song=correct_song, options=options, score=session['score'], round=session['round'], correct_answer=session['correct_answer'])

if __name__ == '__main__':
    app.run(debug=True)
