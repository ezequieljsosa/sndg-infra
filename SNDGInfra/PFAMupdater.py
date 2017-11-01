'''
Created on Nov 1, 2017

@author: eze
'''

import os
import shutil
import subprocess as sp
import logging

from SNDGInfra import dl, md5


_log = logging.getLogger()

class PFAMupdater(object):
    '''    
    '''


    def download(self,config,datadir):
        pfam_dir = datadir + "xfam" 
        if os.path.exists(pfam_dir):
            os.chdir(pfam_dir)
            if os.path.exists("Pfam-A.hmm"):
                shutil.move("Pfam-A.hmm","Pfam-A.hmm.bk" )
            dl("ftp://ftp.ebi.ac.uk/pub/databases/Pfam/current_release/relnotes.txt")
            with open("relnotes.txt") as h:
                release = float(h.readlines()[1].strip().split(" ") [1])
            if release > config["pfam"]:
                dl("wget ftp://ftp.ebi.ac.uk/pub/databases/Pfam/current_release/Pfam-A.hmm.gz")
                dl("wget ftp://ftp.ebi.ac.uk/pub/databases/Pfam/current_release/md5_checksums")
                with open("md5_checksums") as h:
                    md5s = {x[1]:x[0] for x in h.readlines()}
                    if md5("Pfam-A.hmm.gz") == md5s["Pfam-A.hmm.gz"]:
                        sp.call("gunzip Pfam-A.hmm.gz",shell=True)
                    else:
                        _log.error("md5 for Pfam does not match...")
        