def find_max_profit(honey_list, curr_idx, curr_sum, curr_profit):
    if curr_idx >= len(honey_list):
        return curr_profit
    # 현재 꿀을 선택하는 경우
    choose = 0
    if curr_sum + honey_list[curr_idx] <= C:
        choose = find_max_profit(honey_list, curr_idx+1,
                        curr_sum+honey_list[curr_idx],
                        curr_profit+honey_list[curr_idx]**2)
    not_choose = find_max_profit(honey_list, curr_idx+1, curr_sum, curr_profit)
    return max(choose, not_choose)

def calculate_max_profit(honey_list):
    result = find_max_profit(honey_list, 0, 0, 0)
    return result