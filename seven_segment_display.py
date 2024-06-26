def seven_segment_display(number):
    # Define the 5x3 pattern for each digit
    patterns = [
        ["###", "# #", "# #", "# #", "###"],  # 0
        ["  #", "  #", "  #", "  #", "  #"],  # 1
        ["###", "  #", "###", "#  ", "###"],  # 2
        ["###", "  #", "###", "  #", "###"],  # 3
        ["# #", "# #", "###", "  #", "  #"],  # 4
        ["###", "#  ", "###", "  #", "###"],  # 5
        ["###", "#  ", "###", "# #", "###"],  # 6
        ["###", "  #", "  #", "  #", "  #"],  # 7
        ["###", "# #", "###", "# #", "###"],  # 8
        ["###", "# #", "###", "  #", "###"]  # 9
    ]

    # Convert the number to a string to iterate over each digit
    str_num = str(number)

    # Create a list to hold each line of the final output
    lines = [""] * 5

    # Build the display by combining the patterns
    for digit in str_num:
        digit = int(digit)
        for i in range(5):
            lines[i] += patterns[digit][i] + " "

    # Print the result
    for line in lines:
        print(line.strip())


def main():
    while True:
        # Demander à l'utilisateur de saisir un nombre
        user_input = input("Entrez un nombre non négatif (ou 'q' pour quitter): ")

        if user_input.lower() == 'q':
            break

        # Vérifier que l'entrée est un nombre entier non négatif
        if user_input.isdigit():
            number = int(user_input)
            # Appeler la fonction seven_segment_display avec le nombre entré
            seven_segment_display(number)
        else:
            print("Veuillez entrer un nombre entier non négatif valide.")


# Appeler la fonction main si ce script est exécuté
if __name__ == "__main__":
    main()

