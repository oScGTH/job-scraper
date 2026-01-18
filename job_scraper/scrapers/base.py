from abc import ABC, abstractmethod
from job_scraper.models import JobPosting


class BaseJobScraper(ABC):
    def __init__(self, url: str):
        self.url = url

    @abstractmethod
    def scrape(self) -> JobPosting:
        pass