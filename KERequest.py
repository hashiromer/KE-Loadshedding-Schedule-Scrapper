from example_payload import headers
from postTransformations import PostTransform
import requests
import time

class KeRequest:
    def __init__(self, encoded_payload:str):
        self.url="https://staging.ke.com.pk:8490/index.aspx"
        self.method="POST"
        self.timeout=5
        self.encoded_payload=encoded_payload


    def get_response(self):
        self.add_delay()
        response = requests.request(
                    self.method, self.url, headers=headers, data=self.encoded_payload, timeout=self.timeout)
        response=response.text
        pt= PostTransform(response)
        pt.process_data()
        data=pt.get_data()
        return data

    def add_delay(self):
        time.sleep(1)
       
            