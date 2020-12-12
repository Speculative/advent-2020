import re
from itertools import tee

passport_field = re.compile(r"(\w\w\w):([^ \n]+)")


def passport_from(line):
    return {key: value for key, value in passport_field.findall(line)}


def passports():
    with open("4.in", "r") as data:
        current_line = ""
        for line in data:
            if len(line) == 1:
                yield passport_from(current_line)
                current_line = ""
            current_line += line
        yield passport_from(current_line)


passports_1, passports_2 = tee(passports())

# Part 1
required_fields = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"]
print(
    "Part 1:",
    sum(
        all(required_field in passport for required_field in required_fields)
        for passport in passports_1
    ),
)

# Part 2
field_requirements = {
    "byr": lambda s: len(s) == 4 and 1920 <= int(s) <= 2002,
    "iyr": lambda s: len(s) == 4 and 2010 <= int(s) <= 2020,
    "eyr": lambda s: len(s) == 4 and 2020 <= int(s) <= 2030,
    "hgt": lambda s: (
        (height := re.match(r"^(?P<value>\d+)(?P<unit>in|cm)$", s)) is not None
        and (
            (150 <= int(height["value"]) <= 193)
            if height["unit"] == "cm"
            else (59 <= int(height["value"]) <= 76)
        )
    ),
    "hcl": lambda s: re.match(r"^#[0-9a-f]{6}$", s) is not None,
    "ecl": lambda s: s in ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"],
    "pid": lambda s: re.match(r"^[0-9]{9}$", s) is not None,
}

print(
    "Part 2:",
    sum(
        all(
            field in passport and field_requirements[field](passport[field])
            for field in field_requirements
        )
        for passport in passports_2
    ),
)