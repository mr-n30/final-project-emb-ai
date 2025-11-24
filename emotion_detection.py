import requests

def emotion_detector(text_to_analyse: str) -> dict:
    try:
        body = { "raw_document": { "text": text_to_analyse } }
        url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
        headers = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}

        r = requests.post(url, headers=headers, json=body).json()

        anger = r['anger_score']
        disgust = r['disgust_score']
        fear = r['fear_score']
        joy = r['joy_score']
        sadness = r['sadness_score']
        dominant_emotion = max([anger, disgust, fear, joy, sadness])

        response_dict = {
            'anger': anger,
            'disgust': disgust,
            'fear': fear,
            'joy': joy,
            'sadness': sadness,
            'dominant_emotion': dominant_emotion
        }

        return response_dict
    except Exception as e:
        print(f'Error occurred=>{e}')
        return {}
