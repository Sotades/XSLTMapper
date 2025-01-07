from pathlib import Path
from excelutils.excel_reader import ExcelReader

def main():
    # Get the Documents folder path
    documents_path = Path.home() / "Documents"
    
    # Specify your Excel file name
    excel_file = "I409 Outbound Delivery Mapping Sheet.xlsx"  # Replace with your actual Excel file name
    
    # Create full path to Excel file
    excel_path = documents_path / excel_file
    
    try:
        with ExcelReader(excel_path) as excel:
            # Get all sheet names
            sheet_names = excel.get_worksheet_names()
            print(f"Available sheets: {sheet_names}")
            
            # Read the first sheet (you can change 'Sheet1' to your actual sheet name)
            data = excel.read_worksheet(sheet_names[0])
            
            # Print total number of rows
            print(f"\nTotal rows: {len(data)}")
            
            # Print first 5 rows
            print("\nFirst 5 rows:")
            for i, row in enumerate(data[:5], 1):
                print(f"Row {i}:", row)

    except FileNotFoundError:
        print(f"Error: Could not find the file '{excel_file}' in Documents folder")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main() 