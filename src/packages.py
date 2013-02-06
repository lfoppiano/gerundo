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


import yaml
import os
import re
import copy

class Package(yaml.YAMLObject):
    yaml_loader = yaml.loader.SafeLoader
    yaml_dumper = yaml.dumper.SafeDumper

    yaml_tag = u'!Speck'

    def __init__(self, name, version, label, category, url, description,
            dependency, suggestion, documentation):
        self.name = name
        self.version = version
        self.label = label
        self.category = category
        self.url = url
        self.description = description
        self.dependency = dependency
        self.suggestion = suggestion
        self.documentation = documentation

    @classmethod
    def from_yaml(cls, loader, node):
        main_node = copy.copy(node)
        for attribute in main_node.value:
            if attribute[0].value not in ('name', 'version', 'label', 'url',
            'description', 'category', 'dependency', 'suggestion',
            'documentation'):
                main_node.value.remove(attribute)
                continue
            elif attribute[0].value in ('name', 'version', 'label', 'url', 
            'description', 'category'):
                if not isinstance(attribute[1].value, basestring):
                    raise yaml.error.YAMLError
                elif attribute[1].tag == 'tag:yaml.org,2002:null':
                    attribute[1].tag = 'tag:yaml.org,2002:str'
                continue
            elif not isinstance(attribute[1].value, list):
                raise yaml.error.YAMLError
            else:
                for string in attribute[1].value:
                    if not isinstance(string.value, basestring):
                        raise yaml.error.YAMLError
                    elif string.tag == 'tag:yaml.org,2002:null':
                        string.tag = 'tag:yaml.org,2002:str'
        return loader.construct_yaml_object(main_node, cls)

    def __str__(self):
        return 'Name: %s, version: %s, label %s, category: %s' % (self.name,
                self.version, self.label, self.category)

    def __repr__(self):
        return ('%s(name=%r, version=%r, label=%r, category=%r, url=%r, '
                'description=%r, dependency=%r, suggestion=%r, '
                'documentation=%r)') % (self.__class__.__name__, self.name,
                self.version, self.label, self.category, self.url,
                self.description, self.dependency, self.suggestion,
                self.documentation)


class PackageSack:
    def __init__(self):
        self.packages = []

    def load_speck(self, filename):
        """Load a single speck file."""
        speck = file(filename, 'r')
        package = yaml.safe_load(speck)
        speck.close()
        return package

    def load_directory(self, directory='.'):
        """Load all the speck files from a directory."""
        if os.path.isdir(directory):
            specks = [name for name in os.listdir(directory) 
                        if re.search('\\.speck', name)]
            new_packages = []
            for filename in specks:
                new_packages.append(self.load_speck(directory + os.sep +
                        filename))
            return self.add_packages(new_packages)
        else:
            return {}

    def store_sack(self, directory='.'):
        """Dump all the packages into a directory."""
        filelist = []
        for package in self.packages:
            name = directory + os.sep + package.label + '.speck'
            speck = file(name, 'w')
            yaml.safe_dump(package, speck)
            speck.close()
            filelist.append(name)
        return filelist

    def verify_dependencies(self, dependencies):
        """Check PackageSack against a given dependencies' list."""
        for dependency in dependencies:
            exists = False
            for package in self.packages:
                if package.label == dependency:
                    exists = True
                    break
            if not exists:
                return dependency
        else:
            return []

    def add_packages(self, wannabelist):
        """Add a list of packages performing dependencies' checking."""
        missing = {}
        for wannabe in wannabelist:
            unsatisfied = self.verify_dependencies(wannabe.dependency)
            if unsatisfied:
                try:
                    missing[unsatisfied].append(wannabe)
                except KeyError:
                    missing[unsatisfied] = [wannabe]
            else:
                self.packages.append(wannabe)
                try:
                    wannabelist.extend(missing[wannabe.label])
                except KeyError:
                    pass
                else:
                    del missing[wannabe.label]
        return missing

    def get_packages_by_category(self):
        """Return a dictionary that associates package names to categories."""
        out = {}
        for package in self.packages:
            if out.has_key(package.category):
                out[package.category].append(package.name)
            else:
                out[package.category] = [package.name]
        return out

    def __repr__(self):
        return '%s()' % self.__class__.__name__
