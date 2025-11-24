import unittest
from EmotionDetection.emotion_detection import emotion_detector

class TestEmotionDetection(unittest.TestCase):
    def test_emotion_detector(self):
        result = emotion_detector('I am glad this happened')
        self.assertEqual(result.get('dominant_emotion'), 'joy')

if __name__ == "__main__":
    unittest.main()