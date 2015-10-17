from datetime import *
print date
wcount=int(raw_input("how many words do you want to learn? "))
wdate=raw_input("Please enter the due date in yyyy.mm.dd format. ")
year,month,day=map(int,wdate.split("-"))
wdate2=date(year,month,day)
print wdate2

def gunlukkelime(wcount):
    totaldays=wdate2-datetime
    print totaldays
gunlukkelime(wcount)