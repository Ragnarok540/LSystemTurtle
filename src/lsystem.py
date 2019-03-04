from turtle import *

class LSystem:

    def __init__(self, axiom, rules):
        self.axiom = axiom
        self.rules = rules

    def generation(self, n, word):
        if n == 0:
            return word
        else:
            result = ''
            for char in list(word):
                if char in self.rules:
                    result += self.rules[char]
                else:
                    result += char
            return self.generation(n - 1, result)

    def draw(self, n, distance, angle):
        ls = self.generation(n, self.axiom)
        switcher = {
            'F': lambda: forward(distance),
            'G': lambda: forward(distance),
            '+': lambda: left(angle),
            '-': lambda: right(angle)
        }
        for char in list(ls):
            func = switcher.get(char, lambda: None)
            func()

