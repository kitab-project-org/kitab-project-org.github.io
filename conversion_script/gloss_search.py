import json
import os
import sys
import re

abspath = os.path.abspath(sys.argv[0])
dname = os.path.dirname(abspath)
os.chdir(dname)
glossary_path = dname + "/resources/glossary.json"

with open(glossary_path) as f:
  glossary = json.load(f)
  f.close()

blog = "text text text more text passim text text more text passim mARkdown"

def find_terms(glossary, blog):
    sidebar_text = "sidebar:\n\s\s-\stitle:\s\"Glossary\"\n\s\s-\stext:\s\""
    found_term = False
    for term in glossary["glossary"]:
      print(term)
      results = len(re.findall(term["term"], blog))
      if results > 0:
        found_term = True
        sidebar_text = sidebar_text + "**" + term["term"] + ":** " + term["def"] + "<br>"
    sidebar_text = sidebar_text + "\n---"
    if found_term == True:
      return sidebar_text
    else:
      return "---"



print(find_terms(glossary, blog))