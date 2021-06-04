import unittest
from write_word_docs_using_classes import Recipient, JobHunter


class TestRecipient(unittest.TestCase):
    def test_get_recipient_details(self):
        recipient = Recipient("S H", "P I", "23 Baker Street")
        recipient_details = recipient.get_recipient_details()
        expected_details = "S H\nP I\n23 Baker Street"

        self.assertEqual(recipient_details, expected_details)


class TestJobHunter(unittest.TestCase):
    def test_get_job_hunters_details(self):
        jobhunter = JobHunter("J W", "jw@gmail.com", "073", "SE")
        message = jobhunter.get_job_hunters_details()
        expected = "J W\njw@gmail.com | 073 | SE\n"

        self.assertEqual(message, expected)


if __name__ == '__main__':
    unittest.main()