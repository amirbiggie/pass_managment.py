import datetime
import random


class id:
    def __init__(self) -> None:
       self.alphabet = ["b","c","d","i","f","g","h","r","j","a","e"]
       self.nums = range(0,10)
       self.now = datetime.datetime.now()
       self.uniq_part = str(self.now.year*random.randint(1,1000))+str(self.now.microsecond)+str(self.now.day)+str(self.now.month)


    def ganereate_id(self):
        
        id = random.choice(self.alphabet)+str(random.choice(self.nums))+str(random.choice(self.nums))+str(random.choice(self.nums))+self.uniq_part
        return id   