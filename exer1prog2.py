import string


def find_between(star,end):
    total=""
    first=True
    for x in range(star,end):
        if((x%7==0) and (not(x%5==0))):
            if(first):
                total=str(x)
                first=False
            total=total+","+str(x)
    print(total)

star = int(input("first num:"))
end = int(input("second num:"))
if(star>end):
    print("changing start to end and end to start")
    temp=star
    star=end
    end=temp
    del temp
find_between(star,end)