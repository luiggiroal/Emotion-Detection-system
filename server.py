from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask(__name__)


@app.route("/emotionDetector")
def sent_detector():
    text_to_analyze = request.args.get("textToAnalyze")
    if not text_to_analyze:
        return "No text received! Please enter the text to be analyzed."
    response = emotion_detector(text_to_analyze)

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
    return render_template("index.html")


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
