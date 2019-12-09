#!/usr/bin/env python
# -*- coding: utf-8 -*-

from collections import defaultdict
from queue import Empty, LifoQueue


OPCODE_PARAMS = [None, 3, 3, 1, 1, 2, 2, 3, 3, 1]
OPCODE_HALT = 99


class CPUError(Exception):
    pass


class Memory(defaultdict):

    def _check_key(self, key):
        if key < 0:
            raise TypeError(f'Address cannot be negative: {key}')

    def __setitem__(self, key, value):
        self._check_key(key)
        return defaultdict.__setitem__(self, key, value)

    def __getitem__(self, key):
        self._check_key(key)
        return defaultdict.__getitem__(self, key)


def _parse_instruction(instruction):
    opcode = instruction % 100
    modes = [
        (instruction // 100) % 10,
        (instruction // 1000) % 10,
        (instruction // 10000) % 10,
    ]
    return opcode, modes


class IntcodeComputer:

    def __init__(self, code, in_queue=None, out_queue=None, init=None):
        self.code = Memory(
            int, [(i, int(x)) for i, x in enumerate(code.split(','))]
        )
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

    def step(self):
        opcode, modes = _parse_instruction(self.code[self.pc])
        self.pc += 1
        if opcode == OPCODE_HALT:
            self.halt = True
            return OPCODE_HALT
        params = self._get_params(opcode, modes)
        self.pc += len(params)
        try:
            method = getattr(self, f'_opcode_{opcode:02d}')
            method(*params)
        except AttributeError:
            raise CPUError(f'Unknown Opcode {opcode}')

    def run(self):
        self.halt = False
        while True:
            if self.step():
                break

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


def run_fast(code, init=None, inputs=None):
    ic = IntcodeComputer(code, init=init)
    if inputs:
        for inp in reversed(inputs):
            ic.in_queue.put(inp)
    ic.run()
    tmp = []
    while True:
        try:
            tmp.append(ic.output)
        except Empty:
            break
    for out in reversed(tmp):
        print(tmp)
