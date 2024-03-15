from small_latex_module_mmmmarryyy.module_file import generate_latex_table, generate_latex_image

if __name__ == '__main__':
    data = [
        ["Name", "Age", "City"],
        ["Alice", 25, "New York"],
        ["Bob", 30, "Los Angeles"],
        ["Charlie", 22, "Chicago"]
    ]
    image_path = "../test_image/kittens.jpg"

    latex_table = generate_latex_table(data)
    latex_image = generate_latex_image(image_path)

    latex_code = f"""\\documentclass{{article}}\n\\usepackage{{graphicx}}\n\\begin{{document}}\n{latex_table}\n\n\n{latex_image}\n\\end{{document}}"""

    with open("../artifacts/2_2.tex", "w") as file:
        file.write(latex_code)