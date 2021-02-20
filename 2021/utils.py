
"""
handles in and output
"""


def write_output(filename, output):
    """
    writes a list of strings to a .out file

    parameters: 
        - output: list of strings 
        - filename: string
    """
    
    filepath = 'data/output_{}.out'.format(filename)
    print('saving file to {}'.format(filepath))
    print(output)

    with open(filepath, "w") as outfile:
        outfile.write("\n".join(output))

    return 

    