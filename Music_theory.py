#this empty list is used as a precursor to notes sharp/flat
empty_note_list = ()

#triads library
triads = {"Cmaj":"CEG", "Cmin":"CEbG", "Cdim":"CEbGb", "Caug":"CEG#",
 "Dmaj":"DF#A", "Dmin":"DFA", "Ddim":"DFAb", "Daug":"DF#A#",
 "Emaj":"EG#B", "Emin":"EGB", "Edim":"EGBb", "Eaug":"EG#B#",
 "Fmaj":"FA#C", "Fmin":"FAC", "Fdim":"FACb", "Faug":"FA#C#",
 "Gmaj":"GBD", "Gmin":"GBbD", "Gdim":"GBbDb", "Gaug":"GBD#",
 "Amaj":"AC#E", "Amin":"ACE", "Adim":"ACEb", "Aaug":"AC#E#",
 "Bmaj":"BD#F#", "Bmin":"BDF#", "Bdim":"BDF", "Baug":"BD#F##"}
#Notes in Music Scale
Notes_flat = ("A", "Bb", "B", "C", "Db", "D", "Eb", "E", "F", "Gb", "G", "Ab")

Notes_sharp = ("A", "A#", "B", "C", "C#", "D", "D#", "E", "F", "F#", "G", "G#")

#Keys in sharp flow
sharp_keys = ("G", "D", "A", "E", "B", "F#")

#Keys in flat flow
flat_keys = ("F", "Bb", "Eb", "Ab", "Db", "Gb", "C")

key = input("Please enter what key you want to be in.\n\
Here are the available keys: (A, Bb, B, C, Db, D, Eb, E, F, F#/Gb, G, Ab) > ")

if key in sharp_keys:
    empty_note_list = Notes_sharp
elif key in flat_keys:
    empty_note_list = Notes_flat
#index counter used to determine index of key
index = 0
#this loop will attempt to use an index counter to identify the index of the key in Notes sharp or flat
for k in empty_note_list:
    if k == key:
        break
    else:
        index += 1
#this list modifies the empty note list = to some note list
mod_empty_note_list = (empty_note_list[((index)):] + empty_note_list[:((index)+1)])

#major_scale formula
major_scale = mod_empty_note_list[0:3:2] + mod_empty_note_list[4:6:2] +\
mod_empty_note_list[5:12:2] + mod_empty_note_list[12:14]

#minor_scale formula
minor_scale = mod_empty_note_list[0:3:2] + mod_empty_note_list[3:8:2] +\
 mod_empty_note_list[8:13:2]

user_input1 = input("What do you want to see? scales, chords, or games > ")

if user_input1 == "scales":
    scale_type = input("Would you like to see major or minor scales? > ")
    if scale_type == "major":
        print(major_scale)
    elif scale_type == "minor":
        print(minor_scale)
elif user_input1 == "chords":
    chord_input = input("which chords would you like to see? triads, sevenths,\
or extended? > ")
    if chord_input == "triads":
        print("There will be triads here")
    elif chord_input == "sevenths":
        print("There will be seventh chords here")
    elif chord_input == "extended":
        print("There will be extended chords here")
elif user_input1 == "games":
    game_input = input("chord construction or scales quiz? > ")
    if game_input == "chord construction":
        print("There will be a chord construction game here")
    elif game_input == "scales quiz":
        print("There will be a scales quiz game here")
# personal_projects
# personal_projects
