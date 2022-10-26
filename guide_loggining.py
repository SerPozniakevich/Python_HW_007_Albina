
file_guide_xls = "guide_log.csv"
file_guide_txt = "guide_log.txt"


def write_log_guide(fam, nam, phone, descrip):
    with open(file_guide_xls, "a") as f:
        f.write(f"\n{fam} {nam}. телефон {phone}. описание {descrip}")


def write_log_guide_txt(fam, nam, phone, descrip):
    with open(file_guide_txt, 'a') as txt:
        txt.write(f"\n{fam} {nam}. телефон {phone}. описание {descrip}")


def read_log_guide():
    with open(file_guide_xls, "r") as f:
        print(f.read())
