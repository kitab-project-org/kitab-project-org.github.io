---
excerpt:	""
header:
  overlay_image: /images/covers/banner_ocr.jpg
  overlay_filter: rgba(40, 99, 165, 0.45)
  caption: "Escriptorium, an OCR and post-correction interface"
title:		"Optical Character Recognition (OCR)"
layout:		single
sidebar:
  nav: "corpus"
permalink: /corpus/ocr
---
KITAB uses Optical Character Recognition (OCR) tools to further build the OpenITI/KITAB corpus.
To this end, we have created our own OCR pipeline, which is based on [Kraken](http://kraken.re/) and uses transcription models that we are training in close collaboration with the University of Maryland, Northeastern University and Harvard University.
This usage of Kraken is reflected in the unique resource identifiers (URIs) of the resulting files, all of which contain 'Kraken' and the date of their creation in the form of either YYMMDDHH or YYMMDDHHSS in their [versionID]({{ "/corpus/use#uri-structure" | relative_url }}).
For example, Ibn ʿArabi's *Fusus al-hikam* was added to the OpenITI/KITAB corpus through OCR and therefore carries the following URI: [0638IbnCarabi.FususHikam.Kraken21042913-ara1](https://github.com/OpenITI/0650AH/blob/master/data/0638IbnCarabi/0638IbnCarabi.FususHikam/0638IbnCarabi.FususHikam.Kraken21042913-ara1.completed).
The specific version of Kraken as well as the segmentation and transcription models used during the OCR process are documented in the [version yml files of the OCR'd text](https://github.com/OpenITI/0650AH/blob/master/data/0638IbnCarabi/0638IbnCarabi.FususHikam/0638IbnCarabi.FususHikam.Kraken21042913-ara1.yml).
In its most recent version, KITAB's OCR pipeline uses Kraken version 3.0.0.0b21.dev6, the Kraken default segmentation model and the 04-01-2021_ArabPersGeneralized.mlmodel transcription model.
Our OCR pipeline outputs plain text files, alto xml files and yml metadata files.
Notwithstanding several automated post-correction steps and greatly improved character accuracy rates, OCR output currently still requires manual post-correction. The latter happens either directly on the plain text files or in [eScriptorium](https://escripta.hypotheses.org/escriptorium-video-gallery).
If post-correction takes place in eScriptorium, the alto xml output is loaded into eScriptorium together with the image files.
This allows not only efficient post-correction but also the creation of further training data, including line and region annotation.
Currently, our OCR pipeline allows OCR'ing Arabic, Persian and, to a lesser extent, Urdu texts.
