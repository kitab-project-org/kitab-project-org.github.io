---
excerpt:	""
header:
  overlay_image: /images/covers/banner_data2.jpg
  overlay_filter: rgba(40, 99, 165, 0.45)
  caption: "An example of some pairwise text reuse data viewed in speadsheet software"
title:		"Download our data"
layout:		single
sidebar:
  nav: "corpus"
permalink: /data/download
toc: true
toc_sticky: true
---
We try to make our data available in ways that are easy to download. 
No need to scrape our APIs, everything is available in more easily accessible ways. 

## Text corpus

Our entire text corpus is released regularly on Zenodo. This DOI will always lead you to the latest release version of the corpus on Zenodo: [10.5281/zenodo.3082463](https://zenodo.org/doi/10.5281/zenodo.3082463); you'll find links there to earlier release versions.

The texts are also on the OpenITI [GitHub page](https://github.com/openiti), where they are organized in repositories by language and the death date of the author (grouped per 25 years): e.g., https://github.com/OpenITI/0775AH (Arabic texts by authors who died between 751 and 775 AH), https://github.com/OpenITI/PER0575AH (Persian texts by authors who died between 551 and 575 AH).

You can download all repositories containing Arabic texts using this bash script:

```
for i in $(seq -w 0025 25 1450); do (echo $i; git clone "https://github.com/openiti/${i}AH.git"); done;
```

For Persian texts, use this script: 

```
for i in $(seq -w 0025 25 1450); do (echo $i; git clone "https://github.com/openiti/PER${i}AH.git"); done;
```

Single texts can be downloaded through the KITAB [metadata application](https://kitab-project.org/explore). 

## Corpus metadata

Metadata on authors, texts and digital text versions is stored in the text repositories on the OpenITI GitHub page, in YML files.

This metadata is collected into a single file on a daily basis. In the kitab-metadata-automation](https://github.com/OpenITI/kitab-metadata-automation) repository on the OpenITI GitHub page you can find the most up to date version of the metadata in [tsv](https://github.com/OpenITI/kitab-metadata-automation/raw/master/output/OpenITI_Github_clone_metadata_light.csv) and [json](https://github.com/OpenITI/kitab-metadata-automation/raw/master/output/OpenITI_Github_clone_metadata_light.json) format. 

The metadata (in tsv format) of each release version of the corpus is included in the release zip file on [Zenodo](https://zenodo.org/doi/10.5281/zenodo.3082463); the metadata files can also be downloaded separately from [GitHub](https://github.com/OpenITI/kitab-metadata-automation/tree/master/releases). 

## Text reuse data

All text reuse data for a single text (compared pairwise to any other text in the corpus, or to all texts in the corpus at once) can be easily downloaded through our [metadata application](https://kitab-project.org/explore) - click the icon in the text reuse column to open the text reuse pane with all relevant links.

If you want to download all pairwise text reuse data (in tsv format) in one go for the latest corpus release, download it from the KITAB Github page [here](https://github.com/kitab-project-org/pairwise-light). Note that to fit the size limits on GitHub, we remove the columns containing the strings of aligned text from the passim's output. The data still includes the offsets of the aligned strings, so they can be regenerated from the text files. If you need the alignment strings included in the tsv file, you can download them through our [metadata application](https://kitab-project.org/explore); if you for some reason need all text reuse data for the entire corpus including the strings, please contact us. 

If you want to download all text reuse data documenting the overlap of one text with the entire corpus, download it from the KITAB Github page [here](https://github.com/kitab-project-org/one_to_all). 