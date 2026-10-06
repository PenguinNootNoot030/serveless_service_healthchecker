import urllib.request
import time

def lambda_handler(event, context):
    try:
        url = "https://www.google.com"
        start_time = time.perf_counter()
        response = urllib.request.urlopen(url, timeout = 5)
        time_elapsed = round((time.perf_counter() - start_time) * 1000 , 2)
        result = {
            "url" : url,
            "status_code" : response.status,
            "latency_ms" : time_elapsed,
            "healthy" : 200 <= response.status < 400
        }

        print(result)
        return result
    except Exception as error_response:
        time_elapsed = round((time.perf_counter() - start_time) * 1000,2)
        result ={
            "url":url, 
            "latency_ms": time_elapsed, 
            "healthy": False, 
            "error": str(error_response)
        }
        print(result)
        return result