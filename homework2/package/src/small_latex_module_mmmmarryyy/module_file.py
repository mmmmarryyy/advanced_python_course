def generate_latex_image(image_path):
    latex_code = "\\begin{figure}[h]\n"
    latex_code += "\\centering\n"
    latex_code += "\\includegraphics[width=5.0in]{" + image_path + "}\n"
    latex_code += "\\end{figure}"
    
    return latex_code

def generate_latex_table(data):
    latex_code = "\\begin{tabular}{|" + "c|"*len(data[0]) + "}\n"
    latex_code += "\\hline\n"
    
    for row in data:
        assert len(row) <= len(data[0]), f"you provide incorrect number of arguments ({len(row)}) for row: {row}, need {len(data[0])}"
        if (len(row) < len(data[0])):
            for i in range(len(data[0]) - len(row)):
                row.append("")

        latex_code += " & ".join(str(cell) for cell in row)
        latex_code += " \\\\\n"
        latex_code += "\\hline\n"
    
    latex_code += "\\end{tabular}"
    
    return latex_code