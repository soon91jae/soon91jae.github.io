---
layout: single
permalink: /
title: ""
author_profile: true
redirect_from:
  - /about/
  - /about.html
---

<h1 class="home-title">Sunjae Kwon</h1>

I am a Ph.D. candidate in Computer Science at the **University of Massachusetts Amherst**, advised by **Prof. Hong Yu**. My research lies at the intersection of **natural language processing, machine learning, and healthcare**. I work on lexical semantics and multimodal grounding as well as clinical information extraction, medical language understanding, and computational approaches to healthcare research.

Previously, I was an AI Research Scientist at **KAIST** and **UNIST**, and an AI Research Intern at **Tencent America**. I received my M.S. and B.S. in Computer Science from **Sogang University**.

<p class="profile-links"><a href="mailto:sunjaekwon@umass.edu">Email ↗</a><a href="https://scholar.google.com/citations?user=N9ZM-CIAAAAJ&amp;hl=en">Google Scholar ↗</a><a href="https://github.com/soon91jae">GitHub ↗</a><a href="/cv/">Curriculum Vitae ↗</a></p>

## Research

My current interests include:

- **Language understanding:** lexical semantics, word sense disambiguation, grounding, and large language models.
- **Clinical natural language processing:** medical jargon, clinical concepts, behavioral information extraction, and patient education.
- **Medical informatics:** modeling risk factors from electronic health records and making clinical AI more interpretable and useful.

## Selected Publications <span class="section-aside"><a href="/publications/">Full list →</a></span>

{% assign featured_titles = "ODD: A Benchmark Dataset for the Natural Language Processing Based Opioid Related Aberrant Behavior Detection|Vision Meets Definitions: Unsupervised Visual Word Sense Disambiguation Incorporating Gloss Information|MedJEx: A Medical Jargon Extraction Model with Wiki's Hyperlink Span and Contextualized Masked Language Model Score|Word Sense Disambiguation Based on Word Similarity Calculation Using Word Vector Representation from a Knowledge-Based Graph|A Robust Named-Entity Recognition System Using Syllable Bigram Embedding with Eojeol Prefix Information" | split: "|" %}
<div class="paper-list paper-list--featured">
{% for title in featured_titles %}
  {% assign paper = site.data.papers | where: "title", title | first %}
  {% if paper %}
    <article class="paper-entry">
      <div class="paper-title"><span class="paper-number">[{{ paper.number }}]</span> {% if paper.paper %}<a href="{{ paper.paper }}">{{ paper.title }}</a>{% else %}{{ paper.title }}{% endif %}</div>
      <div class="paper-authors">{{ paper.authors | replace: 'Sunjae Kwon', '<strong>Sunjae Kwon</strong>' }}</div>
      <div class="paper-meta"><span class="venue">{{ paper.venue }}</span><span class="paper-year">{{ paper.year }}</span>{% if paper.paper %}<a class="paper-link" href="{{ paper.paper }}">Paper ↗</a>{% endif %}{% if paper.code %}<a class="paper-link" href="{{ paper.code }}">Code ↗</a>{% endif %}{% if paper.poster %}<a class="paper-link" href="{{ paper.poster }}">Poster ↗</a>{% endif %}</div>
    </article>
  {% endif %}
{% endfor %}
</div>

<p class="updated-note"><strong>*</strong> Equal first-author contribution.</p>

## Academic Service

I regularly review for conferences and journals in natural language processing, machine learning, and healthcare informatics. See my [Academic Service](/service/) page for details.

<p class="updated-note">For a complete and updated publication record, please visit <a href="https://scholar.google.com/citations?user=N9ZM-CIAAAAJ&amp;hl=en">Google Scholar</a>.</p>
