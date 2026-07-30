import os
from git import Repo



def clone_repo(url,name):

    path=f"bots/{name}"


    if os.path.exists(path):

        return path


    Repo.clone_from(
        url,
        path
    )


    return path
