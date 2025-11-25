"""Executing this function initiates the application of emotions
detection to be executed over the Flask channel and deployed on
localhost:5000.
"""

from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask(__name__)


@app.route("/emotionDetector")
def sent_detector():
    """This code receives the text from the HTML interface and
    runs emotion detection over it using emotion_detector()
    function. The output returns the score for each
    emotion and the dominant one for the provided text.
    """
    text_to_analyze = request.args.get("textToAnalyze")
    response = emotion_detector(text_to_analyze)
    if response["dominant_emotion"] is None:
        return "Invalid text! Please try again!"

    last_keys = []
    last_values = []
    for _ in range(2):
        last_key = list(response.keys())[-1]
        last_value = response.pop(last_key)
        last_keys.append(last_key)
        last_values.append(last_value)

    emotions = str(response)[1:-1]

    return (
        f"For the give statement, the system response is {emotions} and "
        f"'{last_keys[-1]}': {last_values[-1]}. The dominant emotion is {last_values[-2]}."
    )


@app.route("/")
def render_index_page():
    """This function initiates the rendering of the main application
    page over the Flask channel
    """
    return render_template("index.html")


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
