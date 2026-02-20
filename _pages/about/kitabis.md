---
excerpt:	""
header:
  overlay_image: /images/covers/banner_about2.jpg
  overlay_filter: 0.1
  caption: "Scholars study together (Image from a manuscript of al-Hariri's *Maqamat*, courtesy of the [BNF](https://gallica.bnf.fr/ark:/12148/btv1b8422962f/f14.item.r=maqamat.zoom#))"
author: "sarah_savant"
layout:		single

title:		"The KITABis"
sidebar:
  nav: "about"
toc : true
toc_sticky : true

permalink: /about/kitabis
---

{% assign profiles = site.data.authors %}

{% for full_profile in profiles %}
  {% assign profile = full_profile[1] %}
  {% if profile.kitabi %}
   
    {% if profile.avatar %}
      {% if profile.name %}
        {% assign name = profile.name %}
        {% assign image = profile.avatar %}
        {% if profile.bio_long %}

### {{name}}
![{{name}}]({{image | absolute_url}}){: .align-left} 
{{ profile.bio_long }}
        
        {% elsif profile.bio %}

### {{name}}
![{{name}}]({{image | absolute_url}}){: .align-left} 
{{ profile.bio_long }}

        {% endif %}
      {% endif %}
    {% endif %}
  {% endif %}
{% endfor %}


