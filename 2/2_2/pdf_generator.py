import os
from hamster_latex_gen.table_img_generator import generate_latex_table, generate_latex_image

# example data for a table
data = [
    ["hamster name", "death cause"],
    ["shosha", "ate a magnet, got magnetised to the fridge, starved to death"],
    ["sanya", "died of fright because a man sneezed loudly"],
    ["ponyo", "vacuum cleaner"] 
]

# creating LaTeX code for the table
latex_table = generate_latex_table(data)

# creating LaTeX code for the image
image_path = "C:/Downloads/Python_hw/2/2_2/hamster.PNG"
latex_image = generate_latex_image(image_path)

# creating LaTeX file
latex_file_path = "latex_output.tex"
with open(latex_file_path, "w") as f:
    f.write("\\documentclass{article}\n")
    f.write("\\usepackage{graphicx}\n")  # downloading the graphicx package for working with images
    f.write("\\begin{document}\n")
    f.write(latex_table)
    f.write(latex_image)
    f.write("\\end{document}\n")

# compiling a LaTeX file to PDF
os.system(f"pdflatex {latex_file_path}")

