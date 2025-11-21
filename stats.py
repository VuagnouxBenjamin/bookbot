def get_num_words(string):
    return len(string.split())

def get_character_stats(string): 
    stats = {}

    for char in string.lower():
        if not char in stats:
            stats[char] = 1
        else: 
            stats[char] += 1

    return stats
def sort_on(dict): 
    return dict["num"]

def sort_stat_dictionary(stat_dictionary): 
    stat_list = []
    for stat in stat_dictionary:
        dict = {}
        dict["char"] = stat
        dict["num"] = stat_dictionary[stat]
        stat_list.append(dict)
        
    stat_list.sort(reverse=True, key=sort_on)
    
    return stat_list