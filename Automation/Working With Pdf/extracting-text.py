import re
import pypdf
from PIL.Image import open
from pathlib import Path

footer_regex = re.compile(r"\d+?_\w+:.+?Page\s\w+", re.IGNORECASE)
sample_data_path = Path(__file__).parent / 'data'
""" with open(sample_data_path/'robert-kiyosaki-the-real-book-of-real-estate.pdf', 'rb') as pdfobj:
    pdf_data = pdfobj.read() """

pdf_path = sample_data_path/'robert-kiyosaki-the-real-book-of-real-estate.pdf'
pdf_file = pypdf.PdfReader(pdf_path)


def get_page(page_number: int) -> str | None:
    assert isinstance(page_number, int), "ValueError, page number must be of type int"

    if pdf_file.is_encrypted:
        print("[-]Cannot process an encrypted pdf file")
        return None
    else:
        # getting pages of the pdf
        page_content = pdf_file.get_page(page_number=page_number)
        page_text = page_content.extract_text()
        return page_text


def get_number_of_pages(pdf: pypdf.PdfReader) -> int:
    number_of_pages: int = pdf.get_num_pages()
    return number_of_pages


# the two functions can now be used to extract information from the pdf
print("The number of pages for {} is {}".format(pdf_path.name, get_number_of_pages(pdf_file)))

# and a page can also be fetched easily now
page_number = 10  # say we want to get the page at page 10
print(f"Page {page_number} Content is \n", get_page(page_number=page_number-1))
