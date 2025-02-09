'''
Emotion detector module
'''
import json
import requests

def emotion_detector(text_to_analyze):
    '''
    Emotion detector function
    '''

    url = 'https://sn-watson-emotion.labs.skills.network/v1/' + \
            'watson.runtime.nlp.v1/NlpService/EmotionPredict'
    header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    data = { "raw_document": { "text": text_to_analyze } }

    response = requests.post(url, json=data, headers=header, timeout = 10)
    response_json = json.loads(response.text)
    emotions = response_json["emotionPredictions"][0]["emotion"]
    dominant_emotions = [k for k in emotions.keys() if emotions[k] == max(emotions.values())]

    ret = {
        "anger": emotions["anger"],
        "disgust": emotions["disgust"],
        "fear": emotions["fear"],
        "joy": emotions["joy"],
        "sadness": emotions["sadness"],
        "dominant_emotion": dominant_emotions[0],
    }

    return ret
