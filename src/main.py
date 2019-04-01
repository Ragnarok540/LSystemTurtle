import cmd, sys
from lsystem import LSystem

class LSystemShell(cmd.Cmd):
    intro = 'Welcome to the LSystem shell. Type help or ? to list commands.\n'
    prompt = '(lsystem) '

    def preloop(self):
        self.lsystem = None
        super(LSystemShell, self).preloop()
    
    def do_set(self, arg):
        'Set LSystem (algae, drangoncurve, twindragon, binarytree)'
        switcher = {
            'algae': LSystem('A', {'A': 'AB', 'B': 'A'}),
            'dragoncurve': LSystem('FX', {'X': 'X+YF+', 'Y': '-FX-Y'}),
            'twindragon': LSystem('FX+FX+', {'X': 'X+YF', 'Y': 'FX-Y'}),
            'binarytree': LSystem('0', {'1': '11', '0': '1[+0]-0'})
        }
        self.lsystem = switcher.get(arg, None)

    def do_draw(self, arg):
        'Draw the LSystem (args: generation distance angle)'
        if self.lsystem == None:
            print('LSystem must be set first')
        else:
            self.lsystem.draw(*parse(arg))

    def do_print(self, arg):
        'Print the LSystem string (arg: generation)'
        if self.lsystem == None:
            print('LSystem must be set first')
        else:
            print(self.lsystem.generation(int(arg), self.lsystem.axiom))

    def do_def(self, arg):
        'Print definition of the LSystem'
        if self.lsystem == None:
            print('LSystem must be set first')
        else:
            print(f'Axiom: {self.lsystem.axiom}')
            print(f'Rules: {self.lsystem.rules}')

def parse(arg):
    'Convert a series of zero or more numbers to an argument tuple'
    return tuple(map(int, arg.split()))

if __name__ == '__main__':
    LSystemShell().cmdloop()
