import sys

from twitter_common import *

api_tools = TwitterTools()
api_tools.get_api()

queue = list()
ct = 0
for line in sys.stdin:
    while True:
        if len(queue) == 99:        
            api_tools.get_access(api)
            response = [jsonize_user(user) for user in api_tools.api.lookup_users(screen_names=queue)]
            queue = list()
            print "\n".join(response)
            sys.stderr.write('%d ' % ct)
        queue.append(line.strip())
        ct += 1
        break
            
api_tools.get_access()
response = [jsonize_user(user) for user in api_tools.api.lookup_users(screen_names=queue)]
print "\n".join(response)
    
    
        
    
        
        
