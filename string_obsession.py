def meera_string_obsession(patterns, target_string):
# print("inside meera_string_obsession --check")  
    substr_results_memo = {}

    def substr_removal_helper(current_str, used_patterns):
        key = (current_str, tuple(sorted(used_patterns)))
        if key in substr_results_memo:
            return substr_results_memo[key]
        
        max_substr_removals = 0
        
        for index, pattern in enumerate(patterns):
            if index in used_patterns:
                continue
            position = current_str.find(pattern)
            if position != -1:
                # print("inside if condition --check")
                updated_meera_str = current_str[:position] + current_str[position + len(pattern):]
                new_used_patterns = used_patterns.copy()
                new_used_patterns.add(index)
                current_removals = 1 + substr_removal_helper(updated_meera_str, new_used_patterns)
                max_substr_removals = max(max_substr_removals, current_removals)
        substr_results_memo[key] = max_substr_removals
        return max_substr_removals
    return substr_removal_helper(target_string, set())

number_of_patterns = int(input())
meera_substrings = input().split()
meera_main_string = input().strip()
print(meera_string_obsession(meera_substrings, meera_main_string))
