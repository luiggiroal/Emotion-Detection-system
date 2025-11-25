import requests
import json


def emotion_detector(text_to_analyze):
    """Function that runs emotion detection using the Emotion
    Predict function of the Watson NLP Library.
    Input:
    'text_to_analyze': Text to be analyzed (str)
    Output:
    'response.text': The text attribute of the response object
    as received from the Emotion Predict function."""
    url = (
        "https://sn-watson-emotion.labs.skills.network/"
        "v1/watson.runtime.nlp.v1/NlpService/EmotionPredict"
    )
    headers = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    payload = {"raw_document": {"text": text_to_analyze}}
    response = requests.post(url=url, headers=headers, json=payload, timeout=10)
    if response.status_code == 400:
        list_emotions = [
            "anger",
            "disgust",
            "fear",
            "joy",
            "sadness",
            "dominant_emotion",
        ]
        empty_emotions = {emotion: None for emotion in list_emotions}
        return empty_emotions

    response_dict = json.loads(response.text)
    emotions = response_dict["emotionPredictions"][0]["emotion"]

    # dominant_score = 0
    # dominant_emotion = None
    # for emotion, score in emotions.items():
    #     if score > dominant_score:
    #         dominant_score = score
    #         dominant_emotion = emotion

    # Shorter alternative. Return the emotion with the highest
    # score.
    dominant_emotion = max(emotions, key=emotions.get)

    emotions["dominant_emotion"] = dominant_emotion

    return emotions
