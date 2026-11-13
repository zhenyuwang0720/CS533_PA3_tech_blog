---
layout: default
title: Articles
permalink: /articles/
---
# Technical articles
Full write-ups of experiments, with methods, code, charts, results and limitations.
<div class="grid">
{% for post in site.posts %}
<div class="card"><div class="eyebrow">{{ post.date | date: "%b %d, %Y" }}</div><h3><a href="{{ post.url | relative_url }}">{{ post.title }}</a></h3><p>{{ post.summary }}</p></div>
{% endfor %}
</div>
