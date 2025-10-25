#!/usr/bin/python3
import sys

print("Total arguments:", len(sys.argv))
print("Script name:", sys.argv[0])
print("Arguments:", sys.argv[1:])

octave = int(sys.argv[1])

if ( octave < 0 ) or ( octave > 8) :
    print("Octave is too high or too low")
    exit(0)

bstr = ''

for char in sys.argv[2]:
    result = 0;
    match char:
        case 'G':
            result = 1 + octave * 12
        case 'H': # G#
            result = 2 + octave * 12
        case 'A': # A
            result = 3 + octave * 12
        case 'Q': # A#
            result = 4 + octave * 12
        case 'B': # B
            result = 5 + octave * 12
        case 'C': # C
            result = 6 + octave * 12
        case 'V': #C#
            result = 7 + octave * 12
        case 'D': #D
            result = 8 + octave * 12
        case 'M': #D#
            result = 9 + octave * 12
        case 'E': #E
            result = 10 + octave * 12
        case 'F': #F
            result = 11 + octave * 12
        case 'Y': #F#
            result = 12 + octave * 12
    result = hex(int(result) + 30)
    bstr += '\\x' + result[2:]
print(bstr)
