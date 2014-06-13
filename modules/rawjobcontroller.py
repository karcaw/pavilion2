#!python
"""  Implementation raw Job Control mechanism  """

import sys,os
import subprocess
from basejobcontroller import BaseJobController

class RawJobController(BaseJobController):
    """ class to run a test using no scheduler or special launcher """

    def start(self):

        # build the exact command to run
        cmd =  os.environ['PV_RUNHOME'] + "/" + self.configs['run']['cmd']
        print " ->  RawJobController: invoke %s" % cmd

        # Get any buffered output into the output file now
        # so that the the order doesn't look all mucked up
        sys.stdout.flush()

        # Invoke the cmd and send the output to the file setup when
        # the object was instantiated
        p = subprocess.Popen(cmd, stdout=self.job_log_file, stderr=self.job_log_file, shell=True)
        # wait for the subprocess to finish
        output, errors = p.communicate()

        if p.returncode or errors:
            print "Error: something went wrong!"
            print [p.returncode, errors, output]


    
# this gets called if it's run as a script/program
if __name__ == '__main__':
    
    # instantiate a class to handle the config files
    rjc = RawJobController()

    sys.exit()
    
