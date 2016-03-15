#!/usr/bin/env python

import os
from collections import OrderedDict
import shellvars
try:
    from ConfigParser import RawConfigParser
except ImportError:  # ver. < 3.0
    from ConfigParser import RawConfigParser


vars = shellvars.get_vars('grange-env.sh')
cfg=vars["GRANGE_SERVER_CONFIG"]

# instantiate
class MultiOrderedDict(OrderedDict):
    def __setitem__(self, key, value):
        if isinstance(value, list) and key in self:
            self[key].extend(value)
        else:
            super(OrderedDict, self).__setitem__(key, value)

config = RawConfigParser(dict_type=MultiOrderedDict)

# parse existing file
config.read(cfg)

section="rangeserver"

# read values from a section
loglevel = config.get(section, 'loglevel')
yamlpath = config.get(section, 'yamlpath')

config.set(section, 'yamlpath', 'data')

# save to a file
with open('test_update.ini', 'w') as configfile:
    config.write(configfile)
