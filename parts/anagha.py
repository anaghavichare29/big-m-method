def big_m_method(c, A, b, signs):
    m = len(A)
    n = len(c)

    table = []
    basis = []
    cb = []

    var_names = [f"x{i+1}" for i in range(n)]
    slack_names = [f"s{i+1}" for i in range(m)]
    artificial_names = [f"A{i+1}" for i in range(m)]

    for i in range(m):
        row = list(A[i])
        slack = [0]*m
        artificial = [0]*m

        if signs[i] == "<=":
            slack[i] = 1
            basis.append(slack_names[i])
            cb.append(0)

        elif signs[i] == ">=":
            slack[i] = -1
            artificial[i] = 1
            basis.append(artificial_names[i])
            cb.append(-M)

        elif signs[i] == "=":
            artificial[i] = 1
            basis.append(artificial_names[i])
            cb.append(-M)

        row += slack + artificial + [b[i]]
        table.append(row)

    cj = c + [0]*m + [-M]*m

    table = np.array(table, dtype=float)
    headers = var_names + slack_names + artificial_names + ["RHS"]

    steps = []

    while True:
        df = pd.DataFrame(table, columns=headers)
        df.insert(0, "Basis", basis)
        df.insert(1, "Cb", cb)

        zj = np.dot(cb, table[:, :-1])
        cj_zj = np.array(cj) - zj

        df.loc["Zj"] = ["", "Zj"] + list(zj) + [""]
        df.loc["Cj-Zj"] = ["", "Cj-Zj"] + list(cj_zj) + [""]

        pivot_col = np.argmax(cj_zj)

        if cj_zj[pivot_col] <= 0:
            steps.append((df.copy(), None, None))
            break

        ratios = []
        for i in range(m):
            if table[i][pivot_col] > 0:
                ratios.append(table[i][-1] / table[i][pivot_col])
            else:
                ratios.append(np.inf)

        pivot_row = np.argmin(ratios)

        df["Ratio"] = ratios + ["", ""]

        steps.append((df.copy(), pivot_row, pivot_col))

        # Pivot operation
        pivot = table[pivot_row][pivot_col]
        table[pivot_row] /= pivot

        for i in range(m):
            if i != pivot_row:
                table[i] -= table[i][pivot_col] * table[pivot_row]

        basis[pivot_row] = headers[pivot_col]
        cb[pivot_row] = cj[pivot_col]

    return steps, table, basis