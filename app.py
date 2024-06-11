from flask import Flask, render_template, request, redirect, url_for, session, flash
from random import choice, sample

app = Flask(__name__)
app.secret_key = 'sekretny_klucz'  # Klucz do sesji

# Lista utworów
songs = [
            {"title": "Diamonds", "file": "music/Rihanna - Diamonds.mp3", "artist": "Rihanna",
             "image_url": "https://via.placeholder.com/150"},
            {"title": "Umbrella", "file": "music/Rihanna - Umbrella.mp3", "artist": "Rihanna",
             "image_url": "https://via.placeholder.com/150"},
            {"title": "Dark Horse", "file": "music/Katy Perry - Dark Horse.mp3", "artist": "Katy Perry",
             "image_url": "https://via.placeholder.com/150"},
            {"title": "Only Girl (In The World)", "file": "music/Rihanna - Only Girl (In The World).mp3",
             "artist": "Rihanna", "image_url": "https://via.placeholder.com/150"},
            {"title": "We Found Love", "file": "music/Rihanna - We Found Love ft. Calvin Harris.mp3",
             "artist": "Rihanna", "image_url": "https://via.placeholder.com/150"},
            {"title": "Rockabye", "file": "music/Clean Bandit - Rockabye.mp3", "artist": "Clean Bandit",
             "image_url": "https://via.placeholder.com/150"},
            {"title": "New Rules", "file": "music/Dua Lipa - New Rules.mp3", "artist": "Dua Lipa",
             "image_url": "https://via.placeholder.com/150"},
            {"title": "Lean On", "file": "music/Major Lazer & DJ Snake - Lean On.mp3",
             "artist": "Major Lazer & DJ Snake", "image_url": "https://via.placeholder.com/150"},
            {"title": "Counting Stars", "file": "music/OneRepublic - Counting Stars.mp3", "artist": "OneRepublic",
             "image_url": "https://via.placeholder.com/150"},
            {"title": "Treat You Better", "file": "music/Shawn Mendes - Treat You Better.mp3", "artist": "Shawn Mendes",
             "image_url": "https://via.placeholder.com/150"},
            {"title": "Dont Let Me Down", "file": "music/The Chainsmokers - Dont Let Me Down.mp3",
             "artist": "The Chainsmokers", "image_url": "https://via.placeholder.com/150"},
            {"title": "Hymn For The Weekend", "file": "music/Coldplay - Hymn For The Weekend.mp3", "artist": "Coldplay",
             "image_url": "https://via.placeholder.com/150"},
            {"title": "Give Me Everything", "file": "music/Pitbull - Give Me Everything.mp3", "artist": "Pitbull",
             "image_url": "https://via.placeholder.com/150"},
            {"title": "Call Me Maybe", "file": "music/Carly Rae Jepsen - Call Me Maybe.mp3",
             "artist": "Carly Rae Jepsen", "image_url": "https://via.placeholder.com/150"},
            {"title": "Work from Home", "file": "music/Fifth Harmony - Work from Home.mp3", "artist": "Fifth Harmony",
             "image_url": "https://via.placeholder.com/150"},
            {"title": "Closer", "file": "music/The Chainsmokers - Closer.mp3", "artist": "The Chainsmokers",
             "image_url": "https://via.placeholder.com/150"},
            {"title": "Locked Out Of Heaven", "file": "music/Bruno Mars - Locked Out Of Heaven.mp3",
             "artist": "Bruno Mars", "image_url": "https://via.placeholder.com/150"},
            {"title": "Sorry", "file": "music/Justin Bieber - Sorry.mp3", "artist": "Justin Bieber",
             "image_url": "https://via.placeholder.com/150"},
            {"title": "Thrift shop", "file": "music/MACKLEMORE & RYAN LEWIS - THRIFT SHOP.mp3",
             "artist": "MACKLEMORE & RYAN LEWIS", "image_url": "https://via.placeholder.com/150"},
            {"title": "Play Hard", "file": "music/David Guetta - Play Hard.mp3", "artist": "David Guetta",
             "image_url": "https://via.placeholder.com/150"},
            {"title": "Fireflies", "file": "music/Owl City - Fireflies.mp3", "artist": "Owl City",
             "image_url": "https://via.placeholder.com/150"},
            {"title": "Boulevard of Broken Dreams", "file": "music/Green Day - Boulevard of Broken Dreams.mp3",
             "artist": "Green Day", "image_url": "https://via.placeholder.com/150"},
            {"title": "Basket Case", "file": "music/Green Day - Basket Case.mp3", "artist": "Green Day",
             "image_url": "https://via.placeholder.com/150"},
            {"title": "Daylight", "file": "music/David Kushner - Daylight.mp3", "artist": "David Kushner",
             "image_url": "https://via.placeholder.com/150"},
            {"title": "More Than You Know", "file": "music/Axwell Λ Ingrosso - More Than You Know.mp3",
             "artist": "Axwell Λ Ingrosso", "image_url": "https://via.placeholder.com/150"},
            {"title": "See You Again", "file": "music/Wiz Khalifa - See You Again.mp3", "artist": "Wiz Khalifa",
             "image_url": "https://via.placeholder.com/150"},
            {"title": "The one that got away", "file": "music/Katy Perry - The one that got away.mp3",
             "artist": "Katy Perry", "image_url": "https://via.placeholder.com/150"},
            {"title": "Stereo Hearts", "file": "music/Gym Class Heroes - Stereo Hearts.mp3",
             "artist": "Gym Class Heroes", "image_url": "https://via.placeholder.com/150"},
            {"title": "Heathens", "file": "music/twenty one pilots - Heathens.mp3", "artist": "twenty one pilots",
             "image_url": "https://via.placeholder.com/150"},
            {"title": "Blinding Lights", "file": "music/The Weeknd - Blinding Lights.mp3", "artist": "The Weeknd",
             "image_url": "https://via.placeholder.com/150"},
            {"title": "Save Your Tears", "file": "music/The Weeknd - Save Your Tears.mp3", "artist": "The Weeknd",
             "image_url": "https://via.placeholder.com/150"},
            {"title": "As It Was", "file": "music/Harry Styles - As It Was.mp3", "artist": "Harry Styles",
             "image_url": "https://via.placeholder.com/150"},
            {"title": "Impossible", "file": "music/James Arthur - Impossible.mp3", "artist": "James Arthur",
             "image_url": "https://via.placeholder.com/150"},
            {"title": "Talking To The Moon", "file": "music/Bruno Mars - Talking To The Moon.mp3",
             "artist": "Bruno Mars", "image_url": "https://via.placeholder.com/150"},
            {"title": "Let Her Go", "file": "music/Passenger - Let Her Go.mp3", "artist": "Passenger",
             "image_url": "https://via.placeholder.com/150"},
            {"title": "The Night We Met", "file": "music/Lord Huron - The Night We Met.mp3", "artist": "Lord Huron",
             "image_url": "https://via.placeholder.com/150"},
            {"title": "Ho Hey", "file": "music/The Lumineers - Ho Hey.mp3", "artist": "The Lumineers",
             "image_url": "https://via.placeholder.com/150"},
            {"title": "Banners", "file": "music/Someone To You - Banners.mp3", "artist": "Banners",
             "image_url": "https://via.placeholder.com/150"},
            {"title": "Heart To Heart", "file": "music/James Blunt - Heart To Heart.mp3", "artist": "James Blunt",
             "image_url": "https://via.placeholder.com/150"},
            {"title": "Let It Go", "file": "music/James Bay - Let It Go.mp3", "artist": "James Bay",
             "image_url": "https://via.placeholder.com/150"},
            {"title": "Little Talks", "file": "music/Of Monsters And Men - Little Talks.mp3",
             "artist": "Of Monsters And Men", "image_url": "https://via.placeholder.com/150"},
            {"title": "Im Still Standing", "file": "music/Elton John - Im Still Standing.mp3", "artist": "Elton John",
             "image_url": "https://via.placeholder.com/150"},
            {"title": "Lady", "file": "music/Modjo - Lady.mp3", "artist": "Modjo", "image_url": "https://via.placeholder.com/150"},
             {"title": "Dynamite", "file": "music/Taio Cruz - Dynamite.mp3", "artist": "Taio Cruz",
              "image_url": "https://via.placeholder.com/150"},
            {"title": "Rude Boy", "file": "music/Rude Boy - Rihanna.mp3", "artist": "Rihanna",
             "image_url": "https://via.placeholder.com/150"},
            {"title": "Danza Kuduro", "file": "music/Danza Kuduro - Don Omar.mp3", "artist": "Don Omar",
             "image_url": "https://via.placeholder.com/150"},
            {"title": "California Gurls", "file": "music/Katy Perry - California Gurls.mp3", "artist": "Katy Perry",
             "image_url": "https://via.placeholder.com/150"},
            {"title": "Lights", "file": "music/Ellie Goulding - Lights.mp3", "artist": "Ellie Goulding",
             "image_url": "https://via.placeholder.com/150"},
            {"title": "Replay", "file": "music/Replay - Iyaz.mp3", "artist": "Iyaz",
             "image_url": "https://via.placeholder.com/150"},
            {"title": "Hangover", "file": "music/Taio Cruz - Hangover.mp3", "artist": "Taio Cruz",
             "image_url": "https://via.placeholder.com/150"},
            {"title": "Ni**as In Paris", "file": "music/Jay-Z & Kanye West - Ni__as In Paris.mp3",
             "artist": "Jay-Z & Kanye West", "image_url": "https://via.placeholder.com/150"},
            {"title": "Walking On A Dream", "file": "music/Empire Of The Sun - Walking On A Dream.mp3",
             "artist": "Empire Of The Sun", "image_url": "https://via.placeholder.com/150"},
            {"title": "I Dont Fuck With You", "file": "music/Big Sean - I Dont Fuck With You.mp3", "artist": "Big Sean",
             "image_url": "https://via.placeholder.com/150"}
]

@app.route('/')
def index():
    return render_template('index.html', name='Gość')

@app.route('/templates', methods=['GET', 'POST'])
def podstrona1():
    if 'score' not in session or request.method == 'GET':
        session['score'] = 0
        session['round'] = 0
        session['played_songs'] = []

    if request.method == 'POST':
        selected_option = request.form.get('choice')
        if selected_option == "no_selection" or selected_option != session['correct_answer']:
            is_correct = False
        else:
            session['score'] += 1
            is_correct = True
        session['round'] += 1

        if session['round'] >= 20:
            score = session['score']
            session.clear()
            session['score'] = score
            return redirect(url_for('result'))

    available_songs = [song for song in songs if song['title'] not in session['played_songs']]
    if not available_songs:
        # Jeśli wszystkie utwory zostały odtworzone, zresetuj listę
        session['played_songs'] = []
        available_songs = songs

    correct_song = choice(available_songs)
    session['played_songs'].append(correct_song['title'])

    options = sample(songs, 4)
    if correct_song not in options:
        options.pop()
        options.append(correct_song)
    options = sample(options, 4)
    session['correct_answer'] = correct_song['title']

    return render_template('podstrona1.html', song=correct_song, options=options, score=session['score'], round=session['round'], correct_answer=session['correct_answer'])

@app.route('/result')
def result():
    score = session.get('score', 0)
    points_text = 'punkt' if score == 1 else 'punkty' if score in [2, 3, 4] else 'punktów'
    return render_template('podstrona1wynik.html', score=score, points_text=points_text)

@app.route('/strona3')
def strona3():
    selected_song = request.args.get('song', songs[0]['title'])
    current_song = next((song for song in songs if song['title'] == selected_song), songs[0])
    return render_template('podstrona2.html', current_song=current_song, all_songs=songs)

if __name__ == '__main__':
    app.run(debug=True)