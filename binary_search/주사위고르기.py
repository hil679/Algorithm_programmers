from itertools import product, combinations

def solution(dice):
    one_dice_num = int(len(dice) / 2) # len(dice) // 2
    all_dice_num = len(dice)
    dice_number = [i for i in range(1, len(dice) + 1)]
    dice_combs = list(combinations(dice_number, one_dice_num))
    
    items = []
    comb = list()
    for dice_comb in dice_combs:
        for number in dice_comb:
            items.append(dice[number - 1])
        comb.append(sorted(sum(c) for c in list(product(*items))))
        items.clear()
        
    A, B = 0, 0
    win_dice_choice = 0
    answer=[]
    for i in range(len(comb)):
        A = comb[i]
        B = comb[len(comb) - i - 1]
        
        temp_win_dice_choice = 0
        for a_sum in A:
            start = 0
            end = len(comb[i]) - 1
            while(start <= end):
                mid = (start + end) // 2
                if B[mid] < a_sum:
                    start = mid + 1
                else:
                    end = mid -1
            temp_win_dice_choice += start # 배열의 크기가 모두 같아서 가능한 일인 듯, mid가 많이 전진할 수록 많이 이긴다는 거니까.
        if win_dice_choice < temp_win_dice_choice:
            win_dice_choice = temp_win_dice_choice
            answer = dice_combs[i]
    return answer