from flask import Flask, render_template, request, redirect, url_for, session, flash
from random import choice, sample

app = Flask(__name__)
app.secret_key = 'sekretny_klucz'  # Klucz do sesji

# Lista utworów
songs = [
    {"title": "Diamonds", "file": "music/Rihanna - Diamonds.mp3"},
    {"title": "Umbrella", "file": "music/Rihanna - Umbrella.mp3"},
    {"title": "Dark Horse", "file": "music/Katy Perry - Dark Horse.mp3"},
    {"title": "Only Girl (In The World)", "file": "music/Rihanna - Only Girl (In The World).mp3"},
    {"title": "We Found Love", "file": "music/Rihanna - We Found Love ft. Calvin Harris.mp3"},
    {"title": "Rockabye", "file": "music/Clean Bandit - Rockabye.mp3"},
    {"title": "New Rules", "file": "music/Dua Lipa - New Rules.mp3"},
    {"title": "Lean On", "file": "music/Major Lazer & DJ Snake - Lean On.mp3"},
    {"title": "Counting Stars", "file": "music/OneRepublic - Counting Stars.mp3"},
    {"title": "Treat You Better", "file": "music/Shawn Mendes - Treat You Better.mp3"},
    {"title": "Dont Let Me Down", "file": "music/The Chainsmokers - Dont Let Me Down.mp3"},
    {"title": "Hymn For The Weekend", "file": "music/Coldplay - Hymn For The Weekend.mp3"},
    {"title": "Give Me Everything", "file": "music/Pitbull - Give Me Everything.mp3"},
    {"title": "Call Me Maybe", "file": "music/Carly Rae Jepsen - Call Me Maybe.mp3"},
    {"title": "Work from Home", "file": "music/Fifth Harmony - Work from Home.mp3"},
    {"title": "Closer", "file": "music/The Chainsmokers - Closer.mp3"},
    {"title": "Locked Out Of Heaven", "file": "music/Bruno Mars - Locked Out Of Heaven.mp3"},
    {"title": "Sorry", "file": "music/Justin Bieber - Sorry.mp3"},
    {"title": "Thrift shop", "file": "music/MACKLEMORE & RYAN LEWIS - THRIFT SHOP.mp3"},
    {"title": "Play Hard", "file": "music/David Guetta - Play Hard.mp3"},
    {"title": "Fireflies", "file": "music/Owl City - Fireflies.mp3"},
    {"title": "Boulevard of Broken Dreams", "file": "music/Green Day - Boulevard of Broken Dreams.mp3"},
    {"title": "Basket Case", "file": "music/Green Day - Basket Case.mp3"},
    {"title": "Daylight", "file": "music/David Kushner - Daylight.mp3"},
    {"title": "More Than You Know", "file": "music/Axwell Λ Ingrosso - More Than You Know.mp3"},
    {"title": "See You Again", "file": "music/Wiz Khalifa - See You Again.mp3"},
    {"title": "The one that got away", "file": "music/Katy Perry - The one that got away.mp3"},
    {"title": "Stereo Hearts", "file": "music/Gym Class Heroes - Stereo Hearts.mp3"},
    {"title": "Heathens", "file": "music/twenty one pilots - Heathens.mp3"},
    {"title": "Blinding Lights", "file": "music/The Weeknd - Blinding Lights.mp3"},
    {"title": "Save Your Tears", "file": "music/The Weeknd - Save Your Tears.mp3"},
    {"title": "As It Was", "file": "music/Harry Styles - As It Was.mp3"},
    {"title": "Impossible", "file": "music/James Arthur - Impossible.mp3"},
    {"title": "Talking To The Moon", "file": "music/Bruno Mars - Talking To The Moon.mp3"},
    {"title": "Let Her Go", "file": "music/Passenger - Let Her Go.mp3"},
    {"title": "The Night We Met", "file": "music/Lord Huron - The Night We Met.mp3"},
    {"title": "Ho Hey", "file": "music/The Lumineers - Ho Hey.mp3"},
    {"title": "Banners", "file": "music/Someone To You - Banners.mp3"},
    {"title": "Heart To Heart", "file": "music/James Blunt - Heart To Heart.mp3"},
    {"title": "Let It Go", "file": "music/James Bay - Let It Go.mp3"},
    {"title": "Little Talks", "file": "music/Of Monsters And Men - Little Talks.mp3"},
    {"title": "Im Still Standing", "file": "music/Elton John - Im Still Standing.mp3"},
    {"title": "Lady", "file": "music/Modjo - Lady.mp3"},
    {"title": "Dynamite", "file": "music/Taio Cruz - Dynamite.mp3"},
    {"title": "Rude Boy", "file": "music/Rude Boy - Rihanna.mp3"},
    {"title": "Danza Kuduro", "file": "music/Danza Kuduro - Don Omar.mp3"},
    {"title": "California Gurls", "file": "music/Katy Perry - California Gurls.mp3"},
    {"title": "Lights", "file": "music/Ellie Goulding - Lights.mp3"},
    {"title": "Replay", "file": "music/Replay - Iyaz.mp3"},
    {"title": "Hangover", "file": "music/Taio Cruz - Hangover.mp3"},
    {"title": "Ni**as In Paris", "file": "music/Jay-Z & Kanye West - Ni__as In Paris.mp3"},
    {"title": "Walking On A Dream", "file": "music/Empire Of The Sun - Walking On A Dream.mp3"},
    {"title": "I Dont Fuck With You", "file": "music/Big Sean - I Dont Fuck With You.mp3"}
]



@app.route('/')
def index():
    return render_template('index.html', name='Gość')


@app.route('/templates', methods=['GET', 'POST'])
def podstrona1():
    global correct_song, options
    if 'score' not in session:
        session['score'] = 0
        session['round'] = 0

    if request.method == 'POST':
        selected_option = request.form.get('choice')
        if selected_option == session['correct_answer']:
            flash('Dobra odpowiedź!', 'success')
            session['score'] += 1
        else:
            flash(f'Zła odpowiedź! Prawidłowy tytuł to: {session["correct_answer"]}', 'error')
        session['round'] += 1

    # Losuje nową piosenkę i odpowiedzi tylko przy GET
    if request.method == 'Get' or 'correct_answer' not in session:
        correct_song = choice(songs)
        options = sample(songs, 4)
        if correct_song not in options:
            options.pop()
            options.append(correct_song)
        options = sample(options, 4)
        session['correct_answer'] = correct_song['title']

    return render_template('podstrona1.html', song=correct_song, options=options, score=session['score'], round=session['round'])


if __name__ == '__main__':
    app.run(debug=True)
