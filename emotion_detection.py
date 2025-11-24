import requests

def emotion_detector(text_to_analyse: str) -> dict:
    try:
        body = { "raw_document": { "text": text_to_analyse } }
        url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
        headers = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}

        r = requests.get(url, headers=headers, json=body).json()
        return r
    except Exception as e:
        print(f'Error occurred=>{e}')
        return {}
