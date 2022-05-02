# lambda function invoked as part of step 1 of step function and it will run Glue crawler for generating data catalog on raw data

import json
import boto3
      
print('Loading function')
    
glue = boto3.client(service_name='glue', region_name='ap-south-1', endpoint_url='https://glue.ap-south-1.amazonaws.com')
    
def lambda_handler(event, context):
    #print("Received event: " + json.dumps(event, indent=2))
    
    try:
        glue.start_crawler(Name='AnalyticsworkshopCrawler')
        
    except Exception as e:
        print(e)
        print('Error starting crawler')
        raise e
    return event 
