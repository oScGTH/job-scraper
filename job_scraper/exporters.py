import csv 
from pathlib import Path
from job_scraper.models import JobPosting


def export_to_csv(job: JobPosting, output_path: Path) -> None:
    with output_path.open(mode="w", newline="", encoding="utf-8") as file:
        writer = csv.DictWriter(
            file,
            fieldnames=[
                "title",
                "company",
                "location",
                "deadline",
                "source_url",
            ],
        )
        writer.writeheader()
        writer.writerow(job.__dict__)