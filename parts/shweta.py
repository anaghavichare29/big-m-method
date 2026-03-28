st.title("📊 Big M Method Solver")

obj_input = st.text_input("Enter Objective Function")

constraints_input = st.text_area(
    "Enter Constraints (one per line)"
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

        # Solve
        steps, final_table, basis = big_m_method(c, A, b, signs)

        st.subheader("📊 Iteration Tables")

        for i, (df, prow, pcol) in enumerate(steps):
            st.write(f"### Iteration {i}")

            if pcol is not None:
                st.write(f"Pivot Column: {df.columns[pcol+2]}")
                st.write(f"Pivot Row: {prow}")

            st.dataframe(df)

        # Extract solution
        solution = np.zeros(len(c))
        for i, var in enumerate(basis):
            if var.startswith("x"):
                idx = int(var[1:]) - 1
                solution[idx] = final_table[i][-1]

        optimal_value = sum(c[i]*solution[i] for i in range(len(c)))

        st.subheader("✅ Final Result")

        for i, val in enumerate(solution):
            st.write(f"x{i+1} = {round(val, 4)}")

        st.write("Optimal Value (Z) =", round(optimal_value, 4))

        # ✅ GRAPH
        st.subheader("📈 Graph")
        fig = plot_graph(A, b, solution, num_vars)
        st.pyplot(fig)

    except Exception as e:
        st.error(f"Error: {e}")
