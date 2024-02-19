def mangle_name(name):
    mangled_name = ""
    for char in name:
        if char.isalpha():
            mangled_name += char.upper()
        else:
            mangled_name += char.lower()
    return mangled_name

# Example usage
name = "GitHub Copilot"
mangled_name = mangle_name(name)
print(mangled_name)
# Additional code for name mangling elaboration
def elaborate_mangled_name(mangled_name):
    elaborated_name = ""
    for i, char in enumerate(mangled_name):
        if i % 2 == 0:
            elaborated_name += char.upper()
        else:
            elaborated_name += char.lower()
    return elaborated_name

elaborated_name = elaborate_mangled_name(mangled_name)
print(elaborated_name)
# Additional code for further name mangling elaboration
def further_elaborate_name(elaborated_name):
    further_elaborated_name = ""
    for char in elaborated_name:
        if char.isupper():
            further_elaborated_name += char.lower()
        else:
            further_elaborated_name += char.upper()
    return further_elaborated_name

further_elaborated_name = further_elaborate_name(elaborated_name)
print(further_elaborated_name)