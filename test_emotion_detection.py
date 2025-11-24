import unittest
from EmotionDetection.emotion_detection import emotion_detector

class TestEmotionDetection(unittest.TestCase):
    def test_emotion_detector(self):
        result = emotion_detector('I am glad this happened')
        self.assertEqual(result.get('dominant_emotion'), 'joy')
    def test_emotion_detector(self):
        result = emotion_detector('I am really mad about this')
        self.assertEqual(result.get('dominant_emotion'), 'anger')
    def test_emotion_detector(self):
        result = emotion_detector('I feel disgusted just hearing about this')
        self.assertEqual(result.get('dominant_emotion'), 'disgust')
    def test_emotion_detector(self):
        result = emotion_detector('I am so sad about this')
        self.assertEqual(result.get('dominant_emotion'), 'sadness')
    def test_emotion_detector(self):
        result = emotion_detector('I am really afraid that this will happen')
        self.assertEqual(result.get('dominant_emotion'), 'fear')

if __name__ == "__main__":
    unittest.main()