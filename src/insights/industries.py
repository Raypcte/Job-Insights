from typing import List, Dict
from src.insights.jobs import read


def get_unique_industries(path: str) -> List[str]:
    jobs = read(path)
    industries = []
    for job in jobs:
        industry = job["industry"]
        if industry not in industries:
            industries.append(industry)
    return list(filter(len, industries))

    """Checks all different industries and returns a list of them

    Must call `read`

    Parameters
    ----------
    path : str
        Must be passed to `read`

    Returns
    -------
    list
        List of unique industries
    """
    raise NotImplementedError


# print(get_unique_industries("tests/mocks/jobs_with_industries.csv"))


def filter_by_industry(jobs: List[Dict], industry: str) -> List[Dict]:
    filter_industry = [job for job in jobs if job["industry"] == industry]
    return filter_industry

    """Filters a list of jobs by industry

    Parameters
    ----------
    jobs : list
        List of jobs to be filtered
    industry : str
        Industry for the list filter

    Returns
    -------
    list
        List of jobs with provided industry
    """
    raise NotImplementedError


# print(
#     filter_by_industry(
#         read("tests/mocks/jobs_with_industries.csv"), "solar energy"
#     )
# )
