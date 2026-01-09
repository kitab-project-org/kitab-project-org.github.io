import os
import yaml
from datetime import date
from shared_utilities import append_header_blog
from shared_utilities import clean_yml_to_dict

def build_series_page(series_dict, series_path):

    page_path = os.path.join(series_path, series_dict["taxonomy"] + ".md")
    
    # If the page already exists in our series set - open the page and change the date to today - bringing it back to the front of the homepage
    if os.path.exists(page_path):
        with open(page_path) as f:
             page_text = f.read()
        page_split = page_text.split("---")
        header_text = page_split[1]
        header_dict = clean_yml_to_dict(header_text)
        header_dict["date"] = date.today()
        if len(page_split) == 4:
          page_content = page_split[3]
        else:
          page_content = ""
    else:   
        # Otherwise create a new page
        header_dict ={
            "layout": "category",
            "taxonomy": series_dict["taxonomy"],
            "title": series_dict["title"],
            "permalink": "/series/{}".format(series_dict["taxonomy"]),
            "date": date.today()
        }
        page_content = ""

    # Reassemble the page
    page_content = append_header_blog(header_dict, page_content)

    # Save the output
    with open(page_path, "w") as f:
        f.write(page_content)


