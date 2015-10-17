
hours=int(raw_input("how many hours of lectures do you have this week? "))
def as_study(hours):
    total1 = 0
    total2 = 0
    minutes = hours *60
    saat=minutes/60
    if raw_input("can you speed read? ")=="no":
        total2 = float(minutes * 2) + float(minutes * 2)*0.10
        saat=total2/60.0
        dakika=total2 % 60.0
        if dakika == 0:
            print "Bu hafta gereken: %d saat" %(saat)
        else:
            print "Bu hafta gereken: %d saat %02d dakika" %(saat,dakika)
    else:
        total1 = float(minutes * 2)
        saat=total1/60.0
        dakika=total1 % 60.0
        if dakika ==0:
            print "Bu hafta gereken: %d saat" %(saat)
        else:
            print "Bu hafta gereken: %d saat %02d dakika" %(saat,dakika)
as_study(hours)
