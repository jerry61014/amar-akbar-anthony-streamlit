
import random

def monte_carlo_predict(simulations=10000):
    amar, akbar, anthony = 0, 0, 0

    for _ in range(simulations):
        card_value = random.choice(
            ['A','2','3','4','5','6']*4 +
            ['7','8','9','10']*4 +
            ['J','Q','K']*4
        )

        if card_value in ['A','2','3','4','5','6']:
            amar += 1
        elif card_value in ['7','8','9','10']:
            akbar += 1
        else:
            anthony += 1

    prediction = max(
        [('Amar', amar), ('Akbar', akbar), ('Anthony', anthony)],
        key=lambda x: x[1]
    )[0]

    return prediction

def draw_card():
    deck = (
        ['A','2','3','4','5','6']*4 +
        ['7','8','9','10']*4 +
        ['J','Q','K']*4
    )
    random.shuffle(deck)
    discarded_card = deck.pop(0)
    result_card = deck.pop(0)

    if result_card in ['A','2','3','4','5','6']:
        winner = 'Amar'
    elif result_card in ['7','8','9','10']:
        winner = 'Akbar'
    else:
        winner = 'Anthony'

    return discarded_card, result_card, winner
