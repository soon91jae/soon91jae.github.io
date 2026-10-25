# Updating publications with BibTeX

Edit **[bibliography/publications.bib](../bibliography/publications.bib)** on GitHub and commit to `master`. The **Deploy Academic Pages template site to Pages** action automatically converts the BibTeX into the Jekyll publication lists before building the website.

Existing 32 entries were imported from the previous publication data (25 peer-reviewed, 7 preprint/under review). Do not edit `_data/papers.yml` or `_data/preprints.yml` to update the deployed website: BibTeX takes precedence during deployment.

## Paste a new paper

```bibtex
@article{my_new_paper_2026,
  title = {My New Paper},
  author = {First Author and Sunjae Kwon and Last Author},
  year = {2026},
  category = {P},
  venue = {arXiv preprint},
  url = {https://arxiv.org/abs/XXXX.XXXXX}
}
```

Custom fields:
- `category`: `P` preprint / under review, `C` conference, `W` workshop, `J` journal.
- `venue`: display label, for example `NeurIPS` or `Manuscript under review`.
- `paper` or `url`: paper/preprint URL; optional for unpublished manuscripts.
- `code` and `poster`: optional links.
- `number`: optional stable display number (e.g., `P7`). If omitted, the converter assigns the next available number in its category.

When a preprint is accepted, **edit that same BibTeX entry**: change its `category` and `venue`, and remove the previous `number` so the converter assigns a number in the new category. This prevents the preprint from appearing twice.

Locally, run:

```bash
python -m pip install bibtexparser==1.4.3 PyYAML==6.0.2
python scripts/bibtex_to_jekyll.py
bundle exec jekyll build
```

The converter supports standard BibTeX `author = {A and B and C}` formatting. Imported legacy records retain comma-separated display names.

If Pages appears stale, check the Actions workflow run for the latest master commit, then hard refresh the site.
