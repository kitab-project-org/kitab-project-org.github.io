import yaml
import re

with open("test-header.yml") as f:
    text = f.read()

yaml_text = re.findall(r"---(.*)---", text, flags=re.DOTALL)[0]

yaml_text = re.sub("\t", " ", yaml_text)

print(yaml_text)

yaml_header = yaml.safe_load(yaml_text)

print(yaml_header)

print(yaml_header["glossary"])

yaml_header["glossary"].append({"Title": "title3", "Text": "text3"})

print(type(yaml_header))

yaml_string = "---\n{}---".format(yaml.dump(yaml_header))
print(yaml_string)

with open("test-header.yml", "w") as f:
    f.write(yaml_string)
