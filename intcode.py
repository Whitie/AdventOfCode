#!/usr/bin/env python
# -*- coding: utf-8 -*-

from queue import LifoQueue


MEMORY = 10000
OPCODE_PARAMS = {
    1: 3,
    2: 3,
    3: 1,
    4: 1,
    5: 2,
    6: 2,
    7: 3,
    8: 3,
    9: 1,
}


class CPUError(Exception):
    pass


def _parse_instruction(instruction):
    tmp, opcode = divmod(instruction, 100)
    modes = []
    for _ in range(3):
        tmp, mode = divmod(tmp, 10)
        modes.append(mode)
    return opcode, modes


class IntcodeComputer:

    def __init__(self, code, in_queue=None, out_queue=None, init=None):
        self.code = [int(x) for x in code.split(',')] + [0] * MEMORY
        self.in_queue = in_queue or LifoQueue()
        self.out_queue = out_queue or LifoQueue()
        self.init = init
        self.pc = 0
        self._input = self.in_queue.get
        self._output = self.out_queue.put
        self.halt = None
        self.relative_base = 0

    def _get_params(self, opcode, modes):
        params = []
        for i in range(OPCODE_PARAMS[opcode]):
            if modes[i] == 0:
                params.append(self.code[self.pc + i])
            elif modes[i] == 1:
                params.append(self.pc + i)
            else:
                params.append(self.code[self.pc + i] + self.relative_base)
        return params

    @property
    def output(self):
        return self.out_queue.get_nowait()

    def run(self):
        self.halt = False
        while True:
            opcode, modes = _parse_instruction(self.code[self.pc])
            self.pc += 1
            if opcode == 99:
                self.halt = True
                break
            params = self._get_params(opcode, modes)
            self.pc += len(params)
            try:
                method = getattr(self, f'_opcode_{opcode:02d}')
                method(*params)
            except AttributeError:
                raise CPUError(f'Unbekannter Opcode {opcode}')

    def _opcode_01(self, a, b, target):
        self.code[target] = self.code[a] + self.code[b]

    def _opcode_02(self, a, b, target):
        self.code[target] = self.code[a] * self.code[b]

    def _opcode_03(self, target):
        if self.init is not None:
            self.code[target] = self.init
            self.init = None
        else:
            self.code[target] = self._input()

    def _opcode_04(self, a):
        self._output(self.code[a])

    def _opcode_05(self, a, b):
        if self.code[a]:
            self.pc = self.code[b]

    def _opcode_06(self, a, b):
        if self.code[a] == 0:
            self.pc = self.code[b]

    def _opcode_07(self, a, b, target):
        if self.code[a] < self.code[b]:
            self.code[target] = 1
        else:
            self.code[target] = 0

    def _opcode_08(self, a, b, target):
        if self.code[a] == self.code[b]:
            self.code[target] = 1
        else:
            self.code[target] = 0

    def _opcode_09(self, a):
        self.relative_base += self.code[a]
