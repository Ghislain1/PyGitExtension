import os, sys
import logging
import logging.handlers

from core import info


class StreamToLogger(object):

    def __init__(self, parent_stream, logLevel = logging.INFO):
        self.parent = parent_stream or sys.__stderr__
        self.logger= logging.LoggerAdapter(logging.getLogger("PyGitExtension.sterr",{"source":"stream"}))
        self.logLevel = logLevel
        self.logBuffer =''

    def write(self, text):
        self.logBuffer +=str(text) or ""
        self.parent.write(text)
    
    def flush(self):
        if self.logBuffer.rstrip():
           self.logger.log(self.logLevel, self.logBuffer.rstrip())
           self.logBuffer = ''

class StreamFilter(logging.Filter):
    """Filter out lines that originated on the output"""
    def filter(self, record):
        source = getattr(record, "source", "")
        return source != "stream"

# Set up log formatters
template = '%(levelname)s %(module)s: %(message)s'
console_formatter = logging.Formatter(template)
file_formatter = logging.Formatter('%(asctime)s ' + template, datefmt='%H:%M:%S')

# Configure root logger for minimal logging
logging.basicConfig(level=logging.ERROR)
root_log = logging.getLogger()

# Set up our top-level logging context
log = root_log.getChild('PyGitExtension')
log.setLevel(info.LOG_LEVEL_FILE)
# Don't pass messages on to root logger
log.propagate = False


#
# Create typical stream handler which logs to stderr
#
sh = logging.StreamHandler(sys.stderr)
sh.setLevel(info.LOG_LEVEL_CONSOLE)
sh.setFormatter(console_formatter)

# Filter out redirected output on console, to avoid duplicates
filt = StreamFilter()
sh.addFilter(filt)

log.addHandler(sh)
    


