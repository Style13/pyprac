totalraw=raw_input("total time? ")
hour, min=map(int,totalraw.split(":"))
totalmin=60*hour+min
def pomocount(totalmin):
    result=float(totalmin) / float(25.0)
    print "toplam dakika:",totalmin
    print "number of standart pomodori:",int(result)
pomocount(totalmin)
