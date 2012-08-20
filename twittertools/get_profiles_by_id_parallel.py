import gevent
from gevent import monkey
monkey.patch_all()
from gevent.pool import Pool

import json

pool = Pool(30)

import sys
import codecs
#import cPickle as pickle

from twitter_common import *

auth_file = sys.argv[1]
api_tools = TwitterTools()
api_tools.get_api(auth_file)
api_tools.get_access()

input = codecs.getreader("utf-8")(sys.stdin)
output = codecs.getwriter("utf-8")(sys.stdout)

def get_profiles(users):
    response = None
    for i in range(3):
        try:
            response = [jsonize_user(user) for user in api_tools.api.lookup_users(user_ids=users)]
            break
        except:
            time.sleep(0.5)
            sys.stderr.write("x")
            pass
    if response:
        output.write("\n".join(response) + "\n")
        sys.stderr.write(".")

print >> sys.stderr, "INFO", \
      "Starting to fetch profiles."
        
user_ids = list()
tmp = list()
for ct,line in enumerate(input):
    line = line.rstrip()
    if line == "":
        continue

    user_id = line
    tmp.append(user_id)
    if len(tmp) == 100:
        user_ids.append(tmp)
        pool.spawn(get_profiles, tmp)
        tmp = list()
if tmp:
    pool.spawn(get_profiles, tmp)
    #user_ids.append(tmp)



    


