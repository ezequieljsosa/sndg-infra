'''
Created on Nov 1, 2017

@author: eze
'''
import os
import pandas as pd
import shutil

from SNDGInfra import dl

#from urllib.request import ProxyHandler,build_opener,install_opener
# proxy_support = ProxyHandler({"http":"http://proxy.fcen.uba.ar:8080/",
#                               "ftp":"http://proxy.fcen.uba.ar:8080/"})
# opener = build_opener(proxy_support)
# install_opener(opener)
# pdbl = PDBList(pdb="/data/databases/pdb/divided/",obsolete_pdb="/data/databases/pdb/obsolete/")
# pdbl.update_pdb(file_format="pdb")

class PDBupdater(object):
    '''    
    '''

    def download(self,config,datadir):
        pdbdir = datadir + "pdb/"
        pdbftp = "ftp://ftp.wwpdb.org/pub/pdb/data/structures"
        
        os.chdir(pdbdir)
        
        dl("ftp://ftp.wwpdb.org/pub/pdb/derived_data/index/entries.idx")
        pdbs = pd.read_table("entries.idx",skiprows=2,
                             names=["IDCODE", "HEADER", "ACCESSION DATE", "COMPOUND", 
                                    "SOURCE", "AUTHOR LIST", "RESOLUTION", "EXPERIMENT TYPE"])
        for pdb in pdbs.IDCODE:
            groupdir = pdbdir + "divided/" + pdb[1:3].lower()
            if not os.path.exists(groupdir):
                os.makedirs(groupdir) 
            if not os.path.exists(groupdir+  "/pdb" + pdb.lower() + ".ent" ):
                os.chdir(groupdir)
                dl( pdbftp + "/divided/pdb/" + pdb[1:3].lower()  + "/pdb" + pdb.lower() + ".ent.gz")
        dl("ftp://ftp.wwpdb.org/pub/pdb/data/status/obsolete.dat")
        obsolete = pd.read_table("entries.idx",skiprows=1,
                             names=["OBSLTE", "DATE", "OBS", "SUCCESSOR"])
        for pdb in obsolete.OBS:
            groupdir = pdbdir + "divided/" + pdb[1:3].lower() 
            if os.path.exists(groupdir+  "/pdb" + pdb.lower() + ".ent" ):            
                shutil.move( groupdir+  "/pdb" + pdb.lower() + ".ent" , pdbdir + "obsoletes/")
        