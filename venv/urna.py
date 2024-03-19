import random  # Usada para escolher aleatoriamente um elemento de uma sequência


class Bola:
    def __init__(self, numero):
        self.numero = numero


class Urna:
    def __init__(self):
        self.bolas = [Bola(numero) for numero in range(1, 21)]

    def sortear_bola(self):
        return random.choice(self.bolas)


class Computador:
    def __init__(self):
        self.alvo = None

    def definir_alvo(self, bola):
        self.alvo = bola.numero

    def verificar_alvo(self, palpite):
        if palpite == self.alvo:
            return True
        else:
            return False

    def definir_proximo_alvo(self, bola_sorteada):
        if self.alvo + bola_sorteada.numero > 100:
            print("Infelizmente você ultrapassou o valor limite de 100.")
            return False
        else:
            self.alvo += bola_sorteada.numero
            return True


class Jogo:
    def __init__(self):
        self.urna = Urna()
        self.computador = Computador()

    def reiniciar(self):
        self.computador = Computador()

    def jogar(self):
        print("Welcome criançada!")

        while True:
            bola_sorteada = self.urna.sortear_bola()
            self.computador.definir_alvo(bola_sorteada)

            while True:
                palpite = input("Qual seu palpite? (um número de 1 a 20): ")
                if palpite.isdigit():
                    palpite = int(palpite)
                    if 1 <= palpite <= 20:
                        break
                    else:
                        print("É só de 1 a 20, lembra?. Tente novamente.")
                else:
                    print("Hmmm, só números heim.")

            acertou = self.computador.verificar_alvo(palpite)

            if acertou:
                print(
                    f"Parabéns, agora foi! Alvo {self.computador.alvo}."
                )
                break
            else:
                print("Você errou. Tente novamente!")
                if not self.computador.definir_proximo_alvo(bola_sorteada):
                    break

        print("Fim do jogo.")


# Fazendo o jogo funcionar
jogo = Jogo()
jogo.jogar()
