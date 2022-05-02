CREATE or replace  STORAGE INTEGRATION RAW_STORAGE_INTEGRATION
  TYPE = EXTERNAL_STAGE
  STORAGE_PROVIDER = S3
  ENABLED = TRUE
  STORAGE_AWS_ROLE_ARN = 'arn:aws:iam::246267001764:role/RoleforSnowflakeaccess'
  STORAGE_ALLOWED_LOCATIONS = ('s3://sdlfrawbucket/');
  
  desc storage integration RAW_STORAGE_INTEGRATION;
create or replace stage RAW_ext_stage
  storage_integration = "RAW_STORAGE_INTEGRATION"
  url = 's3://sdlfrawbucket/';
  
create or replace external table RAW_customer
   with location = @RAW_ext_stage/
 auto_refresh=true 
 file_format = (type=csv)
 pattern = '.*customers.*[.]csv';
 
select * from raw_customer;

CREATE or replace  STORAGE INTEGRATION ANALYTICS_STORAGE_INTEGRATION
  TYPE = EXTERNAL_STAGE
  STORAGE_PROVIDER = S3
  ENABLED = TRUE
  STORAGE_AWS_ROLE_ARN = 'arn:aws:iam::246267001764:role/RoleforSnowflakeaccess'
  STORAGE_ALLOWED_LOCATIONS = ('s3://sdlfanalyticsbucket/');

desc storage integration ANALYTICS_STORAGE_INTEGRATION;

create or replace stage analytics_ext_stage
  storage_integration = "ANALYTICS_STORAGE_INTEGRATION"
  url = 's3://sdlfanalyticsbucket/';


create or replace external table analytic_customer
 with location = @analytics_ext_stage/2022/4/23/
 auto_refresh=true 
 file_format = (type=parquet)
 pattern = '.*run-AmazonS3_node1650687657201-14-part-block-0-r-00000-snappy.*[.]parquet';
 
show stages;

select * from analytic_customer;
