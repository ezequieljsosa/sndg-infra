'''
Created on Nov 1, 2017

@author: eze
'''
import os
import logging
import json
import shutil
from _collections import defaultdict

from SNDGInfra.GOupdater import GOupdater
from SNDGInfra.SOupdater import SOupdater
from SNDGInfra.PDBupdater import PDBupdater
from SNDGInfra.PFAMupdater import PFAMupdater
from SNDGInfra.NCBIupdater import NCBIupdater
from SNDGInfra.UNIPROTupdater import UNIPROTupdater
from SNDGInfra import init_log




_log = logging.getLogger()

if __name__ == '__main__':    
    
    datadir = "/data/databases/"
    init_log(datadir + "data.log")
    configpath = datadir + "config.json"
    
    with open(configpath) as h:
        config = defaultdict(lambda : None, json.load(h))
    
    for updater in [ GOupdater(), SOupdater(), PDBupdater(), 
                    PFAMupdater(),  UNIPROTupdater(),  NCBIupdater()]:
        try:
            updater.download(config, datadir )
        except Exception as ex:
            _log.error(ex)
        
    shutil.copy(configpath, configpath + ".bk")
    with open(configpath,"w") as h:
        json.dump(config,h)
    
       
    
    #xfam
    #     wget http://dfam.org/web_download/Current_Release/Dfam.hmm.gz
#     wget ftp://ftp.ebi.ac.uk/pub/databases/Pfam/AntiFam/current/AntiFam.tar.gz
#     wget http://www.treefam.org/static/download/treefam9.hmm3.tar.gz
#     wget ftp://ftp.ebi.ac.uk/pub/databases/Rfam/CURRENT/Rfam.cm.gz
#     wget ftp://ftp.jcvi.org/pub/data/TIGRFAMs/TIGRFAMs_15.0_HMM.LIB.gz


    
    #processed
    ##pdb_seqs       
#     pdbs.seqs_from_pdb_chains()
#     pdbs.seqs_from_pdbs()
#     hmm = Hmmer(database="/data/databases/xfam/Pfam-A.hmm",
#                 query="/data/databases/pdb/processed/chains_from_pdb.fasta",
#                 output_file="/data/databases/pdb/processed/domains.hmm")
#     hmm.query()
#     hmm.create_domains_fasta("/data/databases/pdb/processed/domains.fasta")
    #Correr script de extended_domain
    # print "Hmmer !!!!!!!!!!!!!!!!!"
    # sp.call("hmmscan  --acc --cpu 3 --domtblout /data/databases/pdb/processed/dns_pdbs.tlb --cut_tc /data/databases/xfam/Pfam-A.hmm /data/databases/pdb/processed/seqs_from_pdb.fasta",shell=True)
    # print "buscando doman extended..."  


    
    os.makedirs("/data/databases/ec")
#     wget http://priam.prabi.fr/REL_MAR15/Distribution.zip
#     cd /media/eze/Data/data/databases/ec/PRIAM_MAR15/PROFILES/LIBRARY
#     formatrpsdb -i /media/eze/Data/data/databases/ec/./PRIAM_MAR15/PROFILES/LIBRARY/profiles.list -o T -n PROFILE_EZ -t PRIAM_profiles_database
#     wget ftp://ftp.expasy.org/databases/enzyme/release/enzclass.txt
#     wget ftp://ftp.expasy.org/databases/enzyme/release/enzyme.dat;type=i
# java -jar PRIAM_search.jar -pt 0.5 -mo -1 -mp 70 -cc T -cg T -i /data/projects/Staphylococcus/annotation/ncbi/GCF_000009645.1_ASM964v1_protein.faa -p ./PRIAM_MAR15/
    
    os.makedirs("/data/databases/cog")
#     wget ftp://ftp.ncbi.nih.gov/pub/COG/COG/whog
#     wget ftp://ftp.ncbi.nih.gov/pub/COG/COG/fun.txt
#     wget ftp://ftp.ncbi.nih.gov/pub/COG/COG2014/data/cog2003-2014.csv
    


