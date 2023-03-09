import pypdfium2 as pdfium

pdf = pdfium.PdfDocument("*.pdf")
n_pages = len(pdf)
for page_number in range(n_pages):
    page = pdf.get_page(page_number)
    pil_image = page.render_topil(
        scale=1,
        rotation=0,
        crop=(0, 0, 0, 0),
        colour=(255, 255, 255, 255),
        annotations=True,
        greyscale=False,
        optimise_mode=pdfium.OptimiseMode.NONE,
    )
    pil_image.save(f"image_{page_number+1}.png")
