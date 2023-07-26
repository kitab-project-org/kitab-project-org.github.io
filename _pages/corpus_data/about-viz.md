---
excerpt:	""
header:
  overlay_image: /images/covers/banner_data.png
  overlay_filter: rgba(40, 99, 165, 0.45)
  caption: "A visualisation comparing text reuse between a pair of works"
title:		"About our visualisations"
layout:		single
sidebar:
  nav: "corpus"
toc: true
toc_sticky: true
permalink: /data/viz

---
KITAB's [data sets]({{ '/data' | relative_url }}) are often large and difficult to comprehend. KITAB is, therefore, working to develop and adapt visualisations to help the team and other researchers understand the data. Where relevant we release code and Power BI templates for our visualisations, enabling you to adapt them for your own research, whether or not you are using KITAB's data.
There is a set of core visualisations that we use routinely in our research and reference in our blog posts and publications. This page explains how those visualisations work and how they should be interpreted. For detailed instructions on how to use the applications, please visit our [docs]({{ "docs/openITI" | relative_url }}).
**Please note:** This list of visualisations and applications is being continually updated as we formalise and release our applications. If you are unsure about any of the visualisations used in a publication or a blog post we recommend you return here.
{: .notice--warning}
To access and use our applications and visualisations, please visit the [applications portal]({{ 'data/apps' | relative_url }}).
## The pairwise text reuse visualisation
This application is designed for viewing text reuse between pairs of texts. Image 1 shows a screen grab from the main part of the visualisation.

{% capture image1 %}
[![Pairwise visualisation]({{ "/images/methods/pair-wise-Nujum-Kamil.png" | absolute_url }})]( {{ "/images/methods/pair-wise-Nujum-Kamil.png" | absolute_url }})
Image 1: A pairwise visualisation comparing Ibn Taghribirdi's *Nujum* (on the top) with Ibn al-Athir's *Kamil* (on the bottom).
{% endcapture %}
<div class="notice--primary">
{{ image1 | markdownify }}
</div>
This visualisation layers many types of data. Put simply, it represents each of the two works as a scroll laid on its side, with the top on the left, the bottom on the right and each line containing 300 words (marked on the y-axis). Along the x-axis, each work is divided into milestones (on text reuse and milestones, see our explanation of the [passim algorithm]({{ '/methods/text-reuse#how-does-passim-work' }})). Thus, the top graph in image 1 shows Ibn Taghribirdi's (d. 1470) *Nujum*, and 1 represents the first milestone in the book while 3,745 represents the last milestone. The bottom graph in image 1 shows Ibn al-Athir's (d. 1234) *Kamil*; 1 is the first milestone in the book and 4,500 is the last.
Text passages that are common to both works are highlighted in red. Each of the red bars in the top and bottom graphs represents a milestone that contains text reuse. The height of the bar is determined by the position and length of the reused text within the milestone. For example, a bar that starts at 50 and ends at 100 on the y axis means that the reuse occurs between word 50 and word 100 of that 300-word milestone and that it the reused passage is, therefore, fifty words long.
The yellow lines link the reused passages in the two works. For example, text found around milestone 700 of Ibn al-Athir's *Kamil* (the bottom graph) is reused at milestone 1 of Ibn Taghribirdi's *Nujum*. The yellow lines allow us to understand rearrangement of the text. In the case of Image 1, we can see that the text is reused in almost the same order, but in condensed form. As both works are chronicles, this is to be expected.
Had the text been rearranged, more lines would cross over each other. See, for example, Image 2, which compares al-Tabari's *Taʾrikh* with Ibn Hanbal's (d. 855) *Musnad*. There we can see heavy reuse of the early parts of al-Tabari's work (the parts that cover the Prophet's life) by Ibn Hanbal, but because the *Musnad* is not a chronological account, the text has been rearranged and the lines cross over.
{% capture image2 %}
[![Another pairwise visualisation]({{ "/images/methods/pair-wise-Tarikh-Musnad.png" | absolute_url }})]( {{ "/images/methods/pair-wise-Tarikh-Musnad.png" | absolute_url }})

Image 2: A pairwise visualisation comparing al-Tabari's *Taʾrikh* (on the top) with Ibn Hanbal's *Musnad* (on the bottom). {% endcapture %}
<div class="notice--primary">
{{ image2 | markdownify }}
</div>

We often provide screen captures of such visualisations in our publications to illustrate our discussions of book history. They are, however, part of an interactive visualisation. In the interactive visualisation, clicking on the yellow line linking the two passages will bring up the relevant text and provide the context in each of the two works, allowing you to read and understand the particular reuse instance.

As we have are still refining this visualisation, we are yet to release it to the public. We look forward to sharing it with you soon!
## More explanations of our core visualisations coming soon ...
Return here to see explanations of our new applications, including* the corpus statistics application* the corpus text reuse statistics application* the book DNA explorer.
