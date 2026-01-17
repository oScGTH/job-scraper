# Job Scraper

A Python CLI tool for extracting structured data from individual job postings.

This project is designed as a clean, extensible foundation for collecting job
posting metadata (e.g. title, deadline, source URL) in a structured format that
can later be exported to tools such as Excel.

---

## Current Features

- Command-line interface (CLI)
- Structured job data model
- URL input validation via argparse
- Clean project structure ready for extension

No web scraping is implemented yet. The current focus is on correctness,
architecture, and extensibility.

---

## Project Structure

```text
job-scraper/
├── job_scraper/
│   ├── __init__.py
│   ├── cli.py        # CLI entry point
│   └── models.py     # JobPosting data model
├── outputs/          # Reserved for future exports
├── README.md
└── requirements.txt