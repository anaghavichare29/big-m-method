 st.subheader("📊 Iteration Tables (Big M Method)")

        for i, (df, prow, pcol) in enumerate(steps):
            st.write(f"### Iteration {i}")
            if pcol is not None:
                st.write(f"Pivot Column: {df.columns[pcol+2]}")
                st.write(f"Pivot Row: {prow}")
            st.dataframe(df)

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

        if len(c) == 2:
            st.subheader("📈 Graph")
            plot_graph_dynamic(A, b, solution, st.empty())

    except Exception as e:
        st.error(f"Error: {e}")
