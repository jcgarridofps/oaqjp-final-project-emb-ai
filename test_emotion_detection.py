'''
Test module for EmotionDetection package
'''
import unittest
from EmotionDetection.emotion_detection import emotion_detector

class TestEmotionDetector(unittest.TestCase):
    '''
    EmotionDetector package tests
    '''
    def test_emotion_detector(self):
        '''
        emotion_detector test cases
        '''
        test1 = emotion_detector("I am glad this happened")
        self.assertTrue(test1['dominant_emotion'] == "joy")
        test2 = emotion_detector("I am really mad about this")
        self.assertTrue(test2['dominant_emotion'] == "anger")
        test3 = emotion_detector("I feel disgusted just hearing about this")
        self.assertTrue(test3['dominant_emotion'] == "disgust")
        test4 = emotion_detector("I am so sad about this")
        self.assertTrue(test4['dominant_emotion'] == "sadness")
        test5 = emotion_detector("I am really afraid that this will happen")
        self.assertTrue(test5['dominant_emotion'] == "fear")

unittest.main()
