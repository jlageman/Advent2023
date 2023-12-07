dat = open('input7.txt').read().splitlines()
hands = [x.split()[0] for x in dat]
hand_values = [int(x.split()[1]) for x in dat]
value_dict = {}
for hand, val in zip(hands, hand_values):
    value_dict[hand] = val

def get_answer(card_values, value_dict, five_kind, four_kind, full_house, three_kind, two_pair, one_pair, high_card):
    # sort according to value
    categories = [five_kind, four_kind, full_house, three_kind, two_pair, one_pair, high_card]
    hand_order = []
    for cat in categories:
        if not cat:
            continue
        elif len(cat)==1:
            hand_order.extend(cat)
        else:
            proxies = []
            for hand in cat:
                for rep in card_values.keys():
                    hand = hand.replace(rep, card_values[rep])
                proxies.append(hand)
            hand_order.extend([cat[proxies.index(x)] for x in sorted(proxies)])

    # calculate answer
    answer = 0
    rank = len(hand_order)
    for hand in hand_order:
        answer += rank*value_dict[hand]
        rank -= 1
        
    return answer

# PART 1
card_values = {'A': 'A', 'K': 'B', 'Q': 'C', 'J': 'D', 'T': 'E', '9': 'F', '8': 'G', '7': 'H', '6': 'I', '5': 'J', '4': 'K', '3': 'L', '2': 'M'};
five_kind, four_kind, full_house, three_kind, two_pair, one_pair, high_card = [],[],[],[],[],[],[]

for hand in hands:
    if len(set(hand)) == 1:
        five_kind.append(hand)
    elif len(set(hand)) == 2:
        if hand.count(hand[0]) == 1 or hand.count(hand[0]) == 4:
            four_kind.append(hand)
        elif hand.count(hand[0]) == 2 or hand.count(hand[0]) == 3:
            full_house.append(hand)
    elif len(set(hand)) == 3:
        if any([hand.count(hand[x])==3 for x in range(len(hand))]):
            three_kind.append(hand)
        else:
            two_pair.append(hand)
    elif len(set(hand)) == 4:
        one_pair.append(hand)
    elif len(set(hand)) == 5:
        high_card.append(hand)

answer1 = get_answer(card_values, value_dict, five_kind, four_kind, full_house, three_kind, two_pair, one_pair, high_card)
    
# PART 2
card_values = {'A': 'A', 'K': 'B', 'Q': 'C', 'J': 'N', 'T': 'E', '9': 'F', '8': 'G', '7': 'H', '6': 'I', '5': 'J', '4': 'K', '3': 'L', '2': 'M'};
five_kind, four_kind, full_house, three_kind, two_pair, one_pair, high_card = [],[],[],[],[],[],[]

for hand in hands:
    if len(set(hand)) == 1:
        five_kind.append(hand)
    elif len(set(hand)) == 2:
        if 'J' in hand:
            five_kind.append(hand)
        elif hand.count(hand[0]) == 1 or hand.count(hand[0]) == 4:
            four_kind.append(hand)
        elif hand.count(hand[0]) == 2 or hand.count(hand[0]) == 3:
            full_house.append(hand)
    elif len(set(hand)) == 3:
        if any([hand.count(hand[x])==3 for x in range(len(hand))]):
            if 'J' in hand:
                four_kind.append(hand)
            else:
                three_kind.append(hand)
        else:
            if 'J' in hand:
                if hand.count('J') == 2:
                    four_kind.append(hand)
                else:
                    full_house.append(hand)
            else:
                two_pair.append(hand)
    elif len(set(hand)) == 4:
        if 'J' in hand:
            three_kind.append(hand)
        else:
            one_pair.append(hand)
    elif len(set(hand)) == 5:
        if 'J' in hand:
            one_pair.append(hand)
        else:
            high_card.append(hand)

answer2 = get_answer(card_values, value_dict, five_kind, four_kind, full_house, three_kind, two_pair, one_pair, high_card)