from flask import Flask, render_template, session, request, redirect, url_for
from connection import english_drop, score_cleaned, type_cleaned, aired_cleaned, episodes_cleaned, random_letter

app = Flask(__name__)
app.secret_key = 'your_secret_key'

#name_drop = name_drop.lower()
hints = [episodes_cleaned, type_cleaned, aired_cleaned, score_cleaned]

@app.route('/')
def game():

    if 'guessed_words' not in session:
        session['guessed_words'] = [] #initialize a guessed words list 
    if 'hints_displayed' not in session:
        session['hints_displayed'] = [False, False, False, False] #Initializes the hints list
        
    
    guessed_words = session['guessed_words']

    length = len(english_drop)
    
    correct_guess = english_drop in guessed_words
    
    guess_checker = session.pop('guess_checker', None)  # Get the message and remove it from session
    hints_displayed = session['hints_displayed']

    return render_template('game.html', display_word=english_drop, guessed_words=guessed_words, correct_guess=correct_guess, guess_checker=guess_checker, 
                           hints=hints, hints_displayed=hints_displayed, random_letter=random_letter, length=length)

@app.route('/guess', methods = ['POST'])
def guess():
    guessed_word = request.form['word']  # Get the guessed word from the form

    if 'guessed_words' not in session:
        session['guessed_words'] = []

    # Add the guessed word to the list if it is not already there
    if guessed_word not in session['guessed_words']:
        session['guessed_words'].append(guessed_word)
        
        # Check if the guessed word is correct or incorrect
        if guessed_word == english_drop:
            session['guess_checker'] = f"'{guessed_word}' is correct, Congratulations!" 
        else:
            session['guess_checker'] = f"'{guessed_word}' is incorrect. Try again!"
    
    return redirect(url_for('game'))  # Redirect back to the game page




@app.route('/hint/<int:hint_id>', methods=['POST'])
def hint (hint_id):
    if 'hints_displayed' not in session:
        session['hints_displayed'] = [False, False, False, False]

    session['hints_displayed'][hint_id] = True
    return redirect(url_for('game'))


if __name__ == '__main__':
    app.run(debug = True)
    
