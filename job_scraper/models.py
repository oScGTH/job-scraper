from dataclasses import dataclass
from typing import Optional

@dataclass
class JobPosting:
    title: Optional[str]
    company: Optional[str]
    location: Optional[str]
    deadline: Optional[str]
    source_url: str