import std.string, std.stdio;

char[] GROUPINGS = ['(', '[','{'];
long find_indent(S)(S line) {
    long index;
    foreach(c; GROUPINGS) {
        index = indexOf(line, c);
        if(index != -1) break;
    }
    // No 'groupings', so use the whitespace
    if(index == -1) {
        index = line.length - stripLeft(line).length;
    }
    return index;
}

void main() {
    foreach(ref string line; lines(stdin)) {
        auto indent = find_indent(line);
        
        // Print the first line
        auto first_comma = indexOf(line[indent..$], ',');
        writeln(line[0..(indent+first_comma+1)]);

        // Split the rest!
        auto chunks = split(line[first_comma+1..$], ",");
        foreach(i, ref string chunk; chunks[1..$]) {
            chunk = stripLeft(chunk);
            write(rightJustify(chunk, chunk.length+indent+1));
            if(i < chunks.length - 2) {
                writeln(',');
            }
        }
    }
}
