from typing import List, Dict


class Permutation:

    def __init__(self, permutation: Dict):
        """
        :param permutation:
        Eine permutation ist eine bijektive Abbildung einer Menge in sich selbst. Die Elemente müssen immutabel sein
        """
        domain = set(permutation.keys())
        if domain != set(permutation.values()):
            raise ValueError("Der Parameter permutation ist keine bijektive Selbstabbildung")
        self.__permutation = permutation
        self.__domain = domain


    @property
    def domain(self):
        return self.__domain


    @classmethod
    def neutral(cls, domain: set):
        """
        :param domain:
        :return: Neutrales Element der Permutationsgruppe. Jedes Element wird auf sich selbst abgebildet
        """
        return cls({ element: element for element in domain })


    def __getitem__(self, argument):
        """
        :param argument:
        :return: The image of the argument under the permutation
        """
        return self.__permutation[argument]


    def __len__(self):
        # Die Anzahl der Elemente die permutiert werden
        return len(self.__permutation)


    def __mul__(self, other):
        # Die Hintereinanderausführung. Dabei gilt für alle x der permutierten Menge:
        # (self * other)(x) == self(other(x))
        if set(other.domain) != set(self.domain):
            raise ValueError("Die Hintereinanderausführung von zwei Permutationen ist nur für Permutationen auf der "
                             "gleichen Menge zugelassen")
        komposition = { x: self[other[x]] for x in self.domain }
        return Permutation(komposition)


    def __eq__(self, other):
        if self.domain != other.domain:
            return False
        return self.__permutation == other.__permutation


    def __str__(self):
        return str(self.__permutation)


    def __invert__(self):
        inverted = { value: key for key, value in self.__permutation.items() }
        return Permutation(inverted)


    def __repr__(self):
        return self.__permutation



class IntPermutation(Permutation):
    @classmethod
    def neutral(cls, size: int):
        return IntPermutation(list(range(size)))


    @classmethod
    def cycle(cls, n:int, k: int):
        return cls([(i + k) % n for i in range(n)])


    def __init__(self, permutation: List[int]):
        Permutation.__init__(self, {key: value for key, value in enumerate(permutation)})
        self.order = permutation


    def __getitem__(self, argument):
        """
        :param argument:
        :return: The image of the argument under the permutation
        """
        return self.order[argument]


    def __invert__(self):
        n = len(self.order)
        return IntPermutation([self.order.index(i) for i in range(n)])

    def apply(self, objects_to_be_permuted: List[object]):
        if len(self) != len(objects_to_be_permuted):
            raise ValueError("Permutation has not the same number of elements as the list of objects to be permuted.")
        
        n = len(self)
        return [objects_to_be_permuted[self[i]] for i in range(n)]

    @staticmethod
    def apply_cycle(objects_to_be_permuted: List[object], k: int):
        n = len(objects_to_be_permuted)
        return IntPermutation.cycle(n, k).apply(objects_to_be_permuted)


    def __str__(self):
        return str(self.order)
    

# Testmethoden:

def test_1():
    domain = { "A", "B", "C", "D" }
    p = Permutation.neutral(domain)
    
    assert p.domain == domain
    for element in domain:
        assert p[element] == element

def test_2():
    domain = { "A", "B", "C", "D" }
    p1 = Permutation({ "A": "B", "B": "C", "C": "D", "D": "A" })
    p2 = Permutation({ "A": "C", "B": "D", "C": "A", "D": "B" })
    komposition = p1 * p2

    expected = { x: p1[p2[x]] for x in domain }
    for x in domain:
        assert komposition[x] == expected[x]

def test_3():
    domain = { "A", "B", "C", "D" }

    # gleiche Abbildung
    p1 = Permutation({ "A": "B", "B": "C", "C": "D", "D": "A" })
    p2 = Permutation({ "A": "B", "B": "C", "C": "D", "D": "A" })
    assert p1 == p2

    # verschiedene Abbildung
    p3 = Permutation({ "A": "D", "B": "C", "C": "B", "D": "A" })
    assert p1 != p3

    # verschiedene Domänen
    p4 = Permutation({ "A": "B", "B": "A" })
    assert p1 != p4

    # unterschiedliche Reihenfolge in Dict
    p5 = Permutation({ "B": "C", "A": "B", "C": "D", "D": "A" })
    assert p1 == p5

def test_4():
    domain = { "A", "B", "C", "D" }
    p = Permutation({ "A": "B", "B": "C", "C": "D", "D": "A" })
    invertiert = ~p
    neutral = Permutation.neutral(domain)
    # print('permutation:', p)
    # print('invertiert:', invertiert)
    # print('neutral:', neutral)

    # p * invertiert muss neutrales Element ergeben
    assert (p * invertiert) == neutral
    assert (invertiert * p) == neutral

    # zweifaches Invertieren ergibt wieder p
    assert ~invertiert == p
    
def test_5():
    p1 = IntPermutation.cycle(3, 1)
    p2 = Permutation({ 0: 1, 1: 2, 2: 0 })
    assert p1 == p2

def test_6():
    expected1 = ["W", "I", "N", "E", "R"]
    p = IntPermutation.cycle(5, 2)
    assert p.apply("ERWIN") == expected1

    expected2 = [2, 3, 4, 1]
    assert IntPermutation.cycle(4, 1).apply([1, 2, 3, 4]) == expected2

def test_7():
    expected1 = ["W", "I", "N", "E", "R"]
    assert IntPermutation.apply_cycle("ERWIN", 2) == expected1

    #negatives k
    assert IntPermutation.apply_cycle([1, 2, 3, 4], -2) == [3, 4, 1, 2]

    # k > n
    assert IntPermutation.apply_cycle([1, 2, 3, 4], 6) == [3, 4, 1, 2]

def test_8():
    p = IntPermutation([2, 0, 1, 3])
    expected = IntPermutation([1, 2, 0, 3])
    inv = ~p
    print("Original:", p)
    print("Inverse:", inv) 
    assert inv == expected
    

if __name__ == '__main__':
    print("Starte permutation tests")
    test_1()
    test_2()
    test_3()
    test_4()
    test_5()
    test_6()
    test_7()
    test_8()
    print("Tests erfolgreich durchgeführt")
