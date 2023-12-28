import re


def array_declaration(declaration):
    descriptor = []

    array_definition = re.compile(r'(?P<array_name>[A-Z][A-Z0-9]*)\s:\sarray\s\[(?P<dimensions>.*?)\]\sof\s(?P<type>integer|char|real|bool)\s;')
    dimensions_pattern = re.compile(r'\s*(?P<lower_bound>\d+)\.\.(?P<upper_bound>\d+)\s*')

    match = array_definition.match(declaration)

    if match:
        array_name = match.group('array_name')
        dmn_count = declaration.count('..')
        if dmn_count > 1:
            descriptor.append("Multidimensional array")
        else:
            descriptor.append("One dimensional array")

        descriptor.append(match.group('type'))
        descriptor.append("Integer")
        descriptor.append(str(dmn_count))

        dimensions_str = match.group('dimensions')
        dimensions = []

        matches = dimensions_pattern.findall(dimensions_str)
        for match in matches:
            lower_bound, upper_bound = match
            dimensions.append([lower_bound, upper_bound])

        descriptor.append(dimensions)
        descriptor.append("1000")
        return descriptor


input_declaration = input("Enter your array definition: ")
output = array_declaration(input_declaration)

if output:
    print(output)
else:
    print("Invalid definition")

