---
author: mathew_barber
categories:
- null
- null
glossary:
- def: A computer algorithm used to detect text reuse in the OpenITI Corpus.
  term: passim
- def: The annotation system used on OpenITI texts, see the documentation for more
    details.
  term: mARkdown
header:
  caption: Gentile Bellini - Scribe, 1479-1481 (Image courtesy of [Isabella Stewart
    Gardner Museum](https://www.gardnermuseum.org/experience/collection/10755), Boston)
  overlay_filter: 0.1
  overlay_image: /images/covers/banner_blog.jpg
  show_overlay_excerpt: false
image: "/images/old_blogs/2020-01-10-When-al-Tabar\u012B-is-Not-(Just)-al-Tabar\u012B\
  --The-Challenges-Posed-by-Composite-Editions-in-the-OpenITI-Corpus//media/image1.jpg"
layout: single
tags:
- corpus
- book-history
- null
title: 'When al-Tabari is Not (Just) al-Tabari: The Challenges Posed by Composite
  Editions in the OpenITI Corpus'

---


In the past few months the KITAB team members have been closely studying the issue of versioning and composite editions in the OpenITI corpus. The problem of versioning is the following: For many of the texts in the corpus we possess multiple versions, often based on various editions. Take, for example, al-Tabari’s *Taʾrikh*, of which there are five versions, based on three editions. A closer study of the data by Sarah Savant has shown that these versions sometimes vary greatly in length. Moreover, the passim outputs suggest that some of these versions vary hugely in content (in extreme cases, the passim results suggest that they might be entirely different works).



This problem relates in part to the existence of composite editions in the corpus. Some of the works in the corpus identified as one book might in fact be several different works collected into one book. For example, if for book X, version A is shorter than version C and version C shares only some of its content with version A, it is possible that version C contains all or part of book X plus another work (see Figure 1 below). There are two ways in which such composite editions may have come into being: (1) they were assembled in the original manuscript or (2) they were assembled by the editor.



[![](/images/old_blogs/2020-01-10-When-al-Tabarī-is-Not-(Just)-al-Tabarī--The-Challenges-Posed-by-Composite-Editions-in-the-OpenITI-Corpus//media/image1.jpg)](/images/old_blogs/2020-01-10-When-al-Tabarī-is-Not-(Just)-al-Tabarī--The-Challenges-Posed-by-Composite-Editions-in-the-OpenITI-Corpus//media/image1.jpg)



Figure 1: Location a composite edition. Box size symbolises book length and the grey indicates text similarity.



The existence of composite editions poses an intellectual challenge as much as it does a practical one. The structure of the OpenITI corpus favours single works written by single authors: the GitHub repositories are ordered by death date of author, then by author, then by work. In such a structure, how does one practically categorise a work that was composed by two authors or that is a composite of two works? One answer is to split the books into their constitutive parts and then categorise each piece by its respective author. Such a response is bound to excite intellectual tensions. If the two works were brought together in a manuscript, then surely separating them is ignoring a valuable stage in the intellectual and transmission history of those two books. We must remember that a key component of KITAB’s research is the study of the transmission and reuse of Arabic texts. Passim outputs have revealed that 21% of Ibn al-Athir’s *al-Kamil fi al-taʾrikh* is from al-Tabari’s *Taʾrikh*, but we would not use this as justification for separating al-Tabari’s *Taʾrikh* from Ibn al-Athir’s work.



Separating works assembled by a modern editor would appear more easily justifiable. However, in the context of a Virtual Reading Room (VRR) such as that produced for the Digital Sirah Project (DSP), even this poses difficult questions. If we state in the Reading Room that the digital text is based on a certain edition, our readers might reasonably expect to find everything that is in the original edition also in the digital one. In fact, KITAB’s current mARkdown policy is to preserve the editor’s structural decisions, and why should their choice of works be an exception? In short, the question of composite editions reaches into the very heart of what we mean by a book and what we mean by book history.



Until recently, I could participate in these debates from the blissful perch of my ivory tower, viewing them an engaging intellectual discussion among the many that we have in the KITAB team. Then, when assembling data on al-Tabari’s *Taʾrikh* for the VRR, I made a discomfiting discovery. As the VRR is concerned with the *Sira* of Ibn Ishaq, one rarely ventures beyond the first three volumes of the *Taʾrikh.* However, the entirety of the work will appear in the VRR, and so the contents pages need to be easy to navigate. As I scrolled through the contents list, one title stood out: ‘Then began the year 380 \[AH\].’ Al-Tabari died in the year 310 AH, so unless he had a less-known sideline in time travel or prophecy, this could not possibly have been written by him. Of course, it transpired that it had not been. In fact, the edition we had chosen for the Digital Sirah Project had three additional works added to the end (two continuations of al-Tabari’s history plus another of al-Tabari’s works). Now we shall have to decide: Should all these texts appear in the VRR? If so, how? As separate works, or clearly indicated in the contents pages for al-Tabari’s *Kitab al-Taʾrikh*?



We had been working intensely with al-Tabari’s *Taʾrikh* for over six months, and no one on the Digital Sirah Project team had spotted it was a composite edition. The oversight illustrates the very scale of KITAB’s endeavour. Al-Tabari’s *Taʾrikh* is a large work, and we are working closely with only the *sira* portions of it. Moreover, the additional three texts are comparatively short, so the word count of the version did not appear suspect (there are many reasons word counts might differ, and many of them are benign, such as writing out of dates – which, over the course of a million-word work, can really add up).



This discovery underlines the importance of formulating specific rules and checks to be applied when texts are prepared for addition to the VRR. In fact, one important output of our work to create the VRR is documentation detailing the process to follow when selecting and preparing texts. The task of organising the corpus and inserting it into the VRR is certainly, therefore, a mammoth one.



Nonetheless, we are learning much about our corpus from this detailed look at individual texts, and there is something exciting about working with a corpus that can so routinely surprise.

