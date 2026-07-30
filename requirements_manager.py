import subprocess
import os


def install_requirements(path):

    file=f"{path}/requirements.txt"


    if os.path.exists(file):

        subprocess.run(
            [
                "pip",
                "install",
                "-r",
                file
            ]
        )

        return True


    return False
