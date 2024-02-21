def Summa(arv1:int,arv2:int,arv3=0)->int:
    """Funktsioon tagastab kolme arvu suuma
        Summa(arv1,arv2,arv3)

    :param int arv1: Arv1 sisestab kasutaja       #param->parametr
    :param int arv2: Arv2 sisestab kasutaja 
    :param int arv3: Arv3 sisestab kasutaja 
    :rtype: int
    """
    s=arv1+arv2+arv3 
    return s
def IntKonroll(x)->str:
    #v1
    try:
        x=int(x)
        return"int"
    except:
        try:
            x=float(x)
            return"float"
        except:
            return"str"

#    #2v
#    #if isinstance(x, str):
#    #    return"str"
#    #elif isinstance(x, int):
#    #    return"int"
#    #else:
#    #    return"float"
