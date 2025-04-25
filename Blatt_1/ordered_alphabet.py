from typing import List

class OrderedAlphabet:
    def __init__(self, symbol_sequence: str):
        """
        :param text: Sequenz von Symbolen, wobei kein Symbol mehrfach auftreten darf.
        """
        if len(symbol_sequence) != len(set(symbol_sequence)):
            raise ValueError("Im Parameter 'symbol_sequenz' darf kein Symbol mehrfach vorkommen.")
        
        self.__symbol_sequence = symbol_sequence
        self.__symbol_set = set(symbol_sequence)
        self.__symbol2ord = dict(zip(symbol_sequence, range(len(symbol_sequence))))


    @property
    def symbol_sequence(self):
        return list(self.__symbol_sequence)

    @property
    def symbol2ord(self):
        return dict(self.__symbol2ord)

    def ord(self, symbol:str):
        """
        :param symbol: Sollte ein Symbol aus dem OrderedAlphabet sein. Andernfalls wird ein 'ValueError' geworfen.
        :return: Gibt die Ordnungszahl des Symbols 'symbol' zurück.

        """
        if symbol not in self.symbol2ord:
            raise ValueError(f"Letter {symbol} is not known in this alphabet")
        return self.symbol2ord[symbol]

    def chr(self, id: int):
        """
        :param index: Ordnungszahl eines Symbols (D.h.: 0 <= id < len(self)).
            Andernfalls wird ein 'ValueError' geworfen.
        :return: Das Symbol von self mit der Ordnungszahl 'id'.
        """
        if not (0 <= id < len(self)):
            raise ValueError(f"No letter with id {id} in this alphabet")
        return self.symbol_sequence[id]

    def __contains__(self, symbol: str):
        """
        :param symbol:
        :return: Gibt an ob 'symbol' zum 'OrderedAlphabet' self gehört
        """
        return symbol in self.symbol2ord


    def __getitem__(self, item):
        """
        :param item: Entweder eine Ordnungszahl, oder ein Symbol des Alphabets
        :return: Das zur Ordnungszahl item gehörige Symbol, bzw. die zum Symbol gehörige Ordnungszahl
        """
        if isinstance(item, str):
            return self.ord(item)
        elif isinstance(item, int):
            return self.chr(item)
        else:
            raise TypeError(f"item of invalid type {item.__class__.__name__}. Type str or type int is expected.")

    def __len__(self):
        """
        :return: Die Zahl der Symbole des Alphabets.
        """
        return len(self.symbol_sequence)

    def to_id_list(self, text: str):
        """
        :param text:
        :return: Übersetzt einen Text in die zugehörige Liste von Ordnungszahlen

        Zum Beispiel:
        alphabet= Alphabet("AB")
        alphabet.to_id_list("ABBA") == [0, 1, 1, 0]
        """
        return [self.ord(ch) for ch in text]

    def id_list_to_text(self, id_list: List[int]):
        """
        :param index_list:
        :return: Das inverse zu 'to_id_list. D.h. Eine Übersetzung einer Liste von Ordnungszahlen in den zugehörigen
            text.

        Zum Beispiel:
        alphabet= Alphabet("AB")
        alphabet.id_list_to_text([0, 1, 1, 0]) == "ABBA"
        """
        return "".join([self.chr(i) for i in id_list])

    def __str__(self):
        """
        :return: Der geordnete String aller Symbole des OrderedAlphabet Objekts self.
        """
        return "".join(self.symbol_sequence)

    def __repr__(self):
        """
        :return: Ein String dessen Ausführung ein OrderedAlphabet Objekt erzeugt, dass zu self gleich ist'.
        """
        return f"{self.__class__.__name__}({repr(str(self))})"

    def __eq__(self, other: 'OrderedAlphabet'):
        """
        :param other:
        :return: Vergleich zweier OrderedAlphabet Objekte. Zwei OrderedAlphabet Objekte sind gleich, wenn sie aus den
            gleichen Symbolen in der gleichen Reihenfolge bestehen
        """
        # other muss vom Typ OrderedAlphabet sein
        if not isinstance(other, OrderedAlphabet):
            return False 
        
        return self.symbol_sequence == other.symbol_sequence



# Testmethoden:

def test_1():
    a = OrderedAlphabet("ABCDEFG")
    assert a.symbol_sequence == list("ABCDEFG")
    assert a.symbol2ord == {
        "A": 0,
        "B": 1,
        "C": 2,
        "D": 3,
        "E": 4,
        "F": 5,
        "G": 6
    }

def test_2():
    a = OrderedAlphabet("ABCDEFG")
    for symbol, idx in zip(a.symbol_sequence, range(len(a))):
        assert a.ord(symbol) == idx
        assert a.chr(idx) == symbol
    
    try:
        a.ord("X")
        assert False, "X ist nicht im Alphabet"
    except ValueError:
        pass

    try:
        a.chr(42)
        assert False, "Index 42 ausserhalb des Alphabets"
    except ValueError:
        pass

def test_3():
    a = OrderedAlphabet("ABCDEFG")
    assert "A" in a
    assert "G" in a
    assert "X" not in a

def test_4():
    assert len(OrderedAlphabet("ABCDEFG")) == 7
    assert len(OrderedAlphabet("AB")) == 2
    assert len(OrderedAlphabet("")) == 0

def test_5():
    a = OrderedAlphabet("AB")

    # prüfe leere Eingaben
    assert a.to_id_list("") == []
    assert a.id_list_to_text([]) == ""

    ids = a.to_id_list("ABBA")
    assert ids == [0, 1, 1, 0]

    text = a.id_list_to_text(ids)
    assert text == "ABBA"
    
def test_6():
    a = OrderedAlphabet("AB")
    assert a == OrderedAlphabet("AB")
    assert a != OrderedAlphabet("BA")
    assert a != OrderedAlphabet("ABC")
    assert a != OrderedAlphabet("A")
    assert a != OrderedAlphabet("")
    assert not (a == "AB")

if __name__ == "__main__":
    print("Starte ordered_alphabet tests")
    test_1()
    test_2()
    test_3()
    test_4()
    test_5()
    test_6()
    print("Tests erfolgreich durchgeführt")