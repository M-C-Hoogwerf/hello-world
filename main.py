# Do not modify these lines
__winc_id__ = '71dd124b4a6e4d268f5973db521394ee'
__human_name__ = 'strings'

# Add your code after this line

# part 1

scorer_name1 = "Ruud Gullit"
scorer_name2 = "Marco van Basten"
goal_0 = 32
goal_1 = 54

scorers = scorer_name1 + " " + \
    str(goal_0) + ", " + scorer_name2 + " " + str(goal_1)

report = f"{scorer_name1} scored in the {str(goal_0)}nd minute\n{scorer_name2} scored in the {str(goal_1)}th minute"


# part 2

player = "Ruud Gullit"

first_name = player[:player.find(" ")]
last_name = player[player.find(" ")+1:]

last_name_len = len(last_name)

name_short = f"{first_name[:1]}. {last_name}"

chant = (first_name + "!") + (" " + first_name + "!") * len(first_name[:-1])

good_chant = chant[-1:] != " "
