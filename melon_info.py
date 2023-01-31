"""Print out all the melons in our inventory."""


from melons import melon_information

# name, price, seedless, flesh, rind, weight

def print_melon(melons):
    """Print each melon with corresponding attribute information."""
    for melons, informations in melon_information.items():
        print("-------------------")
        print(f"""{melons.upper()}""")
        for info in informations:
            print(info, ": ", informations[info])
        print("-------------------")
        print()
        


print_melon(melon_information)

# not using this lol:
# price: {melon[]}
# seedless: {}
# flesh_color: {}
# rind_color: {}
# average_weight: {}
# """)


# # #     have_or_have_not = 'have'
# # #     if seedless:
# # #         have_or_have_not = 'do not have'

# # #     print(f'{name}s {have_or_have_not} seeds and are ${price}')

# print_melon("Honeydew")
# # # for i in melon_names:
# # #     print_melon(melon_names[i], melon_prices[i], melon_seedlessness[i])
