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
import shutil
from datetime import date
from datetime import datetime
import json
import yaml
from shared_utilities import set_directories
from shared_utilities import clean_yml_to_dict
from shared_utilities import append_header_blog
from update_blog_gloss import fetch_glossary
from update_blog_gloss import find_terms_add_to_glossary
from update_blog_gloss import update_blog_gloss
from build_series_pages import build_series_page
from update_readme import update_authors_list
from update_readme import update_tags_categories_list



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



# Create string from docx formatted text except those in wrong format
def docx_conv(root, name, images_path, author):        
    extract_img = "--extract-media=" + images_path + author
    full_path = os.path.abspath(os.path.join(root, name))
    if os.path.exists(full_path):
      blog = pypandoc.convert_file(full_path, 'markdown-simple_tables-multiline_tables-grid_tables', extra_args =["--wrap=none", extract_img])
    else:
      blog = None
    return blog

# Function to update the main glossary with new entries
def update_glossary_dict(gloss_path, new_entries):
  gloss = fetch_glossary(gloss_path)
  existing_terms = [x["term"] for x in gloss]
  # Loop through new entries and check they comply
  for entry in new_entries:
    term = False
    definition = False
    if "term" in entry.keys():
      term = True
      terms = True
    else:        
        print("Invalid new glossary in yml - {} - skipping..".format(entry))
        
    if "def" in entry.keys():
      definition = True
      definitions = True
    else:
        print("Invalid new glossary in yml - {} - skipping..".format(entry))
        
    if term and definition:
        if entry["term"] in existing_terms:
           print("Chosen term {} already in glossary.yml - if you wish to update the definition - update in this folder".format(entry["term"]))                 
        else:
          gloss.append(entry)
  
  # If new entries are written write one success message and write out file
  if terms and definitions:
      print("New entries written to the glossary")  
      with open(gloss_path, "w", encoding='utf-8') as f:
          f.write(json.dumps(gloss, indent = 1))
      
def clean_md_update_image_routing(blog_text):
      # Cleaning out uncessary md and tags from the final piece and converting images so they link to gallery view - fix image routine with absolute_url
    
      blog_text = re.sub(r"{width=.*?}", "", blog_text)    
      blog_text = re.sub(r"\!\[[^]]*\]\(\.\.(/images/[^\)]*)\)", r'[![]({{ "\1" | absolute_url }})]({{ "\1" | absolute_url }})', blog_text)
      
      # Cliean up links in the same way
      blog_text = re.sub(r"(\[[^]]*\]\()([^)|]*)(\))", r"\1{{ \2 | absolute_url }}\3", blog_text)

      # Remove double underlines (sometimes added in conversion of hyperlinks)
      blog_text = re.sub(r"\[<u>(.*)</u>\]", "", blog_text)
      
      blog_text = re.sub(r"\[([^\[\]]*)\]{\.ul}", r"\1", blog_text)
      
      # Fix footnotes to gfm standard
      blog_text = re.sub(r"\[(\d{1,2}\])[^(]", r"[^\1", blog_text)
      # This appears to cause a corruption
      # blog_text = re.sub(r"(\n\[\^\d{1,2}\])[^(]", "\1:", blog_text)
      
      # Fix tables to gfm standard
      blog_text = re.sub(r"\|\r\r\n", "|\n", blog_text)
      blog_text = re.sub(r"(\| {3,})+\|", "", blog_text)
      
      # Remove rtl and ltr markers
      blog_text = re.sub(r"\[([^\]]*)\]{dir=\"rtl\"}", r"\1", blog_text)
      blog_text = re.sub(r"\[?\]?{dir=\"rtl\"}", "", blog_text)
      blog_text = re.sub(r"\[?\]?{dir=\"ltr\"}", "", blog_text)
      
      # Change out non-gfm headings
      blog_text = re.sub(r"(.*\r)\r\n.*-{3,40}", r"\1", blog_text)
      
      # Identify and replace any numbered list indentations
      instances = re.findall(r"(\n\d+\..*([\r\n]+>.*)+)", blog_text)
      for group1, group2 in instances:
          new_instance = re.sub(r"\n>\s", "\n\t", group1)
          print(new_instance)
          blog_text = blog_text.replace(group1, new_instance)
      
      return blog_text

def add_thumb_image(header_dict, blog_text):
  images = re.findall(r"(/images/[^\"]*)", blog_text)  
  if len(images) > 0:
      header_dict["image"] = images[0]
  return header_dict

def build_file_name(blog_dir, header_dict):
   title = header_dict["title"]
   if title is None:
      print("No title given - provide a title and try again. Exiting...")
      exit()
   else:
      title_s = re.sub(r"[\s:/.,]", "-", title)[:40]
      
      #  # Get existing titles and check the given title_s doesnt exist (having two blogs with same title creates issues) - if so, add a number to the end
      #  # We have to relist the directories every time this function is run or we run the risk of not accounting for blog titles added during this upload process
      # Commented out - because overwriting is desirable to avoid lots of copies of the same blog on reupload. Changed for a warning - to flag when a blog has the same title as an older blog.
      existing_titles = os.listdir(blog_dir)
      dateless_titles = ["-".join(x.split("-")[3:]) for x in existing_titles]
      if title_s in dateless_titles:
      #     title_s = title_s + "-2"
            print("This blog has the same title as an existing blog - if this is not a reupload delete and change your blog title")
      final_path = os.path.join(blog_dir, str(date.today()) + "-" + title_s + ".md")
      return title_s, final_path

       

# # Add a correctly labelled header to the blog
# def header_build (head_in, blog, glossary):
#     # Sub in the submitted glossary -
#     head_in = re.sub(r"\n---", glossary, head_in)
#     images = re.findall(r"(/images/[^)]*)\)", blog)
#     if len(images) >= 1:
#         thumb = "\nimage: \"" + images[0] + "\"\n---\n"
#         head_in = re.sub(r"\n---", thumb, head_in)
#     # else:
#     #     thumb = "\nimage: \"/images/kitab/mesa.jpg\"\n---\n"
    
    
#     final = head_in + "\n\n" + blog
#     title = re.findall("title:.*\"(.*)\"", head_in)

#     if len(title) > 0 and title[0] != "":
#         title_s = re.sub(r"[\s:/.,]", "-", title[0])[:40]
#     else:
#         title_s = str(datetime.now().microsecond)[:3]

#     return (final, title_s)


  
  

def find_yml_docx_data(in_dir, file_list):
  """Loop through a list of directories and find the yml files return a list of dictionaries pairing the yml header to the docx files"""
  out_list = []
  out_gloss = []
  yml = re.compile(".*\.yml")
  for in_path in file_list:    
    if yml.match(in_path):
      # Load yml as text file
      in_file = os.path.join(in_dir, in_path)
      with open(in_file, encoding='utf-8-sig') as f:
        yml_text = f.read()
      
      # Clean the text and read as dict
      yml_dict = clean_yml_to_dict(yml_text)
      
      # Get the docx path and add to the dictionary
      if "docx" in yml_dict.keys():
         if yml_dict["docx"] is not None:
            out_dict = {"docx": yml_dict["docx"]} 
            del yml_dict["docx"]
            
            # Check if a new author entry is present - add to out_dict
            if "new_author" in yml_dict.keys():
              if yml_dict["new_author"] is not None:
                  for item in yml_dict["new_author"]:
                    if "name" in item.keys():
                        if item["name"] is not None:
                          out_dict["new_author"] = yml_dict["new_author"]
              del yml_dict["new_author"]
            
            # Check if a new glossary entry is present - add to specific output - allowing us to update the global glossary - check that items are not null
            empty_gloss=False
            if "glossary" in yml_dict.keys():
              if yml_dict["glossary"] is not None:
                  for item in yml_dict["glossary"]:
                    if "term" in item.keys():
                        if item["term"] is not None:
                          out_gloss.append(item)
                          empty_gloss = False
                        else:
                          empty_gloss = True
            if empty_gloss:
              del yml_dict["glossary"]



            # Check if series data is present - append it to the final list
            series_data = []
            label = False
            title = False
            if "new_series" in yml_dict.keys():
              if yml_dict["new_series"] is not None:
                  for item in yml_dict["new_series"]:
                    if "label" in item.keys():
                        if item["label"] is not None:
                          if "categories" not in yml_dict.keys():
                            yml_dict["categories"] = []
                          if item not in yml_dict["categories"]:                          
                            yml_dict["categories"].append(item["label"])
                            yml_dict["tags"].append(item["label"])
                          series_dict = {"taxonomy": item["label"]}
                          label = True                          
                    if "title" in item.keys():
                        if item["title"] is not None:
                          series_dict["title"] = item["title"]
                          title = True
                    if label and title:
                      series_data.append(series_dict)
              del yml_dict["new_series"]      
                  
            out_dict["series_data"] = series_data
            
            # Check series field and append any contents
            if "series" in yml_dict.keys():
              if yml_dict["series"] is not None:
                if type(yml_dict["series"] != list:
                  yml_dict["series"] = [yml_dict["series"]
                for item in yml_dict["series"]:
                  if item not in yml_dict["categories"]:
                    yml_dict["categories"].append(item)                
              del yml_dict["series"]

            # Add full header text to output dict
            out_dict["header"] = yml_dict

            out_list.append(out_dict)
  return out_list, out_gloss

def add_new_author(author_yml_path, new_author_list, header):   
  part_1 = new_author_list[0]
  new_author_dict = new_author_list[1]
  new_author_dict.update(part_1)  
  if "name" in new_author_dict.keys():
    author_id = header["author"]
    print("Adding a new author {} with following details: {}".format(author_id, new_author_dict))
    with open(author_yml_path) as f:
        author_dict = yaml.safe_load(f)
    if "bio" in new_author_dict.keys():
       bio = new_author_dict["bio"]
    else:
       bio = ""   
    if "author_id" not in author_dict.keys():
      author_dict[author_id] = {"name": new_author_dict["name"], "avatar": None, "bio": bio}
      with open(author_yml_path, "w") as f:
          yaml.dump(author_dict, f)
    else:
       print("Author Id {} already exists - try another?".format(author_id))
  else:
     print("Author dictionary invalid - it needs a 'name' field, you passed: {}".format(new_author_dict))
  
def clean_up_directories(in_dir, archive_dir, template_yaml_path):
  for root, dirs, files in os.walk(in_dir):
    for idx, name in enumerate(files):
        source_file = os.path.join(root, name)
        archive_dest = os.path.join(archive_dir, name)
        shutil.move(source_file, archive_dest)
    print("{} : file(s) moved to the archive".format(idx+1))
  template_dest = os.path.join(in_dir, "new_header.yml")
  shutil.copy(template_yaml_path, template_dest)
  print("Clean-up done!")
   

def main():

  # Check pypandoc install
  check_pypandoc()

  # Get all the main directories that will be used by the script
  in_dir, header_template, archive_dir, image_out, blog_dir, glossary_path, authors_yml = set_directories()

  # Get a list of directories in the input 
  files_in = os.listdir(in_dir)

  # Convert that list of files into a list of yml_header docx pairs
  docx_data_pairs, new_gloss_terms = find_yml_docx_data(in_dir, files_in)

  # If there are new glossary terms - update the glossary - and use the updated glossary to update glossaries for the existing blogs
  if len(new_gloss_terms) > 0:
     update_glossary_dict(glossary_path, new_gloss_terms)
     update_blog_gloss()
     

  # Fetch the glossary for use in the conversion process - this will be an updated glossary if an update has been run
  gloss = fetch_glossary(glossary_path)

  docx_check = re.compile(".*\.docx")
  # Loop through the pairs run the conversion and build the output text
  for docx in docx_data_pairs:
    # If we have new author - add the author's bio to the authors.yml
    if "new_author" in docx.keys():
       add_new_author(authors_yml, docx["new_author"], docx["header"])
       update_authors_list() 
    
    docx_path = docx["docx"]
    
    # Check we're dealing with a docx file - otherwise we'll trip up the converter
    if docx_check.match(docx_path):
        print(docx_path + " ...format correct")
        # Create the final_path and short title for the blog (short title is to be used in the image path)
        title_s, out_path = build_file_name(blog_dir, docx["header"])
        images_path = os.path.join(image_out, title_s)
        blog_text = docx_conv(in_dir, docx_path, images_path, docx["header"]["author"])

        # Check that function has found the file - if not give an error - and skip - otherwise continue processing
        if blog_text is None:
           print("WARNING - {} - file not found - have you uploaded the corresponding docx file?".format(docx_path))
        else:
            # If we have any data for series - that is a new_series - run the function to create a series page
            if "series_data" in docx.keys():
              series_path = "../_pages/blog-series/"
              for series_dict in docx["series_data"]:
                build_series_page(series_dict, series_path)

            # Run the glossary function and add the found entries to the header  
            header, changed_entries = find_terms_add_to_glossary(gloss, blog_text, docx["header"], overwrite = False)            

            # Clean the text using a function and update the image routing to ensure it will work on a fork
            blog_text = clean_md_update_image_routing(blog_text)

            # Add thumb image to the header
            header = add_thumb_image(header, blog_text)            
            
            # Use function to paste together the blog text and the header
            final_text = append_header_blog(header, blog_text)

            # Write the final text to the out_path
            with open(out_path, "w", encoding='utf-8') as f:
               f.write(final_text)

        # Write out the final converted text
    else:
       print("WARNING - Incorrect format submitted - it must be docx - submitted file name: {}".format(docx_path))
  
  # Once all new blogs have been added - update the existing category and tag lists on the readme for user
  update_tags_categories_list()

  # Once all processing is done - clean-up - move all files in the input to the archive folder - add a fresh template for the next user
  clean_up_directories(in_dir, archive_dir, header_template)

if __name__ == "__main__":
   main()

##!! ADD THIS REGEX SUB: "\[<u>(.*)</u>\]" TO GET RID OF DOUBLE UNDERLINES.
## ADD LINES FOR THUMBNAILS
## ADD REGEX FOR FIXING FN

""" FOOTENOTE REGEX: 1. \[(\d{1,2}\])[^(], [^\1 2. (\n\[\^\d{1,2}\])[^(] , \1: """
""" Table REGEX removing lines: ((\|.*)+\|)\r\r , \1\n """
""" Wrong heading regex: (.*\r)\r\n.*-{3,40} , ## \1"""
