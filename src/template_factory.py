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


from Cheetah.Template import Template

class TemplateBuilder:

    def __init__(self, sacks, outputdir, templatedir):
        """
            init object, if output and template directory are given
            it use it, in opposite case it use the default one.

            TODO: clean and make a less crappy code ;-)
        """

        self.outputdir = outputdir
        self.templatedir = templatedir
        self.sacks = sacks
        self.packages = sacks.packages
        self.categories = sacks.get_packages_by_category().keys()

    def make_template(self):
        self.build_homepage("homepage.tpl")
        self.build_category_pages("categories.tpl")
        self.build_software_pages("software.tpl")


    def build_homepage(self, template, row_num_cat=2):
        output_name = "index.html"
        t_in = open(self.templatedir+"/"+str(template))
        templateThings = {'page_title': "Homepage", 'categories': self.categories,
                'row_num_category': row_num_cat }
        t = Template(str(t_in.read()), searchList=[templateThings])

        t_out = open(str(self.outputdir)+"/"+output_name,"w")
        t_out.write(str(t))
        t_out.close()
    

    def build_category_pages(self, template):
        for item in self.categories:
            t_in = open(self.templatedir+"/"+str(template))  
            templateThings = {'page_title': 'Category :: '+str(item), 
		'packages': self.sacks.get_packages_by_category()[item]}
            t = Template(str(t_in.read()), searchList=[templateThings])

            t_out = open(str(self.outputdir)+"/"+str(item)+".html","w")
            t_out.write(str(t))
            t_out.close()


    def build_software_pages(self, template):
        for item in self.packages:
            t_in = open(self.templatedir+"/"+str(template))  
            item.description = item.description.encode("utf-8")
            templateThings = {'page_title': 'Category :: '+str(item.category),
                    'package': item}
            t = Template(str(t_in.read()), searchList=[templateThings])

            t_out = open(str(self.outputdir)+"/"+str(item.name)+".html","w")
            t_out.write(str(t))
            t_out.close()

