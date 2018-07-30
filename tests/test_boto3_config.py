import boto3
import unittest
import warnings

class Boto3S3AccessTest(unittest.TestCase):
    """ Class to test Awspot instance has read, write, list access to s3 bucket 'awspot-instances' """

    def setUp(cls):
        # setup s3 connection
        cls.s3 = boto3.resource('s3')
        cls.bucket = cls.s3.Bucket('awspot-instances')  
        
        # filter bad ssl warning (result of boto3 bug)
        warnings.filterwarnings("ignore", category=ResourceWarning, message="unclosed.*<ssl.SSLSocket.*>") 

    def test_1_write(self):
        """ write test.txt to bucket """

        with open('test.txt', 'rb') as test_data:
            response = self.bucket.put_object(Key='test.txt', Body=test_data)

        # indicates that the requester was successfully charged for the request.
        charged = response.get('RequestCharged')
        
        self.assertIsNotNone(charged)

    def test_2_read(self):
        """ read test.txt from bucket """
        test_obj =  self.s3.Object('awspot-instances', 'test.txt').get()
        test_contents = test_obj['Body'].read().decode('utf-8') 
        self.assertEqual("This is a test.\n", test_contents)

    def test_3_delete(self):
        """ delete object and confirm object is not list in bucket """

        test_obj = self.s3.Object('awspot-instances', 'test.txt')
        test_obj.delete()

        is_listed = any(obj.key=='test.txt' for obj  in self.bucket.objects.filter(Prefix='test.txt'))
        
        self.assertFalse(is_listed)
    

if __name__ == "__main__":
    unittest.main() 
