---
image: "/images/old_blogs/2020-08-05-Preserving-Pre-Modern-Terminologies//media/image1.png"
header:
  overlay_image: "/images/covers/banner_blog.jpg"
  overlay_filter: 0.1
  caption: "Gentile Bellini - Scribe, 1479-1481 (Image courtesy of [Isabella Stewart Gardner Museum](https://www.gardnermuseum.org/experience/collection/10755), Boston)" 
  show_overlay_excerpt: false 
title: "Preserving Pre-Modern Terminologies"			
author: lorenz_nigst		
layout:		single
categories:
  - 
  - 
tags:
  - corpus
  - 
---
To categorise things is a fundamental human and scholarly instinct and activity. And yet it is one not without obstacles, for we soon learn that the world is more complex than we originally thought or we are confronted with something which refuses to conform to our usual categories. To put it somewhat casually, if our world is populated only by monochrome horses, we probably will have a hard time putting zebras into our usual colour categories – until we make room for them in our classification system. (Of course, even if we fail to do so, we would still be able to pat them on the head and full-heartedly embrace their difference.)

In this blog post, I suggest that similar problems occasionally occur when we try to classify premodern Islamicate texts in our OpenITI/KITAB corpus and when we try to fit certain pieces of information related to them into our existing metadata categories. Many of these texts were produced within intellectual fields with their own distinctive terminologies and practices, which often use terms and refer to activities without equivalent in our contemporary world. This effectively means that our usual categories are on occasion unable to catch differences which they were not made to recognise. (Some more or less extensive periods of head-patting might be necessary here.)

Now, of course, we might simply call a zebra a black horse and ignore the white stripes, but considering the loss of information that this would entail, it is probably not such a good idea. At KITAB, we are convinced that our metadata should, as far as possible, preserve the terminology of our premodern authors and respect distinctions and specificities which they felt were important enough to be reflected in language.

To give a small but illustrative example: In the OpenITI/KITAB corpus, the term *takhrij* often occurs in the context of *mashyakhat* (sg. *mashyakha*), lists of an individual’s shaykhs, in the sense that a particular *mashyakha* is stated to be the ‘*mashyakha* of X, *takhrij* by Y’. For example, our corpus contains the *mashyakha* of Muhammad b. Ibrahim al-Bayani in the *takhrij* of Ibn Rafiʿ al-Sallami. This means that Ibn Rafiʿ al-Sallami contributed to the creation of the *mashyakha* of al-Bayani through an activity called *takhrij* (see below).

[![]({{ "/images/old_blogs/2020-08-05-Preserving-Pre-Modern-Terminologies//media/image1.png" | absolute_url }})]( {{ "/images/old_blogs/2020-08-05-Preserving-Pre-Modern-Terminologies//media/image1.png" | absolute_url }})

Although there is variation with regard to their individual make-up, a *mashyakha* generally is a form of text which mentions the shaykhs of an individual and for each of the shaykhs mentioned adduces one or more Hadiths that were transmitted by him or her.

Such lists of shaykhs may also be termed *muʿjam* (pl. *maʿajim*). A *muʿjam* is essentially the same thing as a *mashyakha*, with the difference that it mostly arranges the shaykhs in alphabetical order.

To a modern reader, this might seem like a strange form of text, but such texts fulfilled clear purposes within the field of knowledge transmission and especially Hadith transmission. They showed the position of an individual within the field and allowed readers to see in condensed form under which scholars that individual had studied and which transmissive chains he therefore ‘owned’. But they also allowed the students of that individual to connect with the same transmissive chains in a structured and efficient way.

But what about this term *takhrij*? To what sort of text and associated practices does it refer and how can we account for its specificities in our metadata?

Grammatically speaking, *takhrij* is the verbal noun of the verb *kharraja*/*yukharriju*, ‘to extract’. In the premodern scholarly social worlds in which the term was used, it clearly refers to a distinct form of scholarly activity.

But what exactly is this activity? While it is not easy to pin down its exact nature, it seems to have been of an essentially compilatory character. It furthermore was something one could do for oneself (‘*kharraja li-nafsihi …*’) or for someone else (‘*kharraja lahu* …’). There are records of siblings engaging in this activity for each other, fathers for their sons, students for their shaykhs and scholarly peers for each other, to name but a few examples. The individual actively engaging in the activity of *takhrij* is referred to as *mukharrij*, whereas the one for whom someone else does so is termed *mukharraj lahu.* It seems that some individuals specialised in this form of activity more than others.[^1] The aforementioned Ibn Rafiʿ al-Sallami is a good example. He is credited with the *takhrij* of more than a dozen *mashyakhat* for others.[^2]

Depending on the structure and content of the individual *mashyakha*, the work involved in its creation must have been a more or less labour-intensive combination of several tasks. The first task involved gathering Hadith material transmitted by the individual shaykhs and the respective transmissive chains by going through one’s own or someone else’s notes, audience certificates and *ijazat* (authorisations to transmit a text; sg. *ijaza*),[^3] making a selection of the gathered material, maybe putting the shaykhs into alphabetical order, maybe adding biographical information for each of them, and so forth.

This essentially compilatory character of the activity is corroborated by other verbs that are used instead of *kharraja*. Apart from the more neutral verb *ʿamila*, ‘to make’, most notable is the verb *jamaʿa*, ‘to gather’. For example, al-Samʿani states that he put together a *muʿjam* for his son (‘*qad kuntu jamaʿtu muʿjam shuyukhihi*’).[^4] Al-Dhahabi refers to this piece of information with the phrase ‘his father produced a *muʿjam* for him’ (‘*ʿamila lahu abuhu muʿjaman*’).[^5]

It is interesting to note that some form of *personal relationship* mostly seems to have played a role when people engaged in this activity for someone else. As has already been pointed out, they put together *mashyakhat/maʿajim* for their kin (even milk relatives[^6]), teachers and peers. Even if someone apparently had to be talked into doing the work, the personal relationship seems to have mattered. An example of the latter case is provided by the introduction to Burhan al-Din al-Jaʿbari’s *Mashyakha al-shamiyya*, which was put together by al-Qasim b. Muhammad al-Birzali (i.e. al-Birzali was the *mukharrij*). Al-Birzali recalls the following in the opening passage of the *mashyakha*:

> He \[Burhan al-Din\] had a *mashyakha* that contained all his shaykhs from Baghdad from whom he transmitted Hadith and that had been put together for him by Jamal al-Din al-Qalanisi and that Hadith students and those who wanted to transmit Hadith (*ṭalabat al-hadith wa-l-raghibuna fi al-riwaya*) read in his presence \[…\]. Then he wanted that another *mashyakha* be put together for him (*yukharraj lahu*) which would contain all his shaykhs from Syria, so that the material transmitted by him and his shaykhs would be more numerous and his students and all those who sought him out, travelled to him and visited him would benefit from that. He wrote to me in that regard and sent a companion of his, who prodded me (*yuharriduni*) into putting together the requested material (*jamʿ al-matlub*).[^7]

The above quotation also illustrates well one purpose of the *mashyakhat*: They showed how each of the shaykhs mentioned in them connected the individual whose *mashyakha* it was (the so-called *sahib al-mashyakha*) to transmissive chains that led all the way to the Prophet and that were needed for the legitimate transmission of knowledge. By the same logic, if the students of the *sahib al-mashyakha* read the *mashyakha* in his presence, they were connected to all of his chains of transmission in a highly efficient and organised way (this, among other motivations that might play a role, explains the interest in large numbers expressed in the above quotation).

But if a *mukharrij* put together a *mashyakha* for someone else, what were the respective contributions of *mukharrij* and *mukharraj lahu*? Who should be considered the ‘author’? Both? Only the *mukharrij*? In the latter case, are we not missing something important in our metadata? And is ‘author’ even a good term to describe this sort of activity?

The question of what the *mukharrij* actually did is not necessarily easy to answer. It is rather fascinating to see how often it puzzles the modern editors of *mashyakhat*, who occasionally state they do not know: ‘As far as the work of the *mukharrij* is concerned, we have no information that would clarify what his work actually consisted in.’[^8] As the editor of al-Subki’s *Muʿjam* suggests, things are even more complicated insofar as the fact that passages are written in the first-person singular does not necessarily mean they were really written by the person they are attributed to. He highlights a passage by al-Dhahabi in which al-Dhahabi writes that the *Muʿjam* of al-Samʿani’s son ʿAbd al-Rahim is ‘his father’s words put in the mouth of ʿAbd al-Rahim’ (‘*wa-huwa kalam abihi ʿala lisan ʿAbd al-Rahim*’).[^9]

To give another example of how difficult it is to determine who did what, the *takhrij* of the *mashyakha* of Muhammad b. al-Anjab al-Naʿʿal is attributed to al-Mundhiri. This much is stated by al-Naʿʿal. But he also writes: ‘Thus I asked God for guidance and put together in this book a large number of the shaykhs who had issued an *ijaza* to me’ (‘*wa-kharrajtu fi hadha al-kitab jumla min mashayikhi al-mujizin*’).[^10] So al-Naʿʿal refers – in the literal sense of the sentence – to himself as engaged in *takhrij*. If so, what role was left to al-Mundhiri, who is explicitly named as the *mukharrij*?

This is not the appropriate place for an extensive study of the practice of *takhrij*. What matters here is that from the perspective of corpus management it would be absurd to build a corpus consisting specifically of Islamicate texts, yet at the same time disregard culturally specific scholarly practices which generate what are unique items of metadata for us. Unless we make use of such terms, we will be turning zebras into black horses.

To an extent, this is what happens in contemporary library catalogues. Thus, with regard to *takhrij* and the distinction in the premodern sources between *mukharrij* and *mukharraj lahu,* the catalogues typically cannot really or fully accommodate the situation created by the premodern scholarly practices.

This may be demonstrated by the two WorldCat entries for al-Bayani’s abovementioned *mashyakha*. In one entry, the work is attributed to Ibn Rafiʿ al-Sallami (i.e. the *mukharrij*); in the other entry, it is attributed to al-Bayani (= Ibn Imam al-Sakhra, i.e. the *mukharraj lahu*).

[![]({{ "/images/old_blogs/2020-08-05-Preserving-Pre-Modern-Terminologies//media/image2.png" | absolute_url }})]( {{ "/images/old_blogs/2020-08-05-Preserving-Pre-Modern-Terminologies//media/image2.png" | absolute_url }})

At KITAB, we are convinced that such information must be recorded in our metadata in a consistent and machine-readable way*.* If our sources tell us that someone acted as a *mukharrij* for someone, we should *always* be able to retrieve the names of both *mukharrij* and *mukharraj lahu*, as well as the fact that they are linked through this particular relationship. We are convinced that being able to search our corpus metadata for information of this kind constitutes real progress in book history, and we are currently working out a system for how to *generally* preserve the premodern terminology we find in our texts and the various relations between texts and persons signified by terms such as *takhrij*, *mukharrij* and *mukharraj lahu*.

Of course, it is not entirely wrong to state that the *mukharrij* is the ‘author’, but it is not entirely right either. Most certainly, such terms force us to be more specific with regard to our notion of authorship, to make room for premodern terminology and to rethink what they meant in the highly specific historical scholarly worlds we are dealing with and in which the terms arose.

From the perspective of corpus management, we must be ready to adapt our metadata categories to accommodate specificities if we become aware of them in the course of research. If we level them, our metadata is much poorer than it has to be. By contrast, preserving them along with the premodern terminologies themselves will lay the foundations for retrieving richer information from our corpus and will allow users to ask different questions.

While none of this can be implemented overnight, it is important to recognise the issue and begin to address it.

[^1]: See the introduction to Taj al-Din ʿAbd al-Wahhab b. ʿAli al-Subki, *Muʿjam al-shuyukh*, *takhrij* Shams al-Din al-Salihi (Beirut, 2004), 15–16.

[^2]: Muhammad b. Ibrahim al-Bayani, *Mashyakhat al-musnid Muhammad b. Ibrahim al-Bayani al-maʿruf bi-Ibn Imam al-Sakhra*, *takhrij* Ibn Rafiʿ al-Sallami (Beirut, 2004), 20–1.

[^3]: For example, Abu ʿAbd Allah Muhammad al-Razi refers to Abu Tahir al-Silafi as the *mukharrij hadhihi al-fawaʾid min masmuʿati*; Abu ʿAbd Allah Muhammad b. Ahmad b. Ibrahim al-Razi, *Mashyakhat al-shaykh al-ajall Abi ʿAbd Allah Muhammad b. Ahmad b. Ibrahim al-Razi al-maʿruf bi-Ibn al-Hattab wa-thabat masmuʿatihi bi-intiqaʾ al-shaykh al-ajall al-imam al-ʿalim al-hafiz Abi Tahir Ahmad b. Muhammad b. Ahmad al-Silafi* (Riyadh, 1994), 100.

[^4]: Abu Saʿd ʿAbd al-Karim b. Muhammad b. Mansur al-Tamimi al-Samʿani, *al-Muntakhab min muʿjam shuyukh al-imam al-hafiz Abi Saʿd ʿAbd al-Karim b. Muhammad b. Mansur al-Samʿani al-Tamimi* (Riyadh, 1996), 112.

[^5]: Shams al-Din Abu ʿAbd Allah Muhammad b. Ahmad al-Dhahabi, *Siyar aʿlam al-nubalaʾ*, ed. Bash­ar ʿAwwad al-Maʿruf and Muhiyy Halal al-Sarhan, vol. 22 (Beirut, 2008), 107.

[^6]: See Ibn al-ʿAttar in al-Nawawi, *al-Ijaz fi sharh sunan Abi Dawud al-Sijistani, wa-fi muqaddimat tahqiqihi Tuhfat al-talibin fi tarjamat al-imam Muhyi al-Din tasnif ʿAlaʾ al-Din ʿAli b. Ibrahim b. al-ʿAttar* (Amman, 2007), 28.

[^7]: Burhan al-Din Abu Ishaq Ibrahim b. ʿUmar b. Ibrahim b. Khalil al-Rabaʿi al-Jaʿbari, *Mashyakha mubaraka shamiyya li-l-shaykh al-imam al-ʿalim al-ʽamil Burhan al-Din Abu Ishaq Ibrahim b. ʿUmar b. Ibrahim b. Khalil al-Rabaʿi al-Jaʿbari al-Shafiʿi nazil balad al-Khalil ʿalayhi al-salam ʿan shuyukhihi al-shamiyyin alladhina ajazu lahu*, *takhrij* al-Qasim b. Muhammad b. Yusuf b. Muhammad al-Birzali, MS Leipzig, Vollers 719-01, fols 2v–3r, available at <https://www.refaiya.uni-leipzig.de/servlets/solr/select?q=%2BobjectType%3A%22islamhs%22+-mymss_ihsstatus%3A%22STAT0001%22+%2B%28allMeta%3A%D9%85%D8%B4%D9%8A%D8%AE%D8%A9+mymss_allmeta_diacr%3A%D9%85%D8%B4%D9%8A%D8%AE%D8%A9%29&XSL.lastPage.SESSION=%2Fsearch_form_islamhs_advanced.xed&fl=id%2CreturnId%2CobjectType&sort=mymss_ihsinvent+asc&version=4.5&mask=search_form_islamhs_advanced.xed&start=0&fl=id,returnId&rows=1&XSL.Style=browse&origrows=25>.

[^8]: Saʾin al-Din Muhammad b. al-Anjab al-Naʿʿal, *Mashyakhat al-Naʿʿal al-Baghdadi*, *takhrij* Rashid al-Din Muhammad b. ʿAbd al-ʿAzim al-Mundhiri (Baghdad, 1975), 22; for a similar statement, see al-Subki, *Muʿjam*, 6.

[^9]: See al-Subki, *Muʿjam*, 6; for the quotation, see Shams al-Din Abu ʿAbd Allah Muhammad b. Ahmad al-Dhahabi, *Tarikh al-islam* (Beirut, 2003), xii, 58.

[^10]: Al-Naʿʿal, *Mashyakha*, 55.
