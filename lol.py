#Pull some ranked data for a specific summoner via riot api

import json # imports json libraries
import requests #imports requests libraries
from sys import argv

script, summoner_name_case = argv

summoner_name = summoner_name_case.lower()

api_key = "api_key=RGAPI-e11bfdbe-75e7-4a05-961e-6c1d441fbfdd"

def summoner_lookup(summoner_name):
    r = requests.get('https://na.api.pvp.net/api/lol/na/v1.4/summoner/by-name/' + summoner_name, params=api_key)
    results = r.json()
    sid = results[summoner_name]['id']
    return str(sid)

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
    return (sq, sqt, sqd, fq, fqt, fqd)


print "Looking up information for summoner : %s" % summoner_name
print "\n"

sq, sqt, sqd, fq, fqt, fqd = summoner_rank()

print "This shitter is %s %s in %s" % (sqt, sqd, sq)
print "This shitter is %s %s in %s" % (fqt, fqd, fq)
