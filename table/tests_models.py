from unittest import TestCase
import datetime
from .models import SampleInformation


# Create your tests here.

class SampleInformationModelTestCase(TestCase):
    """Tests for the SampleInformation model"""
    def setUp(self):
        self.sampleinfo = SampleInformation()
        self.sampleinfo.d_number = "D00.00000"
        self.sampleinfo.date = "2016-01-10"
        self.sampleinfo.worksheet_number = "00000"
        self.sampleinfo.link = "/sample/link"
        # check that we can save it to the database
        self.sampleinfo.save()

    def test_SampleInformation(self):


        # now check we can find it in the database again
        self.all_samples_in_database = SampleInformation.objects.all()
        self.assertEqual(len(self.all_samples_in_database), 1)
        self.only_sample_in_the_database = self.all_samples_in_database[0]
        self.assertEqual(self.only_sample_in_the_database, self.sampleinfo)
        self.assertEqual(str(self.sampleinfo), self.sampleinfo.d_number)

        # and check that it has saved the attributes
        self.assertEquals(self.only_sample_in_the_database.d_number, "D00.00000")
        self.assertEquals(self.only_sample_in_the_database.date,
                          datetime.date(2016, 1, 10))
        self.assertEqual(self.only_sample_in_the_database.worksheet_number, "00000")
        self.assertEqual(self.only_sample_in_the_database.link, "/sample/link")
        self.assertEqual(self.only_sample_in_the_database.classification,
                         "not_checked")
        self.assertEqual(self.only_sample_in_the_database.first_check,
                         "not_checked")
        self.assertEqual(self.only_sample_in_the_database.second_check,
                         "not_checked")

        # test that d_number is a string
        self.assertEqual(self.sampleinfo.d_number.__str__(), "D00.00000")
    def tearDown(self):
        self.sampleinfo.delete()

if __name__ == '__main__':
    unittest.main()
