import pyinotify
import sys
import os
from cryptography.fernet import Fernet
import time
import glob


 
WATCH_PATH = input(">>>Input the file path to monitor : ") # monitoring directory
 
if not WATCH_PATH:
    print("The WATCH_PATH setting MUST be set.")
    sys.exit()
else:
    if os.path.exists(WATCH_PATH):
        print('Found watch path: path=%s.' % (WATCH_PATH))
    else:
        print('The watch path NOT exists, watching stop now: path=%s.' % (WATCH_PATH))
        sys.exit()


 
 # Event callback function
class OnFileHandler(pyinotify.ProcessEvent):
         # Rewrite the file write completion function
    def process_IN_CLOSE_WRITE(self, event):
        # logging.info("create file: %s " % os.path.join(event.path, event.name))
        file_path = os.path.join(event.path, event.name)
        print ( 'complete write file', file_path)
        
         # Rewrite file delete function
    def process_IN_DELETE(self, event):
        print ( "File Delete:% s"% os.path.join (event.path, event.name))
         # Rewrite file change function
    def process_IN_MODIFY(self, event):
        print ( "File Change:% s"% os.path.join (event.path, event.name))
 
         # Rewrite the file creation function
    def process_IN_CREATE(self, event):
        print ( "File creation:% s"% os.path.join (event.path, event.name))
        
        
        
    
    def process_IN_ACCESS(self,event):
        print("File Access:% s"% os.path.join (event.path, event.name))
        
        print("success")
        
        
        
            
            

          
        
        
        
        
        
        
        
       
        
        
        
        
 
 
def auto_compile(path='.'):
 
    wm = pyinotify.WatchManager()
    # mask = pyinotify.EventsCodes.ALL_FLAGS.get('IN_CREATE', 0)
         # Mask = pyinotify.EventsCodes.FLAG_COLLECTIONS [ 'OP_FLAGS'] [ 'IN_CREATE'] # monitor the content, monitor file create, delete and write is completed
    mask = pyinotify.IN_CREATE | pyinotify.IN_CLOSE_WRITE | pyinotify.IN_DELETE | pyinotify.IN_ACCESS
    notifier = pyinotify.Notifier (wm, OnFileHandler ()) # callback function
    wm.add_watch(path, mask, rec=True, auto_add=True)
    print('Start monitoring %s' % path)
    
    while True:
        try:
            notifier.process_events()
            if notifier.check_events():
                notifier.read_events()
        except KeyboardInterrupt:
            notifier.stop()
            break
 
if __name__ == "__main__":
    auto_compile(WATCH_PATH)
    print('monitor close')