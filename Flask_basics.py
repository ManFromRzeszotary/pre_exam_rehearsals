from flask import Flask
from flask import request
import datetime
from datetime import datetime
import random
from random import randint
from random import shuffle

app = Flask(__name__)


@app.route("/<string:name>")
def hello(name):
    return 'Hello ' + name + '!'


@app.route("/<int:age>")  # no parameter methods passed defaults to GET
def age(age):
    return 'You are ' + str(age) + ' and still alive!'


@app.route("/date")  # no parameter methods passed defaults to GET
def display_date():
    # actual date
    return 'It is  ' + str(datetime.today().strftime('%Y-%m-%d')) + ' have a nice day'


@app.route("/time")  # no parameter methods passed defaults to GET
def display_time():
    # actual time
    return 'It is  ' + str(datetime.today().strftime('%H:%M')) + ' have a nice day'


@app.route("/licz/<a>/<b>")  # no parameter methods passed defaults to GET
def sum_nbrs(a, b):
    answer = float(a) + float(b)
    return 'adding ' + str(a) + ' to ' + str(b) + ' gives: ' + str(answer)


@app.route("/losuj")  # no parameter methods passed defaults to GET
def get_three():
    return 'randomly selected digits are: ' + str(randint(0, 9)) + ' ' + str(randint(0, 9)) + ' and ' + str(
        randint(0, 9))


@app.route("/lotek")  # no parameter methods passed defaults to GET
def lotek():
    # sorting a list of strings beware of 11 > 6 :)
    whole_set = [str(x) for x in range(1, 50)]
    random.shuffle(whole_set)
    answer = whole_set[:5]
    answer.sort()
    return 'Your lucky numbers are: ' + ', '.join(answer)


@app.route("/lotek_v1")  # no parameter methods passed defaults to GET
def lotek_v1():
    whole_set = [x for x in range(1, 50)]
    random.shuffle(whole_set)
    lucky_nbrs = whole_set[:5]
    lucky_nbrs.sort()
    answer = ''
    for n in lucky_nbrs:
        answer += str(n) + ', '
    return 'Your lucky numbers are: ' + answer[:-2]


@app.route('/say_hi', methods=['GET'])
def say_hi():
    return """
    <form action="/say_my_name" method="POST">
        <label>Type your name:
            <input type="text" name="print_name">
        <label>
            <button type="submit"> send </button>
        </label>
    </form>
    """


@app.route('/say_my_name', methods=['POST'])
def say_my_name():
    name = request.form['print_name']
    return f'Hello {name}'







@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        # obsłuż dane logowania
        return 'pass data with POST method'
    else:
        return 'get data with GET method'


# Dane, które przesyłamy za pomocą formularza metodą GET znajdują się w obiekcie request.args,
# natomiast te przysyłane metodą POST znajdują się w request.form.
# Dostać się do nich możemy dzięki konstrukcji request.args["nazwa-klucza"] lub request.form["nazwa-klucza"].
# Jeśli chcemy odebrać wiele danych o tej samej nazwie, musimy użyć następujacego kodu:
# request.args.getlist(<nazwa>)
# lub
# request.form.getlist(<nazwa>)
# gdzie nazwa to wartość atrybutu name z HTML-a. Metoda zwraca listę wartości.
# form.html
# < input
# type = "checkbox"
# name = "pizza_topping"
# value = "cheese" >
# dodatkowy
# ser
# # < input
# type = "checkbox"
# name = "pizza_topping"
# value = "ham" >
# szynka
# # app.py
# # @app.route("/pizza/add_toppings", method=["POST"])
# # def add_toppings():
#     tops = request.form.getlist("pizza_topping")
# #     # dalej kod

if __name__ == "__main__":
    app.run(debug=True)
