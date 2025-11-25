from flask import Flask, request, render_template
from EmotionDetection.emotion_detection import emotion_detector

app = Flask(__name__)

@app.route("/", methods=["GET"])
def index():
    return render_template('index.html', title='Title page yo!')

@app.route("/emotionDetector", methods=["GET"])
def analyze():
    """
    Returns detected emotion for provided text.
    """
    text = request.args.get("textToAnalyze")
    r = emotion_detector(text)
    if r.get('dominant_emotion') == None:
        return 'Invalid text! Please try again!'

    return f'Here is your response: {}'

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=1337, debug=True)