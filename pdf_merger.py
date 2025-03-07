from PyPDF2 import PdfFileReader, PdfFileWriter

def merge_pdfs(paths, output):
    pdf_writer = PdfFileWriter()

    for path in paths:
        pdf_reader = PdfFileReader(path)
        for page_num in range(pdf_reader.getNumPages()):
            page = pdf_reader.getPage(page_num)
            pdf_writer.addPage(page)

        # Preserve form fields
        if pdf_reader.getFields():
            pdf_writer.updatePageFormFieldValues(page, pdf_reader.getFields())

    with open(output, 'wb') as out:
        pdf_writer.write(out)

if __name__ == '__main__':
    paths = ['file1.pdf', 'file2.pdf']
    merge_pdfs(paths, 'merged.pdf')
