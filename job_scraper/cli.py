import argparse
from pathlib import Path

from job_scraper.models import JobPosting
from job_scraper.exporters import export_to_csv


def main():
    print("=== CLI STARTED ===")

    parser = argparse.ArgumentParser(
        description="Extract structured data from a job posting URL"
    )
    parser.add_argument("url", help="Job posting URL")
    parser.add_argument(
        "--output",
        default="outputs/job_posting.csv",
        help="Output CSV file path",
    )

    args = parser.parse_args()
    print(f"URL received: {args.url}")

    job = JobPosting(
        title=None,
        company=None,
        location=None,
        deadline=None,
        source_url=args.url,
    )

    export_to_csv(job, Path(args.output))
    print(f"Saved job posting to {args.output}")

    print("JobPosting object created:")
    print(job)


if __name__ == "__main__":
    main()