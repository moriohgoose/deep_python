
def generate_latex_table(data):
    """
    Generate LaTeX code for a table from a 2D list of data.

    Args:
    - data (list of lists): 2D list containing the table data.

    Returns:
    - str: LaTeX code for the table.
    """
    # Begin the document
    latex_code = "\\documentclass{article}\n"
    latex_code += "\\begin{document}\n"

    # Begin the tabular environment
    latex_code += "\\begin{tabular}{|" + "c|" * len(data[0]) + "}\n"
    latex_code += "\\hline\n"

    # Add table rows
    for row in data:
        latex_code += " & ".join(str(cell) for cell in row)
        latex_code += " \\\\\n"
        latex_code += "\\hline\n"

    # End the tabular environment
    latex_code += "\\end{tabular}\n"

    # End the document
    latex_code += "\\end{document}\n"

    return latex_code
