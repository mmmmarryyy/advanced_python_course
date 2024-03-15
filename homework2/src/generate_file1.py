from generate_table import generate_latex_table


if __name__ == '__main__':
    data = [
        ["Name", "Age", "City", "Sex"],
        ["Alice", 25, "New York", "F"],
        ["Bob", 30, "Los Angeles", "M"],
        ["Alex", 22, "Chicago", "M"]
    ]

    latex_code = "\documentclass{article}\n\\begin{document}\n" + generate_latex_table(data) + "\n\end{document}"

    with open("../artifacts/2_1.tex", "w") as file:
        file.write(latex_code)