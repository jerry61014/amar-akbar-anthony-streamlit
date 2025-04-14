
import random
from datetime import datetime

amar_cards = ['A', '2', '3', '4', '5', '6']
akbar_cards = ['7', '8', '9', '10']
anthony_cards = ['J', 'Q', 'K']

def create_deck():
    suits = ['♠', '♥', '♦', '♣']
    deck = [f"{rank}{suit}" for rank in amar_cards + akbar_cards + anthony_cards for suit in suits]
    return deck

def get_group(card):
    rank = card[:-1]
    if rank in amar_cards:
        return 'Amar'
    elif rank in akbar_cards:
        return 'Akbar'
    elif rank in anthony_cards:
        return 'Anthony'

def simulate_round():
    deck = create_deck()
    random.shuffle(deck)
    split_index = random.randint(1, len(deck)-1)
    part1, part2 = deck[:split_index], deck[split_index:]
    selected_part = random.choice([part1, part2])
    if len(selected_part) < 2:
        return None
    discarded = selected_part[0]
    scanned = selected_part[1]
    result = get_group(scanned)
    log_entry = {
        "timestamp": datetime.now(),
        "discarded": discarded,
        "scanned": scanned,
        "result": result
    }
    return log_entry
