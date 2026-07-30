from github_manager import clone_repo
from requirements_manager import install_requirements
from code_runner import start_bot


def create_bot(
    name,
    repo
):

    path=clone_repo(
        repo,
        name
    )


    install_requirements(
        path
    )


    start_bot(
        name
    )


    return True
