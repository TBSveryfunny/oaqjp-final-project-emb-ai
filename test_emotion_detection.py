# Import the function from the 'EmotionDetection' package, and the unittest library.
from EmotionDetection.emotion_detection import emotion_detector
import unittest

# Create the class.
class TestEmotionDetector(unittest.TestCase):
    def test_emotion_detector(self):

        # Test case 1.
        self.assertEqual(emotion_detector("I am glad this happened")["dominant_emotion"], "joy")

        # Test case 2.
        self.assertEqual(emotion_detector("I am really mad about this")["dominant_emotion"], "anger")

        # Test case 3.
        self.assertEqual(emotion_detector("I feel disgusted just hearing about this")["dominant_emotion"], "disgust")

        # Test case 4.
        self.assertEqual(emotion_detector("I am so sad about this")["dominant_emotion"], "sadness")

        # Test case 5.
        self.assertEqual(emotion_detector("I am really afraid that this will happen")["dominant_emotion"], "fear")

# Run the test cases.
unittest.main()