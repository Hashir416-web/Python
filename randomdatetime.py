import random
import time
def getrandomdate(startdate, enddate):
    print("printing random dater between two dates",startdate,"and", enddate)
    randomgenerator=random.random()
    dateformat="%Y-%m-%d"
    starttime=time.mktime(time.strptime(startdate, dateformat))
    endtime=time.mktime(time.strptime(enddate, dateformat))
    randomtime=starttime+randomgenerator*(endtime-starttime)
    randomdate=time.strftime(dateformat,time.localtime(randomtime))
    return randomdate
print("Random date is",getrandomdate("2022-01-01","2025-12-31"))