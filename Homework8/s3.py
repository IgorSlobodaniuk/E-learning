import boto3
import pandas as pd
s3 = boto3.client('s3')


class S3:

    def manage(self):
        buckets = self._get_buckets()
        new_bucket = self._create_bucket()
        self._upload_file(new_bucket)
        object_content = self._read_object(new_bucket)
        self._upload_obj('file1.txt', new_bucket, 'file1.txt')
        self._download_file('file1.txt', new_bucket, 'file1.txt')
        self._delete_object(new_bucket, 'file1.txt')

    def _get_buckets(self):
        return s3.list_buckets()

    def _create_bucket(self):
        return s3.create_bucket(Bucket='bucket_name')

    def _upload_file(self, bucket):
        s3.upload_file(Filename='test.csv', Bucket=bucket, Key='key')

    def _read_object(self, bucket):
        obj = s3.get_object(Bucket=bucket, Key='test.csv')
        return pd.read_csv(obj['Body'])

    def _upload_obj(self, data_file, bucket, filename):
        with open(data_file, 'rb') as data:
            s3.upload_fileobj(data, bucket, filename)

    def _download_file(self, data_file, bucket, filename):
        with open(data_file, 'wb') as f:
            s3.download_fileobj(bucket, filename, f)

    def _delete_object(self, bucket, obj):
        s3.delete_object(Bucket=bucket, Key=obj)
