# Scrivere una classe Cane che definisca i seguenti attributi
#   -Zampe(default 4)
#   -coda(default True)
#   -età (default = 0)
#   -sesso
#
# E i seguenti metodi
#   -abbaia
#   -cammina
#   -corri


class Cane:
    zampe = 4
    coda = True
    eta = 0
    sesso = None

    def abbaia(self):
        print("UUfff")

    def cammina(self):
        print("Camminamento")

    def corri(self):
        print("Corrimento")

    def __init__(self, zampe, coda, eta, sesso):    #costruttore : inizializza gli attributi
        self.zampe = zampe
        self.coda = coda
        self.eta = eta
        self.sesso = sesso


c = Cane(4, False, 2, "M")

print(c.zampe)
print(c.sesso)

