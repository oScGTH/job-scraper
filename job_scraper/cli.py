import argparse
from job_scraper.models import JobPosting


def main():
    print("=== CLI STARTED ===")

    parser = argparse.ArgumentParser(
        description="Extract structured data from a job posting URL"
    )
    parser.add_argument("url", help="Job posting URL")

    args = parser.parse_args()
    print(f"URL received: {args.url}")

    job = JobPosting(
        title=None,
        company=None,
        location=None,
        deadline=None,
        source_url=args.url,
    )

    print("JobPosting object created:")
    print(job)


if __name__ == "__main__":
    main()