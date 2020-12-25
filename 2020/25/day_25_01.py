#!/usr/bin/env python
# -*- coding: utf-8 -*-


INPUT = [13233401, 6552760]
TEST = [5764801, 17807724]
SUBJECT_NUM = 7
MAGIC = 20201227


def get_loop_size(pubkey):
    value = 1
    loops = 0
    while value != pubkey:
        value *= SUBJECT_NUM
        value %= MAGIC
        loops += 1
    return loops


def derive_key(pubkey, loops):
    key = 1
    for _ in range(loops):
        key *= pubkey
        key %= MAGIC
    return key


def main():
    # card_pubkey, door_pubkey = TEST
    card_pubkey, door_pubkey = INPUT
    loops_card = get_loop_size(card_pubkey)
    loops_door = get_loop_size(door_pubkey)
    print(loops_card, loops_door)
    secret_key_1 = derive_key(card_pubkey, loops_door)
    secret_key_2 = derive_key(door_pubkey, loops_card)
    print(secret_key_1, secret_key_2)


if __name__ == '__main__':
    main()
