from context import pyrealb
from pyrealb import *
from tests.test import test

from datetime import datetime,timedelta

def dates_fr():
    loadFr()
    theDate="2015-01-01T11:25:45"
    date=datetime.strptime(theDate,"%Y-%m-%dT%H:%M:%S")
    exp=DT(theDate)
    return [    # natural date
            {},
        {"expression":exp,
         "expected":"le jeudi 1 janvier 2015 à 11 h 25 min 45 s", 
         "message":"Full info"},
        {"expression":DT(theDate).dOpt({"day":False, "date":True}),
         "expected":"le 1 janvier 2015 à 11 h 25 min 45 s", 
         "message":"Without week day"},
        {"expression":DT(theDate).dOpt({"day":False, "month":False, "year":False}),
         "expected":"le 1 à 11 h 25 min 45 s", 
         "message":"Without day, month and year"},
        {"expression":DT(theDate).dOpt({"year":False}),
         "expected":"le jeudi 1 janvier à 11 h 25 min 45 s", 
         "message":"Without year"},
        {"expression":DT(theDate).dOpt({"year":False, "month":False, "date":False, "day":False}),
         "expected":"à 11 h 25 min 45 s", 
         "message":"Only time"},
        {"expression":DT(theDate).dOpt({"year":False, "month":False, "date":False, "day":False, "minute":False, "second":False}),
         "expected":"à 11 h", 
         "message":"Only hour"},
        {"expression":DT(theDate).dOpt({"year":False, "month":False, "date":False, "day":False, "second":False}),
         "expected":"à 11 h 25", 
         "message":"Only hour and minute"},
        {"expression":DT(theDate).dOpt({"month":False, "date":False, "day":False, "hour":False, "minute":False, "second":False}),
         "expected":"en 2015", 
         "message":"Only year"},
        {"expression":DT(theDate).dOpt({"date":False, "day":False, "hour":False, "minute":False, "second":False}),
         "expected":"en janvier 2015", 
         "message":"Only month and year"},
        {"expression":DT(theDate).dOpt({"year":False, "month":False, "date":False, "hour":False, "minute":False, "second":False}),
         "expected":"le jeudi", 
         "message":"Only weekday"},
        {"expression":DT("2015-01-04T11:00:00").dOpt({"minute":False,"second":False}),
         "expected":"le dimanche 4 janvier 2015 à 11 h", 
         "message":"Full info without 0 minutes and 0 seconds"},
        # date in digit
        {"expression":DT(theDate).nat(False),
         "expected":"jeudi 1/1/2015 11:25:45", 
         "message":"Full info"},
        {"expression":DT(theDate).dOpt({"day":False, "date":True}).nat(False),
         "expected":"1/1/2015 11:25:45", 
         "message":"Without week day"},
        {"expression":DT(theDate).dOpt({"day":False, "month":False, "year":False}).nat(False),
         "expected":"1 11:25:45", 
         "message":"Without day, month and year"},
        {"expression":DT(theDate).dOpt({"year":False}).nat(False),
         "expected":"jeudi 1/1 11:25:45", 
         "message":"Without year"},
        {"expression":DT(theDate).dOpt({"year":False, "month":False, "date":False, "day":False}).nat(False),
         "expected":"11:25:45", 
         "message":"Only time"},
        {"expression":DT(theDate).dOpt({"year":False, "month":False, "date":False, "day":False, "minute":False, "second":False}).nat(False),
         "expected":"11", 
         "message":"Only hour"},
        {"expression":DT(theDate).dOpt({"year":False, "month":False, "date":False, "day":False, "second":False}).nat(False),
         "expected":"11:25", 
         "message":"Only hour and minute"},
        {"expression":DT(theDate).dOpt({"month":False, "date":False, "day":False, "hour":False, "minute":False, "second":False}).nat(False),
         "expected":"2015", 
         "message":"Only year"},
        {"expression":DT(theDate).dOpt({"date":False, "day":False, "hour":False, "minute":False, "second":False}).nat(False),
         "expected":"1/2015", 
         "message":"Only month and year"},
        {"expression":DT(theDate).dOpt({"year":False, "month":False, "day":False, "hour":False, "minute":False, "second":False}).nat(False),
         "expected":"1", 
         "message":"Only date"},
        #relative time to Thursday January 1st 2015
        {"expression":DT(date-timedelta(days=1)).dOpt({"rtime":date}),
         "expected":"hier",
         "message":"one day before"},
        {"expression":DT(date-timedelta(days=2)).dOpt({"rtime":date}),
         "expected":"avant-hier",
         "message":"two days before"},
        {"expression":DT(date-timedelta(days=10)).dOpt({"rtime":date}),
         "expected":"il y a 10 jours",
         "message":"since 10 days"},
        {"expression":DT(date).dOpt({"rtime":date}),
         "expected":"aujourd'hui",
         "message":"same day"},
        {"expression":DT(date+timedelta(days=1)).dOpt({"rtime":date}),
         "expected":"demain",
         "message":"one day after"},
        {"expression":DT(date+timedelta(days=4)).dOpt({"rtime":date}),
         "expected":"lundi prochain",
         "message":"four days after"},
        {"expression":DT(date+timedelta(days=10)).dOpt({"rtime":date}),
         "expected":"dans 10 jours",
         "message":"in 10 days"},
    ]

if __name__ == '__main__':
    test("Dates en français","fr",dates_fr)
