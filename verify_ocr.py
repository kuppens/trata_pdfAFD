# Import the required modules
import PyPDF2
import pytesseract
from PIL import Image
from pdf2image import convert_from_path

# Define a function to check if a PDF file is OCR or not
def is_ocr_pdf(filename):
    # Convert the PDF page to an image
    images = convert_from_path(filename, first_page=1, last_page=1)
    
    # If no images are extracted, it means the PDF is not OCR
    if not images:
        return False
    
    # Run OCR on each image and check if the OCR text matches the extracted text
    for image in images:
        ocr_text = pytesseract.image_to_string(image)
        
        # Open the PDF file
        pdf_file = PyPDF2.PdfFileReader(open(filename, "rb"))
        # Get the first page
        page = pdf_file.getPage(0)
        # Extract the text from the page
        text = page.extract_text()
        
        # If the OCR text is empty or different from the extracted text, it means the PDF is OCR
        if not ocr_text or ocr_text != text:
            return True
    
    # Otherwise, it means the PDF is not OCR
    return False

# Test the function on a sample PDF file
filename = "teste_ocr.pdf"
result = is_ocr_pdf(filename)
print(f"The PDF file {filename} is {'' if result else 'not '}OCR.")
