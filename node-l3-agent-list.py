#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import sys
import keystoneclient.v2_0.client as ksclient
from neutronclient.v2_0 import client



def get_keystone_creds():
    try:
        d = {}
        d['version'] = "2.0"
        d['username'] = os.environ['OS_USERNAME']
        d['password'] = os.environ['OS_PASSWORD']
        d['auth_url'] = os.environ['OS_AUTH_URL']
        d['tenant_name'] = os.environ['OS_TENANT_NAME']
    except KeyError:
	print "Credentials error. Run source user-operc.sh"
	sys.exit(1)
    return d

def get_active_node(uuid):
    agents = neutron.list_l3_agent_hosting_routers(uuid)
    val_agents = agents['agents']
    for agent in val_agents:
	if agent['ha_state'] == 'active':
	    return agent['host']

    return None

creds = get_keystone_creds()
neutron = client.Client(**creds)
routers_list = neutron.list_routers(retrieve_all=True)

def main(argv):
    try:
	val_list = routers_list['routers']
	for p in val_list:
            host = get_active_node(p['id'])

	    print ("{0} - {1}".format(p['name'], host)) 

	    
    except:
        print("Sorry exception!")

if __name__ == "__main__":
    main(sys.argv)
