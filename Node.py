from Musica import Musica
class Node:
    def __init__(self, musica=None, left=None, right=None):
        self._musica = musica
        self._left = left
        self._right = right

    def set_musica(self, musica):
        self._musica = musica

    def get_musica(self):
        return self._musica

    def set_left(self, left):
        self._left = left

    def get_left(self):
        return self._left

    def set_right(self, right):
        self._right = right

    def get_right(self):
        return self._right

    def __str__(self):
        return f"{self.get_musica().get_nome()}"

    def insert(self, musica):
        if self.get_musica() == None:
            self.set_musica(musica)
        else:
            ponteiro = self
            while True:
                if ponteiro.get_musica().get_nome() > musica.get_nome():
                    if ponteiro.get_left() == None:
                        node = Node(musica)
                        ponteiro.set_left(node)
                        break
                    else:
                        ponteiro = ponteiro.get_left()
                elif ponteiro.get_musica().get_nome() < musica.get_nome():
                    if ponteiro.get_right() == None:
                        node = Node(musica)
                        ponteiro.set_right(node)
                        break
                    else:
                        ponteiro = ponteiro.get_right()
                else:
                    print("Voce ja possui uma musica com este nome.")
                    return None

    def list_items(self):
        left = self.get_left()
        right = self.get_right()
        if self != None:
            if left != None:
                left.list_items()
            print(self.get_musica().get_nome())
            if right != None:
                right.list_items()

    def search_by_name(self, name):
        ponteiro = self
        while True:
            if ponteiro == None:
                return None
            if ponteiro.get_musica().get_nome() == name:
                return ponteiro
            else:
                if ponteiro.get_musica().get_nome() > name:
                    ponteiro = ponteiro.get_left()
                elif ponteiro-get_musica().get_nome() < name:
                    ponteiro = ponteiro.get_right()

    def in_order_successor(self, root):
        '''
        root: um node da arvore
        retorna o sucessor em ordem da arvore passada
        '''
        p = root.get_right()
        while p.get_left() is not None:
            p  = p.get_left()
        return p

    def remove_by_name(self,name):
        '''
        remove a node(music) based on its name
        '''
        p = q = self
        while p.get_musica().get_nome() is not name:
            #search for the correct node, and save its parent
            q = p
            if name > p.get_musica().get_nome():
                p = p.get_right()
            elif name < p.get_musica().get_nome():
                p = p.get_left()
            #in case we don't find any node
            if p is None:
                print("No music found it")
                return None

        if p.get_right() is None and p.get_left() is None:
            #case the node is a leaf
            if q.get_right() == p:
                q.set_right(None)
            elif q.get_left() == p:
                q.set_left(None)
        elif p.get_right() is None:
            #case the node only have one child
            if q.get_right() == p:
                q.set_right(p.get_left())
            else:
                q.set_left(p.get_left())
        else:
            #case the node has two childs, return the inorder sucessor
            r = self.in_order_successor(p)
            r.set_left(p.get_left())
            if q.get_left() == p:
                q.set_left(r)
            elif q.get_right() == p:
                q.set_right(r)
            p = None

    def search_by_year(self, year):
        left = self.get_left()
        right = self.get_right()
        if self is not None:
            if left is not None:
                left.search_by_year(year)
            if self.get_musica().get_ano() == year:
                print(self.get_musica().get_ano(), self.get_musica().get_nome())
            if right is not None:
                right.search_by_year(year)



if __name__ == "__main__":
   m1 = Musica(30)
   m2 = Musica(24)
   m3 = Musica(40)
   m4 = Musica(20)
   m5 = Musica(25)
   m6 = Musica(35)
   m7 = Musica(45)
   m8 = Musica(18)
   root = Node()
   root.insert(m1)
   root.insert(m2)
   root.insert(m3)
   root.insert(m4)
   root.insert(m5)
   root.insert(m6)
   root.insert(m7)
   root.insert(m8)
   root.remove_by_name(20)
   root.list_items()
