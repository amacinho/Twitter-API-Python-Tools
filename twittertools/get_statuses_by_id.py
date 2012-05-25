# -*- coding: utf-8 -*-
# Copyright 2012 Amaç Herdağdelen
# This file is part of Twitter API Python Tools
# (https://github.com/amacinho/Twitter-API-Python-Tools)

import sys
import json
import time

from twitter_common import *
        
api_tools = TwitterTools()
api_tools.get_api()

ct = 0
for line in sys.stdin:
    ct += 1
    user_id = line.strip()
    
    sys.stderr.write("%d. Getting statuses of %s" % (ct,user_id))
    
    statuses = api_tools.get_all_statuses_by_id(user_id, page=20, rpp=20)
    
    sys.stderr.write(" Done: fetched %d statuses\n" % (len(statuses)))

    print "\n".join(statuses)
    sys.stderr.write('%d %d (%s)\n' % (ct,len(statuses),user_id))
    
