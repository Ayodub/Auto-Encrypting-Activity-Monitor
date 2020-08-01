import time
import sys, os
from watchdog.observers import Observer
from watchdog.events import PatternMatchingEventHandler, LoggingEventHandler


print ("How to use this script")
print ("python3 monitor.py /home/user/folder/to/monitor")
print ("If argv is empty, the script will monitor the path where the script are")
print ("")

patterns = "*"
ignore_patterns = ""
ignore_directories = False
case_sensitive = True
go_recursively = True


if __name__ == "__main__":


    my_event_handler = PatternMatchingEventHandler(patterns, ignore_patterns, ignore_directories, case_sensitive)
    path = sys.argv[1] if len(sys.argv) > 1 else '.'

    def on_created(event):
        print(f"Created: {event.src_path}")

    def on_deleted(event):
        print(f"Deleted: {event.src_path}!")

    def on_modified(event):
        print(f"Modify: {event.src_path}")

    def on_moved(event):
        print(f"Moved: {event.src_path} to {event.dest_path}")

    my_event_handler.on_created = on_created
    my_event_handler.on_deleted = on_deleted
    my_event_handler.on_modified = on_modified
    my_event_handler.on_moved = on_moved


    my_observer = Observer()
    my_observer.schedule(my_event_handler, path, recursive=go_recursively)
    if path == ".":
        print("Monitoring:", os.getcwd())
    else:
        print ("Monitoring:", path)
    my_observer.start()
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        my_observer.stop()
        my_observer.join()
