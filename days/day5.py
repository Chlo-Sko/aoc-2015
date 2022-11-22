from Day import Day

# Create Day Object & Get Input
day = Day(5, "Doesn't He Have Intern-Elves for This?")

# Function That Returns True If String Contains at Least Three Vowels
def has_three_vowels(string):
    vowels = ['a','e','i','o','u']
    vowel_count = 0
    for char in string:
        if char in vowels:
            vowel_count += 1
    if vowel_count >= 3:
        return True
    else: return False

# Function That Returns True if String Contains Double Letter
def has_double_letter(string):
    prev_char = ''
    for char in string:
        curr_char = char
        if curr_char == prev_char:
            return True
        prev_char = curr_char
    return False

# Function That Returns True if String Does Not Contain Letter Combo
def no_danger_combos(string):
    danger_combos = ['ab','cd','pq','xy']
    prev_char = string[0]
    for char in string:
        combo = prev_char + char
        if combo in danger_combos:
            return False
        prev_char = char
    return True

# Function That Returns Count of Nice Based on String Input
def nice_strings():
    nice = 0
    for string in open(day.input_filename):
        if no_danger_combos(string):
            if has_double_letter(string):
                if has_three_vowels(string):
                    nice += 1
        print("String: ", string, " No Danger Combos: ", no_danger_combos(string), " Has Double Letters: ", has_double_letter(string), " Has Three Vowels: ", has_three_vowels(string))
    return nice
