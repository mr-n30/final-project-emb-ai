import requests

def emotion_detector(text_to_analyse: str) -> dict:
    try:
        body = { "raw_document": { "text": text_to_analyse } }
        url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
        headers = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}

        r = requests.post(url, headers=headers, json=body).json()

        anger = r['emotionPredictions'][0]['emotion']['anger']
        disgust = r['emotionPredictions'][0]['emotion']['disgust']
        fear = r['emotionPredictions'][0]['emotion']['fear']
        joy = r['emotionPredictions'][0]['emotion']['joy']
        sadness = r['emotionPredictions'][0]['emotion']['sadness']
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
ķ       return {}
