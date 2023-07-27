---
image: "/images/old_blogs/2020-03-06-The-New-OpenITI-Metadata-Search//media/image1.png"
header:
  overlay_image: "/images/covers/banner_blog.jpg"
  overlay_filter: 0.1
  caption: "Gentile Bellini - Scribe, 1479-1481 (Image courtesy of [Isabella Stewart Gardner Museum](https://www.gardnermuseum.org/experience/collection/10755), Boston)" 
  show_overlay_excerpt: false 
title: "The New OpenITI Metadata Search"			
author: peter_verkinderen		
layout:		single
categories:
  - 
  - 
tags:
  - viz
  - 
---
The OpenITI corpus was designed in a way that makes it easy for scripts to access, identify and analyse the texts in the corpus. As a human reader, it was until now not easy to find a particular text you are interested in: all texts have a file name that starts with the death date of the author, followed by a short transliterated version of the author’s name and the book title (for more on OpenITI’s unique resource identifier (URI) system, see [here](https://alraqmiyyat.github.io/OpenITI/)).

[![]({{ "/images/old_blogs/2020-03-06-The-New-OpenITI-Metadata-Search//media/image1.png" | absolute_url }})]( {{ "/images/old_blogs/2020-03-06-The-New-OpenITI-Metadata-Search//media/image1.png" | absolute_url }})

The text files are stored in GitHub repositories (folders) that represent twenty-five-year time spans of the Hijri era. While this is very convenient for a script, if a human reader does not know the death date of an author, it may be very cumbersome to locate the file in the sixty repositories.

[![]({{ "/images/old_blogs/2020-03-06-The-New-OpenITI-Metadata-Search//media/image2.png" | absolute_url }})]( {{ "/images/old_blogs/2020-03-06-The-New-OpenITI-Metadata-Search//media/image2.png" | absolute_url }})

**We now have a new way to search for files in the OpenITI corpus:**

[**https://kitab-project.org/metadata**](https://kitab-project.org/metadata)

[![]({{ "/images/old_blogs/2020-03-06-The-New-OpenITI-Metadata-Search//media/image3.png" | absolute_url }})]( {{ "/images/old_blogs/2020-03-06-The-New-OpenITI-Metadata-Search//media/image3.png" | absolute_url }})

## Searching and filtering

You can search the metadata of the entire corpus for author and title, in Arabic and the simplified ASCII transliteration used in our URI system. You can also filter the metadata by tags, publishing houses, text collections and so on by using the Search box in the top right of the screen. The metadata table can also be sorted by clicking on the arrows next to the column headers.

## Annotation status and primary/secondary texts

For many texts, the OpenITI corpus contains different digital versions, which we got from different sources. We are currently working hard on adding structural annotation (chapters, paragraphs, dictionary entries, etc.) to the best digital version of every text in the corpus; we call this the ‘primary version’ (PRI).

The legend at the top of the page explains the symbols used for detailing the annotation status of the texts in the corpus:

[![]({{ "/images/old_blogs/2020-03-06-The-New-OpenITI-Metadata-Search//media/image4.png" | absolute_url }})]( {{ "/images/old_blogs/2020-03-06-The-New-OpenITI-Metadata-Search//media/image4.png" | absolute_url }})

Clicking on one of the items in the legend will filter the metadata table, leaving only the texts with the selected annotation status visible.

With the [![]({{ "/images/old_blogs/2020-03-06-The-New-OpenITI-Metadata-Search//media/image5.png" | absolute_url }})]( {{ "/images/old_blogs/2020-03-06-The-New-OpenITI-Metadata-Search//media/image5.png" | absolute_url }}) button, you can also choose to display only the primary texts.

## Notify us of issues with our texts!

If you notice that there is a problem with a text’s URI, you can notify us by clicking the link at the bottom of each Author, Title and Version cells:

[![]({{ "/images/old_blogs/2020-03-06-The-New-OpenITI-Metadata-Search//media/image6.png" | absolute_url }})]( {{ "/images/old_blogs/2020-03-06-The-New-OpenITI-Metadata-Search//media/image6.png" | absolute_url }})

You can also notify us if you notice an issue with the quality of a specific text version (e.g. if it is incomplete) in the Version column.

[![]({{ "/images/old_blogs/2020-03-06-The-New-OpenITI-Metadata-Search//media/image7.png" | absolute_url }})]( {{ "/images/old_blogs/2020-03-06-The-New-OpenITI-Metadata-Search//media/image7.png" | absolute_url }})

Finally, you can alert us when you think that another version of the text deserves to be the primary version:

[![]({{ "/images/old_blogs/2020-03-06-The-New-OpenITI-Metadata-Search//media/image8.png" | absolute_url }})]( {{ "/images/old_blogs/2020-03-06-The-New-OpenITI-Metadata-Search//media/image8.png" | absolute_url }})

Clicking any of these links will bring you to a GitHub issue form (you’ll need a GitHub account – you can create one [here](http://www.github.com/)). Please follow the instructions in the form to complete it, and hit the ‘Submit new issue’ button to send it off:

[![]({{ "/images/old_blogs/2020-03-06-The-New-OpenITI-Metadata-Search//media/image9.png" | absolute_url }})]( {{ "/images/old_blogs/2020-03-06-The-New-OpenITI-Metadata-Search//media/image9.png" | absolute_url }})

**Happy searching!**

 
