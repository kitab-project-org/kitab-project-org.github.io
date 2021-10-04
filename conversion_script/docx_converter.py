# -*- coding: utf-8 -*-
"""
Created on Tue Feb 23 14:42:07 2021

@author: mathe
"""
#!/usr/bin/python

import pypandoc
import re
import os
import sys
from datetime import date
from datetime import datetime
import json

# Getting main directory as script path

abspath = os.path.abspath(sys.argv[0])
dname = os.path.dirname(abspath)
os.chdir(dname)

parent = "\\".join(dname.split("\\")[:-1])
print(parent)
print(dname)

# Setting directories
docx_in = dname + "/input/blogs"
header_in = dname + "/input/headers"
image_out = parent + "/images/blogs/" + str(date.today()) + "/"
blog_dir = parent + "/_posts/"
glossary_path = dname + "/resources/glossary.json"

header_plain = dname + "/resources/header_plain"

docx = re.compile(".*\.docx")

# Get data from glossary json
with open(glossary_path) as f:
  gloss = json.load(f)
  f.close()

# Check terms against a glossary and create a relevant piece of heading
def find_terms(glossary, blog):
  sidebar_text = "\nsidebar:\n  - title: \"Glossary\"\n  - text: \""
  found_term = False
  for term in glossary["glossary"]:
    results = len(re.findall(term["term"], blog))
    if results > 0:
      found_term = True
      sidebar_text = sidebar_text + "**" + term["term"] + ":** " + term["def"] + "<br><br>"
  sidebar_text = sidebar_text + "\"\n---"
  if found_term == True:
    return sidebar_text
  else:
    return "---"


# Create string from docx formatted text except those in wrong format
def docx_conv(root, name, images_path):
        author = re.findall(r"(^.*?)\.", name)[0]
        extract_img = "--extract-media=" + images_path + author
        path = os.path.abspath(os.path.join(root, name))
        blog = pypandoc.convert_file(path, 'md', extra_args =["--wrap=none", extract_img])
        return blog, author.lower()


# Add a correctly labelled header to the blog
def header_build (header, name, blog, glossary):
     with open(header, encoding = "utf-8") as f:
            head_in = f.read()
            f.close()
     author = re.findall(r"(^.*?)\.", name)[0]
     author = re.sub(r"\d", "", author)
     author_code = "author: " + author.lower() + "\n"
     head_in = re.sub(r"author:.*\r?\n", author_code, head_in)
     # Sub in the submitted glossary - set up so it will just replace with metadata end placer if glossary empty
     head_in = re.sub(r"\n---", glossary, head_in)
     images = re.findall(r"\!\[.*?\]\(.*(/images/.*)\)", blog)
     if len(images) >= 1:
         thumb = "\nimage: \"" + images[0] + "\"\n---\n"
     else:
         thumb = "\nimage: \"/images/kitab/mesa.jpg\"\n---\n"
     head_in = re.sub(r"\n---", thumb, head_in)
     
     final = head_in + "\n\n" + blog
     title = re.findall("title:.*\"(.*)\"", head_in)

     if len(title) > 0 and title[0] != "":
          title_s = re.sub(r"[\s:/.,]", "-", title[0])[:40]
     else:
          title_s = str(datetime.now().microsecond)[:3]

     return (final, title_s)





for root, dirs, files in os.walk(docx_in, topdown=False):
    for name in files:
        if docx.match(name):
            print(name + " ...format correct")
            blog, author = docx_conv(root,name, image_out)
            header_path = header_in + "/" + author + ".yml"
            glossary = find_terms(gloss, blog)
            if os.path.exists(header_path):
              final, title_s = header_build(header_path, name, blog, glossary)
            else:
              final, title_s = header_build(header_plain, name, blog, glossary)
            
            # Fixing conversion issues
            # Cleaning out uncessary md and tags from the final piece and converting images so they link to gallery view
            final = re.sub(r"\!\[.*?\]\((.*)(/images/.*)\)", r"[![](\2)](\2)", final)
            final = re.sub(r"{width=.*?}", "", final)
            
            # Remove double underlines (sometimes added in conversion of hyperlinks)
            final = re.sub(r"\[<u>(.*)</u>\]", "", final)
            
            # Fix footnotes to gfm standard
            final = re.sub(r"\[(\d{1,2}\])[^(]", r"[^\1", final)
            # This appears to cause a corruption
            # final = re.sub(r"(\n\[\^\d{1,2}\])[^(]", "\1:", final)
            
            # Fix tables to gfm standard
            final = re.sub(r"((\|.*)+\|)\r\r", "\1\n", final)
            
            # Change out non-gfm headings
            final = re.sub(r"(.*\r)\r\n.*-{3,40}", "\1", final)
            
            # Identify and replace any numbered list indentations
            instances = re.findall(r"(\n\d\..*([\r\n]+>.*)+)", final)
            for group1, group2 in instances:
                new_instance = re.sub(r"\n>\s", "\n\t", group1)
                print(new_instance)
                final = final.replace(group1, new_instance)
   



            # Create outpath - check that file doesn't already exist
            title_s = re.sub(r"\s", "-", title_s)
            outpath = blog_dir + str(date.today()) + "-" + title_s + ".md"
            file_no = 0
            while os.path.isfile(outpath):
                file_no = file_no + 1
                outpath = blog_dir + str(date.today()) + "-" + title_s + str(file_no) + ".md"

            # Write out final blog to correct destination
            f = open(outpath, "w", encoding = "utf-8")
            f.write(final)
            f.close()
            print(outpath + "...written to blog directory")


        else:
            print("error!:\n" + name + " is not correctly formatted. \n Use docx.")
            continue


##!! ADD THIS REGEX SUB: "\[<u>(.*)</u>\]" TO GET RID OF DOUBLE UNDERLINES.
## ADD LINES FOR THUMBNAILS
## ADD REGEX FOR FIXING FN

""" FOOTENOTE REGEX: 1. \[(\d{1,2}\])[^(], [^\1 2. (\n\[\^\d{1,2}\])[^(] , \1: """
""" Table REGEX removing lines: ((\|.*)+\|)\r\r , \1\n """
""" Wrong heading regex: (.*\r)\r\n.*-{3,40} , ## \1"""