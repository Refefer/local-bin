import std.string, std.stdio, std.array, std.algorithm;
import utils;

struct Delim {
    size_t count = 0;
    size_t max_index = 0;
    dchar delim;
    this(dchar d) {
        delim = d;
    }
}

Delim[] count_delims(R)(in char[] delims, in R lines) {
    auto counts = list!Delim(map!Delim(delims));

    foreach(ref string line; lines) {
        foreach(ref count; counts) {
            auto index = lastIndexOf(line, count.delim);
            if(index > -1) {
                count.count += 1;
                if(index > count.max_index) {
                    count.max_index = index;
                }
            }
        }
    }
    return counts;
}

void main() {
    auto data = list!string(lines(stdin));
    auto delims = count_delims("=:", data);

    auto best_delim = reduce!"a.count < b.count ? b : a"(delims);

    auto delim = best_delim.delim;
    auto greatest = best_delim.max_index;
    foreach(line; data) {
        auto index = lastIndexOf(line, delim);
        if(index > -1) {
            write(leftJustify(line[0..index], greatest, ' '), 
                  delim, ' ',
                  stripLeft( line[index+1..$]) );
        } else {
            write(line);
        }
    }
}
