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
        #TODO: Implementieren


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
        #TODO: Vervollständigen


    def __eq__(self, other):
    #TODO: Implementieren
        pass


    def __str__(self):
        return str(self.__permutation)


    def __invert__(self):
        #TODO: Implementieren
        pass


    def __repr__(self):
        return self.__permutation



class IntPermutation(Permutation):
    @classmethod
    def neutral(cls, size: int):
        return IntPermutation(list(range(size)))


    @classmethod
    def cycle(cls, n:int, k: int):
        pass
        #TODO: Implementieren


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
        pass
        # TODO: Implementieren

    def apply(self, objects_to_be_permuted: List[object]):
        if len(self) != len(objects_to_be_permuted):
            raise ValueError("Permutation has not the same number of elements as the list of objects to be permuted.")
        # TODO: Implementieren

    @staticmethod
    def apply_cycle(objects_to_be_permuted: List[object], k: int):
        pass
        # TODO: Implementieren


    def __str__(self):
        return str(self.order)

if __name__ == '__main__':
    pass
