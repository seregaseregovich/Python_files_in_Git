''' Iterators and generators.
What is different. '''


# Example for ITERATOR:
# ====================================

class StringByLetter:
    def __init__(self, string):
        self.string = string
        self.str_len = len(string)
        self.position = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.position < self.str_len:
            letter = self.string[self.position]
            self.position += 1
            return letter.upper()
        raise StopIteration


for letter in StringByLetter('Hi, Diletante'):
    print(letter)
print()
print('===========================')
print()


# Example for GENERATOR:
# ====================================


def string_by_letter(string):
    for letter in string:
        yield letter.upper()


for letter in string_by_letter('Hi, Diletante'):
    print(letter)

# Conclusion:
# ================================================
# A generator is faster than an iterator
# Generator is an inheritor of the iterator class
