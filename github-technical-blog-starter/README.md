# Technical Research Notes

**Python • Artificial Intelligence • Data Science • Reproducible Experiments**

Welcome to my technical blog and open notebook collection. This repository follows the **technical write-up + reproducible notebook + research figures** organization of [a GitHub research write-up](https://github.com/junzhuang-code/potential_defi_tokens), with a GitHub Pages blog added.

🌐 **Website:** https://YOUR_GITHUB_USERNAME.github.io/  
📓 **Notebook catalog:** https://YOUR_GITHUB_USERNAME.github.io/notebooks/

## Articles

| Article | Focus | Companion notebook |
| --- | --- | --- |
| [A Reproducible Python Data Analysis Workflow](_posts/2026-11-13-reproducible-python-analysis.md) | Pandas, rolling mean, plotting | [Open in Colab](https://colab.research.google.com/github/YOUR_GITHUB_USERNAME/YOUR_GITHUB_USERNAME.github.io/blob/main/notebooks/example_analysis.ipynb) |

## Research write-up structure

Each article should contain:

1. **Introduction** — context and the research question
2. **Dataset** — data provenance, assumptions and preparation
3. **Methodology** — algorithms, baselines, and experimental setup
4. **Results** — evaluation tables, plots, and reproducible observations
5. **Discussion** — limitations and interpretation
6. **Conclusion** — findings, future work, and notebook links

## Example notebook

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/YOUR_GITHUB_USERNAME/YOUR_GITHUB_USERNAME.github.io/blob/main/notebooks/example_analysis.ipynb)

The example uses synthetic data and does not claim real-world results.

## Add your own Google Colab notebook

1. In Colab, use **File → Download → Download .ipynb** (or **File → Save a copy in GitHub** if you have authorized GitHub integration).
2. In GitHub, open the `notebooks/` directory, choose **Add file → Upload files**, and upload the `.ipynb` file.
3. Commit the changes to the `main` branch. The Pages workflow regenerates the notebook catalog automatically.
4. For a full research article, copy the example file in `_posts/` to a new `YYYY-MM-DD-title.md` and edit its front matter and contents. Set `notebook: notebooks/your_file.ipynb` to add buttons automatically.

**Important:** Before publishing, remove API keys, private data, account details, and any saved notebook outputs that should not be public. Check that file paths work in a fresh Colab runtime.

## Publish the website

1. Create a **public** GitHub repository named `YOUR_GITHUB_USERNAME.github.io`, replacing the placeholder with your actual GitHub username.
2. Upload the **contents** of this template to the repository root (do not put everything inside another folder).
3. Globally replace `YOUR_GITHUB_USERNAME` in the files with your real username (including `_config.yml` and `README.md`).
4. On GitHub open **Settings → Pages** and set **Source: GitHub Actions**. GitHub Actions should be enabled for the repository.
5. Under **Actions**, run the *Publish technical blog* workflow if it has not run already. Once deployment succeeds, open `https://YOUR_GITHUB_USERNAME.github.io/`.

**Alternative repo name:** For a project repository called `technical-blog`, set `_config.yml` to `baseurl: "/technical-blog"` and `repository_name: "technical-blog"`; the deployed site will be `https://YOUR_GITHUB_USERNAME.github.io/technical-blog/`.

## Directory layout

```text
├── .github/workflows/pages.yml    # Automatic GitHub Pages deployment
├── _config.yml                    # Site options and GitHub username
├── _layouts/                     # Page and post layouts
├── _posts/                       # Technical blog articles
├── _data/notebooks.json          # Auto-generated notebook listing
├── assets/css/style.css          # Responsive styles
├── notebooks/                     # Upload your own Colab .ipynb files
├── tools/build_notebook_index.py # Automatic notebook discovery
├── index.md                       # Homepage
├── articles.md                    # Article listing
├── notebooks.md                   # Notebook catalog
└── about.md                       # Author bio
```

## License / attribution

The template is original starter content; the example notebook uses synthetic data. Choose a license appropriate to your own articles, code and datasets before publishing.
