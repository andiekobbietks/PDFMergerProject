import PyPDF2

def merge_pdfs(paths, output):
    pdf_writer = PyPDF2.PdfFileWriter()

    for path in paths:
        pdf_reader = PyPDF2.PdfFileReader(path)
        for page_num in range(pdf_reader.getNumPages()):
            page = pdf_reader.getPage(page_num)
            pdf_writer.addPage(page)

    with open(output, 'wb') as out:
        pdf_writer.write(out)

if __name__ == '__main__':
    paths = ['file1.pdf', 'file2.pdf']
    merge_pdfs(paths, 'merged.pdf')
