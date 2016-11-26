import random as r
#this empty list is used as a precursor to notes sharp/flat
empty_note_list = ()

#triads library
triads = {"Cmaj":"CEG", "Cmin":"CEbG", "Cdim":"CEbGb", "Caug":"CEG#",
 "Dmaj":"DF#A", "Dmin":"DFA", "Ddim":"DFAb", "Daug":"DF#A#",
 "Emaj":"EG#B", "Emin":"EGB", "Edim":"EGBb", "Eaug":"EG#B#",
 "Fmaj":"FAC", "Fmin":"FAbC", "Fdim":"FAbCb", "Faug":"FAC#",
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

#scales branch of menu
if user_input1 == "scales":
    scale_type = input("Would you like to see major or minor scales? > ")
    if scale_type == "major":
        print(major_scale)
    elif scale_type == "minor":
        print(minor_scale)

#chords branch of menu
elif user_input1 == "chords":
    chord_input = input("which chords would you like to see? triads, sevenths,\
or extended? > ")
    if chord_input == "triads":
        print("There will be triads here")
    elif chord_input == "sevenths":
        print("There will be seventh chords here")
    elif chord_input == "extended":
        print("There will be extended chords here")

#games branch of menu
elif user_input1 == "games":
    game_input = input("spell that chord, name that chord, scales quiz? > ")
    if game_input == "spell that chord":
        #SPELL THAT CHORD GAME
        counter = 0
        correct = 0

        #chord notes quiz
        while counter < 10:
            tries = 2
            rand_chord_name = r.choice(list(triads.keys()))
            rand_chord_spell = triads[rand_chord_name]
            print("Question number {}".format(counter + 1))
            print(rand_chord_name)
            user_guess1 = input("What are the notes in the chords\n\
Remember to use all caps except for the flat symbol> ")
            tries -= 1

            while user_guess1 != rand_chord_spell:

                if user_guess1 == "":
                    print("You typed in nothing, try again")
                    user_guess1 = input("> ")

                elif tries == 0:
                    counter += 1
                    print("Incorrect again! Next Question!")
                    tries = 2
                    break

                elif user_guess1 != rand_chord_spell:
                    tries -= 1
                    print("Nope! Try one more time. Remember no spaces and caps \
on the notes except for the flat symbol")
                    user_guess1 = input("> ")

            if user_guess1 == rand_chord_spell:
                print("Congratulations that is correct")
                correct += 1
                counter += 1
                print("You have gotten {} correct".format(correct))

    elif game_input == "name that chord":
        counter = 0
        correct = 0

        #NAME THAT CHORD GAME
        while counter < 10:
            tries = 2
            rand_chord_name = r.choice(list(triads.keys()))
            rand_chord_spell = triads[rand_chord_name]
            print(rand_chord_spell)
            user_guess1 = input("What is the name of that chord? Remember to\
 abbreviate Major = maj, Minor = min, Augmented = aug, Diminished = dim\n\
 > ")
            tries -= 1

            while user_guess1 != rand_chord_name:

                if user_guess1 == "":
                    print("You typed in nothing, try again")
                    user_guess1 = input("> ")

                elif tries == 0:
                    counter += 1
                    print("Incorrect again! Next Question!")
                    tries = 2
                    break

                elif user_guess1 != rand_chord_name:
                    tries -= 1
                    print("Nope! Try one more time. Remember to abbreviate\
 Major = maj, Minor = min, Augmented = aug, Diminished = dim>")
                    user_guess1 = input("> ")

            if user_guess1 == rand_chord_name:
                print("Congratulations that is correct")
                correct += 1
                counter += 1
                print("You have gotten {} correct".format(correct))

    elif game_input == "scales quiz":
        print("There will be a scales quiz game here")
# personal_projects
# personal_projects
