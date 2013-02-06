#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Copyright (C) 2008:
#  - Matteo Castellini <self {at} mcastellini [dot] net>
#  - Luca Foppiano <luca {at} foppiano [dot] org>
#  
# This program is free software; you can redistribute it and/or 
# modify it under the terms of the GNU General Public License 
# as published by the Free Software Foundation; either version 
# 2 of the License, or (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

# This is a ultra quick and dirty version of sample running script

import sys
import os
import shutil

from urlgrabber import grabber

from packages import PackageSack
from template_factory import TemplateBuilder

from configobj import ConfigObj

# configuration 

config_file = "/home/lfoppiano/develop/gerundo/trunk/gerundo.conf"

config = ConfigObj(config_file)
try:
    outputdir = config['outputdir']
    templatedir = config['templatedir']
    speckdir = config['speckdir']
except(KeyError):
    print "Cannot parse configuration file, please fix it."
    sys.exit(-1)

softwaredir = outputdir+str("/software")

print "* Preparing output directory "+str(outputdir)
try:
    os.stat(outputdir)
    shutil.rmtree(outputdir)
except(OSError):
    pass
finally:
    #directory doen't exists, try to create..
    try:
        os.mkdir(outputdir)
    except (OSError):
        print "Error during "+str(outputdir)+" creation."
        sys.exit(-1)

#os.mkdir(outputdir+"/css")
shutil.copytree(templatedir+"/css",outputdir+"/css")
shutil.copytree(templatedir+"/images",outputdir+"/images")

print "* Retrieving data package informations"
a = PackageSack()
leftovers = a.load_directory(speckdir)

if leftovers:
    print "Error: Some dependencies missing"
    sys.exit()

print "* dependencies satisfied, processing template"
print "* download packages"

try:
    os.stat(softwaredir)
except(OSError):
    os.mkdir(softwaredir)

os.chdir(softwaredir)

# disable reget as it seems to be broken on http:// with already downloaded 
# files
#grab = grabber.URLGrabber(reget=None)
#for item in a.packages:
#    print item.url
#    try:
#        item.local_file = grab.urlgrab(item.url)
#        print item.local_file
#    except(grabber.URLGrabError):
#        print "Error during downloads. Please check your speck files and retry"
#        sys.exit(-1);

#print s.pardir+os.sep+os.pardir+os.sep+"src"

#os.chdir(os.pardir+os.sep+os.pardir+os.sep+"src")


print "* build local website"

templateBuilder = TemplateBuilder(a, outputdir, templatedir)
templateBuilder.make_template()

