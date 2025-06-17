# Use Case:
- You work for a company that conducts polls for private companies and political parties. Participants submit their responses as paper forms or as online PDFs. You currently spend a lot of time and money entering these responses into databases. You want to assess Azure AI Document Intelligence to find out if you can use it to streamline this process using Azure AI Document Intelligence Studio.

- Document intelligence uses machine learning technology to identify and extract key-value pairs and table data from form documents with accuracy, at scale.

- Azure Document Intelligence uses Optical Character Recognition (OCR) capabilities and deep learning models to extract text, key-value pairs, selection marks, and tables from documents.

- Before training a custom model, it's worth verifying if your use case can be analyzed accurately with one of these prebuilt models. 

- Use the `analyze document` function to starts the form analysis, then request the result to get the analysis.

[TODO] Doc Interlience app : https://microsoftlearning.github.io/mslearn-ai-document-intelligence/Instructions/Exercises/02-custom-document-intelligence.html
## Confidence scores
- If the confidence values of the analyzeResult are low, try to improve the quality of your input documents.
- confidence score of 80% or higher is acceptable for a low-risk application.

## The Azure Document Intelligence Studio currently supports the [Model Types](https://learn.microsoft.com/en-us/training/modules/work-form-recognizer/9-form-recognizer-studio):
### Document analysis models
-  Read Model
   - Extract printed and handwritten text lines, words, locations, and detected languages
-  Layout Model
   - Extract text, tables, and structure information from forms. 
   - Also recognize selection marks such as check boxes and radio buttons.
   - documents (PDF and TIFF) and images (JPG, PNG, and BMP).
- General Documents
   - Extract key-value pairs, selection marks, and entities from documents.
### Prebuilt models
- Invoice
   - To extract key information from sales invoices in English and Spanish.
- Receipt
   - To extract data from printed and handwritten receipts.
- W-2
   - To extract data from United States government's W-2 tax declaration form.
- ID document
   - To extract data from United States driver's licenses and international passports.
- Business card
   - To extract names and contact details from business cards.
### Custom models
- To obtain more predictable and standardized results from your unusual form types.
- Custom template models
- Custom neural models
### [Composed models](https://learn.microsoft.com/en-us/training/modules/plan-form-recognizer-solution/4-choose-model-type)
- consists of multiple custom models.
- when you don't know the submitted document type.
  - The results from a composed model include the docType property
---

## Document Intelligence file [input requirements](https://learn.microsoft.com/en-us/training/modules/work-form-recognizer/3-get-started)

- Format must be JPG, PNG, BMP, PDF (text or scanned), or TIFF. Also, Read Support [Microsoft Word] and [Microsoft Excel] docs additionally

- The file size must be less than 500 MB for paid (S0) tier and 4 MB for free (F0) tier.
- Image dimensions must be between 50 x 50 pixels and 10,000 x 10,000 pixels.
- The total size of the training data set must be 500 pages or less.