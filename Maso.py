# Creación de un maso
def mesclar():
    import random as rd
    maso = ['Ac','2c','3c','4c','5c','6c','7c','8c','9c','10c','Jc','Qc','Kc','Ad','2d','3d','4d','5d','6d','7d','8d','9d','10d','Jd','Qd','Kd','Ap','2p','3p','4p','5p','6p','7p','8p','9p','10p','Jp','Qp','Kp','At','2t','3t','4t','5t','6t','7t','8t','9t','10t','Jt','Qt','Kt']
    for i in range(4):
        rd.shuffle(maso)
    return maso
