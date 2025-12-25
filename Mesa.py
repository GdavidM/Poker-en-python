def cartas():

    import Maso as ms

    cartas = ms.mesclar()

    mano_jugador1 = [cartas[0],cartas[1]]
    mano_jugador2 = [cartas[2],cartas[3]]

    mesa = [cartas[4:9]]

    return mano_jugador1, mano_jugador2, mesa, cartas