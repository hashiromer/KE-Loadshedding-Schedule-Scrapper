
from example_payload import PayloadProcessor


class FormOptions:
    def __init__(self) -> None:
        self.reset()
        self.payloadProcessor=PayloadProcessor()
        self.payloadProcessor.add_options_to_payload(self.options)
        


    def __ConstructFormParameter(self):
        self.options['__CALLBACKPARAM'] =\
        "c0:KV|2;[];GB|"+\
        str(self.rangeStart)+\
        ";12|PAGERONCLICK"+\
        str(self.PAGERONCLICK)+"|PN"+\
        str(self.page)+";"
        return self.options

    def MoveToPage(self,pageNumber)->dict:
        options={}
        options['__CALLBACKPARAM'] =\
        "c0:KV|2;[];GB|"+\
        str(self.rangeStart)+\
        ";12|PAGERONCLICK"+\
        str(self.PAGERONCLICK)+"|PN"+\
        str(pageNumber-1)+";"

        return self.getPayload(options)
        
    def reset(self)->None:
        self.rangeStart=20
        self.page=0
        self.PAGERONCLICK=3
        self.options= {
    '__CALLBACKPARAM':  "c0:KV|2;[];GB|20;12|PAGERONCLICK3|PN0;"
        }
        
       
        


    def moveCursortoNextPage(self)->dict:
        self.page+=1
        d= self.__ConstructFormParameter()
        return self.getPayload(d)


    def moveBlock(self)->dict:
        self.rangeStart+=1
        self.PAGERONCLICK+=1
        d= self.__ConstructFormParameter()
        return self.getPayload(d)

    def getPayload(self, partialOptions:dict={})->str:
        self.payloadProcessor.add_options_to_payload(partialOptions)
        return self.payloadProcessor.getPayload()




    def getFormOptions(self)->dict:
        return self.options
       


if __name__ == "__main__":
    formoptions = FormOptions()
    print(formoptions.__ConstructFormParameter())
    #Next page
    formoptions.moveCursortoNextPage()
    print(formoptions.__ConstructFormParameter())
    #Move to next block
    formoptions.moveBlock()
    print(formoptions.__ConstructFormParameter())




# First
# c0:KV|2;[];GB|{20|21|22};12|PAGERONCLICK{3|4|5}|PN{number}

# c0:KV|2;[];GB|20;12|PAGERONCLICK3|PN0;
# c0:KV|2;[];GB|20;12|PAGERONCLICK3|PN1;
# c0:KV|2;[];GB|20;12|PAGERONCLICK3|PN4;
# c0:KV|2;[];GB|21;12|PAGERONCLICK4|PN10;
# c0:KV|2;[];GB|21;12|PAGERONCLICK4|PN2;
# c0:KV|2;[];GB|21;12|PAGERONCLICK4|PN11;
# c0:KV|2;[];GB|21;12|PAGERONCLICK4|PN12;
