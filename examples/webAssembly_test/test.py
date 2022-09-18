import os
import sys
import time
from subprocess import *
import datetime
import time
import threading
import re

# This script do auto testing before release code.
test_list = ["mnist", "cifar10", "vww", "mbnet"]


def runcmd(cmd):
    r = Popen(cmd, stdin=PIPE, stdout=PIPE, stderr=PIPE, shell=True)
    a = []
    for line in r.stdout.readlines():
        a.append(line.decode("utf8").strip())
    return a


for demo in test_list:
    result = runcmd("./run.sh {}".format(demo))
    num = re.findall(r"===tm_run use (\d+?\.\d+?) ms", "".join(result))
    print("running example [{0}] takes  {1}ms in linux, {2}ms in webassembly".format(demo, num[0], num[1]))
