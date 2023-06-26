import re


def decompose_polynomial(formula: str):
    """
    Polynomial exponents are natural numbers.
    If exponents are rationals or negative integers, the formula will not parse
    :return Polynomial dictionary; {exponent: coefficient, ... }
    """
    # Remove whitespace and replace '^' with '**'
    formula = formula.replace(' ', '').replace('^', '**')

    if 'x' not in formula:
        raise ValueError("Please enter variable as 'x'")

    terms = re.findall(r'([+\-]?\s*(?:\d*\.\d+|\d+\.\d*|\.\d+|\d+(?:\.\d*)?)\*?x\*\*\d+|'
                       r'[-]?\s*(?:\d*\.\d+|\d+\.\d*|\.\d+|\d+(?:\.\d*)?)\*?x?|'
                       r'[+\-]?\s*x(?:\*\*\d+)?)', formula)

    terms = [term for term in terms if term]  # remove any empty strings
    powers = []
    coefficients = []
    highest_power = 0

    for term in terms:
        if 'x' in term:
            if '*x**' in term:
                coefficient, power = term.split('*x**')
            elif 'x**' in term:
                coefficient, power = term.split('x**')
                if '+' in term or not coefficient:
                    coefficient = '1.0'
                elif '-' in term or not coefficient:
                    coefficient = '-1.0'
            else:
                coefficient, _ = term.split('*x') if term.endswith('*x') else term.split('x')
                if not coefficient or coefficient == '+':
                    coefficient = '1.0'
                elif coefficient == '-':
                    coefficient = '-1.0'

            coefficients.append(float(coefficient))
            power = int(power) if '**' in term else 1
            powers.append(power)
            highest_power = max(highest_power, power)

        else:
            coefficients.append(float(term))
            powers.append(0)

    poly_dict = dict(zip(powers, coefficients))
    return poly_dict
