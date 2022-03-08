import unittest
from survey import AnonymousSurvey


# Import unittest module and the class to be tested

# Define the class Test... wth imported TestCase slass from unittest module
class TestAnonymousSurvey(unittest.TestCase):
    """Test for the class Anonymous Survey"""

    # method testing is responses are storing
    def test_store_single_response(self):
        """Test that a single response is stored properly"""
        question = "What language did you first learn to speak?"
        my_survey = AnonymousSurvey(question)
        # First we define the attribute  - to create an instance of a class

        # Then call the method and check if the value input
        # is in the list in the same method
        my_survey.store_responses('English')
        self.assertIn('English', my_survey.responses)

    # We want to make sure that more responses will work - let. verify that
    def test_store_three_responses(self):
        """Test that three individual responses are stored properly"""
        question = "What language did you first learn to speak?"
        my_survey = AnonymousSurvey(question)
        responses = ['English', 'Spanish', 'Mandarin']
        # Created a survey object = list of three responses

        # Call method to store each of the objects
        for response in responses:
            my_survey.store_responses(response)

        for response in responses:
            self.assertIn(response, my_survey.responses)


if __name__ == '__main__':
    unittest.main()
