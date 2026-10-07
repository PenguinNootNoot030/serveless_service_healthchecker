# Serverless-service health checker

## Brief
This is a serverless health monitoring system built with AWS.
Every 5 minutes, Amazon Eventbridge invokes a Lambda function to perform an HTTP health check on a provided service.
For each check, the Lambda function records：
- Service ID
- Timestamo of the check
- HTTP status code
- Response time
- Health status
Each health-check result is stored in Dynamo DB.
If a service is unhealthy, an alert is additionally sent out through Amazon SNS.

## Development Log
### 2026-10-06 - Lambda function v1
- Created the initial Lambda function.
- Added basic HTTP service health checking and exception failure to prevent execution failure.

### 2026-10-07
- Updated Lambda function's exception handling logic for handling differnet types of errors, including HTTP error, Url error and Timeout error.
- Removed hardcoded url for intergartion with events in the futrue.
- Added in service_id and timestamp as planned keys for dynamo db integration in the future.
