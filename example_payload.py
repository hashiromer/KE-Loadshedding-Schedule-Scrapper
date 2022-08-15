from urllib.parse import unquote, quote


class PayloadProcessor:
    def __init__(self) -> None:
        self.payload = "__EVENTTARGET=&__EVENTARGUMENT=&__VIEWSTATE=75bMG2iqZw68TRb9R%2BHHUJSZH7GrEdwuDANza%2F1gsiINbPQ8317qddj1VnAZ%2BwMm8nNpRmLuW1nj6g2BgUkkhuUv1dozcz0TvRK3F%2BfQsbHFAnqAxAa7cgeAvhIURkbp1Do7nwPD8%2F1gMMnqTr5RzcfldcyFWIvVzn6p9F3DlMLKsg4%2F6Q2G8qauX3EOk7B2yKumzPW4DpFhXDBEXZsCAQ7Q%2FieWIxqrIVhynrbF6%2Fs%3D&__VIEWSTATEGENERATOR=90059987&uploadGrd%24DXFREditorcol1=&uploadGrd%24DXFREditorcol2=&uploadGrd%24DXFREditorcol3=&uploadGrd%24DXFREditorcol4=&uploadGrd%24DXFREditorcol5=&uploadGrd%24DXFREditorcol6=&uploadGrd%24DXFREditorcol7=&uploadGrd%24DXFREditorcol8=&uploadGrd%24DXFREditorcol9=&uploadGrd%24DXFREditorcol10=&uploadGrd%24DXSelInput=&uploadGrd%24DXKVInput=%5B%5D&uploadGrd%24CallbackState=BwQHAgIERGF0YQbyBAAAAAClBQAApQUAAAoAAAAKAAAAAAoAAAAFR3JpZHMFR3JpZHMHAAALU3dpdGNoX05hbWULU3dpdGNoX05hbWUHAAAGR3JvdXBzBkdyb3VwcwcAAAhDYXRlZ29yeQhDYXRlZ29yeQcAAAtGaXJzdF9DeWNsZQtGaXJzdF9DeWNsZQcAAAxTZWNvbmRfQ3ljbGUMU2Vjb25kX0N5Y2xlBwAAC1RoaXJkX0N5Y2xlC1RoaXJkX0N5Y2xlBwAAC0ZvcnRoX0N5Y2xlC0ZvcnRoX0N5Y2xlBwAAC0ZpZnRoX0N5Y2xlC0ZpZnRoX0N5Y2xlBwAAC1NpeHRoX0N5Y2xlC1NpeHRoX0N5Y2xlBwAAAQAAAAJJRAcABwAHAAcABv%2F%2FBwIJQUdIQSBLSEFOBwINU0hBTUlNIEFITUVEIAcCATQHAglOb3JtYWwtTEwHAgkxMzM1fjE1MDUHAgkwMzA1fjA1MDUHAgEtBwIBLQcCAS0HAgEtBwAHAAb%2F%2FwcCCUFHSEEgS0hBTgcCC1NVTk5ZIFZPSFJBBwIBMQcCCU5vcm1hbC1MTAcCCTA5MDV%2BMTAzNQcCCTAxMDV%2BMDMwNQcCAS0HAgEtBwIBLQcCAS0HAAcABv%2F%2FBwIHQUlSUE9SVAcCGFNVUEVSSU9SIFNJQ0VOQ0UgQ09MTEVHRQcCATIHAgZDT04tTEwHAgkxMDM1fjEyMDUHAgkxNzA1fjE4MzUHAgkwMTA1fjAyMDUHAgkwMzA1fjA0MDUHAgEtBwIBLQcABwAG%2F%2F8HAgdBSVJQT1JUBwILVEFOR0EgU1RBTkQHAgExBwIGQ09OLUxMBwIJMDkwNX4xMDM1BwIJMTYwNX4xNzM1BwIJMDEwNX4wMjA1BwIJMDMwNX4wNDA1BwIBLQcCAS0HAAcABv%2F%2FBwIHQUlSUE9SVAcCFVNJRERJUUlBIE1BU0pJRCBSTVUgKwcCATMHAgZDT04tTEwHAgkxMjA1fjEzMzUHAgkxNzM1fjE5MDUHAgkwMTA1fjAyMDUHAgkwMzA1fjA0MDUHAgEtBwIBLQcABwAG%2F%2F8HAgdBSVJQT1JUBwIPU0hBTUEgQ0VOVFJFICArBwIBMgcCCU5vcm1hbC1MTAcCCTEwMzV%2BMTIwNQcCCTAxMDV%2BMDMwNQcCAS0HAgEtBwIBLQcCAS0HAAcABv%2F%2FBwIHQUlSUE9SVAcCF1NIT1VLQVQgVU1BUiBIT1NQSVRBTCArBwIBOQcCBkNPTi1MTAcCCTEzMDV%2BMTQzNQcCCTE3MzV%2BMTkwNQcCCTAwMDV%2BMDEwNQcCCTA1MDV%2BMDYwNQcCAS0HAgEtBwAHAAb%2F%2FwcCB0FJUlBPUlQHAg1TQU5HQU0gQ0lORU1BBwIBNgcCBkNPTi1MTAcCCTE1MzV%2BMTcwNQcCCTIwMzV%2BMjIwNQcCCTAwMDV%2BMDEwNQcCCTAyMDV%2BMDMwNQcCAS0HAgEtBwAHAAb%2F%2FwcCB0FJUlBPUlQHAgVRRUMgKwcCATYHAglOb3JtYWwtTEwHAgkxNjM1fjE4MDUHAgkwMzA1fjA1MDUHAgEtBwIBLQcCAS0HAgEtBwAHAAb%2F%2FwcCB0FJUlBPUlQHAgtSRVRBIFBMT1QgKwcCAjNjBwICSEwHAgkwODA1fjEwMzUHAgkxMzA1fjE2MDUHAgkxODM1fjIxMDUHAgkyMzA1fjAxMDUHAgEtBwIBLQIFU3RhdGUHXQcLBwACAQcBAgEHAgIBBwMCAQcEAgEHBQIBBwYCAQcHAgEHCAIBBwkCAQcKAgEHAAcABwAHAAIABQAAAIAJAgAHAAkCAAIAAwcEAgAHAAIBBqUFBwACAQcABwAHAAINU2hvd0ZpbHRlclJvdwoCAQIJUGFnZUluZGV4AwcB&DXScript=1_171%2C1_94%2C1_164%2C1_104%2C1_138%2C1_114%2C1_121%2C1_152&DXCss=0_108%2C0_260%2C1_12%2C0_110%2C0_264%2C0_100%2C1_5%2C0_102&__CALLBACKID=uploadGrd&__CALLBACKPARAM=c0%3AKV%7C2%3B%5B%5D%3BGB%7C20%3B12%7CPAGERONCLICK3%7CPN5%3B&__EVENTVALIDATION=ryBIH%2BGqwwiR5H8miIbcIgtdiuImx9XcWZfIJv9GMVoWfbDYJQqUYG3PsHfekIA3Gu0cfKl0CeG4EFsT5sM6CzYEUmaIa71F%2BFZ57nFxtDygvTTzYUnneLSjy6V1mESF"

        self.dict=self.split_payload_to_dict()
    

    def getPayload(self):
        return self.payload

    def getdict(self):
        return self.dict

    def split_payload_to_dict(self) -> dict:
        split = self.payload.split('&')
        split = [i.split("=") for i in split]
        d = dict()
        for key, value in split:
            if key == '__VIEWSTATE' or unquote(key) == 'uploadGrd$CallbackState':
                k = unquote(key)
                v = value
            else:
                k = unquote(key)
                v = unquote(value)
            d[k] = v

        self.dict=d
        return d


    def add_options_to_payload(self, options:dict):
        for k, v in options.items():
            self.dict[k] = v
        self.dict_to_payload()


    def dict_to_payload(self) -> None:
        t = []
        for key, value in self.dict.items():
            if key == '__VIEWSTATE' or key == 'uploadGrd$CallbackState':
                k = quote(key)
                v = value
            else:
                k = quote(key)
                v = quote(value)

            st = k+'='+v
            t.append(st)

        split = '&'.join(t)
        self.payload=split


headers = {
    'Accept': '*/*',
    'Accept-Language': 'en-US,en;q=0.9',
    'Cache-Control': 'no-cache',
    'Connection': 'keep-alive',
    'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
    'DNT': '1',
    'Origin': 'https://staging.ke.com.pk:8490',
    'Pragma': 'no-cache',
    'Referer': 'https://staging.ke.com.pk:8490/index.aspx',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'same-origin',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36',
    'sec-ch-ua': '"Chromium";v="104", " Not A;Brand";v="99", "Google Chrome";v="104"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-gpc': '1'
}
