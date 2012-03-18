# -*- coding: utf-8 -*-
# Copyright 2012 Amaç Herdağdelen
# This file is part of Twitter API Python Tools
# (https://github.com/amacinho/Twitter-API-Python-Tools)

import sys
import tweepy
import time

from twitter_common import *

api_tools = TwitterTools()
api_tools.get_api()
api_tools.get_access()

for ct,user_id in enumerate(sys.stdin):
    user_id = user_id.strip()
    sys.stderr.write("%d. Getting friends of %s" % (ct,user_id))
    
    friends_ids = api_tools.get_all_friends_by_id(user_id)
    
    sys.stderr.write(" Done: fetched %d friends\n" % (len(friends_ids)))
    print "\n".join(["%s\t%s" % (user_id,str(id)) for id in friends_ids])



