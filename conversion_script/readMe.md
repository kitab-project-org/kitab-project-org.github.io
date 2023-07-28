# Instructions for adding blogs

## Fork the website repository
If you have not already forked this repository, click the fork option at the top right. If you already have a fork, go to that fork in your own GitHub (e.g. github.com/mabarber92/kitab-project-org.github.io) and update the fork.

## Create a yml file for the blog post
The yml file is what describes your post and it's content. *Without a yml file, your blog will not be uploaded to the website*. For each docx file containing a blog, there should be a corresponding yml file. If uploading multiple blog posts at once, download the sample yml (new_header.yml) file from the input folder and use this as a template to produce yml files for each blog, and 

The yml file looks like this:
```
header:
  overlay_image: "/images/covers/banner_blog.jpg"
  overlay_filter: 0.1
  caption: "Gentile Bellini - Scribe, 1479-1481 (Image courtesy of [Isabella Stewart Gardner Museum](https://www.gardnermuseum.org/experience/collection/10755), Boston)" 
  show_overlay_excerpt: false  
title:
author:
layout: single
series:
tags:
  - 
docx:
new_author:
  - name:
    bio:
glossary:
  - term:
    def:
new_series:
  - label: 
    title:
```

At an absolute minimum, you must fill out the title, author, and docx fields.

### What each field is used for

```
header:
  overlay_image: "/images/covers/banner_blog.jpg"
  overlay_filter: 0.1
  caption: "Gentile Bellini - Scribe, 1479-1481 (Image courtesy of [Isabella Stewart Gardner Museum](https://www.gardnermuseum.org/experience/collection/10755), Boston)" 
  show_overlay_excerpt: false
```
This is a preset field and it sets the image that appears in the banner at the top of the page. If you change this, you will need to upload the corresponding image, set in 'overlay_image' to the images folder. It is recommended to put it in the 'covers' folder, if you do so.

```
title:
```
The title of the blog between quotation marks (remember when uploading your docx in the next step to remove the title of the blog post from the docx if it is present). For example:
```
title: 'Dispatches from al-Tabari part 1'
```

```
author:
```
The author of the blog. This is specified using an id code. The list of current id codes for authors is in this readme before. As can be seen in this list, multiple-author blogs should use a specific id, with a corresponding biography. If you are a new author (or a new authorial collaboration), then you need to create a new id using the 'new_author' field, see below. For example:
```
author: sarah_savant
```

```
layout: single
```
This specifies the layout used by the website. **DO NOT CHANGE THIS**

```
series:
```
If the blog belongs to an existing blog series, specify here. See below for a list of existing codes for blog series (this list will update automatically, when new series are added). For example:
```
series: tabari
```
```
tags:
```
This field lists any tags you would like to associate with the blog. A list of existing tag codes are found below, but you can create new ones. For example:
```
tags:
 - text-reuse
 - book-history
 - author-practice
```
```
docx:
```
Provide here the exact name of the docx file that is being uploaded into the input folder. **WARNING: If this name does not match the file name exactly, the upload will fail** For example:
```
docx: tabari_blog1.docx
```
```
new_author:
  - name:
    bio:
```
If the blog is written by a new author, then add a new author should be added to this field. For example:
```
new_author: joe_bloggs
  - name: 'Joe Bloggs'
    bio: 'A short biography of the new author...'
```
Use this for adding a new author collaboration, for example (note that you need to use a <br> tag to create a new paragraphy between the author bios:
```
new_author: joe_bloggs_sam_smith
  - name: 'Joe Bloggs and Sam Smith'
    bio: 'A short biography of the first author... <br> A short biography of the second author'
```

```
glossary:
  - term:
    def:
```
The KITAB website uses an automated glossary system that will use an existing glossary (found in : resources/glossary.json) to search for words that are found in your blog post and add definitions to the glossary in the sidebar. If you would like to add new glossary items, use this field to add the terms and definitions. When your blog is uploaded, these new terms will be added to the main glossary.json and can be used by previous blog posts or any following blog posts. For example:
```
glossary:
  - term: 'isnad'
    def: 'A chain of transmission, used as a form of citation.'
  - term: 'scatter graph'
    def: 'A type of graph that is used to study the correlation between variables.'
```

```
new_series:
  - label: 
    title:
```
If you are adding the first blog in a new series (that will appear in the series list on the KITAB website homepage), then you need to give an label (which will be used in the url for the series page) and a title for the series. As the label will be used in the URL, it should not contain any spaces. The 'title' will appear on the homepage and at the top of the series page listing all of the blogs. For example:
```
new_series:
  - label: topic-modelling
    title: Some experimentation in topic modelling
```

## Add the word docx to the folder
Once you have created a yml file for each blog, you need to add the docx and yml files to the input folder. Navigate to the 'conversion_script' folder, and from there to the 'input' folder. Click the 'Add file' dropdown and click 'Upload files' button and drag and drop your docx files into the folder. For the conversion script to work, your files must be saved in 'docx' format. If you have already prepared your yml files, they can also be dropped into the input folder.

## Go to actions and run the workflow

## Check the test website and make corrections

## Submit a pull request to the main website


# Useful data for filling out a yml file

## data.yml (author ids)
| author_id | author name |
| --- | --- |
| abdul_rahman_azzam | Abdul Rahman Azzam |
| anjum_alam | Anjum Alam |
| aslisho_qurboniev | Aslisho Qurboniev |
| claire_savina | Claire Savina |
| david_smith | David Smith |
| gowaart_van_den_bossche | Gowaart Van Den Bossche |
| hamid_reza_hakimi | Hamid Reza Hakimi |
| karen_bauer | Karen Bauer |
| kevin_jaques | Kevin Jaques |
| lorenz_nigst | Lorenz Nigst |
| masoumeh_seydi | Masoumeh Seydi |
| masoumeh_seydi_peter_verkinderen | Masoumeh Seydi and Peter Verkinderen |
| maxim_romanov | Maxim Romanov |
| peter_verkinderen | Peter Verkinderen |
| ryan_muther | Ryan Muther |
| sarah_savant | Sarah Bowen Savant |
| sarah_savant_masoumeh_seydi | Sarah Savant and Masoumeh Seydi |
| sarah_savant_mathew_barber | Sarah Bowen Savant and Mathew Barber |
| sohail_merchant | Sohail Merchant |
| thomas_benfey | Thomas Benfey |
| mathew_barber | Mathew Barber |

## Existing categories
- tabari
- clusters
- fihrist

## Existing tags
- text-reuse
- book-history
- author-practice
- news
- author-practice data, book-history
- events
- release
- corpus
- news release
- corpus data
- viz
- book-forms
- dispersed-texts
- machine-learning
- citation
- news corpus, release
- reg-west
- reg-egypt
- cultural-memory
- iran
- scholar-network
- reg-syr-arab
- reg-east
- khurasan
- releases
- markdown
- passim
- search

#
