from pathlib import Path
import pymupdf
import os

doc_path = "test_file.pdf"
doc = pymupdf.open(filename=doc_path, filetype="pdf")

doc_filename = os.path.splitext(doc_path)[0]
images_path = f"images_{doc_filename}"
if not os.path.isdir(images_path):
    os.mkdir(images_path)

for page_index in range(len(doc)):
    page = doc[page_index]
    pix = page.get_pixmap(dpi=160)
    jpg_path = f"images_{doc_filename}/slide{page_index+1}.jpg"
    pix.save(Path(jpg_path), output="jpg")
