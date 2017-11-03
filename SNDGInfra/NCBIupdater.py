'''
Created on Nov 1, 2017

@author: eze
'''
import os

from SNDGInfra import dl, execute, md5


class NCBIupdater(object):
    '''
    classdocs
    '''


    def download(self,config,datadir):        
        os.chdir(datadir  + "ncbi/")
        dl("ftp://ftp.ncbi.nlm.nih.gov/pub/taxonomy/taxdump.tar.gz")
        dl("ftp://ftp.ncbi.nlm.nih.gov/pub/taxonomy/taxdump.tar.gz.md5")   
             
        md5file = open("taxdump.tar.gz.md5").read()        
        if md5("tardump.tar.gz") == md5file:
            execute("tar xfv taxdump.tar.gz")
            
        dl("ftp://ftp.ncbi.nlm.nih.gov/blast/db/FASTA/nt.gz")
        dl("ftp://ftp.ncbi.nlm.nih.gov/blast/db/FASTA/nt.gz.md5")
        
        md5file = open("nt.gz.md5").read()        
        if md5("nt.gz") == md5file:
            execute("gunzip nt.gz")
        
        
        dl("ftp://ftp.ncbi.nlm.nih.gov/pub/taxonomy/accession2taxid/nucl_gb.accession2taxid.gz")
        dl("ftp://ftp.ncbi.nlm.nih.gov/pub/taxonomy/accession2taxid/nucl_gb.accession2taxid.gz.md5")
        
        md5file = open("nucl_gb.accession2taxid.gz.md5").read()        
        if md5("nucl_gb.accession2taxid.gz") == md5file:
            execute("gunzip nucl_gb.accession2taxid.gz")
        
        
        
        
        