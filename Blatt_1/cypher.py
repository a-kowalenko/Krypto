def caesar_encode(text: str, alphabet: OrderedAlphabet, shift: int):
    """
    :param text: Der zu kodierende Text
    :param alphabet:
    :param shift: Distanz der zyklischen Vertauschung im Alphabet
    :return: Caesar kodierter Text
    Example:
        caesar_encode('HELLO_WORLD', Alphabet('_ABCDEFGHIJKLMNOPQRSTUVWXYZ'), 3) == 'KHOORCZRUOG'
    """
    #TODO: Implementieren Sie diese Methode, ohne die vordefinierten Methoden für die monoalphabetische
    #    Substitution oder die Vigenère Verschlüsselung zu verwenden

def caesar_decode(cypher: str, alphabet: OrderedAlphabet, shift: int):
    """
    :param cypher: Der zu dekodierende Text
    :param alphabet:
    :param shift: Distanz der rückgängig zu machenden zyklischen Vertauschung im Alphabet
    :return: Dekodierter Text
    Example:
        caesar_decode('KHOORCZRUOG', Alphabet('_ABCDEFGHIJKLMNOPQRSTUVWXYZ'), 3) == 'HELLO_WORLD'
    """
    #TODO: Implementieren Sie diese Methode, ohne die vordefinierten Methoden für die monoalphabetische
    #    Substitution oder die Vigenère Verschlüsselung zu verwenden

def substitution_cypher_encode(text: str, alphabet: OrderedAlphabet, permutation: IntPermutation):
    """
    :param text: Der zu kodierende Text
    :param alphabet:
    :param permutation: Die auf das geordnete Alphabet anzuwendende Permutation
    :return: Der mit der Permutation verschlüsselte Text gemäß der Monoalphabetische Substitution.
        (Englisch: Substitution-Cypher
    """
    #TODO: Implementieren

def substitution_cypher_decode(cypher: str, alphabet: OrderedAlphabet, permutation: IntPermutation):
    """
    :param cypher: Der zu dekodierende Text.
    :param alphabet:
    :param permutation: Permutation die rückgängig gemacht werden soll
    :return: Decodierter Text gemäß der Monoalphabetische Substitution.
    """
    #TODO: Implementieren

def caesar_encode_as_special_case_of_substitution_cypher(text: str, alphabet: OrderedAlphabet, shift: int):
    """
    Die gleiche Funktionalität wie caesar_encode
    """
    #TODO: Implementieren Sie die Caesar-Verschlüsselung als Spezialfall der monoalphabetischen Substitution

def encode_vigenere(text: str, alphabet: OrderedAlphabet, key: str):
    """
    :param text: Der zu kodierende Text
    :param alphabet:
    :param key: Schlüsse für das Vigenère-Verfahren
    :return: Der durch key Vigenère-verschlüsselter Text
    """
    #TODO: Implementieren

def decode_vigenere(cypher: str, alphabet: OrderedAlphabet, key: str):
    """
    :param cypher: Der zu dekodierende Text
    :param alphabet:
    :param key: Schlüsse für das Vigenère-Verfahren
    :return: Der durch key Vigenère-verschlüsselter Text
    """
    #TODO: Implementieren

def caesar_encode_as_special_case_of_vignere(text: str, alphabet: OrderedAlphabet, shift: int):
    """
    Die gleiche Funktionalität wie caesar_encode
    """
    #TODO: Implementieren Sie die Caesar-Verschlüsselung als Spezialfall der Vigenère-Verschlüsselung

def caesar_decode_as_special_case_of_vignere(text: str, alphabet: OrderedAlphabet, shift: int):
    """
    Die gleiche Funktionalität wie caesar_decode
    """
    # TODO: Implementieren Sie die Caesar-Verschlüsselung als Spezialfall der Vigenère-Entschlüsselung
