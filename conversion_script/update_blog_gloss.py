from shared_utilities import set_directories
from shared_utilities import clean_yml_to_dict
from shared_utilities import append_header_blog
import re
import os
import yaml
import json
from tqdm import tqdm


def fetch_glossary(glossary_path):
  # Get data from glossary json
  with open(glossary_path, encoding='utf-8') as f:
    gloss = json.load(f)
    return gloss



# Check terms against a glossary and create a relevant piece of heading
def find_terms_add_to_glossary(glossary, blog, header_dict, overwrite = True):
  
  # Get the len of existing terms - if the len of the new glossary is no different- then we can choose not to overwrite it
  if "glossary" in header_dict.keys():
    blog_gloss = header_dict["glossary"]
    old_gloss_len = len(blog_gloss)
  else:
    old_gloss_len = 0
    blog_gloss = []
  
  
  # Clean out website and image links that will create entries for file-type explanations in the glossary
  # Images embedded in links
  blog = re.sub("\[!?\[([^]]*)\]\([^)]+\)\]\([^)]+\)", "\1", blog)
  # Simple images and links
  blog = re.sub("!?\[([^]]*)\]\([^)]+\)", "\1", blog)
  
  # Loop through terms and add them to the blog's glossary if they are found
  found_term = False
  changed_entries = False
  for term in glossary:
    # Wrap the term in spaces to avoid capturing parts of phrases
    term_regex = r"\s" + term["term"] + r"\s"
    
    results = len(re.findall(term_regex, blog, re.IGNORECASE))
    if results > 0:
      found_term = True
      # If term not already in the glossary, append it, if overwrite is set to true then remove the old verison and add the new one
      term_exists = False
      term_pos = None
      for idx, existing_term in enumerate(blog_gloss):
         if term["term"] == existing_term["term"]:            
            term_exists = True
            term_pos = idx              
      if term_exists and overwrite:
         del blog_gloss[term_pos]
         blog_gloss.append(term)
         changed_entries = True        
      if not term_exists:
        blog_gloss.append(term)  
  
  # Compare the old and new glossaries - if the length has changed - re-write them
  new_gloss_len = len(blog_gloss)  
  if new_gloss_len != old_gloss_len:
    changed_entries = True
  

  # Return the header and the status of changed_entries - this allows us to use the output to not overwrite existing header if we wish
  if found_term == True:
    header_dict["glossary"] = blog_gloss
  return header_dict, changed_entries
  

def update_blog_gloss(update_existing_entries = False):
    """This function will loop through the existing blogs, search for the glossary terms in the blogs and update the entries for all blogs
    This function is run by docx_converter.main() when an individual blog has prompted an update to the glossary. Otherwise we run this
    when the glossary has been updated.
    
    Using update_existing_entries will replace any existing entries in the blog glossary with new ones from the main glossary.json
    Set this to true when running an updated glossary where the def of indiviudal entries has been changed and you would like that
    change to be reflected across all blogs"""

    change_counter = 0

    print("Updating glossaries for existing blogs")

    # Set the directories
    in_dir, header_template, archive_dir, image_out, blog_dir, glossary_path = set_directories()

    # Get list of directories
    blog_list = os.listdir(blog_dir)
    gloss = fetch_glossary(glossary_path)

    # Loop and load text
    for blog in tqdm(blog_list):
        blog_path = os.path.join(blog_dir, blog)
        with open(blog_path, encoding='utf-8') as f:
            blog_text = f.read()        
        blog_splits = blog_text.split("---")        
        header = blog_splits[1]
        blog_text = "".join(blog_splits[2:])
        header_dict = clean_yml_to_dict(header)
        
        # If old_style_header is true - find the old style header in the sidebar field and strip it out
        # if old_style_header:
        #     if "sidebar" in header_dict.keys():
        #         sidebar_data = header_dict["sidebar"]
        #         gloss_pos = None
        #         if sidebar_data is not None:
        #             for idx, item in enumerate(sidebar_data):
        #                 if "title" in item.keys():
        #                     if item["title"] == "Glossary":
        #                         gloss_pos = idx
        #         if gloss_pos is not None:
        #             del header_dict["sidebar"][gloss_pos]
            
        header_dict, changed_entries = find_terms_add_to_glossary(gloss, blog_text, header_dict, overwrite=update_existing_entries)

        if changed_entries:
            change_counter = change_counter + 1            
            blog_out = append_header_blog(header_dict, blog_text)

            with open(blog_path, "w", encoding='utf-8') as f:
               f.write(blog_out)
    print("{} blogs updated following change to glossary".format(change_counter))

if __name__ == "__main__":
   # When the function is called directly from this script we update the entries by default - this is because we will only run this action independently of an
   # automatic blog update when there has been a change to the glossary and we need to update all posts accordingly
   update_blog_gloss(update_existing_entries=True)
