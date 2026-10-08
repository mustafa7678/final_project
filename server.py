"""importing essential libraries for emotion detection"""
from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask(__name__)

@app.route("/emotionDetector")

def emotion_detect():
    """Analyze the emotion of the text provided by the user."""

    response = request.args.get("textToAnalyze")
    result = emotion_detector(response)

    anger = list(result)[0]
    disgust = list(result)[1]
    fear = list(result)[2]
    joy = list(result)[3]
    sadness = list(result)[4]
    dominant_emotion = list(result)[5]

    if result['dominant_emotion'] is None:
        return "Invalid text! Please try again!"

    return f"""For the given statement, the system response is
    {anger} : {result['anger']},
    {disgust} : {result['disgust']}, 
    {fear} : {result['fear']}, 
    {joy} : {result['joy']}, 
    {sadness} : {result['sadness']}, 
    {dominant_emotion} : {result['dominant_emotion']}."""

@app.route("/")
def home():
    """Render the home page."""
    return render_template("index.html")

if __name__ == "__main__":
    app.run(host= "0.0.0.0", port=5000)
