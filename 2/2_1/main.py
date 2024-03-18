from latex_generator import generate_latex_table


# Example usage
if __name__ == "__main__":
    table_data = [
        ["hamster name", "death cause"],
        ["shosha", "ate a magnet, got magnetised to the fridge, starved to death"],
        ["sanya", "died of fright because a man sneezed loudly"],
        ["ponyo", "vacuum cleaner"]
    ]

    latex_code = generate_latex_table(table_data)
    print(latex_code)  # Output LaTeX code for the table

    with open("table.tex", 'w') as file:
        file.write(latex_code)