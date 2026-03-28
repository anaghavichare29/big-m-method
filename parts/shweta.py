st.title("📊 Big M Method Solver")
obj_input = st.text_input("Enter Objective Function")

constraints_input = st.text_area(
    "Enter Constraints (one per line)",    
)
if st.button("Solve"):
    try:
        c = parse_objective(obj_input)
        num_vars = len(c)

        A, b, signs = [], [], []

        for line in constraints_input.strip().split("\n"):
            if line.strip() == "":
                continue
            row, val, sign = parse_constraint(line, num_vars)
            A.append(row)
            b.append(val)
            signs.append(sign)

        steps, final_table, basis = big_m_method(c, A, b, signs)
