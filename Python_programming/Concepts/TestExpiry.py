import requests
import time
from datetime import datetime

# API URL
url = 'https://prod-numbers-port.s3.us-west-1.amazonaws.com/prod/Export_Port_In_PhoneNumbers_Detail/port_in_export_2024-10-23%3A05%3A10%3A06.csv?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=ASIAWGIRPFRK4VS5BBHQ%2F20241023%2Fus-west-1%2Fs3%2Faws4_request&X-Amz-Date=20241023T051006Z&X-Amz-Expires=86400&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEE0aCXVzLXdlc3QtMSJIMEYCIQC3iXso1EJEDO6XLqcOPyR5LYGgJkRxYZ%2BYs9%2FBjQsq7wIhAISW8p0c4uP1IaMvyDjCJ5PNxcLhZdOyGzjlyZlvKdhtKpAECLb%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEQABoMNDI1Nzc1Mjc5MTg5IgwkiXmXz4ckTMiYEBsq5ANlrm9ybPewZpcvgOEPRl6FZjUGjHT4jVNTZqNDN1dfRrJkthSeorAOLLab7fDjnoh0rJNqr%2BX%2BQzkKPGo6m1If1eaCBwJNBxZ1Isa6O5FcnNmMrdLimb1B3d%2BmbMx%2BekEfJMNuQoQJmaAIkr8%2BSPqpWRx6f%2Fw1o6um8LHA6vpjzV7sGTVcsOGKSdigNhM4DuoYVukmaxZg%2F9vPWlv1xXLuFwW7ubLDWFrYC1m2c2j3jw6yhiPqTDkRrtvnCsDtu7obikUcxUg%2BbGCmmFjJ6zfLWr%2FFpRYYsa9V3nudsThwLiLOIXVOQUg%2FBOXOdkS8E%2FW1jjRbdmGrtFTxd2mpjpRWKNw8hwHyXmTTaU%2FZlfouBQSfy4CbZKKFjTYF%2B4H2afBW1UqYewUzwk5zsK303rWUE1RMk59G4RmuofJESuNEzp5AISxXjJHwFFAd7Eqa0Aui%2BsY0u%2BNbdXgkTBpqt77p%2B1xY0ZGrmlF%2B6Mrb1O5aBdmRa5r9R4GKz6AQ8RkkG6uwR%2BRIrVzz5BvwBndHlKEwspSGGDMjX9uuxIIJ9Oj%2FG3WfgpXn4AFcUKdHylKJFPomcMMRIzbrKFOrGWDwpXfOZ8GNEVosXMHT7O9WqN60fJtAL%2Bgp8LIzTKajC4pPxoBjMhtjMLCC4rgGOqQB5A5SdoQBVdUvqKB6PqoU1f0EmUU4onhKO3zrpHDMCjIH%2Ba3c8Xw51ryD5qnXjQtf2fJBkrHw6gOJrfoyd00wZXKnX2GCG6xbzuIoOKtT2%2FA3tva%2B6Nadu8vwVYzppJV3hLs9W3v0fbfSPpeFmE2leoHUd4KoztftOisiePt%2FMKvJKtOlwK%2BHob%2BjKDCx%2F2dJ%2FF3WSVNv83J71ttZmhQYnYZuDG0%3D&X-Amz-SignedHeaders=host&X-Amz-Signature=05dafe3c9df78aab8f8110e1c455793b5927bc9d3bde52a714d587d9ebe354f7'

# Non-200 response counter
non_200_counter = 0

# Log file for start and end times
log_file = "api_log.txt"

def log_time(message):
    """Logs the message with a timestamp to the log file."""
    with open(log_file, "a") as f:
        f.write(f"{datetime.now()}: {message}\n")

# Start the process
log_time("Start monitoring API.")

while True:
    try:
        # Make the API request
        response = requests.get(url)
        print(f"API called at {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")

        # Check if the response status code is not 200
        if response.status_code != 200:
            non_200_counter += 1
            log_time(f"Non-200 response received: {response.status_code}. Attempt {non_200_counter}.")
        else:
            non_200_counter = 0  # Reset counter on successful request

        # If 4 consecutive non-200 responses, stop the script
        if non_200_counter >= 4:
            log_time("4 consecutive non-200 responses received. Stopping the script.")
            log_time("End monitoring API.")
            break

        # Sleep for 5 seconds before the next request
        time.sleep(5)

    except Exception as e:
        log_time(f"Error: {e}")
        break
