import PyPDF2

def extract_pdf_pages(pdf_path, start_page, end_page, output_file=None):
    """
    Extracts text from a given page range in a PDF.
    Args:
        pdf_path (str): Path to the input PDF file.
        start_page (int): Starting page number (1-indexed).
        end_page (int): Ending page number (1-indexed).
        output_file (str, optional): Path to save extracted text. Prints if None.
    """
    try:
        # Open PDF
        with open(pdf_path, 'rb') as file:
            reader = PyPDF2.PdfReader(file)
            total_pages = len(reader.pages)
            
            # Validate range
            if start_page < 1 or end_page > total_pages or start_page > end_page:
                raise ValueError(f"Invalid page range. PDF has {total_pages} pages.")

            extracted_text = ""
            for i in range(start_page - 1, end_page):
                page = reader.pages[i]
                extracted_text += page.extract_text() + "\n\n"

            # Save or print
            if output_file:
                with open(output_file, "w", encoding="utf-8") as out:
                    out.write(extracted_text)
                print(f"✅ Extracted pages {start_page}-{end_page} saved to '{output_file}'.")
            else:
                print(f"\n--- Extracted content (Pages {start_page}-{end_page}) ---\n")
                print(extracted_text)

    except Exception as e:
        print(f"❌ Error: {e}")


if __name__ == "__main__":
    # Example usage
    pdf_path = input("Enter path to PDF file: ").strip()
    page_range = input("Enter page range (e.g., 80-112): ").strip()

    # Parse page range
    try:
        start_page, end_page = map(int, page_range.split("-"))
        output_choice = input("Do you want to save to a text file? (y/n): ").lower()

        if output_choice == 'y':
            output_file = input("Enter output filename (e.g., output.txt): ").strip()
            extract_pdf_pages(pdf_path, start_page, end_page, output_file)
        else:
            extract_pdf_pages(pdf_path, start_page, end_page)

    except ValueError:
        print("❌ Invalid page range format. Please use the format: start-end (e.g., 5-10).")
