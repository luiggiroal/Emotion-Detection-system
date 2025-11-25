import unittest
from EmotionDetection.emotion_detection import emotion_detector


class TestEmotionDetector(unittest.TestCase):
    def test_emotion_detection(self):
        def get_dominant_emotion(text_to_analize):
            return emotion_detector(text_to_analize).get("dominant_emotion")

        self.assertEqual(get_dominant_emotion("I am glad this happened"), "joy")
        self.assertEqual(get_dominant_emotion("I am really mad about this"), "anger")
        self.assertEqual(
            get_dominant_emotion("I feel disgusted just hearing about this"), "disgust"
        )
        self.assertEqual(get_dominant_emotion("I am so sad about this"), "sadness")
        self.assertEqual(
            get_dominant_emotion("I am really afraid that this will happen"), "fear"
        )


if __name__ == "__main__":
    unittest.main()
