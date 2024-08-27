## Setting venv

### Activate
```bash
virtualenv .venv
source .venv/Scripts/activate
python -m pip install --upgrade pip
```

### Create a requirements.txt File

```bash
pip freeze > requirements.txt
```

### Deactivate

```bash
deactivate
```

## PDF managament

### Library

[PyMuPDF](https://pymupdf.readthedocs.io/en/latest/index.html)

#### Installation

```bash
pip install --upgrade pymupdf
```

### Plan

1. Open [Document](https://pymupdf.readthedocs.io/en/latest/document.html#document)

```python
import pymupdf

doc = pymupdf.open("a.pdf") # open a document

# 2nd option
doc = pymupdf.Document("a.pdf")
```
2. Iterate over pages

[Page Class Docs](https://pymupdf.readthedocs.io/en/latest/page.html)

```python
for page_index in range(len(doc)): # iterate over pdf pages
    page = doc[page_index] # get the page
```
[pages](https://pymupdf.readthedocs.io/en/latest/document.html#Document.pages) - might consider this for iterating
[page_count](https://pymupdf.readthedocs.io/en/latest/document.html#Document.page_count) - `Document` attribute (`len(doc)` works too)

3. Transform pdf page to image:

[Pixmap](https://pymupdf.readthedocs.io/en/latest/pixmap.html#pixmap)

```python
    pix = page.get_pixmap() # get the pixmap
    filename = f"slide{page_index}.jpg"
    pix.save(filename, output="jpg") # save pdf page to jpg
```
[get_pixmap()](https://pymupdf.readthedocs.io/en/latest/page.html#Page.get_pixmap)

## GUI - Tkinter for now

## Markdown

## Stack Overflow Links

- [page to jpeg 1](https://stackoverflow.com/questions/46184239/extract-a-page-from-a-pdf-as-a-jpeg)

- [page to jpeg 2](https://stackoverflow.com/questions/2693820/extract-images-from-pdf-without-resampling-in-python/34116472#34116472)