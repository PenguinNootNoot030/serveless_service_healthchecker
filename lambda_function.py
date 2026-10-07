import urllib.request
import time
from datetime import datetime,timezone
from urllib.error import URLError, HTTPError

def lambda_handler(event, context):
    try:
        service_id = event["service_id"]
        url = event["url"]
        checked_at = (datetime.now(timezone.utc).isoformat(timespec="milliseconds").replace("+00:00", "Z"))
        start_time = time.perf_counter()
        response = urllib.request.urlopen(url, timeout = 5)
        time_elapsed = round((time.perf_counter() - start_time) * 1000 , 2)
        result = {
            "service_id" : service_id,
            "checked_at" : checked_at,
            "url" : url,
            "status_code" : response.status,
            "time_elapsed_ms" : time_elapsed,
            "healthy" : 200 <= response.status < 400
        }
        print(result)
        return result
    except HTTPError as error_response:
        time_elapsed = round((time.perf_counter() - start_time) * 1000, 2)
        result = {
            "service_id" : service_id,
            "checked_at" : checked_at,
            "url": url,
            "status_code": error_response.code,
            "time_elapsed_ms": time_elapsed,
            "healthy": False,
            "failure_type": "HTTP_ERROR",
            "error": str(error_response)
        }
        print(result)
        return result
    except URLError as error_response:
        time_elapsed = round((time.perf_counter() - start_time) * 1000,2)
        result ={
            "service_id" : service_id,
            "checked_at" : checked_at,
            "url":url, 
            "time_elapsed_ms": time_elapsed, 
            "healthy": False, 
            "failure_type": "URL_ERROR",
            "error": str(error_response)
        }
        print(result)
        return result
    except TimeoutError as error_response:
        time_elapsed = round((time.perf_counter() - start_time) * 1000,2)
        result = {
            "service_id" : service_id,
            "checked_at" : checked_at,
            "url": url,
            "time_elapsed_ms": time_elapsed, 
            "healthy": False,
            "failure_type": "TIMEOUT",
            "error": str(error_response)
        }
        print(result)
        return result

    
