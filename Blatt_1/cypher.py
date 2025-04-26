from Blatt_1.ordered_alphabet import OrderedAlphabet
from Blatt_1.permutation import IntPermutation


# Aufgabe 3

def caesar_encode(text: str, alphabet: OrderedAlphabet, shift: int):
    """
    :param text: Der zu kodierende Text
    :param alphabet:
    :param shift: Distanz der zyklischen Vertauschung im Alphabet
    :return: Caesar kodierter Text
    Example:
        caesar_encode('HELLO_WORLD', Alphabet('_ABCDEFGHIJKLMNOPQRSTUVWXYZ'), 3) == 'KHOORCZRUOG'
    """
    # TODO: Implementieren Sie diese Methode, ohne die vordefinierten Methoden für die monoalphabetische
    #    Substitution oder die Vigenère Verschlüsselung zu verwenden
    text_ids = alphabet.to_id_list(text)
    text_ids = [(x + shift) % len(alphabet) for x in text_ids]

    return ''.join(alphabet.id_list_to_text(text_ids))


def caesar_decode(cypher: str, alphabet: OrderedAlphabet, shift: int):
    """
    :param cypher: Der zu dekodierende Text
    :param alphabet:
    :param shift: Distanz der rückgängig zu machenden zyklischen Vertauschung im Alphabet
    :return: Dekodierter Text
    Example:
        caesar_decode('KHOORCZRUOG', Alphabet('_ABCDEFGHIJKLMNOPQRSTUVWXYZ'), 3) == 'HELLO_WORLD'
    """
    # TODO: Implementieren Sie diese Methode, ohne die vordefinierten Methoden für die monoalphabetische
    #    Substitution oder die Vigenère Verschlüsselung zu verwenden
    text_ids = alphabet.to_id_list(cypher)
    text_ids = [(x - shift) % len(alphabet) for x in text_ids]

    return ''.join(alphabet.id_list_to_text(text_ids))


def substitution_cypher_encode(text: str, alphabet: OrderedAlphabet, permutation: IntPermutation):
    """
    :param text: Der zu kodierende Text
    :param alphabet:
    :param permutation: Die auf das geordnete Alphabet anzuwendende Permutation
    :return: Der mit der Permutation verschlüsselte Text gemäß der Monoalphabetische Substitution.
        (Englisch: Substitution-Cypher
    """
    # TODO: Implementieren
    text_ids = alphabet.to_id_list(text)
    text_ids = [permutation[x] for x in text_ids]

    return ''.join(alphabet.id_list_to_text(text_ids))


def substitution_cypher_decode(cypher: str, alphabet: OrderedAlphabet, permutation: IntPermutation):
    """
    :param cypher: Der zu dekodierende Text.
    :param alphabet:
    :param permutation: Permutation die rückgängig gemacht werden soll
    :return: Decodierter Text gemäß der Monoalphabetische Substitution.
    """
    # TODO: Implementieren
    text_ids = alphabet.to_id_list(cypher)
    inv = ~permutation
    text_ids = [inv[x] for x in text_ids]

    return ''.join(alphabet.id_list_to_text(text_ids))


def caesar_encode_as_special_case_of_substitution_cypher(text: str, alphabet: OrderedAlphabet, shift: int):
    """
    Die gleiche Funktionalität wie caesar_encode
    """
    # TODO: Implementieren Sie die Caesar-Verschlüsselung als Spezialfall der monoalphabetischen Substitution
    return substitution_cypher_encode(text,
                                      alphabet,
                                      IntPermutation.cycle(len(text), shift))


def encode_vigenere(text: str, alphabet: OrderedAlphabet, key: str):
    """
    :param text: Der zu kodierende Text
    :param alphabet:
    :param key: Schlüsse für das Vigenère-Verfahren
    :return: Der durch key Vigenère-verschlüsselter Text
    """
    # TODO: Implementieren
    text_ids = alphabet.to_id_list(text)
    for i in range(len(text_ids)):
        ordK = alphabet.ord(key[i % len(key)])
        text_ids[i] = (text_ids[i] + ordK) % len(alphabet)

    return ''.join(alphabet.id_list_to_text(text_ids))


def decode_vigenere(cypher: str, alphabet: OrderedAlphabet, key: str):
    """
    :param cypher: Der zu dekodierende Text
    :param alphabet:
    :param key: Schlüsse für das Vigenère-Verfahren
    :return: Der durch key Vigenère-verschlüsselter Text
    """
    # TODO: Implementieren
    text_ids = alphabet.to_id_list(cypher)
    for i in range(len(text_ids)):
        ordK = alphabet.ord(key[i % len(key)])
        text_ids[i] = (text_ids[i] - ordK) % len(alphabet)

    return ''.join(alphabet.id_list_to_text(text_ids))


def caesar_encode_as_special_case_of_vignere(text: str, alphabet: OrderedAlphabet, shift: int):
    """
    Die gleiche Funktionalität wie caesar_encode
    """
    # TODO: Implementieren Sie die Caesar-Verschlüsselung als Spezialfall der Vigenère-Verschlüsselung
    key = ''.join([alphabet.chr(shift) for i in range(len(text))])
    return encode_vigenere(text, alphabet, key)


def caesar_decode_as_special_case_of_vignere(text: str, alphabet: OrderedAlphabet, shift: int):
    """
    Die gleiche Funktionalität wie caesar_decode
    """
    # TODO: Implementieren Sie die Caesar-Verschlüsselung als Spezialfall der Vigenère-Entschlüsselung
    key = ''.join([alphabet.chr(shift) for i in range(len(text))])
    return decode_vigenere(text, alphabet, key)


def test_1():
    # example from method body
    p = 'HELLO_WORLD'
    c = caesar_encode(p, OrderedAlphabet('_ABCDEFGHIJKLMNOPQRSTUVWXYZ'), 3)
    # print("Plaintext: " + p)
    assert c == 'KHOORCZRUOG'
    # print("Cypher: " + c)

    d = caesar_decode(c, OrderedAlphabet('_ABCDEFGHIJKLMNOPQRSTUVWXYZ'), 3)
    assert p == d
    # print("Decoded: " + d)

    p = 'TIMEODANAOSETDONAFERENTES'
    c = caesar_encode(p, OrderedAlphabet('ABCDEFGHIJKLMNOPQRSTUVWXYZ'), 3)
    # print("Plaintext: " + p)
    assert c == 'WLPHRGDQDRVHWGRQDIHUHQWHV'
    # print("Cypher: " + c)

    d = caesar_decode(c, OrderedAlphabet('ABCDEFGHIJKLMNOPQRSTUVWXYZ'), 3)
    assert p == d
    # print("Decoded: " + d)


def test_2():
    p = 'ABCD'
    alph = OrderedAlphabet('ABCD')
    perm = IntPermutation([1, 2, 3, 0])

    # print("Plaintext: " + p)
    c = substitution_cypher_encode(p, alph, perm)
    # print("Cypher: " + c)

    assert c == 'BCDA'
    d = substitution_cypher_decode(c, alph, perm)
    # print("Decoded: " + d)


def test_3():
    p = "HELLO_WORLD"
    alph = OrderedAlphabet("_ABCDEFGHIJKLMNOPQRSTUVWXYZ")
    key = "BCD"
    # print("Plain: " + p)
    c = encode_vigenere(p, alph, key)
    # print("Cypher: " + c)
    d = decode_vigenere(c, alph, key)
    assert p == d
    #   print("Decoded: " + d)
    p = "ATTACKATDAWN"
    alph = OrderedAlphabet("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
    key = "LEMONLEMONLE"
    c = "LXFOPVEFRNHR"
    assert c == encode_vigenere(p, alph, key)
    assert p == decode_vigenere(c, alph, key)

def test_4():
    p = 'TIMEODANAOSETDONAFERENTES'
    c = caesar_encode_as_special_case_of_substitution_cypher(p, OrderedAlphabet('ABCDEFGHIJKLMNOPQRSTUVWXYZ'), 3)
    # print("Plaintext: " + p)
    assert c == 'WLPHRGDQDRVHWGRQDIHUHQWHV'
    # print("Cypher: " + c)


def test_5():
    p = 'TIMEODANAOSETDONAFERENTES'
    alph = OrderedAlphabet('ABCDEFGHIJKLMNOPQRSTUVWXYZ')
    c = caesar_encode_as_special_case_of_vignere(p, alph, 3)
    # print("Plaintext: " + p)
    assert c == 'WLPHRGDQDRVHWGRQDIHUHQWHV'
    # print("Cypher: " + c)

    d = caesar_decode_as_special_case_of_vignere(c, alph, 3)
    assert p == d
    print("Decoded: " + d)


if __name__ == '__main__':
    print("Starte cypher tests")
    test_1()
    test_2()
    test_3()
    test_4()
    test_5()
    print("Tests erfolgreich durchgeführt")
