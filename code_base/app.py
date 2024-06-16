from flask import Flask, jsonify, request, send_from_directory
import random

app = Flask(__name__, static_folder='static')

responses = [
    "It is certain.",
    "It is decidedly so.",
    "Without a doubt.",
    "Yes – definitely.",
    "You may rely on it.",
    "As I see it, yes.",
    "Most likely.",
    "Outlook good.",
    "Yes.",
    "Signs point to yes.",
    "Reply hazy, try again.",
    "Ask again later.",
    "Better not tell you now.",
    "Cannot predict now.",
    "Concentrate and ask again.",
    "Don't count on it.",
    "My reply is no.",
    "My sources say no.",
    "Outlook not so good.",
    "Very doubtful."
]

# run app by entering "python app.py"  in the CLI
# Confirm code works by using POSTMAN:
# > set as 'POST' request
# > set URL as http://127.0.0.1:5000/shake
# > choose 'Body'->'raw'->'JSON'
#  enter JSON test text in the Body of the request, example:
# {
#     "question": "Will it rain tomorrow?"
# }
# > hit 'Send' and view response (app must be running)
@app.route('/shake', methods=['POST'])
def shake_ball():
    question = request.json.get('question')
    if not question:
        return jsonify({"error": "No question provided"}), 400
    response = random.choice(responses)
    return jsonify({"response": response})

@app.route('/')
def index():
    return send_from_directory(app.static_folder, 'index2.html')

# Add this route below to app.py before the if __name__ == '__main__': block.
# Explicitly tell Flask to serve static files from the static directory if encountering issues of Flask correctly serving the static files.
# Alternative is to hardcode the route of the css and js files in the html document (it is currently commented out but there for ref.)
@app.route('/<path:path>')
def static_proxy(path):
    return send_from_directory(app.static_folder, path)

# Works when you navigate to the link: http://127.0.0.1:5000/shake
# @app.route('/shake', methods=['GET'])
# def shake_ball():
#     return responses

# Works when you navigate to the link: http://127.0.0.1:5000/respond
# @app.get('/respond')
# def get_req():
#     return responses

if __name__ == '__main__':
    app.run(debug=True)