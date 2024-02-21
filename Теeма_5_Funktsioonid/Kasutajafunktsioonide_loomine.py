
#1
def arithmetic (arv1:int,arv2:int,operatsioon:str)->any:
    """
    :param str operatsıoon: operatsloon sisestab kasutaja
    :rtype: any
    """
    if operatsioon=="+":
        return arv1+arv2
    elif operatsioon=="-":
        return arv1-arv2
    elif operatsioon=="*":
        return arv1*arv2
    elif operatsioon=="/":
        if not (arv2==0):
            return arv1/arv2
        else:
            return "Nulliga jagada ei saa"
    else:
        return "Tundmatu toiming"
