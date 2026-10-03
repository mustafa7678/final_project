from EmotionDetection.emotion_detection import emotion_detector
import unittest

class test_emotion_detection(unittest.TestCase):
    
    def dominant(self,text):
        return emotion_detector(text)['dominant_emotion']

    def test_emotion_detection(self):

        self.assertEqual(self.dominant('I am glad this happened'), 'joy')
        self.assertEqual(self.dominant('I am really mad about this'), 'anger')
        self.assertEqual(self.dominant('I feel disgusted just hearing about this'), 'disgust')
        self.assertEqual(self.dominant('I am so sad about this'), 'sadness')
        self.assertEqual(self.dominant('I am really afraid that this will happen'), 'fear')

if __name__ == '__main__':
    unittest.main()