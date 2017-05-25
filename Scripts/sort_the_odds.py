def sort_array(arr):
    odds_numbers = sorted((x for x in arr if x % 2 != 0), reverse=True)
    print odds_numbers
    # odds_numbers = odds_numbers[::-1]
    sort_odds = [x if x % 2 == 0 else odds_numbers.pop() for x in arr]
    print sort_odds
sort_array([5, 3, 2, 8, 1, 4])
      

