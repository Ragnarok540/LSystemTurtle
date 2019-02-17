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
                    

lsystem = LSystem('A', {'A': 'AB', 'B': 'A'})

print(lsystem.generation(0, lsystem.axiom))
print(lsystem.generation(1, lsystem.axiom))
print(lsystem.generation(2, lsystem.axiom))
print(lsystem.generation(3, lsystem.axiom))

lsystem = LSystem('0', {'1': '11', '0': '1[0]0'})

print(lsystem.generation(0, lsystem.axiom))
print(lsystem.generation(1, lsystem.axiom))
print(lsystem.generation(2, lsystem.axiom))
print(lsystem.generation(3, lsystem.axiom))

lsystem = LSystem('F', {'F': 'F+F-F-F+F'})

print(lsystem.generation(0, lsystem.axiom))
print(lsystem.generation(1, lsystem.axiom))
print(lsystem.generation(2, lsystem.axiom))
print(lsystem.generation(3, lsystem.axiom))


