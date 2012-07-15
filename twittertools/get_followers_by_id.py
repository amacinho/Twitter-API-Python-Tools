# -*- coding: utf-8 -*-
# Copyright 2012 Amaç Herdağdelen
# This file is part of Twitter API Python Tools
# (https://github.com/amacinho/Twitter-API-Python-Tools)

import sys
import tweepy
import time

from twitter_common import *

auth_file = sys.argv[1]

api_tools = TwitterTools()
api_tools.get_api(auth_file)
api_tools.get_access()
for ct,user_id in enumerate(sys.stdin):
    user_id = user_id.strip()
    sys.stderr.write("%d. Getting followers of %s" % (ct,user_id))
    
    follower_ids = api_tools.get_all_followers_by_id(user_id)
    
    if follower_ids != None:
        sys.stderr.write(" Done: fetched %d followers\n" % (len(follower_ids)))
        print "\n".join(["%s\t%s" % (user_id,str(id)) for id in follower_ids])
    else:
        sys.stderr.write(" Problem for %s: fetched no followers\n" % (user_id))
        


