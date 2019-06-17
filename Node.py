from Musica import Musica
class Node:
    def __init__(self, musica=None, left=None, right=None):
        self._musica = musica
        self._left = left
        self._right = right
        self.balance = 0
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
        if self.get_musica() is not None:
            return f"{self.get_musica().get_nome()}"
        return "None"

    def insert(self, musica):
        if self.get_musica() == None:
            self.set_musica(musica)
            return self
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
                elif ponteiro.get_musica().get_nome() == musica.get_nome():
                    #self.list_items()
                    print(musica.get_nome())
                    return None
            #print("Balanced", self.is_balanced(self))
            if self.is_balanced(self) == False:
            	self = self.do_balance(self, musica.get_nome())
            	#pass
            return self
            #print("Ola")
    def left_rotation(self, root):
        y = root.get_right()
        z = y.get_left()

        # Perform rotation
        y.set_left(root)
        root.set_right(z)

        # Update heights
        lh = root.height(root.get_left()) - 1
        rh = root.height(root.get_right()) - 1
        root.balance = lh - rh

        lh = root.height(y.get_left()) - 1
        rh = root.height(y.get_right()) - 1
        y.balance = lh - rh

        # Return the new root
        return y


    def right_rotation(self, root):
        y = root.get_left()
        z = y.get_right()

        # Perform rotation
        y.set_right(root)
        root.set_left(z)

        # Update heights
        lh = root.height(root.get_left()) - 1
        rh = root.height(root.get_right()) - 1
        root.balance = lh - rh

        lh = root.height(y.get_left()) - 1
        rh = root.height(y.get_right()) - 1
        y.balance = lh - rh

        # Return the new root
        return y

    def do_balance(self, root, key):
        balance = root.balance
        # Case 1 - Left Left
        if balance > 1 and key < root.get_left().get_musica().get_nome():
            return self.right_rotation(root)

        # Case 2 - Right Right
        if balance < -1 and key > root.get_right().get_musica().get_nome():
            y = self.left_rotation(root)
            return y
        # Case 3 - Left Right
        if balance > 1 and key > root.get_left().get_musica().get_nome():
            root.set_left(root.left_rotation(root.get_left()))
            return self.right_rotation(root)

        # Case 4 - Right Left
        if balance < -1 and key < root.get_right().get_musica().get_nome():
            root.set_right(root.right_rotation(root.get_right()))
            return self.left_rotation(root)

        return root
    def list_items(self):
        right = self.get_right()
        left = self.get_left()
        if self is not None and self.get_musica() is not None:
            if left != None:
                left.list_items()
            print(self.get_musica().get_nome())
            if right != None:
                right.list_items()



    def search_by_name(self, name):
        '''
        busca uma musica(node) pelo nome passado
        '''
        ponteiro = self
        while True:
            #caso nao ache uma musica, eventualmente o ponteiro sera None
            if ponteiro is None or ponteiro.get_musica() is None:
                return None
            if ponteiro.get_musica().get_nome() == name:
                return ponteiro.get_musica()
            else:
                #move o ponteiro de acordo com a possivel posição (esquerda/direita) da musica(node)
                if ponteiro.get_musica().get_nome() > name:
                    ponteiro = ponteiro.get_left()
                elif ponteiro.get_musica().get_nome() < name:
                    ponteiro = ponteiro.get_right()

    def search(self, name):
        '''
        metodo de busca pelo nome utilizando recursividade
        '''
        left = self.get_left()
        right = self.get_right()
        if self is not None:
            if self.get_musica().get_nome() > name:
                if left is not None:
                    return left.search(name)
            elif self.get_musica().get_nome() < name:
                if right is not None:
                    return right.search(name)
            else:
                return self
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
        left = self.get_left()
        right = self.get_right()
        if self is not None and self.get_musica() is not None:
            if self.get_musica().get_nome() > name:
                if left is not None:
                    self.set_left(left.remove_by_name(name))
            elif self.get_musica().get_nome() < name:
                if right is not None:
                    self.set_right(right.remove_by_name(name))
            else:
                if left is None:
                    #caso possua um filho( a direita) ou nenhum filho
                    self = None
                    return right
                elif right is None:
                    #Caso possua apenas um filho a esquerda
            	    self = None
            	    return left
                #Caso possua dois filhos
                temp = self.in_order_successor(self)
                self.set_musica(temp.get_musica())
                right.remove_by_name(temp.get_musica().get_nome())

        return self

    def remove(self, name):
        root = self.remove_by_name(name)

        if self.is_balanced(root) == False:
            balance = root.balance
            if balance > 1 and root.get_left().balance >= 0:
                return self.right_rotation(root)

            # Case 2 - Right Right
            if balance < -1 and self.get_right().balance <= 0:
                return self.left_rotation(root)

            # Case 3 - Left Right
            if balance > 1 and self.get_left().balance < 0:
                root.set_left(self.left_rotation(root.get_left()))
                return self.right_rotation(root)

            # Case 4 - Right Left
            if balance < -1 and self.get_right().balance > 0:
                root.set_right(self.right_rotation(root.get_right()))
                return self.left_rotation(root)

        return root
    def search_by_year(self, year):
        '''
        procura musicas baseado no ano
        '''
        left = self.get_left()
        right = self.get_right()
        if self is not None:
            if left is not None:
                left.search_by_year(year)
            if self.get_musica().get_ano() == year:
                print("Nome: ", self.get_musica().get_nome())
                print("Autor: ", self.get_musica().get_autor())
                print("Album: ", self.get_musica().get_album())
                print("-" * 20)
            if right is not None:
                right.search_by_year(year)

    def height(self, root):
        '''
        retorna a altura da arvore passada
        obs: height = height - 1
        '''
        if root is None:
            return 0
        return max(self.height(root.get_right()), self.height(root.get_left())) + 1

    def is_balanced(self, root):
        '''
        retorna true caso a arvore esteja balanceada
        '''
        if root is None:
            return True

        lh = root.height(root.get_left()) - 1
        rh = root.height(root.get_right()) - 1
        root.balance = lh - rh

        if ((abs(lh - rh) <= 1) and self.is_balanced(root.get_left()) is True and self.is_balanced(root.get_right()) is True):
            return True

        return False
if __name__ == "__main__":
   m1 = Musica(30)
   m2 = Musica(24)
   m3 = Musica(40)
   m4 = Musica(20)
   m5 = Musica(25)
   m6 = Musica(35)
   m7 = Musica(45)
   m8 = Musica(18)
   m9 = Musica(44)
   m10 = Musica(50)
   m11 = Musica(7)
   m12 = Musica(19)
   m13 = Musica(60)
   root = Node()

   root = root.insert(m1)
   root = root.insert(m2)
   root = root.insert(m3)
   #root.insert(m4)
   root = root.insert(m5)
   root = root.insert(m6)
   root = root.insert(m7)
   #root.insert(m8)
   root = root.insert(m9)
   root.list_items()
   print(root.is_balanced(root))
   root = root.remove(25)
   root.list_items()
   print(root.is_balanced(root))
   #root.insert(m10)
   #root.insert(m11)
   #root.insert(m12)
   #root.insert(m13)
   #root.list_items()
   #root.remove_by_name(40)
   #root.list_items()
   #print(root.is_balanced(root))
   #root.remove(24)
   #print(root.is_balanced(root))
   #root.list_items()
   #print(root.search(40))
   #root.list_items()
   #root.remove(20)



