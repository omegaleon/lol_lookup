#pull stats via riot api

import json # imports json libraries
import requests #imports requests libraries
from sys import argv

script, summoner_name_case = argv

summoner_name = summoner_name_case.lower()


api_key = "api_key=RGAPI-e11bfdbe-75e7-4a05-961e-6c1d441fbfdd"

def walkdict(d):
    stack = d.items()
    while stack:
        k, v = stack.pop()
        if isinstance(v, dict):
            stack.extend(v.iteritems())
        else:
            print("%s: %s" % (k, v))


def summoner_lookup(summoner_name):
    r = requests.get('https://na.api.pvp.net/api/lol/na/v1.4/summoner/by-name/' + summoner_name, params=api_key)
    results = r.json()
    sid = results[summoner_name]['id']
    return str(sid)


#def print_goodies():
    #print "This shitter is %s %s in %s" % (sqt, sqd, sq)
    #print "This shitter is %s %s in %s" % (fqt, fqd, fq)


def summoner_rank():
    summoner_id = summoner_lookup(summoner_name)
    r = requests.get('https://na.api.pvp.net/api/lol/na/v2.5/league/by-summoner/' + summoner_id + '/entry', params=api_key)
    results = r.json()
    aresults = results[summoner_id][0]['entries'][0]
    sq = results[summoner_id][0]['queue']
    sqt = results[summoner_id][0]['tier']
    sqd = results[summoner_id][0]['entries'][0]['division']
    fq = results[summoner_id][1]['queue']
    fqt = results[summoner_id][1]['tier']
    fqd = results[summoner_id][1]['entries'][0]['division']
    #print "This shitter is %s %s in %s" % (sqt, sqd, sq)
    #print "This shitter is %s %s in %s" % (fqt, fqd, fq)
    return (sq, sqt, sqd, fq, fqt, fqd, results)

def print_func():
    print(summoner_rank())

print "Looking up information for summoner : %s" % summoner_name

print "\n"
#print_goodies()

print_func()

print "This shitter is %s %s in %s" % (sqt, sqd, sq)
print "This shitter is %s %s in %s" % (fqt, fqd, fq)

#walkdict(results)
