!
pip install PyPDF2
import
logging
import
io
from
datetime
import
datetime
from
google.colab
import
files
from
PyPDF2
import
PdfReader
,
PdfWriter
logging.basicConfig
(
level=logging.INFO
)
logger = logging.getLogger
(
__name__
)
def
get_pdf_file
(
prompt
)
:
"""Uploads a PDF file from the user's local machin
e."""
uploaded = files.upload
()
for
filename
in
uploaded.keys
():
return
io.BytesIO
(
uploaded
[
filename
])
def
validate_pdf
(
pdf_file
)
:
"""Validates if the uploaded PDF has 13 pages."""
try
:
pdf_reader = PdfReader
(
pdf_file
)
return
len
(
pdf_reader.pages
)
==
13
except
Exception
as
e
:
logger.error
(
f
"Validation error:
{
e
}
"
)
return
False
def
merge_pdfs
(
doc1_file
,
doc2_file
)
:
"""Merges two PDF files and returns the merged PDF
as a BytesIO object."""
doc1 = PdfReader
(
doc1_file
)
doc2 = PdfReader
(
doc2_file
)
writer = PdfWriter
()
# Main merge logic (Modified for your specific req
uirements)
# Add pages from doc1, except for page 2
for
page_num
in
range
(
len
(
doc1.pages
)):
if
page_num !=
1
:
# Skip page 2 of doc1
writer.add_page
(
doc1.pages
[
page_num
])
# Replace page 2 of doc1 with page 2 of doc2
writer.insert_page
(
1
,
doc2.pages
[
1
])
# Insert at index 1 (page 2)
# Insert page 4 of doc2 after page 4 of doc1 (whic
h is now page 4 in the merged doc)
writer.insert_page
(
4
,
doc2.pages
[
3
])
# Save output to BytesIO object
output_buffer = io.BytesIO
()
writer.write
(
output_buffer
)
output_buffer.seek
(
0
)
# Reset buffer position
return
output_buffer
def
main
()
:
"""Main execution function for Google Colab."""
doc1_file = get_pdf_file
(
"Upload first PDF (13 pages)"
)
doc2_file = get_pdf_file
(
"Upload second PDF (13 pages)"
)
if
not
all
([
validate_pdf
(
doc1_file
),
validate_pdf
(
doc2_file
)]):
print
(
"Error: Invalid PDF(s)"
)
return
try
:
merged_pdf = merge_pdfs
(
doc1_file
,
doc2_file
)
timestamp = datetime.now
()
.strftime
(
"%Y%m%d_%H%M%S"
)
# Download the merged PDF
files.download
(
io.BytesIO
(
merged_pdf.getvalue
()),
f
"merged_
{
timestamp
}
.pdf"
)
print
(
"Success: Merged PDF downloaded."
)
except
Exception
as
e
:
print
(
f
"Error: Merge failed:
{
str
(
e
)}
"
)
if
__name__
==
"__main__"
:
main
()
24/01/2025, 20:32 merged_document.ipynb - Colab
https://colab.research.google.com/drive/1XyeG1OY6CKJqoeETw4org3g3uvaBMVI1#scrollTo=7fWx79CrALW4&printMode=true 1/7
Requirement already satisfied: PyPDF2 in /usr/local/lib/python3.11/dist-packages (3.0.1)
Choose files OCT-NOV p…ent form.pdf
OCT-NOV placement form.pdf(application/pdf) - 581172 bytes, last modified: 24/01/2025 - 100% done
Saving OCT-NOV placement form.pdf to OCT-NOV placement form.pdf
Choose files OCT-NOV placement 2.pdf
OCT-NOV placement 2.pdf(application/pdf) - 531640 bytes, last modified: 24/01/2025 - 100% done
Saving OCT-NOV placement 2.pdf to OCT-NOV placement 2.pdf
Error: Merge failed: 'int' object is not subscriptable
!
pip install PyPDF2
import
logging
import
io
from
datetime
import
datetime
from
google.colab
import
files
from
PyPDF2
import
PdfReader
,
PdfWriter
logging.basicConfig
(
level=logging.INFO
)
logger = logging.getLogger
(
__name__
)
def
get_pdf_file
(
prompt
)
:
"""Uploads a PDF file from the user's local machin
e."""
uploaded = files.upload
()
for
filename
in
uploaded.keys
():
return
io.BytesIO
(
uploaded
[
filename
])
def
validate_pdf
(
pdf_file
)
:
"""Validates if the uploaded PDF has 13 pages."""
try
:
pdf_reader = PdfReader
(
pdf_file
)
return
len
(
pdf_reader.pages
)
==
13
except
Exception
as
e
:
logger.error
(
f
"Validation error:
{
e
}
"
)
return
False
def
merge_pdfs
(
doc1_file
,
doc2_file
)
:
"""Merges two PDF files and returns the merged PDF
as a BytesIO object."""
doc1 = PdfReader
(
doc1_file
)
doc2 = PdfReader
(
doc2_file
)
writer = PdfWriter
()
# Main merge logic (Modified for your specific req
uirements)
# Add pages from doc1, except for page 2
for
page_num
in
range
(
len
(
doc1.pages
)):
if
page_num !=
1
:
# Skip page 2 of doc1
writer.add_page
(
doc1.pages
[
page_num
])
# Replace page 2 of doc1 with page 2 of doc2
writer.insert_page
(
1
,
doc2.pages
[
1
])
# Insert at index 1 (page 2)
# Insert page 4 of doc2 after page 4 of doc1 (whic
h is now page 4 in the merged doc)
writer.insert_page
(
4
,
doc2.pages
[
3
])
# Save output to BytesIO object
output_buffer = io.BytesIO
()
writer.write
(
output_buffer
)
output_buffer.seek
(
0
)
# Reset buffer position
return
output_buffer
def
main
()
:
"""Main execution function for Google Colab."""
doc1_file = get_pdf_file
(
"Upload first PDF (13 pages)"
)
doc2_file = get_pdf_file
(
"Upload second PDF (13 pages)"
)
if
not
all
([
validate_pdf
(
doc1_file
),
validate_pdf
(
doc2_file
)]):
print
(
"Error: Invalid PDF(s)"
)
return
try
:
merged_pdf = merge_pdfs
(
doc1_file
,
doc2_file
)
timestamp = datetime.now
()
.strftime
(
"%Y%m%d_%H%M%S"
)
# Download the merged PDF
files.download
(
io.BytesIO
(
merged_pdf.getvalue
()),
f
"merged_
{
timestamp
}
.pdf"
)
print
(
"Success: Merged PDF downloaded."
)
except
Exception
as
e
:
print
(
f
"Error: Merge failed:
{
str
(
e
)}
"
)
24/01/2025, 20:32 merged_document.ipynb - Colab
https://colab.research.google.com/drive/1XyeG1OY6CKJqoeETw4org3g3uvaBMVI1#scrollTo=7fWx79CrALW4&printMode=true 2/7
Requirement already satisfied: PyPDF2 in /usr/local/lib/python3.11/dist-packages (3.0.1)
Choose files OCT-NOV p…ent form.pdf
OCT-NOV placement form.pdf(application/pdf) - 581172 bytes, last modified: 24/01/2025 - 100% done
Saving OCT-NOV placement form.pdf to OCT-NOV placement form.pdf
Choose files OCT-NOV placement 2.pdf
OCT-NOV placement 2.pdf(application/pdf) - 531640 bytes, last modified: 24/01/2025 - 100% done
Saving OCT-NOV placement 2.pdf to OCT-NOV placement 2.pdf
Error: Merge failed: 'int' object is not subscriptable
if __name__ == "__main__":
main()
penspark Generate print hello world using rot13 search Close
!pip install PyPDF2
import logging
import io
from datetime import datetime
from google.colab import files
from PyPDF2 import PdfReader, PdfWriter
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)
def get_pdf_file(prompt):
"""Uploads a PDF file from the user's local machine."""
uploaded = files.upload()
for filename in uploaded.keys():
return io.BytesIO(uploaded[filename])
def validate_pdf(pdf_file):
"""Validates if the uploaded PDF has 13 pages."""
try:
pdf_reader = PdfReader(pdf_file)
return len(pdf_reader.pages) == 13
except Exception as e:
logger.error(f"Validation error: {e}")
return False
def merge_pdfs(doc1_file, doc2_file):
"""Merges two PDF files and returns the merged PDF as a BytesIO object."""
doc1 = PdfReader(doc1_file)
doc2 = PdfReader(doc2_file)
writer = PdfWriter()
# Add pages from doc1, except for page 2
for page_num in range(len(doc1.pages)):
if page_num != 1: # Skip page 2 of doc1
writer.add_page(doc1.pages[page_num])
# Replace page 2 of doc1 with page 2 of doc2 (corrected argument order)
writer.insert_page(doc2.pages[1], 1) # Page first, then index
# Insert page 4 of doc2 after page 4 of the merged doc (corrected argument order)
writer.insert_page(doc2.pages[3], 4) # Page first, then index
# Save output to BytesIO object
output_buffer = io.BytesIO()
writer.write(output_buffer)
output_buffer.seek(0) # Reset buffer position
return output_buffer
def main():
"""Main execution function for Google Colab."""
doc1_file = get_pdf_file("Upload first PDF (13 pages)")
doc2_file = get_pdf_file("Upload second PDF (13 pages)")
if not all([validate_pdf(doc1_file), validate_pdf(doc2_file)]):
print("Error: Invalid PDF(s)")
return
try:
merged_pdf = merge_pdfs(doc1_file, doc2_file)
timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
# Download the merged PDF
files.download(io.BytesIO(merged_pdf.getvalue()), f"merged_{timestamp}.pdf")
print("Success: Merged PDF downloaded.")
except Exception as e:
print(f"Error: Merge failed: {str(e)}")
24/01/2025, 20:32 merged_document.ipynb - Colab
https://colab.research.google.com/drive/1XyeG1OY6CKJqoeETw4org3g3uvaBMVI1#scrollTo=7fWx79CrALW4&printMode=true 3/7
Requirement already satisfied: PyPDF2 in /usr/local/lib/python3.11/dist-packages (3.0.1)
Choose files OCT-NOV p…ent form.pdf
OCT-NOV placement form.pdf(application/pdf) - 581172 bytes, last modified: 24/01/2025 - 100% done
Saving OCT-NOV placement form.pdf to OCT-NOV placement form (1).pdf
Choose files OCT-NOV placement 2.pdf
OCT-NOV placement 2.pdf(application/pdf) - 531640 bytes, last modified: 24/01/2025 - 100% done
Saving OCT-NOV placement 2.pdf to OCT-NOV placement 2 (1).pdf
Error: Merge failed: download() takes 1 positional argument but 2 were given
print(f Error: Merge failed: {str(e)} )
if __name__ == "__main__":
main()
Requirement already satisfied: PyPDF2 in /usr/local/lib/python3.11/dist-packages (3.0.1)
Upload the first PDF (13 pages):
Choose files OCT-NOV p…ent form.pdf
OCT-NOV placement form.pdf(application/pdf) - 581172 bytes, last modified: 24/01/2025 - 100% done
Saving OCT-NOV placement form.pdf to OCT-NOV placement form.pdf
Upload the second PDF (13 pages):
Choose files OCT-NOV placement 2.pdf
OCT-NOV placement 2.pdf(application/pdf) - 531640 bytes, last modified: 24/01/2025 - 100% done
Saving OCT-NOV placement 2.pdf to OCT-NOV placement 2.pdf
Error: Merge failed: download() takes 1 positional argument but 2 were given
!pip install PyPDF2
from google.colab import files
from PyPDF2 import PdfReader, PdfWriter
def get_pdf_file():
"""Uploads a PDF file from the user's local machine."""
uploaded = files.upload()
for filename in uploaded.keys():
return uploaded[filename]
def merge_pdfs(doc1_file, doc2_file):
"""Merges two PDF files and returns the merged PDF as bytes."""
doc1 = PdfReader(doc1_file)
doc2 = PdfReader(doc2_file)
writer = PdfWriter()
# Add pages from doc1, except for page 2
for i, page in enumerate(doc1.pages):
if i != 1: # Skip page 2 (index 1)
writer.add_page(page)
# Replace page 2 of doc1 with page 2 of doc2
writer.insert_page(doc2.pages[1], 1)
# Insert page 4 of doc2 after page 4 of the merged doc
writer.insert_page(doc2.pages[3], 4)
# Save the merged PDF to a bytes object
output_buffer = io.BytesIO()
writer.write(output_buffer)
output_buffer.seek(0)
return output_buffer.getvalue()
def main():
"""Main execution function for Google Colab."""
print("Upload the first PDF (13 pages):")
doc1_file = io.BytesIO(get_pdf_file())
print("Upload the second PDF (13 pages):")
doc2_file = io.BytesIO(get_pdf_file())
try:
merged_pdf = merge_pdfs(doc1_file, doc2_file)
files.download(merged_pdf, "merged.pdf")
print("Success: Merged PDF downloaded as 'merged.pdf'.")
except Exception as e:
print(f"Error: Merge failed: {e}")
if __name__ == "__main__":
import io
main()
!
pip install PyPDF2
import
io
from
google.colab
import
files
24/01/2025, 20:32 merged_document.ipynb - Colab
https://colab.research.google.com/drive/1XyeG1OY6CKJqoeETw4org3g3uvaBMVI1#scrollTo=7fWx79CrALW4&printMode=true 4/7
Requirement already satisfied: PyPDF2 in /usr/local/lib/python3.11/dist-packages (3.0.1)
Upload FIRST PDF (13 pages):
Choose files OCT-NOV p…ent form.pdf
OCT-NOV placement form.pdf(application/pdf) - 581172 bytes, last modified: 24/01/2025 - 100% done
Saving OCT-NOV placement form.pdf to OCT-NOV placement form.pdf
Upload SECOND PDF (13 pages):
Choose files OCT-NOV placement 2.pdf
OCT-NOV placement 2.pdf(application/pdf) - 531640 bytes, last modified: 24/01/2025 - 100% done
Saving OCT-NOV placement 2.pdf to OCT-NOV placement 2.pdf
❌ Error: download() takes 1 positional argument but 2 were given
from
PyPDF2
import
PdfReader
,
PdfWriter
def
get_pdf_file
()
:
"""Uploads a PDF file and returns its bytes."""
uploaded = files.upload
()
return
next
(
iter
(
uploaded.values
()))
# Directly return the file bytes
def
merge_pdfs
(
doc1_bytes
,
doc2_bytes
)
:
"""Merge PDFs by replacing page 2 of doc1 with pag
e 2 of doc2, and inserting doc2's page 4."""
doc1 = PdfReader
(
io.BytesIO
(
doc1_bytes
))
doc2 = PdfReader
(
io.BytesIO
(
doc2_bytes
))
writer = PdfWriter
()
# Add all pages from doc1 except page 2 (index 1)
for
i
,
page
in
enumerate
(
doc1.pages
):
if
i !=
1
:
writer.add_page
(
page
)
# Replace page 2 with doc2's page 2
writer.insert_page
(
doc2.pages
[
1
],
1
)
# Insert doc2's page 4 after merged doc's page 4
writer.insert_page
(
doc2.pages
[
3
],
4
)
# Save merged PDF to bytes
merged_bytes = io.BytesIO
()
writer.write
(
merged_bytes
)
return
merged_bytes.getvalue
()
def
main
()
:
"""Main function to handle uploads, merging, and d
ownload."""
print
(
"Upload FIRST PDF (13 pages):"
)
doc1_bytes = get_pdf_file
()
print
(
"Upload SECOND PDF (13 pages):"
)
doc2_bytes = get_pdf_file
()
try
:
merged_pdf = merge_pdfs
(
doc1_bytes
,
doc2_bytes
)
files.download
(
merged_pdf
,
"merged_document.pdf"
)
# Use keyword argument for filename
print
(
"✅ Success! Merged PDF downloaded as
'merged_document.pdf'."
)
except
Exception
as
e
:
print
(
f
"❌ Error:
{
e
}
"
)
if
__name__
==
"__main__"
:
main
()
!
pip install PyPDF2
import
io
from
google.colab
import
files
from
PyPDF2
import
PdfReader
,
PdfWriter
import
os
def
get_pdf_file
(
prompt
)
:
"""Uploads a PDF file and returns its bytes."""
print
(
prompt
)
uploaded = files.upload
()
if
not
uploaded
:
raise
Exception
(
"No file uploaded."
)
file_name =
next
(
iter
(
uploaded
))
# get the name of the file
return
file_name
,
uploaded
[
file_name
]
# Returns both filename and file bytes
def
merge_pdfs
(
doc1_bytes
,
doc2_bytes
)
:
"""Merge PDFs by replacing page 2 of doc1 with pag
e 2 of doc2, and inserting doc2's page 4."""
doc1 = PdfReader
(
io.BytesIO
(
doc1_bytes
))
doc2 = PdfReader
(
io.BytesIO
(
doc2_bytes
))
writer = PdfWriter
()
# Add all pages from doc1 except page 2 (index 1)
for
i
,
page
in
enumerate
(
doc1.pages
):
24/01/2025, 20:32 merged_document.ipynb - Colab
https://colab.research.google.com/drive/1XyeG1OY6CKJqoeETw4org3g3uvaBMVI1#scrollTo=7fWx79CrALW4&printMode=true 5/7
if
i !=
1
:
writer.add_page
(
page
)
# Replace page 2 with doc2's page 2
writer.insert_page
(
doc2.pages
[
1
],
1
)
# Insert doc2's page 4 after merged doc's page 4
writer.insert_page
(
doc2.pages
[
3
],
4
)
# Save merged PDF to bytes
merged_bytes = io.BytesIO
()
writer.write
(
merged_bytes
)
return
merged_bytes.getvalue
()
def
main
()
:
"""Main function to handle uploads, merging, and d
ownload."""
try
:
file1_name
,
doc1_bytes = get_pdf_file
(
"Upload FIRST PDF (13 pages):"
)
file2_name
,
doc2_bytes = get_pdf_file
(
"Upload SECOND PDF (13 pages):"
)
merged_pdf_bytes = merge_pdfs
(
doc1_bytes
,
doc2_bytes
)
# Save the merged PDF to a temporary file in the c
olab environment
with
open
(
"merged_document.pdf"
,
"wb"
)
as
merged_file
:
merged_file.write
(
merged_pdf_bytes
)
files.download
(
"merged_document.pdf"
)
print
(
"✅ Success! Merged PDF downloaded as
'merged_document.pdf'."
)
os.remove
(
"merged_document.pdf"
)
# Remove the temporary file
except
Exception
as
e
:
print
(
f
"❌ Error:
{
e
}
"
)
if
__name__
==
"__main__"
:
main
()
!pip install PyPDF2
import io
from google.colab import files
from PyPDF2 import PdfReader, PdfWriter
import os
def get_pdf_file(prompt):
"""Uploads a PDF file and returns its name and bytes."""
print(prompt)
uploaded = files.upload()
if not uploaded:
raise Exception("No file uploaded.")
file_name = next(iter(uploaded)) # get the name of the file
return file_name, uploaded[file_name] # Returns both filename and file bytes
def merge_pdfs(doc1_bytes, doc2_bytes):
"""Merge PDFs by replacing page 2 of doc1 with page 2 of doc2, and inserting doc2's page 4."""
doc1 = PdfReader(io.BytesIO(doc1_bytes))
doc2 = PdfReader(io.BytesIO(doc2_bytes))
writer = PdfWriter()
# Add all pages from doc1 except page 2 (index 1)
for i, page in enumerate(doc1.pages):
if i != 1:
writer.add_page(page)
# Replace page 2 with doc2's page 2
writer.insert_page(doc2.pages[1], 1)
# Insert doc2's page 4 after merged doc's page 4
writer.insert_page(doc2.pages[3], 4)
# Save merged PDF to bytes
merged_bytes = io.BytesIO()
writer.write(merged_bytes)
return merged_bytes.getvalue()
def main():
"""Main function to handle uploads, merging, saving to /content, and removing uploaded files."""
try:
file1_name, doc1_bytes = get_pdf_file("Upload FIRST PDF (13 pages):")
file2_name, doc2_bytes = get_pdf_file("Upload SECOND PDF (13 pages):")
merged_pdf_bytes = merge_pdfs(doc1_bytes, doc2_bytes)
# Save the merged PDF directly to the /content directory
output_path = "/content/merged_document.pdf"
24/01/2025, 20:32 merged_document.ipynb - Colab
https://colab.research.google.com/drive/1XyeG1OY6CKJqoeETw4org3g3uvaBMVI1#scrollTo=7fWx79CrALW4&printMode=true 6/7
Requirement already satisfied: PyPDF2 in /usr/local/lib/python3.11/dist-packages (3.0.1)
Upload FIRST PDF (13 pages):
Choose files OCT-NOV p…ent form.pdf
OCT-NOV placement form.pdf(application/pdf) - 581172 bytes, last modified: 24/01/2025 - 100% done
Saving OCT-NOV placement form.pdf to OCT-NOV placement form.pdf
Upload SECOND PDF (13 pages):
Choose files OCT-NOV placement 2.pdf
OCT-NOV placement 2.pdf(application/pdf) - 531640 bytes, last modified: 24/01/2025 - 100% done
Saving OCT-NOV placement 2.pdf to OCT-NOV placement 2.pdf
✅ Success! Merged PDF saved to '/content/merged_document.pdf'.
✅ Uploaded PDF files removed.
with open(output_path, "wb") as merged_file:
merged_file.write(merged_pdf_bytes)
print(f"✅ Success! Merged PDF saved to '{output_path}'.")
# Remove the uploaded files from the Colab environment
os.remove(file1_name)
os.remove(file2_name)
print("✅ Uploaded PDF files removed.")
except Exception as e:
print(f"❌ Error: {e}")
if __name__ == "__main__":
main()
24/01/2025, 20:32 merged_document.ipynb - Colab
https://colab.research.google.com/drive/1XyeG1OY6CKJqoeETw4org3g3uvaBMVI1#scrollTo=7fWx79CrALW4&printMode=true 7/7