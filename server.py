from EmotionDetection.emotion_detection import emotion_detector
from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/emotionDetector")

def emotionDetector():

    response = request.args.get("textToAnalyze")
    result = emotion_detector(response)

    anger = list(result)[0]
    disgust = list(result)[1]
    fear = list(result)[2]
    joy = list(result)[3]
    sadness = list(result)[4]
    dominant = list(result)[5]

    return f"""For the given statement, the system response is
     {anger} : {result['anger']},
     {disgust} : {result['disgust']}, 
     {fear} : {result['fear']}, 
     {joy} : {result['joy']}, 
     {sadness} : {result['sadness']}, 
     {dominant} : {result['dominant_emotion']}."""

@app.route("/")
def home():
    return render_template("index.html")

if __name__ == "__main__":
    app.run(host= "0.0.0.0", port=5000)