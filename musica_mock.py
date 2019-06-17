from Musica import Musica
from Node import Node

def create_mock():
    m1 = Musica(nome="Misery", album="Please Please me", ano=1964, autor="The Beatles")
    m2 = Musica(nome="Chains", album="Please Please me", ano=1964, autor="The Beatles")
    m3 = Musica(nome="Anna", album="Please Please me", ano=1964, autor="The Beatles")
    m4 = Musica(nome="Run for your life",album="Rubber Soul", ano=1965,autor="The Beatles")
    m5 = Musica(nome = "In my life", album="Rubber Soul", ano=1965, autor="The Beatles")
    m6 = Musica(nome="Nowhere man", album="Rubber Soul", ano=1965, autor="The Beatles")
    m7 = Musica(nome="Think for yourself", album="Rubber Soul", ano=1965, autor="The Beatles")
    m8 = Musica(nome="Taxman", album="Revolver", ano=1965, autor="The Beatles")
    m9 = Musica(nome="Yellow Submarine", album="Revolver", ano=1965, autor="The Beatles")
    m10 = Musica(nome="Y")
    root = Node()
    root = root.insert(m1)
    root = root.insert(m2)
    root = root.insert(m3)
    root = root.insert(m4)
    root = root.insert(m5)
    root = root.insert(m6)
    root = root.insert(m7)
    root = root.insert(m8)
    root = root.insert(m9)
    #root = root.insert(m10)
    return root
