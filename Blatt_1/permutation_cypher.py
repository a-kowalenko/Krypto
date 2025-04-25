from Blatt_1.musterloesung.permutation import IntPermutation

class PermutationCypher:
    """
    Klasse für Permutationsschiffren
    """
    def __init__(self, key : IntPermutation):
        self.encrypt_key = key
        self.decrypt_key = ~key
        # TODO: Erweitern Sie die Klasse IntPermutation um die Methode __len__
        #   Diese gibt die Länge der Liste zurück mit der die IntPermutation instantiiert wurde.
        self.len = len(key)

    def encrypt(self, message : str):
        """
        Verschlüsselt die Nachricht im Parameter message.
        """
        # TODO: Implementieren Sie diese Methode:
        #   Zunächst müssen Sie die Länge der Nachricht auf ein Vielfaches von self.len erweitern.
        #   Dazu hängen Sie maximal self.len-1 Leerzeichen an.
        #   Anschliessend teilen Sie die Nachricht in Blöcke der Länge self.len auf und kodieren diese einzeln
        #   Die kodierten Blöcke hängen Sie aneinander und geben Sie anschliessend zurück

    def decrypt(self, cypher : str):
        """
        Entschlüsselt cypher
        """
        # TODO: Implementieren Sie diese Methode:
        #   Werfen Sie einen ValueError mit geeigneter Fehlermeldung falls len(cypher) kein Vielfaches von self.len ist.
        #   Andernfalls entschlüsseln Sie die Nachricht unter der Annahme, dass cypher eine mit self.encrypt verschlüsselte
        #   Nachricht war. Die entschlüsselte Nachricht kann dabei um bis zu self.len-1 viele Leerzeichen verlängert sein.
        #   Was dafür zu tun ist ergibt sich aus den Erklärungen für self.encrypt

if __name__ == '__main__':
    # Wir Verwenden die Permutation die auch im Skript verwendet wurde. Da die Zählung von Python
    # bei 0 beginnt, sind die Werte jeweils um 1 kleiner.
    key = IntPermutation([3, 1, 4, 2, 0])
    krypto_system = PermutationCypher(key)
    cypher = krypto_system.encrypt("sonnesonn")
    print(cypher)
    message = krypto_system.decrypt(cypher)
    print(message)
    assert cypher == "noensno ns"
    assert message == "sonnesonn "

