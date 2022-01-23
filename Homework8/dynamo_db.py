import boto3
from boto3.dynamodb.conditions import Key

dynamodb = boto3.resource('dynamodb', endpoint_url="http://localhost:8000")


class DynamoDB:
    def manage(self):
        table = self._create_table()
        table_data = self._read(table)
        filter_data = self._read_with_condition(table, '2022')
        updated_data = self._update_item(table, '2022', 'title')
        self._delete_table(table)

    def _create_table(self):
        table = dynamodb.create_table(
            TableName='Test',
            KeySchema=[
                {
                    'AttributeName': 'year',
                    'KeyType': 'HASH'
                },
                {
                    'AttributeName': 'title',
                    'KeyType': 'RANGE'
                }
            ],
            AttributeDefinitions=[
                {
                    'AttributeName': 'year',
                    'AttributeType': 'N'
                },
                {
                    'AttributeName': 'title',
                    'AttributeType': 'S'
                },

            ],
            ProvisionedThroughput={
                'ReadCapacityUnits': 10,
                'WriteCapacityUnits': 10
            }
        )
        return table

    def _delete_table(self, table):
        table.delete()

    def _read(self, table):
        response = table.scan()
        return response

    def _read_with_condition(self, table, year):
        response = table.query(
            KeyConditionExpression=Key('year').eq(year)
        )
        return response['Items']

    def _update_item(self, table, year, title):
        response = table.update_item(
            Key={
                'year': year,
                'title': title
            },
            UpdateExpression="set info.rating=:r, info.plot=:p, info.actors=:a",
            ExpressionAttributeValues={
                ':r': 'test1',
                ':p': 'test2',
                ':a': 'test3'
            },
            ReturnValues="UPDATED_NEW"
        )
        return response
