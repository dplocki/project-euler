# https://projecteuler.net/problem=54

from collections import Counter
from enum import IntEnum
from typing import Tuple
 
# creating enumerations using class
class Hand(IntEnum):
    HighCard = 1
    OnePair = 2
    TwoPairs = 3
    ThreeOfKind = 4
    Straight = 5
    Flush = 6
    FullHouse = 7
    FourOfKind = 8
    StraightFlush = 9
    RoyalFlush = 10

def parse_value(rawHand: str) -> int:
    if rawHand in '0123456789':
        return int(rawHand)

    if rawHand == 'T':
        return 10

    if rawHand == 'J':
        return 11

    if rawHand == 'Q':
        return 12

    if rawHand == 'K':
        return 13

    if rawHand == 'A':
        return 14

def parse_hand(rawHand: str) -> Tuple[Hand, int, int]:
    cards = [(parse_value(rawHand[0]), rawHand[1]) for rawHand in rawHand.split()]
    values_counter = Counter(card[0] for card in cards)
    suits = Counter(card[1] for card in cards)
    values = sorted(values_counter.keys(), reverse=True)
    are_consecutive = values[0] - values[-1] == 4 and len(set(values)) == 5

    if len(suits) == 1 and are_consecutive and values[0] == 14:
        return Hand.RoyalFlush, 

    if len(suits) == 1 and are_consecutive:
        return Hand.StraightFlush, values[0]

    four_of_kind = [key for key, value in values_counter.items() if value == 4]
    if len(four_of_kind) == 1:
        return Hand.FourOfKind, four_of_kind[0], *list(value for value in values if value != four_of_kind[0])

    three_of_kind = [key for key, value in values_counter.items() if value == 3]
    two_of_kind = [key for key, value in values_counter.items() if value == 2]
    if len(three_of_kind) == 1 and len(two_of_kind) == 1:
        return Hand.FullHouse, three_of_kind[0], two_of_kind[0]

    if len(suits) == 1:
        return Hand.Flush, *values

    if are_consecutive:
        return Hand.Straight, *values

    if len(three_of_kind) == 1:
        return Hand.ThreeOfKind, three_of_kind[0], *list(value for value in values if value != three_of_kind[0])

    if len(two_of_kind) == 2:
        pairs_values = sorted([two_of_kind[0], two_of_kind[1]], reverse=True)
        return Hand.TwoPairs, *pairs_values, *list(value for value in values if value not in pairs_values)

    if len(two_of_kind) == 1:
        return Hand.OnePair, two_of_kind[0], *list(value for value in values if value != two_of_kind[0])

    return Hand.HighCard, *values

def is_player_1_win(first_player_hand: Tuple, second_player_hand: Tuple) -> bool:
    for p1, p2 in zip(first_player_hand, second_player_hand):
        if p1 > p2:
            return True
        elif p1 < p2:
            return False

    raise Exception('Equal?')

assert parse_hand('AC JC TC QC KC')[0] == Hand.RoyalFlush
assert parse_hand('9C JC TC QC KC') == (Hand.StraightFlush, 13)
assert parse_hand('9H 9D 9C 9S KC') == (Hand.FourOfKind, 9, 13)
assert parse_hand('2H 2D 4C 4D 4S') == (Hand.FullHouse, 4, 2)
assert parse_hand('2H AH 4H 3H QH') == (Hand.Flush, 14, 12, 4, 3, 2)
assert parse_hand('2H 3D 5C 6D 4S') == (Hand.Straight, 6, 5, 4, 3, 2)
assert parse_hand('9H 9D 8C 9S KC') == (Hand.ThreeOfKind, 9, 13, 8)
assert parse_hand('2H 2D 9C 9S KC') == (Hand.TwoPairs, 9, 2, 13)
assert parse_hand('2H 2D 7C 9S KC') == (Hand.OnePair, 2, 13, 9, 7)
assert parse_hand('2H 3D 7C 9S KC') == (Hand.HighCard, 13, 9, 7, 3, 2)

def test_is_player_1_win(hand_1: str, hand_2: str): return is_player_1_win(parse_hand(hand_1), parse_hand(hand_2))

assert test_is_player_1_win('5H 5C 6S 7S KD', '2C 3S 8S 8D TD') == False
assert test_is_player_1_win('5D 8C 9S JS AC', '2C 5C 7D 8S QH') == True
assert test_is_player_1_win('2D 9C AS AH AC', '3D 6D 7D TD QD') == False
assert test_is_player_1_win('4D 6S 9H QH QC', '3D 6D 7H QD QS') == True
assert test_is_player_1_win('2H 2D 4C 4D 4S', '3C 3D 3S 9S 9D') == True

# file is aviable on link: https://projecteuler.net/project/resources/p054_poker.txt
with open('p054_poker.txt', 'r') as file:
    print(sum(1
        for line in file.readlines()
        if is_player_1_win(parse_hand(line[0:3 * 5 - 1]), parse_hand(line[3 * 5:]))))
