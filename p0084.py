# https://projecteuler.net/problem=84
# More details: https://www.monopolyland.com/rolling-doubles-in-monopoly/
from collections import defaultdict
from functools import cache
from itertools import cycle
import random
from typing import Dict, Generator

BOARD = [
    'GO', 'A1', 'CC1', 'A2', 'T1', 'R1', 'B1', 'CH1', 'B2', 'B3',
    'JAIL', 'C1', 'U1', 'C2', 'C3', 'R2', 'D1', 'CC2', 'D2', 'D3',
    'FP', 'E1', 'CH2', 'E2', 'E3', 'R3', 'F1', 'F2', 'U2', 'F3',
    'G2J', 'G1', 'G2', 'CC3', 'G3', 'R4', 'CH3', 'H1', 'T2', 'H2'
]
BOARD_SIZE = len(BOARD)

@cache
def goto_field(fieldName: str) -> int:
    return BOARD.index(fieldName)

@cache
def goto_find_next(from_field: int, field_name_startswith: str) -> int:
    while True:
        from_field = (from_field + 1) % BOARD_SIZE
        if BOARD[from_field].startswith(field_name_startswith):
            return from_field

def build_cards_deck(card_number: int) -> Generator[int, None, None]:
    cards = list(range(card_number))
    random.shuffle(cards)
    for card in cycle(cards):
        yield card

def simulation(player_dice_size: int) -> Generator[int, None, None]:
    CHANCE_CARDS_NUMBER = 16

    community_chest_cards = build_cards_deck(CHANCE_CARDS_NUMBER)
    chances_cards = build_cards_deck(CHANCE_CARDS_NUMBER)

    player_position = 0
    double_dice_counter = 0

    while True:
        dice1 = random.randrange(player_dice_size) + 1
        dice2 = random.randrange(player_dice_size) + 1

        if dice1 == dice2:
            double_dice_counter += 1
        else:
            double_dice_counter = 0

        if double_dice_counter == 3:
            player_position = goto_field('JAIL')
        else:
            player_position = (player_position + dice1 + dice2) % BOARD_SIZE
            if BOARD[player_position].startswith('CC'):
                card = next(community_chest_cards)

                if card == 1:
                    player_position = goto_field('GO')
                elif card == 2:
                    player_position = goto_field('JAIL')

            elif BOARD[player_position].startswith('CH'):
                card = next(chances_cards)

                if card == 1:
                    player_position = goto_field('GO')
                elif card == 2:
                    player_position = goto_field('JAIL')
                elif card == 3:
                    player_position = goto_field('C1')
                elif card == 4:
                    player_position = goto_field('E3')
                elif card == 5:
                    player_position = goto_field('H2')
                elif card == 6:
                    player_position = goto_field('R1')
                elif card == 7 or card == 8:
                    player_position = goto_find_next(player_position, 'R')
                elif card == 9:
                    player_position = goto_find_next(player_position, 'U')
                elif card == 10:
                    player_position = (player_position - 3) % BOARD_SIZE

            elif BOARD[player_position] == 'G2J':
                player_position = goto_field('JAIL')

        if BOARD[player_position] == 'JAIL':
            double_dice_counter = 0

        yield player_position

def run_simulation(player_dice_size: int):
    ROUND_NUMBER_PER_GAME = 1000
    NUMBER_OF_GAMES = 2000

    results = defaultdict(int)

    for _ in range(NUMBER_OF_GAMES):
        for position, _ in zip(simulation(player_dice_size), range(ROUND_NUMBER_PER_GAME)):
            results[position] += 1

    return results

def build_modal_string(results: Dict[int, int]) -> str:
    return ''.join(
            str(v).zfill(2)
            for v in list(v for v, _ in sorted(
                    results.items(),
                    key=lambda x:x[1],
                    reverse=True)
                )[:3])


assert build_modal_string(run_simulation(6)) == '102400'
print(build_modal_string(run_simulation(4)))
