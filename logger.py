import os


def get_logs(name):

    file=f"bots/{name}/log.txt"


    if os.path.exists(file):

        return open(
            file
        ).read()


    return "No Logs"
