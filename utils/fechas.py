import datetime


def now():
    return datetime.datetime.now()

if __name__=="__main__":
    print("Imprimo la fecha desde el modulo de fechas, esto esta mal: ", now())