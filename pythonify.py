import argparse


__all__ = ["pythonify"]


def pythonify(
    in_fp, out_fp,
    indent_size: int = 4,
    eol_spacing: int = 1,
):
    # Read input file
    infile = open(in_fp, "r")

    content = ""
    cur_indent = 0
    bracket_position = 0

    for line in infile.readlines():
        # Convert tabs to spaces if needed
        while line.find("\t") != -1:
            line = line.replace("\t", "    ")

        # Try to keep relative indentation between lines
        line = line.rstrip()
        left_space_count = len(line) - len(line.lstrip())
        spaces_to_keep = max(0, left_space_count - cur_indent*indent_size)
        line = line[left_space_count - spaces_to_keep:]

        # This is the safest way to do identation, but sometimes it looks bad
        # line = line.strip()

        if len(line) + cur_indent*indent_size > bracket_position:
            bracket_position = len(line) + cur_indent*indent_size
        content += line + '\n'

        # Update indentation level
        cur_indent += line.count('{') - line.count('}')        

    infile.close()


    # Write to output file
    outfile = open(out_fp, "w")

    bracket_position += eol_spacing
    cur_indent = 0
    cur_line_len = 0

    for idx in range(len(content)):
        char = content[idx]

        # In some cases, we need to know the next character
        if idx < len(content) - 1:
            next_char = content[idx + 1]
        else:
            next_char = None

        # Process newline characters
        if char == '\n':
            if next_char in ['{', '}']:
                continue
            else:
                outfile.write('\n')
                cur_line_len = cur_indent * indent_size
                outfile.write(' ' * (cur_indent * indent_size))

        # Handle brackets
        elif char in '{}':
            if cur_line_len < bracket_position:
                outfile.write(' ' * (bracket_position - cur_line_len))
                cur_line_len = bracket_position
            outfile.write(char)
            cur_line_len += 1
            if char == '{':
                cur_indent += 1
            else:
                cur_indent -= 1
            if next_char not in ['\n', ';', '{', '}']:
                outfile.write('\n')
                cur_line_len = cur_indent * indent_size
                outfile.write(' ' * (cur_indent * indent_size))
        
        # Python users don't need semicolons
        elif char == ';':
            if next_char == '\n' and cur_line_len < bracket_position:
                outfile.write(' ' * (bracket_position - cur_line_len))
                cur_line_len = bracket_position
            cur_line_len += 1
            outfile.write(char)
        elif char != '\n':
            outfile.write(char)
            cur_line_len += 1
            
    outfile.close()


def parser():
    parser = argparse.ArgumentParser(
        description="convert C++/Java code into a 'pseudo Python' format",
        epilog="example: python3 pythonify.py -i example.cpp -o output.cpp",
        formatter_class=argparse.RawDescriptionHelpFormatter,
    )

    parser.add_argument("-i", "--input", help="Input file path", required=True)
    parser.add_argument("-o", "--output", help="Output file path", required=True)
    parser.add_argument("-s", "--indent_size", help="Indent size", type=int, default=4)
    parser.add_argument("-e", "--eol_space", help="EOL spacing", type=int, default=1)

    return parser


if __name__ == "__main__":
    args = parser().parse_args()
    pythonify(
        args.input, args.output,
        indent_size=args.indent_size,
        eol_spacing=args.eol_space,
    )