from pathlib import Path
import pymupdf
import os


def generate_images(filepath: Path, dirpath: Path):
    document = pymupdf.open(filename=filepath, filetype="pdf")
    file_name_without_ext = filepath.stem

    images_path = dirpath / f"images_{file_name_without_ext}"
    if not images_path.exists():
        os.mkdir(images_path)

    digits = len(str(document.page_count))
    for page_idx in range(len(document)):
        page = document[page_idx]
        pixmap = page.get_pixmap(dpi=160)
        jpg_path = images_path / f"slide{str(page_idx+1).zfill(digits)}.jpg"
        pixmap.save(jpg_path, output="jpg")


def generate_md_file(filepath: Path, dirpath: Path):
    file_name_without_ext = filepath.stem
    images_path = dirpath / f"images_{file_name_without_ext}"

    with open(dirpath / f"{file_name_without_ext}.md", "w") as f:
        f.write(f"# {file_name_without_ext}\n")
        slides = sorted(images_path.glob("*.jpg"))
        for slide_img in slides:
            slide_relative_path = slide_img.relative_to(dirpath)
            image_line = (
                f"![{slide_img.stem}]({slide_relative_path})\n\n"
                f"- [ ] completed \n\n**Notes:** \n\n---\n\n"
            )
            f.write(image_line)
        return
