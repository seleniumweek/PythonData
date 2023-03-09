from pdf2image import convert_from_path
from pytesseract import image_to_string
from fpdf import FPDF
from PIL import Image

def convert_pdf_to_img(pdf_file):
    return convert_from_path(pdf_file)

def convert_image_to_text(file):
    text = image_to_string(file)
    return text

def get_text_from_any_pdf(pdf_file):
    images = convert_pdf_to_img(pdf_file)
    final_text = ""
    pdf_path = "\\Docs\\"
    for index, image in enumerate(images):
        image.save(f'output/{pdf_path}-{index}.png')

    for pg, img in enumerate(images):
        final_text += convert_image_to_text(img)
    return final_text

def text():
    pages = convert_from_path("D:\\doc.pdf", 500)
    for page in pages:
        page.save('out.jpg', 'JPEG')
#text()
finalwords=get_text_from_any_pdf("D:\\Doc.pdf")
with open('D:\\EducationalDocs\\readme1.txt', 'w') as f:
    f.write(finalwords)
f.close()    
  
