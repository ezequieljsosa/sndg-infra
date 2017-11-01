import hashlib
import logging
import subprocess as sp

_log = logging.getLogger()
log_format = "%(asctime)s - %(name)s - %(lineno)d - %(levelname)s - %(message)s"

def init_log(log_file_path=None):
    default_formatter = logging.Formatter(log_format)
    console_handler = logging.StreamHandler()
    console_handler.setFormatter(default_formatter)    
    root = logging.getLogger()
    
    if log_file_path:
        fh = logging.FileHandler(log_file_path)
        fh.setLevel(logging.DEBUG)
        fh.setFormatter(default_formatter)
        root.addHandler(fh)
            
    root.addHandler(console_handler)
    root.setLevel(logging.DEBUG)

def md5(fname):
    hash_md5 = hashlib.md5()
    with open(fname, "rb") as f:
        for chunk in iter(lambda: f.read(4096), b""):
            hash_md5.update(chunk)
    return hash_md5.hexdigest()

def execute(template,**parameters):
    cmd = template.format(template,**parameters)
    _log.debug(cmd)
    sp.call(cmd,shell=True)
    _log.debug(cmd  + " --> Executed correctly")

def dl(url):    
    execute("wget  " + url + " -O " + url.split("/")[-1])
    
    
    
    