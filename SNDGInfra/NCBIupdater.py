'''
Created on Nov 1, 2017

@author: eze
'''
import os
import logging

from SNDGInfra import dl, execute, md5_equal

_log = logging.getLogger()

class NCBIupdater(object):
    '''
    classdocs
    '''


    def download(self,config,datadir):
        
        if not os.path.exists(datadir  + "ncbi/"):
            os.makedirs(datadir  + "ncbi/")
                
        os.chdir(datadir  + "ncbi/")
        dl("ftp://ftp.ncbi.nlm.nih.gov/pub/taxonomy/taxdump.tar.gz")
        dl("ftp://ftp.ncbi.nlm.nih.gov/pub/taxonomy/taxdump.tar.gz.md5")   
             
        md5file = open("taxdump.tar.gz.md5").read().split(" ")[0]     
        if md5_equal("taxdump.tar.gz", md5file):
            execute("tar xfv taxdump.tar.gz")
        
            
        dl("ftp://ftp.ncbi.nlm.nih.gov/blast/db/FASTA/nt.gz")
        dl("ftp://ftp.ncbi.nlm.nih.gov/blast/db/FASTA/nt.gz.md5")
        
        md5file = open("nt.gz.md5").read().split(" ")[0]        
        if md5_equal("nt.gz", md5file):
            execute("gunzip nt.gz")
        
        
        dl("ftp://ftp.ncbi.nlm.nih.gov/pub/taxonomy/accession2taxid/nucl_gb.accession2taxid.gz")
        dl("ftp://ftp.ncbi.nlm.nih.gov/pub/taxonomy/accession2taxid/nucl_gb.accession2taxid.gz.md5")
        
        md5file = open("nucl_gb.accession2taxid.gz.md5").read().split(" ")[0]       
        if md5_equal("nucl_gb.accession2taxid.gz",md5file):
            execute("gunzip nucl_gb.accession2taxid.gz")
        
        
        
        
        