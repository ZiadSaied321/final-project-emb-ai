
import requests
import json


def emotion_detector(text_to_analyze):
    URL = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    Headers = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    Input_json = { "raw_document": { "text": text_to_analyze } }
    
    response = requests.post(URL,json = Input_json, headers = Headers)
    formatted_response = json.loads(response.text)
    emotions = formatted_response['emotionPredictions'][0]['emotion']
    
    dominant = 'anger'
    dominant_value = -100000
    for emotion in emotions.keys():
        if emotions[emotion] > dominant_value:
            dominant = emotion
            dominant_value = emotions[dominant]
    
    emotions['dominant_emotion'] = dominant
    return emotions