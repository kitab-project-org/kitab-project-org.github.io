import yaml

author_yaml_path = "../_data/authors.yml"

with open(author_yaml_path) as f:
    yaml_dict = yaml.safe_load(f)

print(yaml_dict["sarah_savant"])