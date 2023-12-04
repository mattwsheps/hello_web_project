import os
from flask import Flask, request

# Create a new Flask app
app = Flask(__name__)

# == Your Routes Here ==

@app.route('/hello', methods=['GET'])
def hello():
    name = request.args['name'] # The value is 'David'

    # Send back a friendly greeting with the name
    return f"Hello {name}!"

@app.route('/goodbye', methods=['POST'])
def goodbye():
    name = request.form['name'] # The value is 'Alice'

    # Send back a fond farewell with the name
    return f"Goodbye {name}!"

@app.route('/submit', methods=['POST'])
def submit():
    name = request.form['name']
    message = request.form['message']

    return f'Thanks {name}, you sent this message: "{message}"'

@app.route('/wave', methods=['GET'])
def wave():
    name = request.args['name']

    return f"I am waving at {name}"

@app.route('/count_vowels', methods=['POST'])
def post_count_vowels():
    vowels = ['a','e','i','o','u']
    text = request.form['text']
    vowels_in_text = [i for i in text if i in vowels]
    vowels_num = len(vowels_in_text)
    return f'There are {vowels_num} vowels in "{text}"'

@app.route('/sort-names', methods=['POST'])
def post_sort_names():
    names_str = request.form['names']
    names_list = names_str.split(',')
    sorted_names_list = sorted(names_list)
    sorted_names_str = ','.join(sorted_names_list)
    return f"{sorted_names_str}"

@app.route('/names', methods=['GET'])
def get_names():
    if 'add' not in request.args:
        return "You didn't submit any names!", 400
    names_list = ['Alice', 'Julia', 'Karim']
    added_names = request.args['add'].split(',')
    names_list += added_names
    sorted_names_list = sorted(names_list)
    return ', '.join(sorted_names_list)


# These lines start the server if you run this file directly
# They also start the server configured to use the test database
# if started in test mode.
if __name__ == '__main__':
    app.run(debug=True, port=int(os.environ.get('PORT', 5001)))

