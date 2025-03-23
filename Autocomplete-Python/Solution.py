import sys
import io
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

class Term:
    def __init__(self, query, weight):
        if weight < 0:
            raise ValueError("Weight must be non-negative")
        self.query = query
        self.weight = weight
    
    def __lt__(self, other):
        return self.query < other.query
    
    def __repr__(self):
        return f"{self.weight}\t{self.query}"


class BinarySearchDeluxe:
    def first_index_of(terms, prefix):
        low, high = 0, len(terms)
        while low < high:
            mid = (low + high) // 2
            if terms[mid].query.startswith(prefix):
                high = mid
            elif terms[mid].query < prefix:
                low = mid + 1
            else:
                high = mid
        return low if low < len(terms) and terms[low].query.startswith(prefix) else -1


    def last_index_of(terms, prefix):
        low, high = 0, len(terms)
        while low < high:
            mid = (low + high) // 2
            if terms[mid].query.startswith(prefix):
                low = mid + 1
            elif terms[mid].query < prefix:
                low = mid + 1
            else:
                high = mid
        return low - 1 if low > 0 and terms[low - 1].query.startswith(prefix) else -1

class Autocomplete:
    def __init__(self, terms):
        self.terms = sorted(terms, key=lambda t: t.query)
    
    def all_matches(self, prefix):
        first = BinarySearchDeluxe.first_index_of(self.terms, prefix)
        last = BinarySearchDeluxe.last_index_of(self.terms, prefix)
        if first == -1 or last == -1:
            return []
        matched_terms = self.terms[first:last+1]
        return sorted(matched_terms, key=lambda term: term.weight, reverse=True)
    
    def number_of_matches(self, prefix):
        first = BinarySearchDeluxe.first_index_of(self.terms, prefix)
        last = BinarySearchDeluxe.last_index_of(self.terms, prefix)
        return 0 if first == -1 or last == -1 else last - first + 1


def read_file(filename):
    with open(filename, 'r', encoding='utf-8') as file:
        n = int(file.readline().strip())
        terms = []
        for _ in range(n):
            line = file.readline().strip().split('\t')
            weight = int(line[0])
            query = line[1]
            terms.append(Term(query, weight))
        return terms


def main():
    filename = input().strip()
    terms = read_file(filename)
    k = int(input().strip())
    autocomplete = Autocomplete(terms)

    while True:
        try:
            prefix = input().strip()
            results = autocomplete.all_matches(prefix)
            print(f"{autocomplete.number_of_matches(prefix)} matches")
            for i in range(min(k, len(results))):
                print(results[i])
        except EOFError:
            break


main()