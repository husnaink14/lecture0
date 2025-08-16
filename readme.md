# UN/LOCODE Scraper

A Python tool to fetch, parse, and export UN/LOCODE data for a given country code into Excel files.

## Features

- Web interface to input a 2-letter country code
- Downloads and parses UN/LOCODE data from the UNECE website
- Exports the parsed data to an Excel file in the `output/` directory
- Built with Flask, BeautifulSoup, pandas, and openpyxl

## Project Structure

```
.
├── src/
│   ├── app.py           # Flask web app
│   ├── config.py        # Configuration (base URL, country codes)
│   ├── downloader.py    # Downloads HTML content
│   ├── main.py          # Main orchestration logic
│   ├── parser.py        # Parses HTML to DataFrame
│   ├── templates/
│   │   └── index.html   # Web form template
│   └── test.py          # Test script
├── output/              # Excel files are saved here
├── requirements.txt     # Python dependencies
└── .gitignore
```

## Installation

1. **Clone the repository:**
   ```sh
   git clone <repo-url>
   cd unlocode_scraper
   ```

2. **Install dependencies:**
   ```sh
   pip install -r requirements.txt
   ```

## Usage

1. **Run the web application:**
   ```sh
   python -m src.app
   ```
   or
   ```sh
   cd src
   python app.py
   ```

2. **Open your browser and go to:**  
   [http://127.0.0.1:5000/](http://127.0.0.1:5000/)

3. **Enter a 2-letter country code** (e.g., `DE` for Germany) and submit.

4. **Check the `output/` directory** for the generated Excel file (e.g., `locode_DE.xlsx`).

## Notes

- The app fetches data from [UNECE UN/LOCODE](https://service.unece.org/trade/locode/).
- Only one country code is processed at a time via the web interface.
- Excel files are overwritten if the same country code is submitted again.

## License

MIT License

---

*This project is for educational and research purposes only. Not