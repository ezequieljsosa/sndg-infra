'''
Created on Nov 1, 2017

@author: eze
'''
import os
import requests
import datetime
import email.utils as eut

from SNDGInfra import dl

class SOupdater(object):
    '''
    
    '''


    def download(self,config,datadir):
        sodir = datadir + "so/"    
        if not os.path.exists(sodir):
            os.makedirs(sodir)
        
        if not os.path.exists(sodir):
            os.makedirs(sodir)
        r = requests.get('https://raw.githubusercontent.com/The-Sequence-Ontology/SO-Ontologies/master/releases/so-xp.owl/so-xp.obo')
        length = int(r.headers['Content-Length'])
        r.close()
        
        if (not config["so"]) or (length != config["so"]) :
            os.chdir(sodir)
            dl("https://raw.githubusercontent.com/The-Sequence-Ontology/SO-Ontologies/master/releases/so-xp.owl/so-xp.obo")
            config["so"] = length
        