import sys
sys.path.insert(0, r'c:\Users\sarva\OneDrive\Desktop\ocr_tool')
from app import get_text_chunks, extract_fields

# Test single invoice
chunks = get_text_chunks(r'c:\Users\sarva\OneDrive\Desktop\ocr_tool\invoices\bill_01_INV20240001 (1).pdf')
print("=== Single PDF: {} page(s) ===".format(len(chunks)))
for i, text in enumerate(chunks):
    f = extract_fields(text)
    print("  Page {}: InvNo={}, Date={}, Qty={}, Cost={}, Conf={}".format(
        i+1, f["Invoice No."], f["Invoice Date"], f["Quantity"], f["Cost"], f["Confidence Score"]))

print()

# Test multi-invoice PDF
chunks = get_text_chunks(r'c:\Users\sarva\OneDrive\Desktop\ocr_tool\invoices\multi_invoice_9bills.pdf')
print("=== Multi PDF: {} page(s) ===".format(len(chunks)))
for i, text in enumerate(chunks):
    f = extract_fields(text)
    print("  Page {}: InvNo={}, Date={}, Qty={}, Cost={}, Conf={}".format(
        i+1, f["Invoice No."], f["Invoice Date"], f["Quantity"], f["Cost"], f["Confidence Score"]))
