# THE setUp() Method

# Will modify the test survey.py into more eficient code
import unittest
from survey import AnonymousSurvey


# Import unittest module and the class to be tested

# Define the class Test... wth imported TestCase slass from unittest module
class TestAnonymousSurvey(unittest.TestCase):
    """Test for the class Anonymous Survey"""

    def setUp(self):
        """
        Create a survey and set of responses for use in all test methods
        """
        question = "What language did you first learn to speak?"
        self.my_survey = AnonymousSurvey(question)
        self.responses = ['English', 'Spanish', 'Mandarin']

    # method testing is responses are storing
    def test_store_single_response(self):
        """Test that a single response is stored properly"""
        self.my_survey.store_responses(self.responses[0])
        self.assertIn(self.responses[0], self.my_survey.responses)

    # We want to make sure that more responses will work - let. verify that
    def test_store_three_responses(self):
        """Test that three individual responses are stored properly"""

        # Call method to store each of the objects
        for response in self.responses:
            self.my_survey.store_responses(response)

        # Writing another loop ensuring that each response is in responses
        for response in self.responses:
            self.assertIn(response, self.my_survey.responses)


if __name__ == '__main__':
    unittest.main()
