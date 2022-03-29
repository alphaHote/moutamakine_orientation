
def read_txt(path):
    txt=""
    with open(path, 'r', encoding='utf-8') as fis:
        for line in fis.readlines():
            txt+=line
    return txt


import similarite as sim

ecoles=read_txt("data_depart.txt").split("</ecole>")

mon_text="etre un avocat devoue dans avenir sinon etre le juge dyal imahom ga3"

mx=0.0
choix=""
for ecole in ecoles:
    s=sim.simhash(ecole,mon_text)
    print(s)
    # if s>mx:
    #     mx=s
    #     choix=ecole

print(mx)
print(choix)


