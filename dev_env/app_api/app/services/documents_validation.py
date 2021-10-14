import re


def cpf_validate(cpf):

    cpf_clear = re.sub('\D', '', cpf)

    if len(cpf_clear) != 11 or cpf_clear[:-2] == "123456789":
        return False

    verify_sum = 0

    for pos, digit in enumerate(cpf_clear[0:-2]):

        verify_sum += (10 - pos) * int(digit)

    dv = 0 if verify_sum % 11 < 2 else (11 - verify_sum % 11)

    if dv != int(cpf_clear[-2]):
        return False

    verify_sum = 0

    for pos, digit in enumerate(cpf_clear[0:-1]):

        verify_sum += (11 - pos) * int(digit)

    dv = 0 if verify_sum % 11 < 2 else (11 - verify_sum % 11)

    return dv == int(cpf_clear[-1])
