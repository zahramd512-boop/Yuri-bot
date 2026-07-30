import os
from code_runner import restart_bot



def update_code(
    name,
    code
):

    path=f"bots/{name}/main.py"


    with open(
        path,
        "w",
        encoding="utf-8"
    ) as f:

        f.write(code)



    restart_bot(
        name
    )


    return True
