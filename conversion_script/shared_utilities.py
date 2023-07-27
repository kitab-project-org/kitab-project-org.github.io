import os
import yaml

def set_directories():
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
  return in_dir, header_template, archive_dir, image_out, blog_dir, glossary_path

def clean_yml_to_dict(yml_text):  
    # Clear any tabs that may interfere with parsing
    yml_text = re.sub("\t", " ", yml_text)
    # Load the yaml
    yml_dict = yaml.safe_load(yml_text)
    return yml_dict