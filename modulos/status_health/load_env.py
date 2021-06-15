import os 


def load():
    # f = open(".env", r)
    # mis_envs = f.readlines()
    # f.close()
    # ahora vemos con with que es un context manager
    with open(".env", "r") as f:
        mis_envs = f.readlines()

    # ['SMTP_PASS="hola"\n']
    final = {}
    for x in mis_envs:
        env_var = x.strip().split("=")
        print(env_var)
        # KEY : SMTP_PASS
        # VALUES: "hola"
        final.update({env_var[0]: env_var[1]})


    print(final)
    return final



print(f"Este modulo es: {__name__}")
if __name__ == "__main__":

    print("Hola mundo")
    load()
