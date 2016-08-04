import datetime
from datetime import timedelta
from urllib import urlopen
import json

nw= datetime.datetime.now()
nw1= nw+timedelta(hours=12.5)
print nw1
INV_AMT=0
CURR_AMT=0
def googleQuote(st):

    num=prc=0
    try:
        #url = '%s%s' % ('http://www.google.com/finance/info?q=', ticker)
        url1= '%s' % ('http://finance.google.com/finance/info?client=ig&q='+st)
        doc = urlopen(url1)
        content = doc.read()
        quote = json.loads(content[3:])
    except:
        print "---xxx----"
        return

    if st=="BOM:506260": st="BSE:ANUHpharma"

    print '%16s' % (st),
    q=quote[0][u'l'].replace(",","")
    print '%10s'% ("_"+( str(float(q)))+"_"),
    try: print '%9s' %(str(float(quote[0][u'cp']))+"%"),
    except: print '%9s' %(str((quote[0][u'cp']))+"%"),
    try: print '%9s' %(" ("+str(float(quote[0][u'c']))+")"),
    except:print '%9s' %(" ("+str((quote[0][u'c']))+")"),

    diff= nw1-datetime.datetime.strptime(quote[0][u'lt_dts'].replace("T"," ").replace("Z","")+".000000", "%Y-%m-%d %H:%M:%S.%f")
    if "day" in str(diff): print '%22s' % "More than 1day ago",
    else:
        part= str(diff).split(":")
        sec= int(part[0])*3600+int(part[1])*60+float(part[2])
        if int(sec/60)<600:
            print '%12s' % ((str(int(sec/60))+"m")+str(int(sec- 60*(int(sec/60))))+"s ago"),
        else: print '%12s' % "Long ago",

    """##########################################################################"""
    if "DHANUKA" in st:
        num= 50
        prc= 563.56
    if "SANGHI" in st:
        num= 600
        prc= 50.62
    if "ANUH" in st:
        num= 54
        prc= 200.70
    if "KOKUYO" in st:
        num= 220
        prc= 72.42
    if "GODREJ" in st:
        num= 25
        prc= 258.36

    """##########################################################################"""

    snum= str(num)
    sprc= str(prc)
    print '%5s' % (snum),
    print '%10s'%("@ "+sprc),
    print '%9s' % str(int(num*prc)),
    print '%7s' % (str(int(num*(float(q) - prc)))),
    print "[gn "+str(float(int((10000*(float(q) - prc))/prc))/100)+"%]",
    print ""
    global INV_AMT,CURR_AMT
    INV_AMT= INV_AMT+(prc*num)
    CURR_AMT= CURR_AMT+(num*float(q))


if __name__ == "__main__":
    scriplist= ['NSE:DHANUKA','NSE:SANGHIIND','NSE:KOKUYOCMLN','NSE:GODREJPROPsold','BOM:506260']
    for st in scriplist:
        if 'sold' not in st: googleQuote(st)
    print "       ==>>",INV_AMT,"    ",CURR_AMT,"    ",CURR_AMT - INV_AMT,"   ~",float(int((CURR_AMT-INV_AMT)*10000/INV_AMT))/100,"%",
