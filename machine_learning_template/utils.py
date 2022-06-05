from pathlib import Path


def get_repo_path(n=2):
    """return the directory based on n levels from pwd

    Args:
        n (int): level of lookback directory from the pwd

    Returns:
        repo_dir (str) : the directory based on the n levels from the pwd
    """
    dir_path = Path(__file__).resolve()
    repo_dir = dir_path.parents[n]
    print(f"This is repo dir from _util file: {repo_dir}")
    return repo_dir
