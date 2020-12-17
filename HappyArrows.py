import random

PURPLE = '\033[95m'
BLUE = '\033[94m'
GREEN = '\033[92m'
YELLOW = '\033[93m'
RED = '\033[91m'
RESET = '\033[0m'
BOLD = '\033[1m'
UNDERLINE = '\033[4m'

arrows = "⬆↗→↘↓↙←↖"

class RubikTime:
    def __init__(self, size=3):
        self.size = size
        self.clocks = [ [ 0 for j in range(size)] for i in range(size)]
        self.handles = [ [ [i, j] for j in range(size - 1)] for i in range(size - 1)]
        self.current = 0
        self.shuffle()
        print("\033[2J")
        print(self)

    def loop(self):
        while self.game_over() == False:
            add = self.get_input()
            self.handle_move(add)
            print(self)
        if args.fireworks == False:
            print("Well Played and Happy Birthday Erwan! <3")
        else:
            Screen.wrapper(demo)

    def shuffle(self):
        size = (self.size - 1) ** 2
        arrow_len = len(arrows)
        for _ in range(size ** 2):
            self.current = random.randint(0, size - 1)
            add = random.randint(-arrow_len + 1, arrow_len - 1)
            self.handle_move(add)
        self.current = 0

    def rotate(self, move, add):
        self.clocks[move[0]][move[1]] = (self.clocks[move[0]][move[1]] + add) % len(arrows)
        while self.clocks[move[0]][move[1]] < 0:
            self.clocks[move[0]][move[1]] += len(arrows)

    def handle_move(self, add):
        size = self.size - 1
        handle = self.handles[self.current // size][self.current % size]
        move = [handle[0] + 0, handle[1] + 0]
        self.rotate(move, add)
        move = [handle[0] + 1, handle[1] + 0]
        self.rotate(move, add)
        move = [handle[0] + 0, handle[1] + 1]
        self.rotate(move, add)
        move = [handle[0] + 1, handle[1] + 1]
        self.rotate(move, add)

    def game_over(self):
        for clocks in self.clocks:
            for clock in clocks:
                if clock != 0:
                    return False
        return True

    def get_input(self):
        while True:
            data = input()
            try:
                cur = int(data)
                if cur >= 0 and cur < (self.size - 1) ** 2:
                    self.current = cur
                    print(self)
            except:
                pass
            if data == "r":
                return 1
            elif data =="t":
                return -1


    def __str__(self):
        msg = ""
        msg += "\033[0;0H"
        max_len = len(str(((self.size - 1) ** 2) - 1))
        label = 0
        for row in range(self.size):
            labels = ""
            for col in range(self.size):
                c = self.clocks[row][col]
                if c == 0:
                    msg += BLUE
                else:
                    msg += RED
                msg += arrows[c] + " " + " " * max_len
                msg += RESET
                if col < self.size - 1 and label < (self.size - 1) ** 2:
                    if label == self.current:
                        labels += GREEN + BOLD
                    labels += "  " + "{1:<{0}d}".format(max_len, label)
                    if label == self.current:
                        labels += RESET
                    label += 1
            msg += "\n"
            if labels:
                msg += labels + "\n"
        msg += "⟳ R" + " " * (self.size * (2 + max_len) - 6 - 1) + "T↻"
        msg += "\n"
        return msg



if __name__ == "__main__":
    import argparse
    from end import demo
    from asciimatics.screen import Screen
    parser = argparse.ArgumentParser()
    parser.add_argument("-s", "--size", help="Side size of RubikTime", default=5, type=int)
    parser.add_argument("-f", "--fireworks", help="Display fireworks if victory", action='store_true')
    args = parser.parse_args()
    HappyPuzzle = RubikTime(args.size)
    HappyPuzzle.loop()
