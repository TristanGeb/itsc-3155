import string



class item:
    #name='none'
    #amount=0
    def __init__(self,newname,newamount):
        #print(" giveing:"+newname+","+newamount)
        self.name=newname
        self.amount=newamount
        #print(" got:"+self.name+","+self.amount)
    def get_name(self):
        return self.name
    def get_amount(self):
        return self.amount
    def __str__(self):
        return self.name+","+self.amount
    #def tostr(self):


def printlist(list,startingstr):
    #print(" list len:",len(list))
    stri=startingstr
    for x in list:
        print(x)
        stri=stri+x.__str__()
    #print(stri)

def add(list,item):
    list_len=len(list)
    #print("imputing:",item)

    #printlist(list," begin:")

    if(list_len==0):
        #print("   list is empty, added at beg")
        list.append(item)
    else:
        i=0
        endflag=False
        while(i<list_len and not(endflag)):
            # is less then insert
            am=item.get_amount()
            li=list[i].get_amount()
            if(am<li):
                #print("   adding at :"+i)
                list.insert(i,item)
                endflag=True
            i=i+1
                
   # printlist(list," end:")
    #print("list:"+str(list))
    #print(item.tostr())



valid=False
while(not valid):
    amount_of_items=int(input("amount of items:"))

    if(True):
        valid=True
    else:
        print("input a number")
list=[]

for x in range(0,amount_of_items):
    str=input("input item and price: ")
    while(str[0]==' '):
        str=str[1:len(str)]
    newname=str[0:str.find(' ')]
    newamount=str[str.find(' '):len(str)]

    newitem=item(newname,newamount)

    #print(newitem.get_name()+","+newitem.get_amount())
    add(list,newitem)
printlist(list,"list:")