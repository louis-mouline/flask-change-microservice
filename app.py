from flask import Flask
from flask import request, jsonify


app = Flask(__name__)


def change(amount):
    # calculate the resultant change and store the result (res)
    res = []
    coins = [1, 5, 10, 25]  # value of pennies, nickels, dimes, quarters
    coin_lookup = {25: "quarters", 10: "dimes", 5: "nickels", 1: "pennies"}

    # divide the amount*100 (the amount in cents) by a coin value
    # record the number of coins that evenly divide and the remainder
    coin = coins.pop()
    num, rem = divmod(int(amount * 100), coin)
    # append the coin type and number of coins that had no remainder
    res.append({num: coin_lookup[coin]})

    # while there is still some remainder, continue adding coins to the result
    while rem > 0:
        coin = coins.pop()
        num, rem = divmod(rem, coin)
        if num:
            if coin in coin_lookup:
                res.append({num: coin_lookup[coin]})
    return res


def multiply(amount, multiplier=100):
    # Multiply the change amount by a fixed value
    res_change = change(amount)
    print(f"This is the {res_change} x 100")

    res = []
    for coin in res_change:
        ncoins = next(iter(coin))
        res.append({int(ncoins) * multiplier: coin.get(ncoins)})

    return res


@app.route("/")
def hello():
    """Return a friendly HTTP greeting."""
    print("I am inside hello world")
    return "Hello World! I can make change at route: /change/<dollar>/<cents> or I can multiply by 100: /multiply/<dollar>/<cents>"


@app.route("/change/<dollar>/<cents>")
def changeroute(dollar, cents):
    print(f"Make Change for {dollar}.{cents}")
    amount = f"{dollar}.{cents}"
    result = change(float(amount))
    return jsonify(result)


@app.route("/change-json", methods=["POST"])
def changejsonroute():
    res = []
    content = request.args.to_dict(flat=False)
    key = next(iter(content))

    if key == "amount":
        for amount in content.get(key):
            print(f"Make Change for {amount} using POST")
            result = change(float(amount))
            res.append(result)
        return jsonify(res)

    return "Error! Value accepted: {'amount': <value>}"


@app.route("/multiply/<dollar>/<cents>")
def multiplyroute(dollar, cents):
    print(f"Multiply by 100 for {dollar}.{cents}")
    amount = f"{dollar}.{cents}"
    result = multiply(float(amount))
    return jsonify(result)


if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5000, debug=True)
