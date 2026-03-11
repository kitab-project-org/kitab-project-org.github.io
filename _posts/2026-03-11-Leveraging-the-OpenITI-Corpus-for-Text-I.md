---
author: lorenz_nigst
header:
  caption: Gentile Bellini - Scribe, 1479-1481 (Image courtesy of [Isabella Stewart
    Gardner Museum](https://www.gardnermuseum.org/experience/collection/10755), Boston)
  overlay_filter: 0.1
  overlay_image: /images/covers/banner_blog.jpg
  show_overlay_excerpt: false
image: /images/blogs/2026-03-11/Leveraging-the-OpenITI-Corpus-for-Text-Ilorenz_nigst/media/image1.jpg
layout: single
tags:
- corpus
title: 'Leveraging the OpenITI Corpus for Text Identification: Two Examples from Geniza
  Documents'

---
Among many other things, the steadily growing OpenITI corpus of machine-actionable texts constitutes a useful tool for identifying hitherto unidentified text passages, or at least shedding *some* light on them.

In this brief blog post, I will take a look at two examples of unidentified poetic texts found on Geniza fragments. More specifically, I would like to underscore the usefulness of leveraging the corpus *as a corpus* which is tantamount to saying that it sometimes is helpful to glide over the totality of the OpenITI corpus and take a closer look at the subset of titles resulting from such corpus-wide searches instead of merely using the corpus as a practical point of access to individual texts. Needless to say, enabling different forms of leveraging the corpus *as a corpus* is the reason why we have been building the OpenITI corpus in the first place.

The two examples of unidentified text on which I shall focus below can demonstrate this with particular clarity insofar as both of them have to do with text passages that, in different ways, do *not* form part of the OpenITI corpus (not least a reminder that building the OpenITI corpus very much is an ongoing project). Using the corpus as a mere point of access to the respective texts therefore is not even an option.

The first example concerns (fragments of) a number of verses from the diwan of al-Mutanabbī (d. 354/965) which are *not* included in the version of Mutanabbī's diwan currently found in the OpenITI corpus (0354Mutanabbi.Diwan.JK007610-ara1) but which can be found in print editions of the former. The second example concerns what seems to be a commentary of Abū Tammām's (d. 231/845) *Ḥamāsa*. The *Ḥamāsa* currently also does not form part of the OpenITI corpus.

Nonetheless, leveraged *as a corpus*, the OpenITI corpus allows zeroing in on the hitherto unidentified text fragments in a relatively straightforward way and knowing something more about them.

# **Example \# 1:**

[\[John Rylands Library, University of Manchester, JRL Gaster ar. 373. Available online through the Princeton Geniza Project at https://geniza.princeton.edu/documents/33068/, accessed February 25, 2026.\]]{.mark}

The first [example]](https://geniza.princeton.edu/en/documents/33068/) (JRL Gaster ar. 373 1) [is described as follows on the Princeton Geniza Project site:]{.mark}

> ['Unidentified text in Arabic script. Part or all of it looks like poetry. Ruling regarding bathing according to Islamic jurisprudence on verso.']{.mark}

The text found on the document indeed is poetry but poetry is found on both recto and verso. The recto side contains verses by al-Waʾwāʾ al-Dimashqī (d. appr. 385/995), a part of which also occurs in Ibn Zurayq (d. 420/1029):

[![]({{ "/images/blogs/2026-03-11/Leveraging-the-OpenITI-Corpus-for-Text-Ilorenz_nigst/media/image1.jpg" | absolute_url }})]({{ "/images/blogs/2026-03-11/Leveraging-the-OpenITI-Corpus-for-Text-Ilorenz_nigst/media/image1.jpg" | absolute_url }})

**أستودع الله في بغداد لي** قمرا // بالكرخ **من** **فلك الأزرار مطلعه**

**ودعته وبودي** **أن** تودع**ني** // **روح الحياة وأني لا أودعه**

**و**ك**م** تشب**ث** بي **يوم** **الرحيل** ضحى // **وأدمعي مستهلات وأدمعه**

**وكم تشفع في** **أن لا أفا**رقه // وللضرورة حال لا تشفعه

The verso side, on which I shall focus in this first example, contains fragments of verses by al-Mutanabbī (d. 354/965):

[![]({{ "/images/blogs/2026-03-11/Leveraging-the-OpenITI-Corpus-for-Text-Ilorenz_nigst/media/image2.jpg" | absolute_url }})]({{ "/images/blogs/2026-03-11/Leveraging-the-OpenITI-Corpus-for-Text-Ilorenz_nigst/media/image2.jpg" | absolute_url }})

**وأما وحقك** **وهو** غاية مقسم // لل**حق أنت وما سواك** الباطل

ال**طيب** أنت إذا **أصابك** طيبه // **والماء أنت إذا اغتسلت الغاسلوا**

**ما دار في الحنك اللسان وقلبت** // **قل**ما بأحسن ما ثناك أنامل

As has already been said further above, while these verses are *not* contained in the current OpenITI version of al-Mutanabbī's diwan which has been sourced from the *Jāmiʿ al-kabīr* collection (see 0354Mutanabbi.Diwan.JK007610-ara1, ms24), their identification nonetheless is relatively straightforward if we glide over the entire corpus and benefit from the resulting bird's eye view.

For example, if we search the OpenITI corpus for the phrase *ightasalta l-ghāsilū* (see the left end of the second line on JRL Gaster ar. 373 1 / verso), we get the following list of titles:

**اغتسلت الغاسل**

|  |  |
|-------------------------------------------------------------|-----------|
| <mark style="background-color:green">0392IbnCabdCazizJurjani.Wisata.JK010638-ara1</mark> | 1402 |
| <mark style="background-color:green">0392IbnCabdCazizJurjani.Wisata.JK010638-ara1</mark> | 5830 |
| <mark style="background-color:green">0429AbuMansurThacalibi.MutanabbiWaMaLahu.Shamela0037032-ara1.completed</mark> | 974 |
| 0429AbuMansurThacalibi.YatimatDahr.Shamela0006743-ara1.mARkdown | 3062 |
| <mark style="background-color:green">0449AbuCalaMacarri.MucjizAhmad.JK010753-ara1</mark> | 9017 |
| <mark style="background-color:green">0449AbuCalaMacarri.MucjizAhmad.JK010753-ara1</mark> | 9018 |
| <mark style="background-color:green">0468IbnAhmadWahidiNaysaburi.SharhDiwanMutanabbi.JK010754-ara1</mark> | 7289 |
| 0471CabdQahirJurjani.DalailIcjaz.JK001019-ara1 | 1313 |
| <mark style="background-color:green">0492AbuMurshidMacarri.TafsirAbyat.JK010780-ara1</mark> | 3861 |
| <mark style="background-color:green">0492AbuMurshidMacarri.TafsirAbyat.JK010780-ara1</mark> | 3862 |
| 0710IbnAydamurMustacsimi.DurrFarid.Sham19Y0020762-ara1 | 26255 |
| 0710IbnAydamurMustacsimi.DurrFarid.Sham19Y0020762-ara1 | 86513 |
| <mark style="background-color:green">0975BakathirHadrami.TanbihAdib.ShamAY0034457-ara1</mark> | 2294 |
| <mark style="background-color:green">1073YusufBadiciDimashqi.SubhMunabbi.JK010778-ara1</mark> | 4442 |

This strongly, and more or less immediately, indicates a link with al-Mutanabbī insofar as seven out of the ten works where the phrase occurs have an explicit connection with al-Mutanabbī's poetry or diwan in the sense that they are commentaries or similar (see the titles marked in green). Thus, even if the verses in question are missing from the OpenITI version of al-Mutanabbī's diwan, leveraging the corpus *as a corpus* successfully allows us to bring *other works* into sight that contain the respective verses, most notably different commentaries, which as a subset shine a light on the phrase.

That the verses indeed belong to al-Mutanabbī's diwan can be confirmed by consulting other versions / editions of the diwan than the one currently in the OpenITI corpus. For example, if we look at the last three verses on page 80 [here](https://archive.org/details/ar107diwan14/page/n179/mode/2up) or the first three verses on page 114 [here](https://www.digitale-sammlungen.de/view/bsb10249668?page=274%2C275), the verses found on JRL Gaster ar. 373 1 / verso are all there.

# **Example \# 2:**

\[Jewish Theological Seminary Library, ENA 3977.3. Available online through the Princeton Geniza Project at https://geniza.princeton.edu/documents/10852/, accessed February 25, 2026.\]

The second example is provided by the document Jewish Theological Seminary Library ENA 3977.3, likewise accessible through the Princeton Geniza Project.

The available [description](https://geniza.princeton.edu/en/documents/10852/) of the fragment states the following:

> 'Literary work in Arabic script. Lexicographic? Citing aphorisms and verses of poetry, and seems to be explaining the usage of *aʿwar*.'

The fragment indeed contains the verses of poetry and the particular lexicographical explanation referred to in the above description (see the last line of the page below: *wa-yuqālu aʿwara l-rajul*):

[![]({{ "/images/blogs/2026-03-11/Leveraging-the-OpenITI-Corpus-for-Text-Ilorenz_nigst/media/image3.jpg" | absolute_url }})]({{ "/images/blogs/2026-03-11/Leveraging-the-OpenITI-Corpus-for-Text-Ilorenz_nigst/media/image3.jpg" | absolute_url }})

However, even regular close-reading tells us that more is going on in this fragment. Thus, for example, other lexemes apart from *muʿwir* are explained (see *wiṭāb*); on the recto side, one finds a brief introduction to the poem.

But can we find out more about the fragment than close-reading can tell us if we again leverage the OpenITI corpus *as a corpus*? That is, can a structured bird's eye view on the corpus-wide occurrences of the verses found in the document perhaps again shed some additional light on the text fragment and lead the way?

Before putting the rule to the test, it is important to underline that the [order](https://geniza.princeton.edu/en/documents/10852/) in which the images are provided by the Princeton Geniza Project unfortunately is somewhat misleading here. This insofar as the page shown in the image which currently comes in second place (ENA 3977.3 2) visibly has sewing stations on the *right* side which would seem to indicate that it corresponds to the recto side, hence must come first in terms of the reading order whereas ENA 3977.3 1, where the holes are found on the *left* side and which would seem to indicate verso, must come second in the reading order.

So, let us start with image ENA 3977.3 2:

[![]({{ "/images/blogs/2026-03-11/Leveraging-the-OpenITI-Corpus-for-Text-Ilorenz_nigst/media/image4.jpg" | absolute_url }})]({{ "/images/blogs/2026-03-11/Leveraging-the-OpenITI-Corpus-for-Text-Ilorenz_nigst/media/image4.jpg" | absolute_url }})

If we conduct a corpus-wide search for the half verse **ولم يستشر في أمره غير نفسه** occurring in the first line on the page, the following OpenITI titles figure among the search results, given here with the number of the line in which the phrase occurs in the respective OpenITI text file:

​​

|  |  |
|-----------------------------------------------------------|--------|
| 0562IbnHamdun.TadhkiraHamduniyya.JK009325-ara1 | 11506 |
| <mark style="background-color:yellow">0328IbnCabdRabbih.CiqdFarid.Shamela0023789-ara1.completed</mark> | 15122 |
| <mark style="background-color:green">0421IbnMuhammadMarzuqi.SharhDiwanHamasa.Shamela0026536-ara1.completed</mark>  | 967 |
| <mark style="background-color:green">0467AbuQasimFarisi.SharhHamasa.Sham19Y0016435-ara1</mark>  | 318 |
| 0609AbuCabbasJarrawi.HamasaMaghribiyya.JK006908-ara1 | 3462 |
| 0656IbnAbiHadid.SharhNahjBalagha.Shia002185Vols-ara1.completed | 18884 |
| 0692IbnCabdZahir.RawdZahir.GVDB20200120-ara1.mARkdown | 1508 |
| <mark style="background-color:blue">0702IbnCabdRahmanCubaydi.TadhkiraSacdiyya.JK010743-ara1</mark>  | 186 |
| <mark style="background-color:purple">0710IbnAydamurMustacsimi.DurrFarid.Sham19Y0020762-ara1</mark>  | 54093 |
| <mark style="background-color:yellow">0718AbuIshaqWatwat.GhurarKhasais.Shamela0001349-ara1.mARkdown</mark>  | 8931 |
| 1041Maqqari.NafhTib.Shamela0001002-ara1.completed | 41743 |
| <mark style="background-color:darkgreen">1093CabdQadirBaghdadi.KhizanatAdab.JK007143-ara1</mark>  | 59601 |

If we move further down, the next verse, which occurs after a brief introduction which attributes it to Taʾabbaṭa Sharran and gives some context, starts with the half verse

**إذا المرء لم يحتل وقد جد جده**

If we again conduct a corpus-wide search for this phrase, we get the following list of titles, again given here with the respective line numbers:

|  |  |
|--------------------------------------------------------------|-------|
| <mark style="background-color:red">0001TaabbataSharran.Diwan.JK007513-ara1 | 116 |
| <mark style="background-color:yellow">0328IbnCabdRabbih.CiqdFarid.Shamela0023789-ara1.completed | 15279 |
| 0362AbuFarajIsbahani.Aghani.JK000927-ara1.completed | 60951 |
| 0362AbuFarajIsbahani.Aghani.JK000927-ara1.completed | 129493 |
| <mark style="background-color:green">0421IbnMuhammadMarzuqi.SharhDiwanHamasa.Shamela0026536-ara1.completed | 978 |
| <mark style="background-color:green">0467AbuQasimFarisi.SharhHamasa.Sham19Y0016435-ara1 | 327 |
| <mark style="background-color:green">0502IbnCaliTabriziShaybani.DiwanHamasa.JK001099-ara1 | 389 |
| 0521MuhammadHamadhani.TakmilatTarikhTabari.Shamela0009783BK3-ara1.completed | 5572 |
| 0654SibtIbnJawzi.MiratZaman.Sham19Y0023644-ara1 | 118739 |
| 0659SadrDinBasri.Hamasa.JK006907-ara1 | 820 |
| 0685IbnSacidMaghribi.NashwatTarab.Shamela0028174-ara1.completed | 6583 |
| 0685SadidDinMuhallabi.MuthallathatLughawiyya.ShamAY0037030-ara1 | 71 |
| <mark style="background-color:blue">0702IbnCabdRahmanCubaydi.TadhkiraSacdiyya.JK010743-ara1 | 197 |
| <mark style="background-color:purple">0710IbnAydamurMustacsimi.DurrFarid.Sham19Y0020762-ara1 | 10102 |
| <mark style="background-color:yellow">0718AbuIshaqWatwat.GhurarKhasais.Shamela0001349-ara1.mARkdown | 9531 |
| 0743SharafDinTibi.FutuhGhayb.Sham19Y0020891-ara1 | 15177 |
| 0761JamalDinIbnHisham.TakhlisShawahid.Sham19Y0017916-ara1 | 4066 |
| 0855BadrDinCayni.MaqasidNahwiyya.Sham19Y0016714-ara1 | 13084 |
| 0855BadrDinCayni.MaqasidNahwiyya.Sham19Y0016714-ara1 | 30086 |
| 0911Suyuti.SharhShawahidMughni.Sham19Y0017724-ara1 | 17394 |
| <mark style="background-color:blue">1093CabdQadirBaghdadi.KhizanatAdab.JK007143-ara1 | 55986 |
| 1093CabdQadirBaghdadi.SharhAbyatMughni.Sham19Y0150966-ara1 | 54670 |

The two lists above are interesting insofar as there clearly is some overlap, meaning, there are several works in which both verses occur. Even more interestingly, several of these titles (see the ones marked in green) have a relation with Abū Tammām's *Ḥamāsa*. This link with the *Ḥamāsa* becomes even stronger if we take a closer look at the one *Ḥamāsa-*related work missing from the first list (0502IbnCaliTabriziShaybani.DiwanHamasa.JK001099-ara1). Upon closer inspection, we can see that the half-verse

**ولم يستشر في أمره غير نفسه**

occurs as the variant

**ولم يستشر في رأيه غير نفسه**

here (see line 382 of 0502IbnCaliTabriziShaybani.DiwanHamasa.JK001099-ara1), Thus, if we factor in this variant reading, 0502IbnCaliTabriziShaybani.DiwanHamasa.JK001099-ara1 also figures on the first list.

Given this strong presence of *Ḥamāsa-*related works on the two lists, is it perhaps the case that the fragment Jewish Theological Seminary Library, ENA 3977.3 has something to do with Abū Tammām's *Ḥamāsa*?

If we zoom in on Abū Tammām's *Ḥamāsa,* this hypothesis can be corroborated insofar as the succession of verses found in the *Ḥamāsa* manifestly corresponds to the succession of verses found on JewishTheological Seminary Library, ENA 3977.3 on the condition that we read the images in the correct order as suggested above.

Thus, the first two lines of ENA 3977.3 2 (see below) correspond to the last verse of a poem by Saʿd b. Nāshib:

**ولم يستشر في أمره غير نفسه** // **ولم يرض إلا قايم السيف صاحبا**

[![]({{ "/images/blogs/2026-03-11/Leveraging-the-OpenITI-Corpus-for-Text-Ilorenz_nigst/media/image4.jpg" | absolute_url }})]({{ "/images/blogs/2026-03-11/Leveraging-the-OpenITI-Corpus-for-Text-Ilorenz_nigst/media/image4.jpg" | absolute_url }})

Afterwards, there is an introductory transition to a poem by Taʾabbaṭa Sharran (*'wa-qāla Taʾabbaṭa Sharran'*). The latter sets in with:

**إذا المرء لم يحتل وقد جدّ جدّه // أضاع وقاسى أمره وهو مدبر**

This exactly corresponds to the succession of verses found in the *Ḥamāsa* (see, for example, [here](https://gallica.bnf.fr/ark:/12148/btv1b11002868p/f6.item.r=%D8%A7%D9%84%D8%AD%D9%85%D8%A7%D8%B3%D8%A9.zoom) (last line on the right side and second line on the left side) and [here](https://gallica.bnf.fr/ark:/12148/btv1b11002888h/f6.item.r=%D8%A7%D9%84%D8%AD%D9%85%D8%A7%D8%B3%D8%A9) (third line from the bottom right and last line on the right). It is plausible that the same succession of verses also occurs in commentaries of the *Ḥamāsa* (see, for example, [al-Tibrīzī's *sharḥ*](https://archive.org/details/3907pdf_202001/page/n59/mode/2up), pp. 60--61).

This succession of verses also is corroborated by the numbers of the lines in which the two verses occur in the OpenITI text files, and which are given next to the titles in the two lists above. If we zoom in on these lines numbers, we can see clearly that the two verses for which we searched occur in close proximity precisely in *those* texts that are commentaries of Abū Tammām's *Ḥamāsa*.

> **First list = occurrences of ولم يستشر في أمره غير نفسه**
>
> 0421IbnMuhammadMarzuqi.SharhDiwanHamasa.Shamela0026536-ara1.completed: 967
>
> 0467AbuQasimFarisi.SharhHamasa.Sham19Y0016435-ara1: 318
>
> 0502IbnCaliTabriziShaybani.DiwanHamasa.JK001099-ara1: 382

>
> **Second list = occurrences of إذا المرء لم يحتل وقد جدّ جدّه**
>
> 0421IbnMuhammadMarzuqi.SharhDiwanHamasa.Shamela0026536-ara1.completed: 978
>
> 0467AbuQasimFarisi.SharhHamasa.Sham19Y0016435-ara1: 327
>
> 0502IbnCaliTabriziShaybani.DiwanHamasa.JK001099-ara1: 389

As can be seen, in the case of all three commentaries, there are some ten lines between the two verses, which suits a commentary which adds some text between the verses it explains (967:978; 318:327; 382:389). For other titles that also occur on both lists, that clearly is *not* the case and there is no comparable proximity. For example, in 0710IbnAydamurMustacsimi.DurrFarid.Sham19Y0020762-ara1, the first verse we searched for occurs in line 54093, the second one in line 10102, that is, very far apart from each other.

The tentative link of the fragment Jewish Theological Seminary Library, ENA 3977.3 with Abū Tammām's *Ḥamāsa* is further corroborated by the fact that al-ʿUbaydī's (d. 8^th^/14^th^ century) *Tadhkira al-saʿdiyya* figures on both lists given above (see 0702IbnCabdRahmanCubaydi.TadhkiraSacdiyya.JK010743-ara1 highlighted in blue). As is well known, Abū Tammām's *Ḥamāsa* is one of three *ḥamāsāt* which were ingested by al-ʿUbaydī in his *Tadhkira* ('*aqdamtu ʿalā khtiyār mā huwa nafīs al-maʿnā...min al-ḥamāsāt al-thalātha allatī waqaʿat ilayya: ḥamāsat Abī Tammām...wa-ḥamāsat Abī Hilāl...wa-ḥamāsat...Ibn Fāris'*, p. 42).

Against this backdrop, and with the suggested correct reading order (ENA 3977.3 2, ENA 3977.3 1), the situation already is much clearer: The fragment contains verses that also occur in Abū Tammām's *Ḥamāsa* (see the black lines below), and their succession exactly corresponds to the succession in which they occur in Abū Tammām's *Ḥamāsa*. Interspersed are all sorts of explanations, ranging from lexicographical explanations to a brief allusion to the context of Taʾabbaṭa Sharran's poem (see the red lines below):

[![]({{ "/images/blogs/2026-03-11/Leveraging-the-OpenITI-Corpus-for-Text-Ilorenz_nigst/media/image4.jpg" | absolute_url }}){: style="max-width:50%"}]({{ "/images/blogs/2026-03-11/Leveraging-the-OpenITI-Corpus-for-Text-Ilorenz_nigst/media/image4.jpg" | absolute_url }})[![]({{ "/images/blogs/2026-03-11/Leveraging-the-OpenITI-Corpus-for-Text-Ilorenz_nigst/media/image3.jpg" | absolute_url }}){: style="max-width:50%"}]({{ "/images/blogs/2026-03-11/Leveraging-the-OpenITI-Corpus-for-Text-Ilorenz_nigst/media/image3.jpg" | absolute_url }})

**ولم يستشر في أمره غير نفسه** // **ولم يرض إلا قايم السيف صاحبا**

**وقال**{: "style="color:red}

**تأبط شرا وكان خرج يشتار عسلا**{: "style="color:red}

**فوافته لحيان وهو في الغار فأرسل**{: "style="color:red}

**ما كان معه من العسل على الجبل وأنج\[...\]**{: "style="color:red}

**عليه ففاتهم**{: "style="color:red}

**إذا المرء لم يحتل وقد جد جده** // **أضاع وقاسى أمره وهو مدبر**

**لكن أخو الحزم الذي ليس نازلا** // **به الخطب إلا وهو للقصد مبصر**

**فذاك قريع الدهر ما** عاش **حول** // **إذا سد منه منخر جاش منخر**

**حول شديد الحيل**{: "style="color:red}

**أقول للحيان وقد صفرت لهم // وطابي ويومي ضيق الجحر معور**

**الوطاب زقاق اللبن وصفرت خلت**{: "style="color:red}

**وهو مثل هاهنا وإنما يريد أنه قد**{: "style="color:red}

**بدت لهم مقاتله أي لم يبق لي حيل**{: "style="color:red}

**وقيل أمل وقيل أراد خلا قلبي**{: "style="color:red}

**من ودهم ويقال أعور الرجل**{: "style="color:red}

The above strongly indicates that this fragment indeed corresponds to a fragment of a commentary on Abū Tammām's *Ḥamāsa*. The text on the fragment sets in with the last verse of a poem by Saʿd b. Nāshib for which no lexical explanations are given. It then moves on to a poem by Taʾabbaṭa Sharran, to which it gives a brief introduction and through which it then moves until it runs into a lexeme or a phrase considered to require an explanation. The commentary is short and minimal, but it clearly appears to be falling back on other existing commentaries of the same poem.

Even if we currently do not have, and perhaps will never have, a text in the OpenITI corpus that *exactly* corresponds to what is found on Jewish Theological Seminary Library, ENA 3977.3, the structured recourse to the OpenITI corpus outlined above can clearly contribute to expanding our knowledge regarding this Geniza document. Leveraging the corpus *as a corpus* again has led the way and has allowed us to see more.

**Literature**

Muḥammad b. ʿAbd al-Raḥmān al-ʿUbaydī, *al-Tadhikra al-saʿdiyya* *fī l-ashʿār al-ʿarabiyya*, ed. ʿAbd Allāh al-Jabbūrī (Baghdād: Maktabat al-Ahliyya, 1972).
