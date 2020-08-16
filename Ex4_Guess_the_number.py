from flask import Flask, request

app = Flask(__name__)


def build_page(title, content):
    base = '''<html>
    <head>
        <title>{}</title>
    </head>
    <body>
        <h3>{}</h3>
        <hr/>
            {}
        <hr/>
        &copy;2020
    </body>
</html>'''
    return base.format(
        title,title,content
    )


form_base = '''
    <form method='POST'>
        <p>Think the number from 0 to 1000</p>
        <input name="min_number" value="{}" type="hidden" />
        <input name="max_number" value="{}" type="hidden" />
        <input type="submit" value="Play"/>
    </form>
'''
form_play = '''
    <form method='POST'>
        <p>Step {step}: Guessing, your number is: {guess}</p>
        <input type="submit" name="answer" value="To big" />
        <input type="submit" name="answer" value="To small" />
        <input type="submit" name="answer" value="You win" />
        <input name="min_number" value="{min_number}" type="hidden" />
        <input name="max_number" value="{max_number}" type="hidden" />
        <input name="guess" value="{guess}" type="hidden" />
        <input name="step" value="{step}" type="hidden" />
    </form>
'''
form_win = '''
    <form method='POST'>
        <p>Step {step}: Win !!!!!, your number is: {guess}<br><a href="/">Click, to play again!</a></p>
    </form>
'''


@app.route("/", methods=['GET', 'POST'])
def guess_game():
    if request.method == 'POST':
        min_number = int(request.form["min_number"])
        max_number = int(request.form["max_number"])
        answer = request.form.get("answer")
        guess = int(request.form.get("guess", 500))
        step = int(request.form.get("step", 1))
        if answer == "You win":
            return build_page("Game", form_win.format(step=step, guess=guess))
        elif answer == "To big":
            max_number = guess
            step += 1
        elif answer == "To small":
            min_number = guess
            step += 1

        guess = int((max_number - min_number) / 2) + min_number
        return build_page("Game", form_play.format(step=step, guess=guess, min_number=min_number, max_number=max_number))
    else:
        return build_page("Game", form_base.format(0, 1000))


if __name__ == "__main__":
    app.run()
