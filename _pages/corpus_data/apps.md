---
layout: splash
header:
  overlay_image: /images/covers/banner_data.png
  overlay_filter: rgba(40, 99, 165, 0.45)
  caption: "A visualisation comparing text reuse between a pair of works"
  actions:
    - label: "Learn more about the Corpus and Data"
      url: /corpus
title: "Our applications"

corpus_app:
  - image_path: /images/covers/corpus_app.png
    alt: "placeholder image 2"
    title: "The Corpus data application"
    excerpt: 'Do you want to explore data relating to our corpus metadata? <br><br> Check back here soon to try our latest app!'
    url: "#test-link"
    btn_label: "Corpus App - coming soon..."
    btn_class: "btn--primary"
metadata_app:
  - image_path: /images/covers/web_app.png
    alt: "placeholder image 2"
    title: "The KITAB web application"
    excerpt: 'Looking for a particular book to download in our corpus? Wanting to explore text reuse? <br><br> Search for books and view text reuse visualisations using the KITAB web application.'
    url: "https://kitab-project.org/explore"
    btn_label: "Explore the corpus"
    btn_class: "btn--primary"
diff_viewer:
  - image_path: /images/apps/diff_square_cropped.png
    alt: "A text pair aligned through the diff viewer"
    title: "The diff viewer"
    excerpt: "An application that allows you to see the differences between two related pieces of text. It is used primarily to read passim outputs, but it can be used with any two (relatively short) pieces of related text."
    url: "https://kitab-project.org/diffViewer/"
    btn_label: "Use the diff viewer"
    btn_class: "btn--primary" 
coming_soon:
  - image_path: /images/kitab/textalignment.png
    alt: "placeholder image 2"
    title: "Coming soon..."
    excerpt: 'Interested in exploring our other datasets? KITAB will be releasing more data and applications soon.<br><br> Subscribe to be notified when new applications are added to the portal.'
    url: "/subscribe"
    btn_label: "Subscribe for updates"
    btn_class: "btn--primary"

permalink: /data/apps
---
Welcome to KITAB's application portal. All of our latest applications can be accessed through this site. You can use them to explore our many data sets, in particular our text reuse data. For guidance on how to use the different applications, please visit our [visualisations page]({{ 'data/viz' | relative_url }}). As we are still refining our applications, we have yet to release many of them to the public, but we look forward to sharing them with you soon!


{% include feature_row id="metadata_app" type="left" %}


{% include feature_row id="diff_viewer" type="right" %}
{% include feature_row id="coming_soon" type="left" %}
