# How to update and manage the KITAB website

In the following you find an explanation of the website set-up and some step-by-step guides for updating and adding content to the KITAB website. It is recommended that you consult this document before making any changes to file structures, adding new pages or making changes to existing pages. 

You will find here sections containing guides on the following:
- the structure and format of the website.
- making changes to existing pages (note that the homepage and application portal have special formats and will be treated in subsections).
- adding new pages to the website.
- using the automatic blog uploading procedure.
- manually adding blogs to the website 

## Resources:
- Minimal mistakes [documentation](https://mmistakes.github.io/minimal-mistakes/docs/quick-start-guide/).
- [Guide](https://github.github.com/gfm/) to GitHub flavoured markdown (GFM).
- [Guide](https://shopify.github.io/liquid/) to Liquid - the programming language used by Jekyll to produce html. You may need this to add theme-specific features or stable internal links.
- [Guide]() to running Jekyll commands
- [Guide]() to installing Jekyll through Windows Subsystem for Linux (WSL) 

## Dependencies

### GitHub
If you plan to run the blog post upload script or make any changes locally, then a familiarity with basic GitHub is essential. Windows users should use Git Bash, Linux or Mac users can use the git functionality in their command line.

To get the repository locally, run the following command:
- git clone **ADD**

Before making any updates, make sure to run:
- 'git pull origin master' 
This will fetch any changes that have been made by any users or on the remote before you make your own changes. This is essential for avoiding merge conflicts.

If you make any updates, take the following approach:
1. Run 'git add .'
1. Run 'git commit -m "**easy to identify commit message**"
1. Run 'git push origin master'
1. Wait a short while to allow GitPages to process your changes and then go to the website to see your changes take effect. 

*WARNING: once you push changes to the main repository they will be added to the website. Make sure that you are happy with your changes before committing them to the main repository (this also applies if you make changes online). Once a change has been pushed to the remote (or committed in the remote - i.e. committed on the GitHub website), you will need to change it back manually and create another commit, to revert (or you will need to reset to an earlier commit - this is not recommended).

Given the above risks, it is recommended that you check big changes by running Jekyll locally before commiting your changes to the remote.


### Jekyll
Small changes to the website or blog uploads can be done without needed to install and run Jekyll locally. If you plan to make large changes to the website or add new pages, it is recommended that you install Jeykll on your local machine. This will allow you to test the website prior to uploading your changes to GitHub. The following steps

#### Windows vs Mac and Linux
The recommended route is to run Jekyll throughout Windows Subsystem for Linux, using Ubuntu. You will need to Activate WSL and install Ubuntu, on this (check [this]() guide). Mac and Linux users can use their command line.

#### Install Jekyll and get gems for our website
1. run: 'sudo install Jekyll'
1. run: 'gem install bundler'
1. 'cd' into the KITAB website directory (the GitHub repository that you downloaded in in the step above)
1. run 'bundle update' - this uses the website's specs to get the appropriate gems and versions
1. At this stage (or the following stage) you may find that you get an error telling you that some of your gems are the wrong version. To fix this run gem install 'gem-version' (where you give the name of the gem specified in the error and the version specified). To troubleshoot these issues it is recommend you search for the error in google and follow a stack exchange thread - almost all of the errors you will encounter will be resolved there.
1. to check everything is installed correctly run 'bundle exec jekyll serve'. This will serve the website locally.
1. Navigate to the local server address given in the command line to see the local instance of the website.

#### Checking your changes by running Jekyll locally
Whenever you make any changes to the website, you can use the following steps to check how those updates look in your browser before pushing them to the main website.
1. Open WSL Ubuntu in Windows or command line in Mac or Ubuntu
1. run : 'bundle exec jekyll serve'.
1. Navigate to the local server in the browser to look at your changes.
1. Use 'ctrl' + 'c' to end the local server process (it is recommended that you do this before making further changes).

**A note on making updates while the server is running** Jekyll allows you to make changes while the server is running and to see those changes locally. When you make a change, it will automatically re-run the build process and push the changes to the server. In some cases, it seems that this process errors and will hang (the command line will hang and you won't be able to end the server). If you find this happens, we recommend you use the command 'bundle exec jekyll serve --no-watch' to run the server. If you do this the website will not update as you make changes, but it will be more stable. In this case you will need to end the server and re-run 'bundle exec jekyll serve --no-watch' everytime that you want to see changes.

### Python
If you plan to run the blog docx conversion script on your local machine (for details on how to see below), you will need to install Python 3.6 on your local machine and use pip install to install any dependencies. For the dependencies see the requirements.txt file in the 'conversion_script' folder of the repository.

## About the structure and format of the website

The KITAB website is built from the Jekyll theme minimal-mistakes with some minimal added html for the home page. It is hosted using GitHub pages. Updates can be made directly to the markdown within this GitHub repository, or by cloning and editing the files locally.

For updating the website, there are four important folders:
1. _data
1. _pages
1. _posts
1. images

You may also need to make changes to the following files:
1. index.html
1. config.yml

You are unlikely to need to make any modifications to any other folders in the repository. Some of the folders contain files that are essential for Jekyll to build the website and changes are likely to cause **catastrophic** damage to the website. **Approach with caution.**

### _data

This folder contains three files, two of which are important for our use:
1. authors.yml
1. navigation.yml

authors.yml contains all of the data for the authors of blog posts. If there is a new author, they will need to be added to this yml. All fields for each author do not need to filled out. For best functionality, the minimum needed is: name, avatar, and bio. 

The contents of all fields should be given as quotation marks, bios should be around 30 words or less. The author id separated by the underscore (e.g. sarah_savant) needs to match the author given in the header matter of the blog post.

navigation.yml provides the structure of the website. The addresses used in this file should be match those in the header matter for relevant pages. The navigation is set up to provide sidebar navigation for all pages of the website. For guidance on how to use the navigation file, see the Minimal Mistakes [documentation](https://mmistakes.github.io/minimal-mistakes/docs/navigation/)

Changes to this file should only be made if a new page is added, or if a title needs to be changed in the top navigation or any of the sidebar navigation. Never change the field id 'main', and try to avoid changing other field ids (e.g. about, corpus) or url fields. Changes to these will cause the website to break if corresponding changes are not made in the headers of relevant pages. 

### _pages

This folder contains all of the markdown files for the pages of the website. The folder structure is present to aid your navigation, but changes to this structure will not make any impact on the website itself. If you want to change the content of any pages of the website, you will be making the changes to the markdown pages in this folder. If you want to add a new page to the website, you will be adding that page to this folder (or potentially one of the subfolders).

### _posts

This is where all of the blog posts for the website are stored in markdown format. When Jekyll builds the website, it looks for new blogs in this folder and uploads them accordingly. If you use a script to convert and upload a blog, then it will automatically be added to this folder. Otherwise, you will be adding the markdown file for the blog post to this folder.

### images

Any images on the website are stored here. **The structure of this folder matters - any changes to organisation will lead to broken links and missing images. Only add images to this folder, do not change the structure**

### index.html

This contains the content for the homepage of the website. Although it is an html file, Jekyll automatically converts the content of this file from markdown. You will find that this page contains markdown, liquid and html. Specific guidance will be provided below on how to making changes to the content of this page.

### config.yml

The file detailing the settings for the website. You are unlikely to need to make changes to this file. It controls matters such as: the name of the website, the type of commenting API that it uses, and the main theme template to use.

### A note on the theme colour customisation

This KITAB website uses a modified version of the 'air' skin. The skin is specified in the config file under 'minimal_mistakes_skin'. To add KITAB colours to the website, small changes have been made to: _sass/minimal-mistakes/skins/_air.scss

In this file one field has been changed:

$primary-color: #2862a5 !default; 

This sets the primary-color to the KITAB logo blue. If the theme were to be reset to default, make sure to update this field in _air.scss and specify the 'air' skin in config.yml.

## Making changes to existing pages

There is presently no procedure for converting website pages from docx to markdown using a python script. This is due to the increased level of customisation available in the pages part of the website (for example, for the insertion of text boxes). 

It is recommended that you modify the pages directly in the markdown file. This can be done through two 
