    
def today1():
    import datetime as dt
    today=dt.datetime.now()
    hours=today.hour
    y1=today.year
    M1=today.month
    d1=today.day
    s1=str(y1)+" "+str(M1)+" "+str(d1)
    
    print(s1)

today1()
  