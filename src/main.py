# main.py
from .config import BASE_URL, COUNTRY_CODES # Modified import statement
from .downloader import download_html # Modified import statement
from .parser import parse_locode_data # Modified import statement
import pandas as pd
import os

def main():
    all_country_dataframes = {}

    print("Starting the main process...") # Added print statement

    for code in COUNTRY_CODES:
        url = f"{BASE_URL}{code.lower()}.htm"
        html_content = download_html(url)
        if html_content:
            print(f"Attempting to parse data for {code.upper()}...") # Added print statement
            df = parse_locode_data(html_content, code.upper())
            if df is not None:
                all_country_dataframes[code.upper()] = df
                print(f"Successfully parsed and stored data for {code.upper()}.") # Added print statement
            else:
                print(f"Parsing returned no data for {code.upper()}.") # Added print statement
        else:
            print(f"No HTML content downloaded for {code.upper()}. Skipping parsing.") # Added print statement


    if all_country_dataframes:
        print("\nDataFrames were created. Proceeding to save.") # Added print statement
        # Create the output directory if it doesn't exist
        output_dir = "output"
        print(f"Checking for or creating output directory: {output_dir}") # Added print statement
        os.makedirs(output_dir, exist_ok=True)
        print(f"Output directory '{output_dir}' is ready.") # Added print statement


        # You can either save each country's data to a separate sheet
        # or concatenate them into one DataFrame and save to one sheet.
        # Here's an example of saving each to a separate sheet:

        excel_filename = os.path.join(output_dir, "selected_countries_locodes.xlsx")
        print(f"Attempting to save data to {excel_filename}") # Added print statement
        with pd.ExcelWriter(excel_filename) as writer:
            for country_code, df in all_country_dataframes.items():
                print(f"Saving sheet for {country_code}...") # Added print statement
                df.to_excel(writer, sheet_name=country_code, index=False)
                print(f"Sheet for {country_code} saved.") # Added print statement
        print(f"\nDataFrames successfully saved to {excel_filename}")
    else:
        print("\nNo DataFrames were created. Skipping save.") # Added print statement


if __name__ == "__main__":
    main()