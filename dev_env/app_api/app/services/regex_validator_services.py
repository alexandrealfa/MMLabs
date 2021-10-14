import re


def regex_validator(value, rule):
    regex_adjusted = re.compile(rule)
    match = regex_adjusted.match(value)
    return bool(match)


