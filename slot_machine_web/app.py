from flask import Flask, render_template, request
import random

app = Flask(__name__)

SYMBOLS = ['CHERRY', 'WATERMELON', 'LEMON', 'BELL', 'STAR']

def spin_row():
    return [random.choice(SYMBOLS) for _ in range(3)]

def get_payout(row, bet):
    if row[0] == row[1] == row[2]:
        payouts = {
            'CHERRY': 3,
            'WATERMELON': 4,
            'LEMON': 5,
            'BELL': 10,
            'STAR': 20
        }
        return bet * payouts.get(row[0], 0)
    elif row[0] == row[1] or row[1] == row[2] or row[0] == row[2]:
        return int(bet * 0.5)
    return 0

@app.route("/", methods=["GET", "POST"])
def index():
    balance = 10000
    result = []
    payout = 0
    message = ""
    
    if request.method == "POST":
        try:
            bet = int(request.form["bet"])
            if bet <= 0:
                message = "Bet must be greater than 0."
            elif bet > balance:
                message = "Insufficient funds."
            else:
                result = spin_row()
                payout = get_payout(result, bet)
                message = f"You {'won' if payout > 0 else 'lost'} ${payout:,}."
                balance = balance - bet + payout
        except ValueError:
            message = "Invalid input."

    return render_template("index.html", symbols=SYMBOLS, result=result, payout=payout, message=message, balance=balance)

if __name__ == "__main__":
    app.run(debug=True)
