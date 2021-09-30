---
image: "/images/old_blogs/2021-01-21-Diversifying-the-OpenITI-corpus,-One-Text-at-a-Time//media/image1.jpg"
header:
  overlay_image: "/images/covers/banner_blog.jpg"
  overlay_filter: 0.1
  caption: "Gentile Bellini - Scribe, 1479-1481 (Image courtesy of [Isabella Stewart Gardner Museum](https://www.gardnermuseum.org/experience/collection/10755), Boston)" 
  show_overlay_excerpt: false 
title: "Diversifying the OpenITI corpus, One Text at a Time"			
author: gowaart_van_den_bossche		
layout:		single
categories:
  - 
  - 
tags:
  - corpus
  - book-history
  - reg-syr-arab
  - book-forms
  - 

---
The vast majority of texts in the OpenITI corpus were sourced from three major collections of digital texts originally prepared by organisations based in the Middle East (see Peter Verkinderen’s excellent blog post on the largest of them, [Shamela](http://kitab-project.org/2020/12/03/al-maktaba-al-shamila-a-short-history/)). These collections have proven invaluable to researchers, not least because they have facilitated digital forms of analysis, but they all entailed choices about which textual materials should belong on their platforms and which should not. Shamela, for example, did not originally include any poetry and focused largely on Sunni traditionalism. Another significant omission in each of these collections is the rich corpus of Arabic texts written by and for non-Muslims.

While it would be naive to think that OpenITI is itself unbiased, we do aim to be as inclusive as possible and try to address several of the issues found in other collections. First, we bring the separate collections together and engage all of them in a continuous dialogue on text reuse. Second, we identify and try to fill gaps in the corpus through digitising texts ourselves or through collaborating with other research teams. This has led to the inclusion of texts digitised by other academic projects in fields that are of only marginal interest to the major text collections. Thanks to the concerted efforts of Peter Verkinderen and Lorenz Nigst, we now have a number of agrarian treatises, Greco-Arabic philosophical materials and texts of ancient wisdom, as well as some materials preserved in the so-called Cairo Geniza. We list all these various collections and individual contributors with their URI identifiers [here](https://github.com/OpenITI/Annotation).

In the meantime, I have also contributed a number of texts I am interested in by using Optical Character Recognition software, typing up manuscript treatises and contacting people who have published texts online. To encourage people to contribute materials they may have to our corpus, I will here briefly describe a small set of texts I have contributed to the OpenITI in this way. If readers of this blog feel inclined to contribute textual materials in exchange for text reuse data, they should get in contact with KITAB team members and we will happily accept their offers.

[![](/images/old_blogs/2021-01-21-Diversifying-the-OpenITI-corpus,-One-Text-at-a-Time//media/image1.jpg)](/images/old_blogs/2021-01-21-Diversifying-the-OpenITI-corpus,-One-Text-at-a-Time//media/image1.jpg)

Some time ago I was researching historical accounts about a Mamluk expedition against the Nusayri-ʿAlawis in the Lebanese Kisrawan region (the rugged mountain terrain north and northeast of Beirut) which took place in 704/1304. To my pleasant surprise, I found a number of Maronite sources that discuss these events. One of these was a type of text I had not encountered before in my readings of Arabic literature: an epic poem in the z*ajaliyya* form written by the Maronite bishop Jibraʾil Ibn al-Qilaʿi (d. 921/1516). Ibn al-Qilaʿi had been instrumental in spreading adherence to the Catholic Pope amongst Maronites in the region of present-day Lebanon, thus strengthening the full communion with Rome which the Maronite Church still follows.[^1] The poem is usually referred to as *Madiha fi Jabal Lubnan*, and it describes acts of heroic resistance against outsiders by Maronite chiefs from the dawn of time up to the bishop’s own day. It consists of 294 quatrains, of which the first three hemistiches rhyme with each other and the fourth ends on a monorhyme sustained throughout the entire poem. While there are many Arabic poems discussing or commenting on historical events, they do not tend to be narrative in the way an epic poem usually is. Ibn al-Qilaʿi’s work, by contrast, is highly narrative, if not in a linear chronological way. Furthermore, Ibn al-Qilaʿi’s introductory verses express some interesting ideas about time, history and memory which I am hoping to unpack more in further research. Consider, for example, this quatrain, which seems to conceive of an important role for poets in preserving cultural memory:

> ما كان يخبر عنه انسان \* وكيف العصور بتتغير   \*   وفيها العقول بتتحير  \*  ولولا توجد في الاسطار  
>
> How the ages change
>
> while intellects get confused
>
> if it weren’t for you finding in the lines of text
>
> what informs man about himself

Because of its relatively short length I decided to digitise this poem by using Google’s OCR engine, which can be used via Google Drive. The added personal benefit is that by post-correcting the digital text I am effectively skim reading it as a whole, familiarising myself with its structure and identifying interesting sections to return to in more detail. Ibn al-Qilaʿi’s text was edited by Bulus Qaraʾli in 1937 as part of his book *Hurub al-muqaddamin* (‘The wars of the \[Maronite\] commanders’), a blend of primary texts and commentary by Qaraʾli on the Maronite community’s vicissitudes in dealing with their surroundings across the ages. Because of this hybrid publication form, digitising this edition posed a number of challenges and obliged me to make some editorial choices. We always record these kinds of decisions in a so-called yml file, a specific format of markup language which we use to record various forms of metadata in a formalised and computer-readable way. We use three forms of such files: one for author metadata (which includes an author’s birth and death date and various geographical locations, as well as personal relationships), one for general book metadata (including, among others, variant titles and relationships to other books) and one for version metadata. Below is an example of my version metadata for Ibn al-Qilaʿi’s *Madiha*:

00\#VERS\#CLENGTH\#\#: 20224

00\#VERS\#LENGTH\#\#\#: 4673

00\#VERS\#URI\#\#\#\#\#\#: 0921JibrailIbnQilaci.MadihaFiJabalLubnan.GVDB20200821-ara1

80\#VERS\#BASED\#\#\#\#: http://www.worldcat.org/oclc/784489194

80\#VERS\#COLLATED\#: http://www.worldcat.org/oclc/784489194

80\#VERS\#LINKS\#\#\#\#: https://www.noor-book.com/كتاب-حروب-

    المقدمين-1075-1450-pdf-1593183859

90\#VERS\#ANNOTATOR: Gowaart Van Den Bossche

90\#VERS\#COMMENT\#\#: `This text was digitised with Google OCR and corrected by Gowaart. I have followed the edition's lack of consistently noting the hamza and using a generic ha instead of ta ``marbuta``. The edition of the text is somewhat complicated. It interlaces the poem included here with a 19th-``century anonymous ``mukhtasar`` (see ``Salibi``, "Maronite Historians of Medieval Lebanon", p. 39) as well as a commentary by the editor. For ``OpenITI`` purposes I felt it was best to separate these three`` ``layers, and`` assign separate URIs to the poem and the ``mukhtasar``, while`` ``deleting the editorial commentary. I have also deleted the titles, as these seem to be part of the commentary rather than the poem. As a ``result`` the pagination looks like the text has gaps, but this is entirely due to my reorganisation of the texts. The poem is a ``zajaliyya`` in Lebanese colloquial. This poetic form is in quatrains, as opposed to the`` ``usual Arabic two ``hemistiches``. Currently ``mARkdown`` does not accommodate this form (in which the first three ``hemistiches`` rhyme with one another, while the last hemistich follows the ``endrhyme`` of each other quatrain in the poem), so I have followed some other editors of other texts by splitting the quatrain into two parts. This way it looks identical to other Arabic poetry, except that the end rhyme only happens every two lines.` 90\#VERS\#DATE\#\#\#\#\#: 2020-08-21

90\#VERS\#ISSUES\#\#\#: NO\_MAJOR\_ISSUES

See Hamidreza’s blog post for another example of a yml file and some discussion of how it should be used within the [OpenITI annotation process](http://kitab-project.org/2020/06/12/tagging-the-structure-of-texts-in-the-openiti-corpus/). 

Having grown interested in Ibn al-Qilaʿi (a more malignant observer might say I fell down a substantial rabbit hole), I did some further research and stumbled upon the Academia page of the Lebanese cleric P. Elie Saade. He has edited a few *zajaliyya*s he found in manuscripts across his home country and published them on his page. I contacted him directly to ask whether he would want to contribute his editions to the OpenITI, something he happily agreed to do. Consequently, we were able to add one more poem written by Ibn al-Qilaʿi (a hagiography of the third-century saint Mar Nuhra) to our corpus, as well as a nineteenth-century *zajaliyya* by a Lebanese priest. Saade had transcribed both of these into Arabic script from the Karshuni (Arabic in Syriac script) originals in which they have been preserved. He has also since then notified me of another *zajaliyya* he has published which deals with the experience of the First World War in Lebanon. I hope to add this text to the corpus in the near future. You can find the OpenITI versions of the two first texts through the links below. Note the ‘PES + date’ at the end of the URI: this identifies P. Elie Saade as the contributor to the corpus. Note also that in the above-cited yml file the URI bears my initials, GVDB, as I was the one who digitised this text through OCR. In this way we keep track of the diverse origins of text versions in our corpus while harmonising their contents as much as possible. 

[0921JibrailIbnQilaci.QissatMarNuhra.PES20201020-ara1](https://github.com/OpenITI/0925AH/tree/master/data/0921JibrailIbnQilaci/0921JibrailIbnQilaci.QissatMarNuhra)

[1337IstifanThani.Zajaliyya.PES20201021-ara1](https://github.com/OpenITI/1350AH/tree/master/data/1337IstifanThani/1337IstifanThani.Zajaliyya)

Through such additions our corpus becomes a little more balanced, but these are of course only small steps towards capturing the true diversity of the Arabic written tradition. There is still a lot of work to be done to achieve a more rounded balance in the corpus. Indeed, three new Christian Arabic texts within a corpus of some 5,000 individual texts is but a drop in an Islamic ocean. It will also come as no surprise that neither of these three texts showcases a lot (if any) reuse. The one case of reuse identified by passim for Ibn al-Qilaʿi is from a late nineteenth-century compendium of Christian Arabic texts compiled by the great Jesuit Chaldean Catholic scholar Louis Cheikho (d. 1927), in which a number of verses from the *Madiha* are directly quoted. Even fully capturing the relatively minor *zajaliyya* tradition poses further challenges. Because they are generally seen as of limited literary value (Kamal Salibi called Ibn al-Qilaʿi’s poems ‘dull’) and because of their highly regional character, only very few of these texts have been edited and published. As noted, the majority exist only in manuscripts written in Karshuni, so it requires people fluent in both scripts to properly transcribe and edit them. They are also largely written in colloquial Arabic. This issue of script and language is another aspect we would like our metadata to reflect better, especially as more Geniza materials (much of which are written in Judaeo-Arabic, that is, Arabic written in Hebrew script) will be added to the corpus in the future. 

What I wanted to highlight more generally is that pooling the various resources of Arabic texts increasingly available online into one harmonised corpus is all well and good, but if we want to really remedy major gaps and issues we also need concerted efforts from scholars to identify gaps in the corpus and to actively curate and contribute materials. Here are a few ways in which you can get involved:

1.  If you notice that relevant texts/genres/… are missing in our corpus, we can show you how to add these texts yourself (or you can simply notify us that we should include them, especially if you can propose a way to acquire them in digital format).

2.  If you are a specialist, you could become a curator of texts in your field, identifying gaps, creating lists of texts to be digitised, and so on.

3.  Inform us about other projects that have digitised texts that may not be in our corpus.

The photograph used in this blog post was taken by Gowaart in May 2017 in one of the Maronite monasteries in the beautiful Kadisha Valley below Bsharré in North Lebanon.

[^1]: The most comprehensive treatment of Ibn al-Qilaʿi remains K. S. Salibi, *Maronite Historians of Medieval Lebanon* (Beirut, 1959).
