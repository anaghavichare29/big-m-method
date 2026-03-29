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




def plot_graph(A, b, solution, num_vars):
    fig = plt.figure()

    # ✅ 2 VARIABLES
    if num_vars == 2:
        ax = fig.add_subplot(111)
        x = np.linspace(0, 10, 200)

        for i in range(len(A)):
            a1, a2 = A[i]
            if a2 != 0:
                y = (b[i] - a1 * x) / a2
                ax.plot(x, y)

        ax.scatter(solution[0], solution[1])
        ax.set_xlabel("x1")
        ax.set_ylabel("x2")
        ax.set_title("2D Graph")

    # ✅ 3 VARIABLES (NEW 🔥)
    elif num_vars == 3:
        ax = fig.add_subplot(111, projection='3d')

        x = np.linspace(0, 10, 30)
        y = np.linspace(0, 10, 30)
        X, Y = np.meshgrid(x, y)

        for i in range(len(A)):
            a1, a2, a3 = A[i]
            if a3 != 0:
                Z = (b[i] - a1*X - a2*Y) / a3
                ax.plot_surface(X, Y, Z, alpha=0.3)

        ax.scatter(solution[0], solution[1], solution[2])
        ax.set_xlabel("x1")
        ax.set_ylabel("x2")
        ax.set_zlabel("x3")
        ax.set_title("3D Feasible Region")

    return fig
