---
layout: default
title: Home
---
<div class="hero">
  <div class="eyebrow">Python · Artificial Intelligence · Applied Research</div>
  <h1>Research that you can read, reproduce, and run.</h1>
  <p class="lead">Technical notes, practical experiments, and openly available Google Colab notebooks. Each article connects the reasoning, code, and results.</p>
  <p class="actions"><a class="button" href="{{ '/articles/' | relative_url }}">Explore articles</a><a class="button outline" href="{{ '/notebooks/' | relative_url }}">Browse notebooks</a></p>
</div>
<h2>Latest articles</h2>
<div class="grid">
{% for post in site.posts limit:6 %}
  <div class="card"><div class="eyebrow">{{ post.date | date: "%b %d, %Y" }}</div><h3><a href="{{ post.url | relative_url }}">{{ post.title }}</a></h3><p>{{ post.summary | default: post.excerpt | strip_html | truncate: 150 }}</p><a href="{{ post.url | relative_url }}">Read article →</a></div>
{% endfor %}
</div>
<h2>Run the experiments</h2>
<p>Every notebook is linked to its source on GitHub and can be opened directly in Google Colab. See the <a href="{{ '/notebooks/' | relative_url }}">notebook catalog</a>.</p>
