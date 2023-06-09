from typing import Union, List, Dict
from src.insights.jobs import read


def get_max_salary(path: str) -> int:
    jobs = read(path)
    salaries = [
        int(salary["max_salary"])
        for salary in jobs
        if salary["max_salary"].isnumeric()
    ]
    return max(salaries)

    """Get the maximum salary of all jobs

    Must call `read`

    Parameters
    ----------
    path : str
        Must be passed to `read`

    Returns
    -------
    int
        The maximum salary paid out of all job opportunities
    """
    raise NotImplementedError


def get_min_salary(path: str) -> int:
    jobs = read(path)
    salaries = [
        int(salary["min_salary"])
        for salary in jobs
        if salary["min_salary"].isnumeric()
    ]
    return min(salaries)

    """Get the minimum salary of all jobs

    Must call `read`

    Parameters
    ----------
    path : str
        Must be passed to `read`

    Returns
    -------
    int
        The minimum salary paid out of all job opportunities
    """
    raise NotImplementedError


def matches_salary_range(job: Dict, salary: Union[int, str]) -> bool:
    try:
        new_salary = int(salary)
        new_min = int(job["min_salary"])
        new_max = int(job["max_salary"])
        if (
            (not new_salary and new_salary != 0)
            or (not new_min and new_min != 0)
            or (not new_max and new_max != 0)
        ):
            raise ValueError("nao sao valores validos")
        if new_min > new_max:
            raise ValueError("minimo maior que o maximo")
        return new_min <= new_salary <= new_max
    except (KeyError, TypeError, ValueError):
        raise ValueError("nao sao valores validos")

    """Checks if a given salary is in the salary range of a given job

    Parameters
    ----------
    job : dict
        The job with `min_salary` and `max_salary` keys
    salary : int
        The salary to check if matches with salary range of the job

    Returns
    -------
    bool
        True if the salary is in the salary range of the job, False otherwise

    Raises
    ------
    ValueError
        If `job["min_salary"]` or `job["max_salary"]` doesn't exists
        If `job["min_salary"]` or `job["max_salary"]` aren't valid integers
        If `job["min_salary"]` is greather than `job["max_salary"]`
        If `salary` isn't a valid integer
    """
    raise NotImplementedError


def filter_by_salary_range(
    jobs: List[dict], salary: Union[str, int]
) -> List[Dict]:
    result = []
    for job in jobs:
        try:
            if matches_salary_range(job, salary):
                result.append(job)
        except ValueError as error:
            print(f"Error: {error}")
    return result
    """Filters a list of jobs by salary range

    Parameters
    ----------
    jobs : list
        The jobs to be filtered
    salary : int
        The salary to be used as filter

    Returns
    -------
    list
        Jobs whose salary range contains `salary`
    """
    raise NotImplementedError
