---
excerpt:	""
header:
  overlay_image: /images/covers/banner_github.jpg
  overlay_filter: rgba(40, 99, 165, 0.45)
  caption: "An example of a folder in an OpenITI repository on GitHub"
title:		"Using the corpus"
layout:		single
sidebar:
  nav: "corpus"
permalink: /corpus/use
toc: true
toc_sticky: true

---
## Which corpus?

The KITAB corpus exists in two forms. On the one hand, there is the *ever-changing corpus* that reflects our ongoing work and that we manage via [GitHub](https://github.com/OpenITI). We constantly add new texts and/or metadata, annotate texts, occasionally rename or delete files, remove parts from our text files that do not belong to the text properly speaking, and so forth.

It is this changing corpus whose texts and metadata files can be identified, accessed and downloaded individually both though OpenITI [GitHub](https://github.com/OpenITI) and through our [metadata search application](https://kitab-project.org/metadata).

This changing corpus furthermore constitutes the main interface and point of contact between KITAB and the public. Any user of our corpus with a GitHub account is able to [submit issues](https://github.com/OpenITI/Annotation/issues/new/choose) with regard to our text and metadata files.

On the other hand, we release unchanging *instances* of our corpus through Zenodo twice a year (for the latest releases, see [here]({{ '/corpus/releases' | relative_url }})). These instances are tantamount to 'snapshots' of the entire corpus at a particular point in time. They are *stable versions of the corpus* and remain available for download indefinitely.

These stable versions of our corpus are necessary not only to generate the specific data sets we use in our research but also, more generally, to ensure the replicability of the results of research based on our corpus, the consistency of the assertions made with regard to it and the citability of our texts.

**It is upon each user to decide which corpus they want to use, and their choice will depend on their needs, their goals and the level of collaboration with KITAB they are interested in.**
{: .notice--primary}

## Finding files in the KITAB corpus

Finding texts and metadata files in the KITAB corpus requires understanding how it is structured and organised. To make things a bit easier, we have sought to organise our corpus in a way that readily makes sense to the human mind.

Perhaps it is best to imagine the organisational structure of the corpus by thinking of a physical library and its rows of shelves.

Once filled, all the rows of shelves taken together will correspond to our entire corpus. But according to which logic do we distribute the books over those rows of shelves? Which book sits where and why?

KITAB stores text files and corresponding metadata files as a series of Github repositories that group the authors according to their year of death in sets of twenty-five lunar years.

Thus, all authors who died in the years 0 to 25 according to the Hijri calendar are grouped together in one repository named 0025AH; all authors who died between 26 and 50 according to the Hijri calendar are grouped together in a repository named 0050AH; and so forth. Consequently, the KITAB corpus consists of about sixty such repositories, which constitute the most encompassing organisational unit of our corpus.

In our imagined library, each of these repositories containing the works of authors who died within the same twenty-five-year span corresponds to a row of shelves, and each row consists of separate bookcases reserved for individual authors.

For example, walking down the aisles of our library, we would stop at the row which says '0750AH' to search for books by al-Dhahabi, who died in the year 748 AH, and we would stop at the row of shelves which says '0425AH' to search for books by al-Tawhidi, who died in 414 AH.

In each author's 'bookcase', a specific place is reserved for each book written by the author in question. On the top shelf are all books that contain work A, on the second shelf all books that contain work B, and so on.

For example, in our imagined library, the shelf reserved for al-Tawhidi would have five shelves reserved for five different works by al-Tawhidi, and the actual books would sit on those respective shelves.

Within the structure of the KITAB corpus, the bookcase reserved for a particular author corresponds to the author folder, and the shelves reserved for the individual works written by that author correspond to the book subfolders within the author folder.

To remain with the example of al-Tawhidi, in the [author folder reserved for Tawhidi](https://github.com/OpenITI/0425AH/tree/master/data/0414AbuHayyanTawhidi) (the 'bookcase'), there are five subfolders (the 'shelves'), each of which contains all versions which we have of the respective work (that is, the actual files).

Thus, in the [book subfolder reserved for al-Tawhidi's *Akhlaq al-wazirayn*](https://github.com/OpenITI/0425AH/tree/master/data/0414AbuHayyanTawhidi/0414AbuHayyanTawhidi.AkhlaqWazirayn), there are two concrete text files that actually contain the work ([JK009310](https://github.com/OpenITI/0425AH/tree/master/data/0414AbuHayyanTawhidi/0414AbuHayyanTawhidi.AkhlaqWazirayn), [Shamela0012541](https://github.com/OpenITI/0425AH/blob/master/data/0414AbuHayyanTawhidi/0414AbuHayyanTawhidi.AkhlaqWazirayn/0414AbuHayyanTawhidi.AkhlaqWazirayn.Shamela0012541-ara1.completed)).

Although the metaphor is not perfect, just as, in a physical library, we have to walk down the aisles until we find the relevant row and then go to the correct bookcase and search the appropriate shelf until we finally locate the book we are looking for, in the KITAB corpus the location of individual files is governed by a comparable logic:

We must first navigate 'walk' to the appropriate twenty-five-year repository, then to the relevant author folder and then to the book folder, and this is where we finally find the actual text file.

Whenever we would, in a physical library, look for the next-level organisational unit (row, bookcase, shelf), we move, within the KITAB corpus, to the next-level folder within a repository.

## URI structure

Several pieces of information are required to locate a file in our corpus: the date of death according to the Hijri calendar, the author's name, the book title and information about the specific version of the book desired.

The key element which integrates all of these pieces of information and ensures the necessary organisational consistency in our corpus is the unique resource identifier (URI) (for details, see [here]({{ '/docs/openITI#uris--cts-like-folder-structure' | relative_url }})).

All files in our corpus are assigned a URI, which conforms to the following pattern:

AuthorID.BookID.VersionID-ara1
{: .notice--primary .text-center}

There are three central components here, separated by dots:

**AuthorID:** The AuthorID consists of an author's year of death according to the Hijri calendar plus that part of the author's name by which the author was most commonly known, i.e., the *shuhra* (e.g. 0414AbuHayyanTawhidi). Each author in our corpus has exactly one AuthorID.
{: .notice--primary}

**BookID:** The BookID consists of a component of the book title that is sufficiently distinct to make it recognisable (e.g. AkhlaqWazirayn). For each work in our corpus, there is exactly one BookID.
{: .notice--primary}

**VersionID:** The VersionID uniquely designates a particular text file in our corpus. It always consists of a first part, which indicates its origin, and a second part, which is always a number. The first part can refer to an online library, such as 'Shamela'; the acronym of a partner project, such as 'GRAR'; the initials of an individual who made a significant contribution to the text file; or the OCR tool we used, such as 'Kraken' (e.g. the versionID Shamela0012541 identifies the Shamela version of al-Tawhidi's *Akhlaq al-wazirayn* in our corpus). Each version of a work in our corpus has exactly one versionID. VersionIDs allow us to accommodate multiple versions of the same text. The addition -ara1 indicates that the work is in Arabic.
{: .notice--primary}

The full URI of the Shamela version of al-Tawhidi's *Akhlaq al-wazirayn* in our corpus is thus

0414AbuHayyanTawhidi.AkhlaqWazirayn.Shamela0012541-ara1
{: .notice--primary .text-center}

In contrast to AuthorID and BookID, which occasionally need to be corrected as they store minimal metadata that may contain errors, the versionID is assigned to a work the moment it becomes part of our collection and stays with it forever. The versionID alone thus allows identification of any work in our corpus univocally, which is why we occasionally use it as a shorthand for the full URI.

URIs do not only serve as unique identifiers for the individual text files in our corpus. Their individual components are also used for naming the author and book subfolders.

In fact, if we remove the versionID from the URI, the combination of AuthorID and BookID may be used as a unique work identifier. Likewise, if we remove the versionID and bookID, we are left with a unique author identifier.

0414AbuHayyanTawhidi.AkhlaqWazirayn.Shamela0012541|Unique Resource Identifier
0414AbuHayyanTawhidi.AkhlaqWazirayn|Unique Work Identifier
0414AbuHayyanTawhidi|Unique Author Identifier
{: .notice--primary .align-center}

KITAB consistently uses the unique author identifiers and the unique work identifiers to name the folders and subfolders found in the twenty-five-year repositories. The unique author identifiers thereby serve as the names of the author folders and the unique work identifiers serve as the names of the book subfolders.

Consequently, whenever two (or more) of our identifiers overlap with regard to the next higher component of the identifier, they fall within the same hierarchically higher folder, which carries the name of the overlapping part.

<span style="color:green">0414AbuHayyanTawhidi</span>.<span style="color:red">AkhlaqWazirayn</span>.JK009310-ara1\
<span style="color:green">0414AbuHayyanTawhidi</span>.<span style="color:red">AkhlaqWazirayn</span>.Shamela0012541-ara1\
<span style="color:green">0414AbuHayyanTawhidi</span>.<span style="color:blue">Basair</span>.JK009288-ara1\
<span style="color:green">0414AbuHayyanTawhidi</span>.<span style="color:blue">Basair</span>.Shamela0026423-ara1
{: .notice--primary .text-left}

{% capture except_notice %} 
**Please note:** There are certain exceptional author IDs that we use in the corpus in specific cases where an author cannot be identified, where the author's death date is unknown or where the author is still alive. Please find these variants in the table below. They are constantly being reviewed by the team, so check back here for updates.

  ID | Meaning
  --- | ---
  0001Quran.Mushaf (previously 0001KitabAllah.QuranKarim) | The Quran
  Anonymous | Unknown author (date in URI will correspond to the period when we think the author was alive)
  1450 | Date used for authors who are still alive
  Pseudo- | An indication that a work attributed to the author, but the attribution is uncertain or disputed



{% endcapture %}


<div class="notice--warning">
{{ except_notice | markdownify }}
</div> 


## Metadata files

The KITAB corpus contains not only plain text files but also yml metadata files.

There are three kinds of metadata files in our corpus that reflect the three types of identifiers contained in our URIs:

**Author metadata files** are named after the unique author identifier (e.g. 0414AbuHayyanTawhidi.yml). They store machine-readable information about the author in question as well as non-machine-readable freeform comments (for the template, see [here](https://github.com/OpenITI/Annotation/blob/master/templates_for_metadata/auth_template.yml)).
{: .notice--primary}

**Book metadata files** are named after the unique work identifier (e.g. 0414AbuHayyanTawhidi.AkhlaqWazirayn.yml). They store machine-readable information about the book or work in question as well as non-machine-readable freeform comments (for the template, see [here](https://github.com/OpenITI/Annotation/blob/master/templates_for_metadata/book_template.yml)).
{: .notice--primary}

**Version metadata files** use the unique resource identifier, which also identifies the corresponding plain text file (e.g. 0414AbuHayyanTawhidi.AkhlaqWazirayn.Shamela0012541-ara1.yml). They store machine-readable information about the specific version of the work in question as well as non-machine-readable freeform comments (for the template, see [here](https://github.com/OpenITI/Annotation/blob/master/templates_for_metadata/vers_template.yml)).
{: .notice--primary}

It is useful to fall back on our imagined library once more: our metadata files are like sheets of paper attached to each author's bookcase, each individual shelf in that bookcase and each of the actual books sitting on the shelves.

Thus, each author folder contains an author metadata file, which stores machine-readable information about that particular author.

Each book subfolder contains a book metadata file, which stores machine-readable information about that particular book or work.

And we accompany every text file with a version metadata file that stores machine-readable information about the specific version of a work contained in that particular text file.

We mostly fill in our metadata files in the course of subprojects; as a result,, not all of them contain information at present.

## Two ways of searching for files in the KITAB corpus

The text and metadata files contained in the KITAB corpus can be accessed by everyone and for free, in either of two ways:

First, files can be accessed through the twenty-five-year repositories available at [OpenITI GitHub](https://github.com/OpenITI) by navigating to the text or metadata file through the relevant folders and subfolders. This requires knowing the year of the author's death, as without that piece of information, the appropriate repository cannot be identified.

Second, files can be accessed by using the [KITAB metadata application](https://kitab-project.org/metadata) (for further information, see [here]()). This second option is preferable, as it allows finding files in our corpus without knowing the author's death date.

KITAB's metadata app allows users to search for each of the components of a URI separately (i.e. the AuthorID, the BookID, and the VersionID).

Furthermore, since many (though not all) files in our corpus contain metadata in Arabic (for example, the Arabic book titles of the original editions), users can also search for texts in Arabic.

The metadata app provides direct access to the text files by clicking on the versionID column of the app.

Metadata files can be accessed by clicking on the author name or the book title. Doing so takes the user to the folder or folder that contains the respective yml file.

<div class="notice--danger">
{{ "**Note on metadata searches:** For searches in Arabic, the presence of a hamza on an alif makes a difference (see the different results obtained for الأمان vs الامان). At present, the Arabic metadata is not entirely consistent in this respect.

For searches using transliterations, please observe the following rules:
* The International Journal of Middle Eastern Studies (IJMES) scheme is followed in its simplified version, omitting all diacritics so that only ASCII characters are used. The two most problematic Arabic letters are dealt with in the following manner: (1) hamzas are omitted to avoid using non-letter characters; (2) ʿayns are transliterated with c, which is capitalised when appropriate (ʿAli \> Cali; *Aʿyan al-Shiʿa* \> AcyanShica).
* إبن as part of a name is written in full and capitalised: ʿAli b. Abi Talib \> CaliIbnAbiTalib.
* Although an effort has been made to use *shuhra*s for AuthorIDs, when this is not possible, the following formula is used: Ibn + Ism Abihi + Nisba (these are the onomastic elements most commonly available in the metadata).
* The word *kitab* is dropped from titles, unless it is the major keyword, as in the case of Sibawayhi's *Kitab*, whose unique identifier is 0180Sibawayh.KitabSibawayh.
* Definite articles are dropped everywhere: *Tarikh al-islam* \> TarikhIslam.
* Multipart names and titles are written together, in camel case. In other words, there are no spaces between words, but each word is capitalised: *al-Nasikh wa-l-mansukh* \> NasikhWaMansukh.
* *Taʾ marbuta*s are transliterated as -t in genitive constructions (*idafa*s)." | markdownify}}
</div>
