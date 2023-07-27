from shared_utilities import set_directories
from shared_utilities import clean_yml_to_dict
from docx_converter import append_header_blog
import re
import os
import yaml
import json


def fetch_glossary(glossary_path):
  # Get data from glossary json
  with open(glossary_path, encoding='utf-8') as f:
    gloss = json.load(f)
    return gloss



# Check terms against a glossary and create a relevant piece of heading
def find_terms_add_to_glossary(glossary, blog, header_dict):
  
  # Get the len of existing terms - if the len of the new glossary is no different- then we can choose not to overwrite it
  if old_gloss_len in header_dict.keys():
    old_gloss_len = len(header_dict["glossary"])
  else:
    old_gloss_len = 0
  
  blog_gloss = []
  
  # Clean out website and image links that will create entries for file-type explanations in the glossary
  # Images embedded in links
  blog = re.sub("\[!?\[[^]]*\]\([^)]+\)\]\([^)]+\)", "", blog)
  # Simple images and links
  blog = re.sub("!?\[[^]]*\]\([^)]+\)", "", blog)
  
  # Loop through terms and add them to the blog's glossary if they are found
  found_term = False
  for term in glossary:
    results = len(re.findall(term["term"], blog))
    if results > 0:
      found_term = True
      blog_gloss.append(term)  
  
  # Compare the old and new glossaries - if the length has changed - re-write them
  new_gloss_len = len(blog_gloss)
  if new_gloss_len != old_gloss_len:
    changed_entries = True
  else:
    changed_entries = False

  # Return the header and the status of changed_entries - this allows us to use the output to not overwrite existing header if we wish
  if found_term == True:
    header_dict["glossary"] = blog_gloss
  return header_dict, changed_entries
  

def update_blog_gloss(old_style_header = False):

    # Set the directories
    in_dir, header_template, archive_dir, image_out, blog_dir, glossary_path = set_directories()

    # Get list of directories
    blog_list = os.listdir(blog_dir)
    gloss = fetch_glossary(glossary_path)

    # Loop and load text
    for blog in blog_list:
        blog_path = os.path.join(blog_dir, blog)
        with open(blog_path, encoding='utf-8') as f:
            blog_text = f.read()
        blog_splits = blog.split("---")[1]
        header = blog_splits[1]
        blog_text = blog_splits[2]
        header_dict = clean_yml_to_dict(header)
        
        # If old_style_header is true - find the old style header in the sidebar field and strip it out
        if old_style_header:
            if "sidebar" in header_dict.keys():
                sidebar_data = header_dict["sidebar"]
                gloss_pos = None
                for idx, item in enumerate(sidebar_data):
                    if item["title"] == "Glossary":
                        gloss_pos = idx
                if gloss_pos is not None:
                    del header_dict["sidebar"][gloss_pos]
            
        header_dict, changed_entries = find_terms_add_to_glossary(gloss, header_dict)

        if changed_entries:
            blog_out = append_header_blog(header_dict, blog_text)

            with open(blog_path, "w", encoding='utf-8') as f:
               f.write(blog_out)

if __name__ == "__main__":
   update_blog_gloss(old_style_header=True)
