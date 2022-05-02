# lambda function to start the glue job for data transformation to Parquet and saving the transformed file into the analytics DB

import json
import boto3 
import uuid
import datetime
           
def lambda_handler(event, context):
 # print(event)
 client = boto3.client('glue')
 now = datetime.datetime.now()
# print(now)
 year = lambda x: x.year
 month = lambda x: x.month
 day = lambda x: x.day
 year2 = year(now)
 month2 = month(now)
 date2 = day(now)
 prefix = "s3://sdlfanalyticsbucket" + "/" + str(year2) + "/" + str(month2) + "/" + str(date2) + "/"
 response = client.start_job_run(
               JobName = 'analyticsworkshopjob',
               Arguments = {
                 '--prefix': prefix} )
 return event             
                 
                 
