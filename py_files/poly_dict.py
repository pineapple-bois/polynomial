import regex as re

def decompose_polynomial(formula: str):
    powers = []
    coefficients = []

    # Remove whitespace and replace '^' with '**'
    formula = formula.replace(' ', '').replace('^', '**')

    # Use regular expression to split the polynomial into individual terms
    terms = re.findall(r'[\+\-]?\s*\d*\*?x\*\*\d+|[\+\-]?\s*\d*\*?x?|\d+', formula)
    terms = [term for term in terms if term]   # remove any empty strings

    highest_power = 0  # Track the highest power encountered

    for term in terms:
        if 'x' in term:
            if '*x**' in term:
                coefficient, power = term.split('*x**')
                coefficients.append(int(coefficient))
                powers.append(int(power))
                highest_power = max(highest_power, int(power))
            elif 'x**' in term:
                coefficient, power = term.split('x**')
                if '+' in term:
                    coefficients.append(1)
                    powers.append(int(power))
                    highest_power = max(highest_power, int(power))
                elif '-' in term:
                    coefficients.append(-1)
                    powers.append(int(power))
                    highest_power = max(highest_power, int(power))
                else:
                    coefficients.append(1)
                    powers.append(int(power))
                    highest_power = max(highest_power, int(power))
            else:
                if term.endswith('*x'):
                    coefficient, _ = term.split('*x')
                    coefficients.append(int(coefficient))
                    powers.append(1)
                    highest_power = max(highest_power, 1)
                elif term == 'x':
                    coefficients.append(1)
                    powers.append(1)
                    highest_power = max(highest_power, 1)
                else:
                    if term == '+x':
                        coefficients.append(1)
                        powers.append(1)
                        highest_power = max(highest_power, 1)
                    elif term == '-x':
                        coefficients.append(-1)
                        powers.append(1)
                        highest_power = max(highest_power, 1)
                    else:
                        if '+' in term:
                            coefficients.append(float(term))
                            powers.append(1)
                            highest_power = max(highest_power, 1)
                        elif '-' in term:
                            coefficients.append(-float(term))
                            powers.append(1)
                            highest_power = max(highest_power, 1)
        else:
            coefficients.append(int(term))
            powers.append(0)


    poly_dict = dict(zip(powers, coefficients))
    return poly_dict