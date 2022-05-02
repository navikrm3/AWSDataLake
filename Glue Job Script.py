import sys
from awsglue.transforms import *
from awsglue.utils import getResolvedOptions
from pyspark.context import SparkContext
from awsglue.context import GlueContext
from awsglue.job import Job

args = getResolvedOptions(sys.argv, ["JOB_NAME", "prefix"])
sc = SparkContext()
glueContext = GlueContext(sc)
spark = glueContext.spark_session
job = Job(glueContext)
job.init(args["JOB_NAME"], args)

# Script generated for node Amazon S3
AmazonS3_node1650686454768 = glueContext.create_dynamic_frame.from_options(
    format_options={"quoteChar": '"', "withHeader": True, "separator": ","},
    connection_type="s3",
    format="csv",
    connection_options={"paths": ["s3://sdlfrawbucket/"], "recurse": True},
    transformation_ctx="AmazonS3_node1650686454768",
)

# Script generated for node Amazon S3
AmazonS3_node1650687657201 = glueContext.write_dynamic_frame.from_options(
    frame=AmazonS3_node1650686454768,
    connection_type="s3",
    format="glueparquet",
    connection_options={"path": args["prefix"], "partitionKeys": []},
    format_options={"compression": "snappy"},
    transformation_ctx="AmazonS3_node1650687657201",
)

job.commit()
