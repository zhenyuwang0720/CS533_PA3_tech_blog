---
layout: default
title: Notebooks
permalink: /notebooks/
---
# Run the notebooks
Each file is stored in this GitHub repository. **Open in Colab** creates an editable session in your own Google environment; it does not modify the original repository.
<div class="grid">
{% for item in site.data.notebooks %}
<div class="card"><div class="eyebrow">Jupyter / Google Colab</div><h3>{{ item.title | escape }}</h3><p>{{ item.description | escape }}</p>
<a class="button" href="https://colab.research.google.com/github/{{ site.github_username }}/{{ site.repository_name }}/blob/main/{{ item.path }}">Open in Colab ↗</a>
<a class="button outline" href="https://github.com/{{ site.github_username }}/{{ site.repository_name }}/blob/main/{{ item.path }}">View .ipynb</a>
</div>
{% endfor %}
</div>
<p class="muted">To add a notebook, upload a <code>.ipynb</code> file into <code>notebooks/</code> and commit it to <code>main</code>. GitHub Actions rebuilds this catalog automatically.</p>
