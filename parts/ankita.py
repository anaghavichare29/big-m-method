def parse_objective(obj_str):
    terms = re.findall(r'([+-]?\d*)x(\d+)', obj_str.replace(" ", ""))
    max_var = max(int(var) for _, var in terms)

    c = [0] * max_var
    for coef, var in terms:
        if coef in ["", "+"]:
            coef = 1
        elif coef == "-":
            coef = -1
        else:
            coef = int(coef)
        c[int(var) - 1] = coef

    return c

def parse_objective(obj_str):
    terms = re.findall(r'([+-]?\d*)x(\d+)', obj_str.replace(" ", ""))
    max_var = max(int(var) for _, var in terms)

    # 🔴 LIMIT TO 3 VARIABLES
    if max_var > 3:
        raise ValueError("Only up to 3 variables are supported.")

    c = [0] * max_var
    for coef, var in terms:
        if coef in ["", "+"]:
            coef = 1
        elif coef == "-":
            coef = -1
        else:
            coef = int(coef)
        c[int(var) - 1] = coef

    return c
