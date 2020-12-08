from re import compile

password_pattern = compile(
    r"(?P<n1>[0-9]+)-(?P<n2>[0-9]+) (?P<letter>[a-z]): (?P<password>[a-z]+)"
)
password_lines = open("2.in", "r").read().splitlines()


def policy_matches(policy, lines):
    return sum(
        policy(int(match["n1"]), int(match["n2"]), match["letter"], match["password"])
        for match in (password_pattern.match(line) for line in lines)
    )


# Part 1
def reps_in_range(min_reps, max_reps, letter, password):
    return min_reps <= sum(1 for l in password if l == letter) <= max_reps


print(
    "Part 1:",
    policy_matches(
        reps_in_range,
        password_lines,
    ),
)

# Part 2
def xor_letter_match(pos_1, pos_2, letter, password):
    return (password[pos_1 - 1] == letter) != (password[pos_2 - 1] == letter)


print(
    "Part 2:",
    policy_matches(
        xor_letter_match,
        password_lines,
    ),
)