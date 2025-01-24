# Project Diagrams

## PDF Merging Process
```mermaid
flowchart TD
    A[Start] --> B[Load First PDF]
    B --> C[Load Second PDF]
    C --> D{Validate PDFs}
    D -->|Valid| E[Copy Pages 1-1]
    D -->|Invalid| X[Show Error]
    E --> F[Replace Page 2]
    F --> G[Copy Pages 3-3]
    G --> H[Insert Page 4]
    H --> I[Copy Remaining Pages]
    I --> J[Preserve Form Fields]
    J --> K[Save Merged PDF]
    K --> L[End]
```

## Component Architecture
```mermaid
classDiagram
    class PDFMerger {
        +validate_pdf()
        +merge_pdfs()
        +preserve_form_fields()
    }
    class UIHandler {
        +get_pdf_file()
        +show_error()
        +show_success()
    }
    class FileHandler {
        +save_pdf()
        +load_pdf()
    }
    PDFMerger --> UIHandler
    PDFMerger --> FileHandler
```

## Form Field Handling Process
```mermaid
sequenceDiagram
    participant User
    participant UI
    participant Merger
    participant PyPDF2
    User->>UI: Select PDFs
    UI->>Merger: Process Files
    Merger->>PyPDF2: Read PDFs
    PyPDF2->>Merger: Return PDF Objects
    Merger->>PyPDF2: Copy Pages
    Merger->>PyPDF2: Preserve AcroForm
    PyPDF2->>Merger: Return Merged PDF
    Merger->>UI: Return Result
    UI->>User: Show Success
