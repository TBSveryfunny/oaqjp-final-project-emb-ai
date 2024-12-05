import requests
import json

def emotion_detector(text_to_analyze):
    # URL of the emotion detection service
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'

    # Constructing the request payload in the expected format
    myobj = { "raw_document": { "text": text_to_analyze } }

    # Custom header specifying the model ID for the emotion detection service
    header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}

    # Sending a POST request to the emotion detection API
    response = requests.post(url, json=myobj, headers=header)

    # Add error handling for invalid text
    if response.status_code == 400:
        return {'anger': None, 'disgust': None, 'fear': None, 'joy': None, 'sadness': None, 'dominant_emotion': None}

    # Parsing the JSON response from the API
    formatted_response = json.loads(response.text)

    # Extracting emotion scores from the response
    values = formatted_response['emotionPredictions'][0]['emotion']

    # Getting the dominant emotion from the values, and adding it to the values dict
    max_key = max(values, key=values.get)
    values['dominant_emotion'] = max_key

    return values
