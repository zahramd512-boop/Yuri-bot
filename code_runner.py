import subprocess


running={}



def start_bot(name):

    process=subprocess.Popen(
        [
            "python",
            f"bots/{name}/main.py"
        ]
    )


    running[name]=process


    return True



def stop_bot(name):

    if name in running:

        running[name].terminate()

        del running[name]



def restart_bot(name):

    stop_bot(name)

    start_bot(name)
