---
excerpt:	""
header:
  overlay_image: /images/covers/banner_data2.jpg
  overlay_filter: rgba(40, 99, 165, 0.45)
  caption: "An example of some pairwise text reuse data viewed in speadsheet software"
title:		"About our data"
layout:		single
sidebar:
  nav: "corpus"
permalink: /data
toc: true
toc_sticky: true
---
Our data is created about and from the corpus. This page will provide a basic overview of our main data sets, which feature in our [blog]({{ '/blogs' | relative_url}}) and other [research]({{ '/research/articles' | relative_url }}). If you want like to explore how these data sets are created, consult our [methods pages]({{ '/methods' | relative_url }}).
Data sets evolve organically as the team works and researches. If during our research we develop a corpus-level data set that we believe will be of broader interest to KITAB's research or the research community, we set up a pipeline for its production. This ensures that the data set will be kept up to date with the corpus as it expands. We recommend you return to this page to keep abreast of the data that we are producing.
{% capture release-notice %} 
**Please note:** Not all of the data sets listed here have been released to the public. This page is intended as guidance to help those who are working for us to use and interpret our data sets and those reading our blog or other publications to understand the data sets behind our research. The following data sets have not yet been publicly released:
* all passim data sets* *isnad*-related data.
We plan to release our data sets to the public soon. Subscribe to our mailing list to be notified when we release data.
<a href='/subscribe' class='btn btn--primary align-center' >Subscribe for updates</a>
{% endcapture %}
<div class="notice--warning">
{{ release-notice | markdownify }}
</div>
## Corpus metadata
As noted in [using the corpus]({{ '/corpus/use#metadata-files' }}), we collect and store metadata about the books and authors in our corpus in yml files. We use these to create a file documenting metadata about all books in the corpus, including details such as* full book titles* author death dates* relationships between books in the corpus (for example, if one book is a commentary on another).
The yml files are being updated as the corpus is annotated. For the moment, many fields in the metadata file are populated using the metadata provided by the online libraries from which our texts are taken (such as al-Maktaba al-Shamila). Much of this data is accurate, but as it has been collected automatically and not been verified by the KITAB team, some caution should be exercised before using it.
The metadata file can be downloaded in one of two places:
1. We publish the metadata file every time we release the corpus. See our latest [releases]({{ '/corpus/releases' | relative_url }}) to download. This data is tied to the particular release and best if you need to cite a stable corpus. On the *stable* versus the *changing* corpus, see our guide on [using the corpus]({{ '/corpus/use#which-corpus' | relative_url }}).
2.  To access the latest metadata, updated with the corpus, visit the [corpus metadata page](https://kitab-corpus-metadata.azurewebsites.net/) and click on 'Excel' or 'CSV' to download the latest metadata file for the whole corpus.
{% capture meta-help %}
**Please note:** Corpus metadata can only be produced by hand, and producing high-quality metadata requires much time and effort. It is, however, essential for certain types of analysis of the corpus. If you find that metadata relevant to works in your field is out of date or erroneous, please consider helping us by updating it.
<a href='{{'/about/get-involved' | relative_url }}' class='btn btn--primary align-center' >How to get involved</a>
{% endcapture %}
<div class="notice--warning">
{{ meta-help | markdownify }}
</div>

## Passim text reuse data sets
A major part of our research is based on text reuse detection using the [passim algorithm]({{ '/methods/text-reuse#introducing-passim' | relative_url }}). We run passim on our corpus every time we release a new version of the corpus. For most runs we include only primary texts (that is, only one version of each text). This ensures that we get the best text reuse results. Occasionally we include the secondary texts, as this type of run allows us to better understand the different [versions]({{ '/corpus/use#uri-structure' | relative_url }}) that we have of certain texts and the differences between them. For each run, we produce two types of passim data set: **normal** and **aggregated**.
The **normal** data set uses passim alignments based on the milestones (the 300-word chunks into which we divide texts before running passim). In this data set, large alignments might be split across multiple milestones; this data set is especially useful for [book-to-book visualisation]({{ '/data/viz' | relative_url }}). The **aggregated** data set takes large alignments that cross milestones and brings them together into one alignment; this data set is particularly useful for close reading. For more detail on the distinction between the two data sets and why we continue to produce both, see our [page on text reuse]({{ '/methods/text-reuse' | relative_url }}).
The **normal** data set is good for visualisation because each alignment can be referred to using its milestone position, which corresponds uniformly to a 300-word chunk of the text -- many of our visualisations put the milestone number on the x-axis. The **aggregate** data set is better for understanding lengthy instances of text reuse.
For both of these data sets there are two forms of data:
### Alignment files
If passim identifies text reuse between two books, a file is produced. In the file, each row contains one alignment between the pair of texts, recording the aligned text (aligned using [Smith-Waterman]({{ '/methods/text-reuse#how-does-passim-work' | relative_url }})), the location of the alignment in each book and some statistics about the alignment. For detailed guidance on the data fields, see our .
The file name takes the format *versionID1_versionID2*. (On book IDs and the way we name the books in our corpus, see our page on [using the corpus]({{ 'corpus/use#uri-structure' | relative_url }}).) The file recording alignments between Ibn Hisham's *Sira* and al-Tabari's *Taʾrikh* would, therefore, be
Shamela0009783BK1-ara1.completed_Shamela0023833-ara1.completed.csv
{: .notice--primary}
For ease of identifying text pairs, we produce each alignment file in both directions; so
Shamela0023833-ara1.completed_Shamela0009783BK1-ara1.completed.csv
{: .notice--primary}
would be a flipped version of the same file.
A separate file is produced for each of the **normal** and **aggregated** data sets. The main difference between the two types of alignment files is that the location of **normal** alignments is given as a milestone, whereas for **aggregated** alignments a milestone range is provided.
### Passim text reuse statistics
From the alignment files we calculate statistics about text reuse in our corpus. In the passim statistics file, each row documents the relationship between a pair of related books, recording, for example, the following (for a full outline of the data fields, see our ):* How many words are shared between the two books* what percentage of one book is shared with the compared book.
There are two types of statistics files: **monodirectional** and **bidirectional**. A **monodirectional** file lists each book pair once. In this file it is entirely random whether a particular book is listed as book 1 or book 2. **Bidirectional** data is produced by taking the **monodirectional** data set and adding flipped versions of the book pairs. It therefore effectively contains a duplicate of each book relationship.
Although it might sound like **bidirectional** data would distort our text-reuse statistics, it is essential for certain kinds of analysis. For example, if one wishes to plot how text reuse changes over time, with the date on the x-axis, the **bidirectional** data makes it easy to record both sides of the relationship on a graph.
Caution should be exercised, however. Any kind of summary statistics calculated on the basis of the **bidirectional** data set could be distorted because each book pair is recorded twice. When using the data, think carefully about which data set will best suit your needs.
We produce text reuse statistics for both **normal** and **aggregated** data.
**Please note:** Our passim statistics files are enormous and grow with every expansion of the corpus. Bidirectional data sets now exceed 1 gigabyte in size. This data is too large to be used in most spreadsheet software (such as Excel), and working with the raw data will require some knowledge of PowerBI or scripting in languages such as Python. Our recommended route for exploring the passim statistics is our PowerBI statistics application, which we will soon release on the [application portal]({{ '/data/apps' | relative_url }}).
{: .notice--warning}
## *Isnad* classifier data sets
When we run the [*isnad* classifier]({{ '/methods/sub-genre#automatic-isnad-detection-our-first-case-study' | relative_url }}), we typically produce three types of data set:
1. *isnad*-tagged texts, with the beginning and end positions of *isnad*s tagged
2. *isnad* position files, which record the location of *isnad*s in each text relative to the structural annotation
3. whole-corpus statistics -- a file recording the number of *isnad*s in each text and the percentage of each text that consists of *isnad*s.
At present, in contrast to text reuse data, we do not routinely create *isnad* data for the whole corpus, but we plan to develop a pipeline for it in the future, as we move to using *isnad* data more routinely in our research.
## Other experimental data sets
In addition to these data sets, we routinely produce data sets to guide our research or improve our digital methods. To explore these data sets, it is best to read our [blog]({{ 'data/blogs' | relative_url }}). If you have any questions about those data sets and think you could help, we encourage you to contact the specific blog authors.
