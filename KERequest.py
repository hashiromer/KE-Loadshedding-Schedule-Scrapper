from example_payload import headers
from formOptions import PayloadManager
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
                                    self.method,
                                    self.url,
                                    headers=headers,
                                    data=self.encoded_payload,
                                    timeout=self.timeout,
                            
                                )
        response=response.text
        pt= PostTransform(response)
        pt.process_data()
        data=pt.get_data()
        return data

    def add_delay(self):
        time.sleep(2)
       



class KEManager:
    def __init__(self) -> None:
        self.payloadManager=PayloadManager()
        self.breaks=[10, 100,145]


    def start_requests(self):
        start_page=0
        last_page=15
        for i in range(start_page,last_page):
            print(i)
            if i in self.breaks:
                self.payloadManager.moveBlock()
            payload=self.payloadManager.get_payload()
            keRequest=KeRequest(payload)
            data=keRequest.get_response()
            self.payloadManager.moveCursortoNextPage()

           




if __name__ == "__main__":
    #Create a Request object
    # payload_manager= PayloadManager()
    # encodedPayload=payload_manager.getEncodedPayload()
    # keRequest= KeRequest(encodedPayload)
    # data_list=keRequest.get_response()
    # #Create Datarows from data
    # new_rows=list ( map(lambda x: DataRow(x).get_row(), data_list) )
    # print(new_rows)

    #Testing proxy connection
    proxies={
          "http": "http://104.16.192.38:80",
           "https": "https://104.16.192.38:80",

        }

    r= requests.get("https://httpbin.org/ip", proxies=proxies, timeout=5)
    print(r.status_code, r.text)
    origin = r.json()['origin']
    print(origin)


