import requests


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
    return response.text
