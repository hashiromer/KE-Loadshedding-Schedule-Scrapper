from dataUtils import  get_load_shedding_schedule, save_to_disk


class Main:
    def __init__(self, isTest=False):
        self.test=isTest

    def run(self):
        if self.test==True:
            with open("datadump.txt") as f:
                response = f.read()
        else:
            data=get_load_shedding_schedule()
            print("Total Feeders: ", len(data))
            save_to_disk(data)
