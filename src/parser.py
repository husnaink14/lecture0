# parser.py
from bs4 import BeautifulSoup
import pandas as pd

def parse_locode_data(html_content, country_code):
    """Parses HTML content to extract LOCODE data into a pandas DataFrame."""
    if not html_content:
        print(f"No HTML content to parse for {country_code}.")
        return None

    soup = BeautifulSoup(html_content, 'html.parser')
    print(f"HTML content parsed successfully for {country_code}!")

    data = []
    header = []
    tables = soup.find_all('table')
    if len(tables) > 2:
        data_table = tables[2]
        rows = data_table.find_all('tr')
        if len(rows) > 1:
            header_cols = rows[0].find_all(['th', 'td'])
            header = [col.text.strip() for col in header_cols]

            for row in rows[1:]:
                cols = row.find_all('td')
                cols = [col.text.strip() for col in cols]
                data.append(cols)

            print(f"Extracted {len(data)} rows of data for {country_code}.")

            if data and header:
                df = pd.DataFrame(data, columns=header)
                print(f"DataFrame created for {country_code}")
                return df
            else:
                print(f"No data or header available to create a DataFrame for {country_code}.")
                return None
        else:
            print(f"No data rows found within the table for {country_code}.")
            return None
    else:
        print(f"Could not find the expected data table on the page for {country_code}.")
        return None