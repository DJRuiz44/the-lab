def create_character(name, strength, intelligence, charisma):
    if not isinstance(name, str) or name == "":
        return "The character should have a name"
    elif len(name) > 10:
        return "The character name is too long"
    elif " " in name:
        return "The character name should not contain spaces"
    
    if not isinstance(strength, int) or not isinstance(intelligence, int) or not isinstance(charisma, int):
        return "All stats should be integers"
    elif strength < 1 or intelligence < 1 or charisma < 1:
        return "All stats should be no less than 1"
    elif strength > 4 or intelligence > 4 or charisma > 4:
        return "All stats should be no more than 4"
    stat_sum = strength + intelligence + charisma
    if stat_sum != 7:
        return "The character should start with 7 points"
    full_dot = '●'
    empty_dot = '○'
    print(f"STR{strength * full_dot + (10-strength) * empty_dot }\nINT{intelligence * full_dot + (10-intelligence) * empty_dot}\nCHA{charisma * full_dot + (10-charisma) * empty_dot}:")
create_character("Daniel", 4, 2, 1)
