import re
import os
from shared_utilities import clean_yml_to_dict


def list_to_md_table(list_of_lists):
    row_list = []
    for sub_list in list_of_lists:
        row = " | " + " | ".join(sub_list) + " | "
        row_list.append(row)
    md_table = "\n".join(row_list)
    return md_table

def update_authors_list(author_yml = "../_data/authors.yml", readMe = "readMe.md"):
    readMe = "readMe.md"
    with open(author_yml) as f:
        yml_text = f.read()
    
    yml_dict = clean_yml_to_dict(yml_text)
    list_for_table = [["author_id", "author name"]] 
    for item in yml_dict.keys():    
        list_for_table.append([item, yml_dict[item]["name"]])
    
    md_table = list_to_md_table(list_for_table)

    with open(readMe) as f:
        readMe_text = f.read()
    
    author_loc = "## data.yml (author ids)"
    new_author_text = author_loc + "\n" + md_table + "\n\n"
    author_regex = r"## data\.yml \(author ids\)[^#]+"

    readMe_text = re.sub(author_regex, new_author_text, readMe_text)

    with open(readMe, "w") as f:
        f.write(readMe_text)

def update_tags_categories_list(posts_dir = "../_posts/", readMe = "readMe.md"):
    posts_list = os.listdir(posts_dir)
    tag_list = []
    category_list = []
    for post in posts_list:
        post_path = os.path.join(posts_dir, post)        
        with open(post_path, encoding="utf-8-sig") as f:
            post_text = f.read()
        post_text_yaml = post_text.split("---")[1]

        yaml_dict = clean_yml_to_dict(post_text_yaml)           
        if "tags" in yaml_dict.keys():
            
            if yaml_dict["tags"] is not None:
               
                for tag in yaml_dict["tags"]:
                    if tag is not None:
                        if tag not in tag_list:
                            tag_list.append(tag)
        if "categories" in yaml_dict.keys():
            
            if yaml_dict["categories"] is not None:
                
                for category in yaml_dict["categories"]:
                    if category not in category_list:
                        if category is not None:
                            category_list.append(category)
    
    print(tag_list)
    print(category_list)
    tag_md = "## Existing tags\n- " + "\n- ".join(tag_list) + "\n\n"
    category_md = "## Existing categories\n- " + "\n- ".join(category_list) + "\n\n"

    tag_regex = r"## Existing tags[^#]+"
    category_regex = r"## Existing categories[^#]+"

    with open(readMe) as f:
        readMe_text = f.read()

    readMe_text = re.sub(tag_regex, tag_md, readMe_text)
    readMe_text = re.sub(category_regex, category_md, readMe_text)

    with open(readMe, "w") as f:
        f.write(readMe_text)

if __name__ == "__main__":
    update_authors_list()
    update_tags_categories_list()




