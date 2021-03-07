import os
import threading
import time

class FileListener:



    def __init__(self, filepath, accessthreshold=10):
        self.filepath = filepath
        self.started = False
        self.accessthresh = accessthreshold
        self.sleep = int(accessthreshold/3)
        self.ishealthy=True


    def monitor(self):

        if not os.path.isfile(self.filepath):
            print(f"No SUCH FILE exists to be monitored {self.filepath} ")
            raise Exception("File missing")
        self.started=True
        runner = threading.Thread(name="monitor", target=self._monitorThread, args=(0, ))
        runner.setDaemon(True)
        runner.start()

    def isFileBeingModified(self):
        return self.ishealthy

    def _monitorThread(self,dummy):
        while(self.started):
            stat = os.stat(self.filepath)
            lastmod = stat.st_mtime
            now = time.time()
            fileage = now - lastmod
            if fileage>self.accessthresh:
                self.ishealthy = False
            else:
                self.ishealthy = True
            time.sleep(self.sleep)

        print("ListenThread is stopping")


if __name__ ==  '__main__':
    fl = FileListener("./logtest/test.log")
    fl.monitor()
    while(True):
        time.sleep(4)
        print(f"File being modified {fl.isFileBeingModified()} ")