---
excerpt:	""
header:
  overlay_image: /images/covers/banner_clusters.jpg
  overlay_filter: rgba(40, 99, 165, 0.60)
  caption: "A prototype visualisation showing text reuse clusters for 8 milestones of al-Tabari's *Taʾrikh* relating to Abbasid history"
title:		"Network analysis"

layout:		single

permalink: /methods/networks
sidebar:
  nav: "methods"
---
Network analysis is a fundamental and well-developed field in the Digital Humanities. KITAB team members are using various computational methods to analyse networks through both our text reuse data and manually curated data sets, documenting connections between books and scholars. For this work we do not rely on a single defined tool, and we encourage you to read our [blog]({{ "methods/scholar-network" | relative_url }}) to explore the various methods we draw on.
There are two main directions that we are following in network analysis:
## Networks from *isnad*s
As we note [here]({{ 'methods/sub-genre' | relative_url }}), we seek to identify automatically *isnad*s in texts across the corpus. One aim of this work is to convert the automatically identified *isnads* into strings of related names, which can then be interpreted as networks.
Converting *isnad*s into networks is a complex process, because it requires addressing both name variation (that is, one person being referred to by multiple names) and shared names (that is, multiple people being referred to by the same name). We are working to resolve these problems computationally, using the position of names within *isnad*s to infer instances of name variation and to distinguish shared names. We are also approaching the latter problem by examining the position of *isnad*s within texts, since names might be shortened on their second or third mention.
Sarah Savant and Masoumeh Seydi are working together to create ground truth of the names used in the *isnad*s of two authors: al-Tabari and Ibn ʿAsakir. Ryan Muther is addressing the problem computationally, using the ground truth to test and improve his methods. This analysis is a work in progress, and for the latest updates you should see our [blog posts on the subject]({{ 'methods/scholar-network' | relative_url }}).
## Networks from text reuse data
We hope to convert some of our text reuse data into networks that illustrate how pieces of text are shared and disseminated. This is particularly challenging because of the size of our corpus and because the of the large amount of Hadith within our texts (which can be potentially shared across hundreds of texts). The passim algorithm outputs a data set called 'Cluster data', which documents how the milestones in our texts are networked together. For an explanation of how passim works and what milestones are, see [here]({{ 'methods/text-reuse' | relative_url }}). Unfortunately, this data set is messy and difficult to read, largely because of *isnad*s, which create non-meaningful clusters of shared names.
We have recently experimented with running passim without *isnad*s (by excluding the automatically tagged *isnad*s produced through this [method]({{ 'methods/sub-genre' | relative_url }})), and we will explore how this changes the cluster data. We are also working on producing networks from the text reuse data using other methods. Watch this space!
