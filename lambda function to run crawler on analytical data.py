# lambda function to run crawler on analytics data 

import json
import boto3
         
print('Loading function')
     
glue = boto3.client(service_name='glue', region_name='ap-south-1', endpoint_url='https://glue.ap-south-1.amazonaws.com')
    
def lambda_handler(event, context):
    #print("Received event: " + json.dumps(event, indent=2))
     
    try:
        glue.start_crawler(Name='Analyticsworkshopcrawler2')
#        print(json.dumps(event))
#        jsonStr = event.decode("utf-8")
#        event_data = json.loads(str(event))
#        message = str(event_data)
#        print(event_data)
#        bucket = event_data["bucket_name"]
#        print(bucket)
    except Exception as e:
        print(e)
        print('Error starting crawler')
        raise e
