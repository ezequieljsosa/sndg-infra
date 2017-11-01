'''
Created on Nov 1, 2017

@author: eze
'''
import os
import requests
import datetime
import email.utils as eut
from SNDGInfra import dl

class GOupdater(object):
    '''
    classdocs
    '''


    def download(self,config,datadir):
        godir = datadir + "go/"
    
        if not os.path.exists(godir):
            os.makedirs(godir)
        r = requests.get('http://geneontology.org/ontology/go.obo')
        lastchange = datetime.datetime(*eut.parsedate(r.headers['last-modified'])[:6])
        r.close()
        
        if (not config["go"]) or (lastchange > datetime.datetime.strptime(config["go"], '%Y%m')):
            os.chdir(godir)
            dl("http://geneontology.org/ontology/go.obo")
            dl("http://geneontology.org/ontology/go-basic.obo")        
            dl("http://geneontology.org/ontology/subsets/goslim_generic.obo")
            dl("http://geneontology.org/ontology/subsets/goslim_plant.obo")
            dl("http://geneontology.org/ontology/subsets/goslim_virus.obo")
            config["go"] = lastchange.strftime("%Y%m")
        