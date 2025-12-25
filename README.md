# Creando un Juego de Poker

Bueno el poker tiene varias versiones en si mismo, pero lo manejare de la siguiente forma.
- 1 jugadores prueba
- 1 jugador Humano (Usuario)

## Maso
El maso tiene 4 palos distintos.
- Diamante
- Corazon
- Ticas
- Trebol

Cada uno de estos palos tiene 13 cartas respectivamente.
- A (As) La primera carta de cada palo representa al 1 o 14 (Depende de la combinación de cartas que haga el Jugador).
- 2-10 un grupo de cartas del 2 al 10.
- J,Q,K (11, 12 y 13 respectivamente).

## Presupuesto
Por fines practicos se omitiran ciertas cosas.
- Cada jugador va a tener un presupuesto de $100 en la primera ronda.
- El concepto de ciegas no se manejara. El usuario podra, salir, aumentar la apuesta, e igualarla.

## Juego
- Al inicio de cada ronda. El maso se mesclara 4 veces para asegurar aleatoriedad en cada ronda.
- cada jugador resive 2 cartas
- preFlop: Cada jugador indica el monto con el que quiere ir. Pueden gastar todo el presupuesto o igualar la apuesta del otro.
- Flop: se muestran 3 de las 5 cartas en la mesa.
- cada jugador vuelve a tener la oportunidad de modificar el monto
- Turn: se muesta la 4ta carta de las 5 en la mesa.
- Cada jugador puede modificar el monto
- River: se muesta la 5ta y ultma carta de la mesa.
- Cada jugador puede modificar el monto antes de mostar sus cartas.

## Jerarquia de manos
- Par
- Trio
- Escalera
- Color
- FULL
- POKER
- Escalera de color
- Escalera Real


## Condicionales
### Por turnos
- Cada jugador puede pasar, retirarse, igualar o subir
- Si uno de los dos jugadores se decide `retirarse`, el otro se queda con el bote. Fin del juego.
- Si uno de los dos jugadores decide `pasar`, el otro se queda con el bote. Pasan a una ronda nueva.
- Los jugadores pueden `subir`, hasta terminar su presupuesto.
- Para pasar al siguiente turno deben de `igualar` la apuesta.




