#!/usr/bin/env python3

from typing import List

class hhc:
    def __init__(self, input: List[str]):
        self.iram = input
        self.acc_val = 0
        self.inst_ptr = 0
        self.func = {}
        self.func['acc'] = self.acc
        self.func['jmp'] = self.jmp
        self.func['nop'] = self.nop

    def reset(self) -> None:
        self.inst_ptr = 0
        self.acc_val = 0

    def run(self) -> bool:
        visited = []
        while True:
            visited.append(self.inst_ptr)
            inst = self.iram[self.inst_ptr]
            self.inst_ptr += 1
            self.decode(inst)
            if self.inst_ptr in visited:
                #print(self.inst_ptr, self.acc_val)
                return False
            elif self.inst_ptr == len(self.iram):
                return True
            elif self.inst_ptr > len(self.iram):
                return False

    def decode(self, line: str) -> None:
        (operand, value) = line.split()
        self.func[operand](value)

    def acc(self, value) -> None:
        self.acc_val += int(value)

    def jmp(self, value) -> None:
        # Undo implicit instruction pointer increment
        self.inst_ptr += int(value) - 1

    def nop(self, value) -> None:
        return


with open('./input.txt') as fd:
    items = [x.strip() for x in fd]

gameboy = hhc(items)
for idx, inst in enumerate(gameboy.iram):
    save_inst = gameboy.iram[idx].split()
    if save_inst[0] in ['jmp', 'nop']:
        new_op = 'jmp' if save_inst[0] == 'nop' else 'nop'
        gameboy.iram[idx] = ' '.join([new_op, save_inst[1]])
        if gameboy.run():
            print(idx, gameboy.acc_val)
            exit()
        gameboy.iram[idx] = ' '.join(save_inst)
        gameboy.reset()
