import boto3
import json
from datetime import datetime
import time
import base64
my_stream_name = 'BotoDemo'
kinesis_client = boto3.client('kinesis', region_name=('ap-south-1'))
response = kinesis_client.describe_stream(StreamName=my_stream_name)

my_shard_id = response['StreamDescription']['Shards'][0]['ShardId']
print (my_shard_id )
shard_iterator = kinesis_client.get_shard_iterator(StreamName=my_stream_name,
                                                      ShardId=my_shard_id,
                                                      ShardIteratorType='TRIM_HORIZON')

my_shard_iterator = shard_iterator['ShardIterator']
#print (my_shard_iterator)
record_response = kinesis_client.get_records(ShardIterator=my_shard_iterator,
                                              Limit=1)
cnt=0
record_response = kinesis_client.get_records(ShardIterator=record_response['NextShardIterator'],
                                                  Limit=2)
print(record_response)
#print(record_response['Records'][0]['Data'])
data=record_response['Records'][0]['Data'].decode('utf8')
#print(data)
data=json.loads(data)
#print(data['img'])
data1=base64.b64decode(data['img'])
#print(data1)
filename = 'b.jpg'
with open(filename, 'wb') as f:
    f.write(data1)
     #wait for 5 seconds
    #time.sleep(0.1)
