import requests

def emotion_detector(text_to_analyse: str) -> dict:
    try:
        body = { "raw_document": { "text": text_to_analyse } }
        url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
        headers = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}

        r = requests.post(url, headers=headers, json=body)

        response_dict = {
            'anger': None,
            'disgust': None,
            'fear': None,
            'joy': None,
            'sadness': None,
        }

        if r.status_code == 400:
            return response_dict
        
        r = r.json()

        anger = r['emotionPredictions'][0]['emotion']['anger']
        disgust = r['emotionPredictions'][0]['emotion']['disgust']
        fear = r['emotionPredictions'][0]['emotion']['fear']
        joy = r['emotionPredictions'][0]['emotion']['joy']
        sadness = r['emotionPredictions'][0]['emotion']['sadness']

        response_dict = {
            'anger': anger,
            'disgust': disgust,
            'fear': fear,
            'joy': joy,
            'sadness': sadness,
        }

        response_dict['dominant_emotion'] = max(response_dict, key=response_dict.get)

        if response_dict['dominant_emotion'] == None:
            return 'Invalid text! Please try again!'

        return response_dict
    except Exception as e:
        print(f'Error occurred=>{e}')
        return {"error": str(e)}
