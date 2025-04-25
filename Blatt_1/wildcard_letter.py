from collections import defaultdict


class UnknownSymbol:
    def __init__(self, value = None):
        self.value = value

    def __repr__(self):
        return '*' if self.value is None else self.value

    def __eq__(self, other):
        return self is other

    def __hash__(self):
        return id(self)

class UnknownSymbolString:
    def __init__(self, cypher):
        if isinstance(cypher, str):
            symbol_dict = defaultdict(UnknownSymbol)
            for letter in cypher:
                symbol_dict[letter] = UnknownSymbol(letter)
            self.cypher_list = [symbol_dict[letter] for letter in cypher]
        elif isinstance(cypher, list):
            self.cypher_list = list(cypher)
        else:
            raise ValueError()

    def __iter__(self):
        return iter(self.cypher_list)

    # def __next__(self):
    #     if self.n <= self.max:
    #         result = 2 ** self.n
    #         self.n += 1
    #         return result
    #     else:
    #         raise StopIteration

    def __len__(self):
        return len(self.cypher_list)

    def __str__(self):
        return "".join([str(symbol) for symbol in self.cypher_list])

    def __setitem__(self, key, value):
        self.cypher_list[key].value = value

    def __eq__(self, other):
        if len(self.cypher_list) != len(other.cypher_list):
            return False
        ret = all(x == y for x, y in zip(self.cypher_list, other.cypher_list))
        return ret

    def __hash__(self):
        return hash(tuple(hash(letter) for letter in self.cypher_list))

if __name__ == '__main__':
    cypher = (
        '5 3‡‡† 305)) 6* ;48 26)4‡.#) '
        '4‡);80 6* ;48 †8P60) )85; '
        '1‡(;:}‡*8 †83(88) 5*† ;46(;88* '
        '96*?;8) *‡(;485); 5*† '
        '2: *‡(;4 956* 2(5*-4 )8P8*;4 '
        '0692 85); )6†8 )4‡‡; 1(‡9 '
        ';48 081; 8:8 ‡1 ;48 †85;4#)}485† '
        '5 288 06*8 1(‡9 ;48 ;(88 '
        ';4(‡?34 ;48 )4‡; 161;: 188; ‡?;'
    )
    unknown_symbol_string = UnknownSymbolString(cypher)
    unknown_symbol_string[cypher.index(' ')] = ' '
    print(unknown_symbol_string)
    unknown_symbol_string[cypher.index('8')] = 'E'
    print(unknown_symbol_string)
    unknown_symbol_string[cypher.index(';')] = 'T'
    unknown_symbol_string[cypher.index('4')] = 'H'
    print(unknown_symbol_string)
    unknown_symbol_string[cypher.index('(')] = 'R'
    print(unknown_symbol_string)
    unknown_symbol_string[cypher.index('‡')] = 'O'
    unknown_symbol_string[cypher.index('?')] = 'U'
    unknown_symbol_string[cypher.index('3')] = 'G'
    print(unknown_symbol_string)
    unknown_symbol_string[cypher.index('†')] = 'D' # GOOD
    print(unknown_symbol_string)
    unknown_symbol_string[cypher.index(')')] = 'S' # DEGREES
    print(unknown_symbol_string)
    unknown_symbol_string[cypher.index('1')] = 'F' # FEET
    print(unknown_symbol_string)
    unknown_symbol_string[cypher.index('9')] = 'M' # FROM
    print(unknown_symbol_string)
    unknown_symbol_string[cypher.index('0')] = 'L' # LEFT
    print(unknown_symbol_string)
    unknown_symbol_string[cypher.index('5')] = 'A' # GLASS
    print(unknown_symbol_string)
    unknown_symbol_string[cypher.index(':')] = 'Y' # FORTY
    print(unknown_symbol_string)
    unknown_symbol_string[cypher.index('6')] = 'I' # FIFTY
    print(unknown_symbol_string)
    unknown_symbol_string[cypher.index('*')] = 'N' # IN
    print(unknown_symbol_string)
    unknown_symbol_string[cypher.index('P')] = 'V' # DEVIL
    print(unknown_symbol_string)
    unknown_symbol_string[cypher.index('2')] = 'B' # BY
    print(unknown_symbol_string)
    unknown_symbol_string[cypher.index('.')] = 'P' # BISHOP
    print(unknown_symbol_string)
    unknown_symbol_string[cypher.index('-')] = 'C'
    print(unknown_symbol_string)
    unknown_symbol_string[cypher.index('#')] = '\''
    print(unknown_symbol_string)
    unknown_symbol_string[cypher.index('}')] = '-'
    print(unknown_symbol_string)




