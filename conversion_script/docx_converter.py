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


def check_pypandoc():
  """We need this for running on github actions - if a pandoc install is not found on the os there - it will install it"""
  # Load pandoc if needed
  if hasattr(pypandoc, 'ensure_pandoc_installed'):
      # pylint: disable=E1101
      pypandoc.ensure_pandoc_installed(delete_installer=True)
  else:
      try:
          pypandoc.get_pandoc_path()
      except OSError:
          pypandoc.download_pandoc()

def set_directories()
  """Set the directories for locating the files to convert and where to put those files when converted"""
  abspath = os.path.abspath(sys.argv[0])
  dname = os.path.dirname(abspath)
  os.chdir(dname)

  in_dir = dname + "/input"
  header_template = dname + "/resources/header_plain"
  archive_dir = dname + "/archive"
  image_out = "../images/blogs/" + str(date.today()) + "/"
  blog_dir = "../_posts/"
  glossary_path = dname + "/resources/glossary.json"
  return in_dir, header_template, archive_dir image_out, blog_dir, glossary_path

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
    return "\n---"


# Create string from docx formatted text except those in wrong format
def docx_conv(root, name, images_path):        
    extract_img = "--extract-media=" + images_path + author
    path = os.path.abspath(os.path.join(root, name))
    blog = pypandoc.convert_file(path, 'markdown-simple_tables-multiline_tables-grid_tables', extra_args =["--wrap=none", extract_img])
    return blog


# Add a correctly labelled header to the blog
def header_build (head_in, blog, glossary):
    # Sub in the submitted glossary -
    head_in = re.sub(r"\n---", glossary, head_in)
    images = re.findall(r"\!\[.*?\]\(.*(/images/[^)]*)\)", blog)
    if len(images) >= 1:
        thumb = "\nimage: \"" + images[0] + "\"\n---\n"
        head_in = re.sub(r"\n---", thumb, head_in)
    # else:
    #     thumb = "\nimage: \"/images/kitab/mesa.jpg\"\n---\n"
    
    
    final = head_in + "\n\n" + blog
    title = re.findall("title:.*\"(.*)\"", head_in)

    if len(title) > 0 and title[0] != "":
        title_s = re.sub(r"[\s:/.,]", "-", title[0])[:40]
    else:
        title_s = str(datetime.now().microsecond)[:3]

    return (final, title_s)

def fetch_glossary(glossary_path):
  # Get data from glossary json
  with open(glossary_path) as f:
    gloss = json.load(f)
  
  return gloss

def find_yml_docx(file_list):
  """Loop through a list of directories and find the yml files return a list of dictionaries pairing the yml header to the docx files"""
  out_list = []
  yml = re.compile(".*\.yml")
  for in_file in file_list:    
    if yml.match(in_file):
      with open(in_file, encoding='utf-8-sig') as f:
        yml_text = f.open()  
      corresponding_docx = re.findall(r"docx:\s*['\"](.*)['\"]\n", yml_text)[0]
      yml_header = "".join(re.split("---", yml_text)[:3])
      out_list.append({"docx": corresponding_docx, "header": yml_header})
  return out_list


def main():

  # Check pypandoc install
  check_pypandoc()

  # Get all the main directories that will be used by the script
  in_dir, header_template, archive_dir, image_out, blog_dir, glossary_path = set_directories()

  # Get a list of directories in the input 
  files_in = os.listdir(in_dir)

  # Convert that list of files into a list of yml_header docx pairs
  docx_pairs = find_yml_docx(files_in)

  # Fetch the glossary for use in the conversion process
  gloss = fetch_gloss(glossary_path)

  docx_check = re.compile(".*\.docx")
  # Loop through the pairs run the conversion and build the output text
  for docx in docx_pairs:
    docx_path = docx["docx"]
    # NEED TO ADD A CHECK THAT FILE EXISTS - AND REPORT AN ERROR
    # Check we're dealing with a docx file - otherwise we'll trip up the converter
    if docx_checl.match(docx_path):
        print(docx_path + " ...format correct")
        blog_text = docx_conv(in_dir, docx_path)

        # Take cleaning steps - build into function and use it here

        # Use function to paste together the blog text and the header
        final_text = header_build(docx["header"], blog_text, glossary)

        # Write out the final converted text





# Getting main directory as script path



parent = "\\".join(dname.split("\\")[:-1])
print(parent)
print(dname)

# Setting directories
docx_in = dname + "/input/blogs"
header_in = dname + "/input/headers"
image_out = "../images/blogs/" + str(date.today()) + "/"
blog_dir = "../_posts/"
glossary_path = dname + "/resources/glossary.json"

header_plain = dname + "/resources/header_plain"

docx = re.compile(".*\.docx")









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
            final = re.sub(r"\!\[.*?\]\(.*(/images/[^)]*)\)", r"[![](\1)](\1)", final)
            final = re.sub(r"{width=.*?}", "", final)
            
            # Remove double underlines (sometimes added in conversion of hyperlinks)
            final = re.sub(r"\[<u>(.*)</u>\]", "", final)
            
            final = re.sub(r"\[([^\[\]]*)\]{\.ul}", r"\1", final)
            
            # Fix footnotes to gfm standard
            final = re.sub(r"\[(\d{1,2}\])[^(]", r"[^\1", final)
            # This appears to cause a corruption
            # final = re.sub(r"(\n\[\^\d{1,2}\])[^(]", "\1:", final)
            
            # Fix tables to gfm standard
            final = re.sub(r"\|\r\r\n", "|\n", final)
            final = re.sub(r"(\| {3,})+\|", "", final)
            
            # Remove rtl and ltr markers
            final = re.sub(r"\[([^\]]*)\]{dir=\"rtl\"}", r"\1", final)
            final = re.sub(r"\[?\]?{dir=\"rtl\"}", "", final)
            final = re.sub(r"\[?\]?{dir=\"ltr\"}", "", final)
            
            # Change out non-gfm headings
            final = re.sub(r"(.*\r)\r\n.*-{3,40}", r"\1", final)
            
            # Identify and replace any numbered list indentations
            instances = re.findall(r"(\n\d+\..*([\r\n]+>.*)+)", final)
            for group1, group2 in instances:
                new_instance = re.sub(r"\n>\s", "\n\t", group1)
                print(new_instance)
                final = final.replace(group1, new_instance)
   



            # Create outpath - check that file doesn't already exist
            title_s = re.sub(r"\s|\?|:|,", "-", title_s)
            outpath = blog_dir + str(date.today()) + "-" + title_s + ".md"
            file_no = 0
            while os.path.isfile(outpath):
                file_no = file_no + 1
                outpath = blog_dir + str(date.today()) + "-" + title_s + str(file_no) + ".md"

            # Write out final blog to correct destination
            f = open(outpath, "w", newline="", encoding = "utf-8")
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
