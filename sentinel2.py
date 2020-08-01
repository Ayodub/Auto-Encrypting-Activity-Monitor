import os
import pyinotify
import glob
import pyinotify,subprocess
from cryptography.fernet import Fernet




target = input("input the filepath of your important files: ")


#----------------------------
#GENERATE KEY:


def write_key():  #define generate encryption key
    key = Fernet.generate_key()
    with open("key.key", "wb") as key_file:
        key_file.write(key)

write_key() #generate encryption

# INSERT DECRYPTION METHOD HERE LATER

print("\n>>>Your decryption key has been generated in the location of this script.\n>>>it is recommended you hide this in a separate location to this script.")




class EventProcessor(pyinotify.ProcessEvent):
    _methods = ["IN_ACCESS",
                "IN_ATTRIB",
                "IN_CLOSE_NOWRITE",
                "IN_CLOSE_WRITE",
                "IN_DELETE",
                "IN_DELETE_SELF",
                "IN_IGNORED",
                "IN_MODIFY",
                "IN_MOVE_SELF",
                "IN_MOVED_FROM",
                "IN_MOVED_TO",
                "IN_Q_OVERFLOW",
                "IN_UNMOUNT",
                "default"]

def process_generator(cls, method):
    def _method_name(self, event):
        
        currentdirectory=event.pathname
        
        

        def load_key():   #loads the encryption key
            return open("key.key", "rb").read()

        def encrypt(filename, key):  
            f = Fernet(key)


        key = load_key()  # initialize the Fernet class

        f = Fernet(key)   #file_list = os.listdir(currentdirectory)

        print("Method name: process_{}()\n"
               "Path name: {}\n"
               "Event Name: {}\n".format(method, event.pathname, event.maskname))
        for x in glob.glob(currentdirectory +'/**/*/*', recursive=True):    # Main loop to encrypt all files recursively
# double asterix ** tells program to encrypt all types of files

            filepath = os.path.join(currentdirectory, x)
            newfile = os.path.join(currentdirectory, x + '.aes')
            # Encrypt
            if "aes" not in filepath:
                if os.path.isfile(filepath):   #make sure it is a file, otherwise if it is folder it will give error
                    print('>>> Located: \t' + filepath + '')
                    print('>>> Encrypted: \t' + newfile + '\n')
                    with open(filepath, "rb") as file:      #rb= "read in binary"
                        file_data = file.read()
                
                    encrypted_data = f.encrypt(file_data)  

                    with open(newfile, "wb") as file:  # wb = "write in binary"
                        file.write(encrypted_data)
                        
            elif "aes" in filepath:
                THIS_IS_A_PURPOSEFUL_ERROR_WHICH_WORKS_FOR_SINGLE_TARGET #THIS STOPS ENCRYPTING EVERYTHING THROUGH AN ERROR. This works for watching a single file, as it is already encrypted, but if there's still other files to protect need a different method

                #os.remove(fullpath)  #removes the old file
                
    _method_name.__name__ = "process_{}".format(method)
    setattr(cls, _method_name.__name__, _method_name)
    

for method in EventProcessor._methods:
    process_generator(EventProcessor, method)
    

watch_manager = pyinotify.WatchManager()
event_notifier = pyinotify.Notifier(watch_manager, EventProcessor())

watch_this = os.path.abspath(target)
watch_manager.add_watch(watch_this, pyinotify.ALL_EVENTS)
event_notifier.loop()





#----------------------------------------------------------
#ENCRYPTION
          
