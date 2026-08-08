# some tasks might also involve getting images from a particular pdf and then write or process the extracted images using a separate
# library
# This can also be achieved using pypdf 

import pypdf
import send2trash
from pathlib import Path

sample_data_path = Path(__file__).parent / 'data'
pdf_path = sample_data_path/'robert-kiyosaki-the-real-book-of-real-estate.pdf'
pdf_file = pypdf.PdfReader(pdf_path)


img_dir = sample_data_path / 'extracted-images'
img_dir.mkdir(parents=True, exist_ok=True)

def extract_images_from_page(page_number: int) -> None:
    assert isinstance(page_number, int), "ValueError, page number must be of type int"

    if pdf_file.is_encrypted:
        print("[-]Cannot process an encrypted pdf file")
        return
    else:
        # getting pages of the pdf
        page_content = pdf_file.get_page(page_number=page_number)
        images = page_content.images
        if images:
            for img_index, img in enumerate(images, start=1):
                img_path = img_dir / f'page_{page_number}_image_{img_index}.jpg'
                with open(img_path, 'wb') as img_file:
                    img_file.write(img.data)
                

# extracting all the images from page 1 - 10
for page_num in range(10):
    extract_images_from_page(page_number=page_num)

# send2trash.send2trash(img_dir) # uncomment this line if you want to clear your device after running the script
