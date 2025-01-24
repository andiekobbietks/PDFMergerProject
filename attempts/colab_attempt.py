from PyPDF2 import PdfFileReader, PdfFileWriter

def merge_pdfs(paths, output):
    pdf_writer = PdfFileWriter()

    for path in paths:
        pdf_reader = PdfFileReader(path)
        for page_num in range(pdf_reader.getNumPages()):
            page = pdf_reader.getPage(page_num)
            pdf_writer.addPage(page)

    with open(output, 'wb') as out:
        pdf_writer.write(out)

if __name__ == '__main__':
    paths = ['/content/file1.pdf', '/content/file2.pdf']
    merge_pdfs(paths, '/content/merged.pdf')
