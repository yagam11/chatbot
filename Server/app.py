from flask import Flask, jsonify, request, render_template
import random
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/botResponse', methods=['GET', 'POST'])
def botResponse():
    # GET request
    if request.method == 'GET':
        message = {'greeting':'Hello from Flask!'}
        return jsonify(message)  # serialize and use JSON headers
    # POST request
    """
    if request.method == 'POST':
        BOT_MSGS = [
        "早上好！",
        "抱歉，我没有明白!",
        "今天天气很好!",
        "祝你有美好的一天！",
        "抱歉，我有点累！"]
        r = random.choice(BOT_MSGS)
        return jsonify({"message": r})
    """
    if request.method == 'POST':
        data = request.get_json()
        msg_text = data.get('msgText', '')
        return jsonify({"message": msg_text})
    
app.run()

