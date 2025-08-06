import unittest
from EmotionDetection.emotion_detection import emotion_detector
class tset_emotion_detector(unittest.TestCase):
    def tset_emotion_detector(self):
        result1 = emotion_detector('I am glad this happened')
        self.assertEqual(result_1['dominant_emotion'],'joy')

        result1 = emotion_detector('I am really mad about this')
        self.assertEqual(result_1['dominant_emotion'],'anger')

        result1 = emotion_detector('I feel disgusted just hearing about this')
        self.assertEqual(result_1['dominant_emotion'],'disgust')

        result1 = emotion_detector('I am so sad about this')
        self.assertEqual(result_1['dominant_emotion'],'sadness')

        result1 = emotion_detector('I am really afraid that this will happen')
        self.assertEqual(result_1['dominant_emotion'],'fear')

unittest.main()