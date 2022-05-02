#lambda function invoked by SQS notification once an object added to s3 bucket

import json
import boto3 
import uuid
import datetime
       
def lambda_handler(event, context):
 # print(event)
 client = boto3.client("sqs")
 client2 = boto3.client("stepfunctions")
 transactionID = str(uuid.uuid1())
 now = datetime.datetime.now()
# print(now)
 year = lambda x: x.year
 month = lambda x: x.month
 day = lambda x: x.day
 year2 = year(now)
 month2 = month(now)
 date2 = day(now)
 prefix = "s3://sdlfanalyticsbucket" + "/" + str(year2) + "/" + str(month2) + "/" + str(date2) + "/"
# print(prefix)
 input = {"bucket_name": "sdlfrawbucket", "object": "abcd.csv", "prefix": prefix}
# event_body = json.loads(event['Records'][0]['body'])
# event_body = json.loads(event)
#  event_body2 = json.loads(event_body["Records"][0]["s3"])
#  data = event[0]['body']['object']['key']
#  data2 = event_body['Records']['body']['object']['key']
# message = str(event_body) 
# response = client2.send_message(
#   QueueUrl = "https://sqs.ap-south-1.amazonaws.com/246267001764/SQSafterLambda1",
#   MessageBody = message)
#  print(str(event_body))
#  print(str(data2))
 response = client2.start_execution(
   stateMachineArn = 'arn:aws:states:ap-south-1:246267001764:stateMachine:MyStateMachine',
   name = transactionID,
   input = json.dumps(input)
   )
 
# return {
#   'statusCode': response["ResponseMetadata"]["HTTPStatusCode"],
#  'body': json.dumps(response["ResponseMetadata"])
#  }
  
  
  
  
  
