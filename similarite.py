import numpy as np

#list des composantes uniques 
def get_unique(l_in):
    return np.unique(np.array(l_in)).tolist()


#le cardinale de l'intersection des enssembles X et Y
def a(X,Y):
    xx=get_unique(X)
    yy=get_unique(Y)
    card=0
    for x in xx:
        if yy.count(x)>0:
            card+=1
    return card
#le cardinale des éléments contenus dans X et non dans Y
def b(X,Y):
    xx=get_unique(X)
    yy=get_unique(Y)
    card=0
    for x in xx:
        if yy.count(x)==0:
            card+=1
    return card

#le cardinale des éléments contenus dans Y et non dans X
def c(X,Y):
    xx=get_unique(X)
    yy=get_unique(Y)
    card=0
    for y in yy:
        if xx.count(y)==0:
            card+=1
    return card

#la similarité de Tversky
def sim_Tversky(X,Y,alpha=1.0,beta=1.0):
    aa=float(a(X,Y))
    bb=float(b(X,Y))
    cc=float(c(X,Y))
    return aa/(aa+alpha*bb+beta*cc)





####################################################################################
from simhash import Simhash, SimhashIndex

def simhash(x,y):
    return 1.0-(float(Simhash(x).distance(Simhash(y)))/100.0)