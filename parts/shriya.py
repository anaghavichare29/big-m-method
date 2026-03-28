def parse_constraint(constraint, num_vars):
    parts = re.split(r'(<=|>=|=)', constraint)
    expr, sign, val = parts[0], parts[1], float(parts[2])
    row = [0] * num_vars
    terms = re.findall(r'([+-]?\d*)x(\d+)', expr.replace(" ", ""))

    for coef, var in terms:
        if coef in ["", "+"]:
            coef = 1
        elif coef == "-":
            coef = -1
        else:
            coef = int(coef)

        row[int(var) - 1] = coef

    return row, val, sign
