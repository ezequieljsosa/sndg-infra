'''
Created on Nov 1, 2017

@author: eze
'''
import os
import logging

from SNDGInfra import dl, execute

_log = logging.getLogger()

class UNIPROTupdater(object):
    '''
    classdocs
    '''


    def download(self,config,datadir):        
        os.chdir(datadir  + "uniprot/")
        dl("ftp://ftp.uniprot.org/pub/databases/uniprot/current_release/knowledgebase/complete/uniprot_sprot.xml.gz")
        dl("ftp://ftp.uniprot.org/pub/databases/uniprot/uniref/uniref50/uniref50.fasta.gz")
        dl("ftp://ftp.uniprot.org/pub/databases/uniprot/uniref/uniref90/uniref90.fasta.gz")
        dl("ftp://ftp.uniprot.org/pub/databases/uniprot/current_release/knowledgebase/idmapping/idmapping.dat.gz")
        execute("gunzip *")
        for x in os.listdir("./"):
            if x.endswith(".gz"):
                _log.error(x + " was not downloaded correctly")
        
        