#!/usr/bin/python3
import sys

octave = int(sys.argv[1])

if ( octave < 0 ) or ( octave > 8) :
    print("Octave is too high or too low")
    exit(0)

bstr = ''

noteDuration = sys.argv[2] 

for char in sys.argv[3]:
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
    if int(noteDuration) < 16 :
        bstr += '\\x0' + hex(int(noteDuration))[2:]
    else:
        bstr += '\\x' + hex(int(noteDuration))[2:]
print(bstr)
