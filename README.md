# Job Scraper

A Python CLI tool for extracting structured data from individual job postings.

This project is designed as a clean, extensible foundation for collecting job
posting metadata (e.g. title, deadline, source URL) in a structured format that
can later be exported to tools such as Excel.

---

## Current Features

- Command-line interface (CLI)
- Structured job data model
- CSV export (Excel-compatible)
- URL input validation via argparse

No web scraping is implemented yet. The current focus is on correctness,
architecture, and extensibility.

---

## Project Structure

```text
job-scraper/
├── job_scraper/
│   ├── __init__.py
│   ├── cli.py        # CLI entry point
│   ├── models.py     # JobPosting data model
│   └── exporters.py  # CSV export logi
├── outputs/          # Reserved for future exports
├── README.md
└── requirements.txt
```

## CSV Export (Excel-compatible)

The tool can export structured job posting data to a CSV file that can be opened
directly in Excel.

The export functionality is implemented as an isolated module to keep concerns
separated from the CLI and data model.

### Usage

Run the CLI with a job posting URL:

python -m job_scraper.cli https://example.com/job/123

### Default Output

By default, the CSV file is written to:

outputs/job_posting.csv

### Custom Output Path

A custom output path can be provided using the --output flag:

python -m job_scraper.cli https://example.com/job/123 --output outputs/my_jobs.csv

### CSV Structure

The generated CSV file contains the following columns:

- title
- company
- location
- deadline
- source_url

All fields except source_url may be empty if the information is not available.

The file is written using UTF-8 encoding and avoids common Excel issues such as
extra blank lines on Windows.

Each CSV file currently contains a single job posting; support for multiple
entries may be added in a future iteration.

## Scraper Architecture

The project defines a clear architecture for web scraping without coupling it
to the CLI, data model, or export logic.

Scraping is handled through a dedicated scraper layer, allowing new job sites
to be added without modifying existing functionality.

### Base Scraper Interface

All scrapers in the project are required to implement a shared base interface.
This ensures a consistent contract across different job sites.

Each scraper is responsible for handling a single job posting URL and must
return a structured JobPosting object.