---
author: peter_verkinderen
categories:
- null
- null
glossary:
- def: a csv ('Comma Separated Values') file is a plain text file containing data
    in a table. Each row in the table starts on a new line, and columns are separated
    using a comma (sometimes another character like a tab).
  term: csv
header:
  caption: Gentile Bellini - Scribe, 1479-1481 (Image courtesy of [Isabella Stewart
    Gardner Museum](https://www.gardnermuseum.org/experience/collection/10755), Boston)
  overlay_filter: 0.1
  overlay_image: /images/covers/banner_blog.jpg
  show_overlay_excerpt: false
image: /images/old_blogs/2021-07-13-A-Token-Frequency-Counter-For-OpenITI-Texts//media/image1.png
layout: single
tags:
- viz
- null
title: A Token Frequency Counter For OpenITI Texts

---


One of the participants in our [KITAB user group](http://kitab-project.org/2020/07/24/call-for-participation/) asked for an easy way to find out which are the most frequently used words in a text.



There are quite a lot of online tools that allow you to upload a file (or provide a link to a web page) and will produce a nice table with word counts.



Unfortunately, this specific user group participant works with the largest text in the KITAB corpus, Ibn al-ʿAsakir’s [*Taʾrikh madinat Dimashq*](https://raw.githubusercontent.com/OpenITI/0575AH/master/data/0571IbnCasakir/0571IbnCasakir.TarikhDimashq/0571IbnCasakir.TarikhDimashq.JK000916-ara1.mARkdown), which weighs in at about 75 MB in the OpenITI version, and none of the sites I tried out was willing to accept such a large file. Others failed to produce a frequency list even with smaller books, probably because they don’t deal well with Arabic.



There are a number of other options to create frequency lists from a text, but most involve using a programming language such as Python or R. Since most of our user group participants do not have any background in programming, we thought about using this question as an opportunity to show the user group how to install Python or R and run a simple script to create the frequency list (for example, using the fantastic R stylo library).



However, even demonstrating something simple like this to people who do not have Python or R installed and are working on different platforms always takes quite some time, time we didn’t have during our user group meeting.



So, after getting frustrated with a number of websites that promise to convert a text into a frequency list, I decided to build such an online tool for OpenITI myself.



This was quite straightforward because I could build on work we have done for our [OpenITI Python library](https://pypi.org/project/openiti/) and other subprojects.



The tool can be found [here](https://openiti.github.io/tokenFrequency/).



 



 [![]({{ "/images/old_blogs/2021-07-13-A-Token-Frequency-Counter-For-OpenITI-Texts//media/image1.png" | absolute_url }})]( {{ "/images/old_blogs/2021-07-13-A-Token-Frequency-Counter-For-OpenITI-Texts//media/image1.png" | absolute_url }})



 



In its simplest form, you upload a text and get a table with token frequency counts in return. You can browse through the table online or download it as a csv file (by clicking ‘Download table as csv file’ at the top of the table) that you can import into a spreadsheet program.



[![]({{ "/images/old_blogs/2021-07-13-A-Token-Frequency-Counter-For-OpenITI-Texts//media/image2.png" | absolute_url }})]( {{ "/images/old_blogs/2021-07-13-A-Token-Frequency-Counter-For-OpenITI-Texts//media/image2.png" | absolute_url }})



An additional advantage of building such a tool yourself is that you can customise it to your own wishes. I added a number of options I would personally find useful:



-   a minimum limit for the number of times a token needs to be in the text for it to be included in the table



-   a list of ‘stop words’ – that is, tokens to be excluded from the count



-   an option to define what the tool must consider a token. By default, it considers any sequence of Arabic-script characters a token (see below for a full list of these characters). You can also provide your own definition of what characters should be considered a token by providing a regular expression of your own. (Note for those who know about this type of stuff: Javascript’s regular-expression engine is used for the tokenisation, so `MARKDOWN_HASHa9611d04392ad1acb0cd7642a0e405dfMARKDOWN_HASH` refers only to ASCII word characters.)



-   an option to split off a metadata header, so that words that are not really part of the text are not counted in. By default, the OpenITI metadata header is split off from the main body of the text, but you can also provide a regular expression of your own to split off headers that are delimited in another way.



[![]({{ "/images/old_blogs/2021-07-13-A-Token-Frequency-Counter-For-OpenITI-Texts//media/image3.png" | absolute_url }})]( {{ "/images/old_blogs/2021-07-13-A-Token-Frequency-Counter-For-OpenITI-Texts//media/image3.png" | absolute_url }})



This was a really quick build; if you would find more options useful, don’t hesitate to contact me!



**A cautionary note about tokens**



The tool extracts ‘tokens’ from the text and counts them. The word ‘token’ is frequently used as a synonym for ‘word’, but they are not exactly the same. A token is nothing more than a sequence of characters, in our case defined by default as an unbroken sequence of Arabic-script characters, bounded on either side by characters that do not belong to that list of characters (there are other ways to define tokens as well). The tool does not try to analyse this sequence of characters as a word with a specific meaning, a specific form of a specific verb or the like.



For example, the token <span dir="rtl">ولكتابه</span> (*wa-li-kitabi-hi*, ‘and for his book’) could be considered four separate words, but the tool considers it one token. The opposite is also true: the name ʿAbd Allah is written in Arabic using two separate tokens (in our definition), ʿAbd and Allah, and both are thus counted separately.



Moreover, the plural of <span dir="rtl">كتاب</span> *kitab* is <span dir="rtl">كتب</span> *kutub*, and both are considered (and counted as) separate tokens by the tool, although they are arguably the same word. This problem is compounded with verbs, since Arabic expresses their number, gender, tense and so on using prefixes and suffixes. Each form of the same verb is thus considered a separate token.



This means that if you’re interested in how many times an author used a specific ‘word’ in the text, you may have to sum up a large number of different versions of the word.



For example, if we want to know how many times Ibn ʿAsakir uses the word *kitab* in his *Taʾrikh madinat Dimashq*, we could try to sum up the counts for these tokens:



count | token 
||
3560 | <span dir="rtl">كتب</span> 
2585 | <span dir="rtl">كتاب</span> 
1805 | <span dir="rtl">كتابه</span> 
1320 | <span dir="rtl">الكتاب</span> 
1204 | **<span dir="rtl">فكتب</span>** 
1111 | **<span dir="rtl">وكتب</span>** 
492 | <span dir="rtl">كتابا</span> 
278 | <span dir="rtl">بكتاب</span> 
276 | <span dir="rtl">الكتب</span> 
263 | **<span dir="rtl">كتبه</span>** 
196 | <span dir="rtl">كتابي</span> 
150 | <span dir="rtl">كتابيهما</span> 
108 | <span dir="rtl">بالكتاب</span> 
103 | **<span dir="rtl">كتبنا</span>** 
96 | **<span dir="rtl">كتبهم</span>** 
91 | **<span dir="rtl">وكتبه</span>** 
87 | <span dir="rtl">كتابك</span> 
87 | **<span dir="rtl">كتبا</span>** 
81 | <span dir="rtl">وكتاب</span> 
50 | <span dir="rtl">بكتابه</span> 
47 | <span dir="rtl">لكتاب</span> 
40 | <span dir="rtl">والكتاب</span> 
39 | <span dir="rtl">كتبي</span> 
35 | **<span dir="rtl">كتبها</span>** 
29 | <span dir="rtl">بكتب</span> 
27 | <span dir="rtl">كتابنا</span> 
20 | **<span dir="rtl">وكتبنا</span>** 
20 | <span dir="rtl">كتابها</span> 
19 | **<span dir="rtl">فكتبه</span>** 
19 | <span dir="rtl">الكتابين</span> 
16 | <span dir="rtl">بالكتب</span> 
15 | <span dir="rtl">بكتابك</span> 
14 | **<span dir="rtl">فكتبنا</span>** 
13 | <span dir="rtl">كتابهم</span> 
12 | <span dir="rtl">بكتابي</span> 
12 | **<span dir="rtl">فكتبها</span>** 
11 | <span dir="rtl">ولكتابه</span> 
10 | **<span dir="rtl">كتبك</span>** 
10 | <span dir="rtl">كتابكم</span> 
9 | <span dir="rtl">كتابهما</span> 
9 | <span dir="rtl">للكتب</span> 
9 | <span dir="rtl">والكتب</span> 
8 | **<span dir="rtl">كتبكم</span>** 
7 | **<span dir="rtl">وكتبا</span>** 
7 | <span dir="rtl">وكتبهم</span> 
6 | **<span dir="rtl">فكتبا</span>** 
6 | <span dir="rtl">وكتابه</span> 
6 | <span dir="rtl">كتابين</span> 
5 | <span dir="rtl">لكتابه</span> 
5 | <span dir="rtl">بكتبه</span> 
4 | <span dir="rtl">للكتاب</span> 
4 | <span dir="rtl">فالكتاب</span> 
4 | <span dir="rtl">وكتابا</span> 
4 | **<span dir="rtl">وكتبها</span>** 
4 | <span dir="rtl">لكتبه</span> 
4 | <span dir="rtl">بكتابة</span> 
4 | <span dir="rtl">لكتب</span> 
4 | <span dir="rtl">وبكتاب</span> 
3 | <span dir="rtl">بكتابهم</span> 
3 | <span dir="rtl">وبالكتاب</span> 
3 | <span dir="rtl">وبكتابك</span> 
3 | **<span dir="rtl">وكتبهما</span>** 
3 | <span dir="rtl">بكتبي</span> 
3 | <span dir="rtl">وكتابي</span> 
3 | <span dir="rtl">أفبكتاب</span> 
2 | **<span dir="rtl">كتبهن</span>** 
2 | <span dir="rtl">وكتبي</span> 
2 | <span dir="rtl">والكتابان</span> 
2 | <span dir="rtl">فكتاب</span> 
2 | <span dir="rtl">بكتابين</span> 
2 | <span dir="rtl">بكتبك</span> 
2 | <span dir="rtl">كتابان</span> 
2 | <span dir="rtl">أكتاب</span> 
2 | <span dir="rtl">وبكتابه</span> 
2 | <span dir="rtl">كالكتاب</span> 
2 | ***<span dir="rtl">قرأالكتاب</span>*** 
2 | <span dir="rtl">وكتابها</span> 
1 | **<span dir="rtl">الكتبا</span>** 
1 | <span dir="rtl">وكتابهم</span> 
1 | <span dir="rtl">وكتابك</span> 
1 | <span dir="rtl">والكتابين</span> 
1 | <span dir="rtl">بكتبكم</span> 
1 | **<span dir="rtl">كتباه</span>** 
1 | <span dir="rtl">بكتابكم</span> 
1 | <span dir="rtl">بالكتابين</span> 
1 | <span dir="rtl">كتابى</span> 
1 | **<span dir="rtl">وكتبك</span>** 
1 | <span dir="rtl">الكتبات</span> 
1 | ***<span dir="rtl">قرأكتاب</span>*** 
1 | <span dir="rtl">الكتابان</span> 
1 | **<span dir="rtl">أقرألكتاب</span>** 
1 | <span dir="rtl">ككتابكم</span> 
1 | <span dir="rtl">فكتابك</span> 
1 | ***<span dir="rtl">تصنيفكتاب</span>*** 
1 | **<span dir="rtl">والكتبا</span>** 
1 | ***<span dir="rtl">بهذاالكتاب</span>*** 
1 | ***<span dir="rtl">كتابنه</span>*** 
1 | ***<span dir="rtl">واكتابي</span>*** 
1 | ***<span dir="rtl">فقرأكتاب</span>*** 
1 | <span dir="rtl">ولكتابك</span> 
1 | ***<span dir="rtl">وإنماالكتاب</span>*** 
1 | <span dir="rtl">لكتابك</span> 



But even that approach is not always successful. For example, the word *kataba* (‘he wrote’) and the word *kutub* (‘books’) are clearly separate words, but they are written in exactly the same way in unvocalised Arabic (<span dir="rtl">كتب</span>) and are thus considered to be one token, and counted as such.



It is impossible to know from the frequency list how often the token <span dir="rtl">كتب</span> refers to a book and how often to the act of writing. By way of illustration, I have marked in bold the cases in the table where there is uncertainty over whether the verb or the noun is used.



The example also shows another use case for such frequency lists: it shows a number of tokens that are clearly errors in the text, often due to the omission of a space (marked in bold and italics in the table); these all appear only once or twice in the text. Combining such frequency information for all texts in the corpus could give us an idea of what tokens in our texts are likely to be errors and should be flagged as such. We are currently experimenting with the use of such frequency lists of single tokens (and of token bigrams – combinations of two adjacent tokens) extracted from the entire OpenITI corpus for identifying possible OCR mistakes in texts produced by the [OCR](https://medium.com/@openiti/openiti-aocp-9802865a6586) pipeline we are setting up to get additional texts into the corpus. More about this in a later blog post!



**Appendix: list of Unicode characters**



By default, the tool considers any sequence of the following unicode characters a token:



-   <span dir="rtl">ء</span> ARABIC LETTER HAMZA



-   <span dir="rtl">آ</span> ARABIC LETTER ALEF WITH MADDA ABOVE



-   <span dir="rtl">أ</span> ARABIC LETTER ALEF WITH HAMZA ABOVE



-   <span dir="rtl">ؤ</span> ARABIC LETTER WAW WITH HAMZA ABOVE



-   <span dir="rtl">إ</span> ARABIC LETTER ALEF WITH HAMZA BELOW



-   <span dir="rtl">ئ</span> ARABIC LETTER YEH WITH HAMZA ABOVE



-   <span dir="rtl">ا</span> ARABIC LETTER ALEF



-   <span dir="rtl">ب</span> ARABIC LETTER BEH



-   <span dir="rtl">ة</span> ARABIC LETTER TEH MARBUTA



-   <span dir="rtl">ت</span> ARABIC LETTER TEH



-   <span dir="rtl">ث</span> ARABIC LETTER THEH



-   <span dir="rtl">ج</span> ARABIC LETTER JEEM



-   <span dir="rtl">ح</span> ARABIC LETTER HAH



-   <span dir="rtl">خ</span> ARABIC LETTER KHAH



-   <span dir="rtl">د</span> ARABIC LETTER DAL



-   <span dir="rtl">ذ</span> ARABIC LETTER THAL



-   <span dir="rtl">ر</span> ARABIC LETTER REH



-   <span dir="rtl">ز</span> ARABIC LETTER ZAIN



-   <span dir="rtl">س</span> ARABIC LETTER SEEN



-   <span dir="rtl">ش</span> ARABIC LETTER SHEEN



-   <span dir="rtl">ص</span> ARABIC LETTER SAD



-   <span dir="rtl">ض</span> ARABIC LETTER DAD



-   <span dir="rtl">ط</span> ARABIC LETTER TAH



-   <span dir="rtl">ظ</span> ARABIC LETTER ZAH



-   <span dir="rtl">ع</span> ARABIC LETTER AIN



-   <span dir="rtl">غ</span> ARABIC LETTER GHAIN



-   <span dir="rtl">ف</span> ARABIC LETTER FEH



-   <span dir="rtl">ق</span> ARABIC LETTER QAF



-   <span dir="rtl">ك</span> ARABIC LETTER KAF



-   <span dir="rtl">ل</span> ARABIC LETTER LAM



-   <span dir="rtl">م</span> ARABIC LETTER MEEM



-   <span dir="rtl">ن</span> ARABIC LETTER NOON



-   <span dir="rtl">ه</span> ARABIC LETTER HEH



-   <span dir="rtl">و</span> ARABIC LETTER WAW



-   <span dir="rtl">ى</span> ARABIC LETTER ALEF MAKSURA



-   <span dir="rtl">ي</span> ARABIC LETTER YEH



-   <span dir="rtl">ً</span> ARABIC FATHATAN



-   <span dir="rtl">ٌ</span> ARABIC DAMMATAN



-   <span dir="rtl">ٍ</span> ARABIC KASRATAN



-   <span dir="rtl">َ</span> ARABIC FATHA



-   <span dir="rtl">ُ</span> ARABIC DAMMA



-   <span dir="rtl">ِ</span> ARABIC KASRA



-   <span dir="rtl">ّ</span> ARABIC SHADDA



-   <span dir="rtl">ْ</span> ARABIC SUKUN



-   <span dir="rtl">ٰ</span> ARABIC LETTER SUPERSCRIPT ALEF



-   <span dir="rtl">ـ</span> ARABIC TATWEEL



-   <span dir="rtl">٠</span> ARABIC-INDIC DIGIT ZERO



-   <span dir="rtl">١</span> ARABIC-INDIC DIGIT ONE



-   <span dir="rtl">٢</span> ARABIC-INDIC DIGIT TWO



-   <span dir="rtl">٣</span> ARABIC-INDIC DIGIT THREE



-   <span dir="rtl">٤</span> ARABIC-INDIC DIGIT FOUR



-   <span dir="rtl">٥</span> ARABIC-INDIC DIGIT FIVE



-   <span dir="rtl">٦</span> ARABIC-INDIC DIGIT SIX



-   <span dir="rtl">٧</span> ARABIC-INDIC DIGIT SEVEN



-   <span dir="rtl">٨</span> ARABIC-INDIC DIGIT EIGHT



-   <span dir="rtl">٩</span> ARABIC-INDIC DIGIT NINE



-   <span dir="rtl">ٮ</span> ARABIC LETTER DOTLESS BEH



-   <span dir="rtl">ٹ</span> ARABIC LETTER TTEH



-   <span dir="rtl">پ</span> ARABIC LETTER PEH



-   <span dir="rtl">چ</span> ARABIC LETTER TCHEH



-   <span dir="rtl">ژ</span> ARABIC LETTER JEH



-   <span dir="rtl">ک</span> ARABIC LETTER KEHEH



-   <span dir="rtl">گ</span> ARABIC LETTER GAF



-   <span dir="rtl">ی</span> ARABIC LETTER FARSI YEH



-   <span dir="rtl">ے</span> ARABIC LETTER YEH BARREE



-   <span dir="rtl">۱</span> EXTENDED ARABIC-INDIC DIGIT ONE



-   <span dir="rtl">۲</span> EXTENDED ARABIC-INDIC DIGIT TWO



-   <span dir="rtl">۳</span> EXTENDED ARABIC-INDIC DIGIT THREE



-   <span dir="rtl">۴</span> EXTENDED ARABIC-INDIC DIGIT FOUR



-   <span dir="rtl">۵</span> EXTENDED ARABIC-INDIC DIGIT FIVE



-   <span dir="rtl">۶</span> EXTENDED ARABIC-INDIC DIGIT SIX



-   <span dir="rtl">۷</span> EXTENDED ARABIC-INDIC DIGIT SEVEN



-   <span dir="rtl">۸</span> EXTENDED ARABIC-INDIC DIGIT EIGHT



-   <span dir="rtl">۹</span> EXTENDED ARABIC-INDIC DIGIT NINE



-   <span dir="rtl">۰</span> EXTENDED ARABIC-INDIC DIGIT ZERO

