import random
def Tirar2Dados():
    Tirada1 = random.randint(1,6)
    Tirada2 = random.randint(1,6)
    if( Tirada1 == 4):
        return Tirada2
    elif( Tirada2 == 4):
        return Tirada1
    return 0


def Juego():

    ResultadoJuan = Tirar2Dados()
    
    if(ResultadoJuan == 0):
        ResultadoJuan = Tirar2Dados()
    elif(ResultadoJuan < 4):  #En caso de que uno de los dados sea 4 y el otro sea menor a 4, el jugador tira el otro dado y se queda con su resultado como puntaje
        ResultadoJuan = random.randint(1,6)

        

    ResultadoMaria = Tirar2Dados()

    if(ResultadoMaria == 0):
        ResultadoMaria = Tirar2Dados()
    elif(ResultadoMaria < ResultadoJuan): #En caso de que uno de los dados sea 4 y maria tenga menos puntaje que juan, ella tira de nuevo ya que no tiene nada que perder
        ResultadoMaria = random.randint(1,6)
    elif(ResultadoMaria == ResultadoJuan and ResultadoMaria < 4):#En caso de que uno de los dados sea 4, el jugador tira el otro dado y se queda con su resultado como puntaje
        ResultadoMaria = random.randint(1,6)
    
    if(ResultadoMaria < ResultadoJuan):
        return "Juan gana el juego"
    elif(ResultadoJuan < ResultadoMaria):
        return "María gana el juego"
    else:
        return "El juego resulta en empate"

def SimulacionDeJuegos(cantDeVeces):
    JuanGana = 0
    MariaGana = 0
    Empate = 0
    for i in range(cantDeVeces):
        Partida = Juego()
        if(Partida == "Juan gana el juego"):
            JuanGana += 1
        elif(Partida == "María gana el juego"):
            MariaGana += 1
        else:
            Empate += 1

    return (f"En {cantDeVeces} juegos Juan ganó {JuanGana} veces María ganó {MariaGana} veces y empataron {Empate} veces")

print(SimulacionDeJuegos(100))