
class FormOptions:
    def __init__(self) -> None:
        self.options= {
    '__CALLBACKPARAM': "c0:KV|2;[];GB|20;12|PAGERONCLICK3|PN0;"
    # 'uploadGrd$CallbackState': '',
    # '__VIEWSTATE': '',
    # '__VIEWSTATEGENERATOR': '',
    # '__EVENTVALIDATION': '',
    # 'DXCss': ''
        }

        self.rangeStart=20
        self.page=0
        self.PAGERONCLICK=3

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
        return options
        


    def moveCursortoNextPage(self)->dict:
        self.page+=1
        return self.__ConstructFormParameter()

    def moveBlock(self)->dict:
        self.rangeStart+=1
        self.PAGERONCLICK+=1
        return self.__ConstructFormParameter()



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
