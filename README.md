Welcome to Gerundo project (the almighty dragon) 
=======

Input Formats 

== Esempio XML ==
{{{
#!xml
<?xml version='1.0' encoding='utf-8'?>
<software>
        <label>firefox</label>
        <version>2.0.0.10</version>
        <url>http://www.google.it/mozilla</url>
        <description>OMGWTF</description>
        <category>internet</category>
        <dependency>
                <required>nobody</required>
                <required>nowhere</required>
                <required>nowhat</required>
        </dependency>
        <suggestions>
                <suggestion>cup of the</suggestion>
        </suggestions>
        <documentations>
                <source>http://somewhere/somewhat/WTF.html</source>
        </documentations>
</software>
}}}

== Esempio YAML ==
{{{
#!yaml
name: Firefox
version: 2.0.0.10
label: firefox-2.0.0.10 #(name)-(version) used to perform dependency resolution
url: http://www.mozilla.com/firefox/releases/firefox-2.0.0.10.exe
description: >
    Firefox è il browser della Mozilla Foundation. È bello, figo, stabile, 
    piace alle ragazze e ciò rende i giovani uomini che lo usano più
    appetibili.
category: internet
dependency:
    - nobody
    - nowhere
    - nowhat
suggestion:
    - cup of tea
documentation:
    - http://somewhere.com/somewhat/wtf.pdf
}}}
= Project's tasks =

 1. XML --> oggetto e oggetto --> XML
 2. Oggetto --> [wiki:treeDir albero directory]
 3. Oggetto --> CSS+XHTML
 4. Frontend grafico= How to write a template =

Template exchanging is a wonderful feature of gerundo. At this moment, templates are fixed and simple.
You can write your own and apply to your pages.

== Template structure ==
Template is divided into three pages: homepage, category page and software page. The first one, is the starting page when you browse, category page is a list of software under a certain category and software page is single description page for specific software (es firefox page contain information about what is firefox, documentation url and so on)
Each page has three main parts: header, content and footer

This is a proposal for directory layout:


 * software
  - *.exe|*.zip|*.xpi
 * kmeleon
 * web
  * css
   - *.css
  * images
   - *.png|*.jpg
  * *.html
 * autorun.inf
 * tarantasio.ico
 * start.ini
 * start.exe

