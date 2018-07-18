# FoxDot Introduction Workshop
# ============================

# Part 1: Basics
# --------------

# To "run" code in FoxDot, put your text cursor on the line of code and press Ctrl+Enter or Cmd+Enter on MacOS.

print("Hello, World")

# Multiple lines not separated by blank space are run together

num = 2 + 2
print("2 + 2 is", num)

# We use "print" to show data in the console at the bottom of the screen. 
# To start making sound in FoxDot, we assign a "Player" a digital instrument using:

p1 >> pads()

p1.stop()

# p1 is the name of our "Player", and the arrows (>>) are used to give it instructions.
# The first instruction is "start playing the 'pads' instrument. These instruments are
# called "SynthDefs" - to see a list of the avaiable SynthDefs just run

print(SynthDefs)

# For now we'll just use the "pads" instrument.

# Most instructions are put inside the bracket, but some actions are done uing functions.
# e.g. to stop a player, we "call" the stop function by typing the name, then a dot, followed by
# the name of the action and then brackets.

# Players are all two character names - if we use a three character, we get an error

foo >> pads()

# To change the behaviour of "p1" we can give it instructions inside the brackets:

p1 >> pads()

p1 >> pads(2)

p1 >> pads([0,2,4])

p1.stop()

# The first instruction is the pitch - it can be a single value or a list of values in square brackets.
# 0 refers to the *first* note in the scale - it might seem a bit confusing but it'll will make sense soon!

# If we use round brackets instead of square, it plays the notes together

p1 >> pads((0,2,4))

p1 >> pads([0,1,2,(3,5,7)])

p1.stop()

# Putting a list inside of another list alternates which value is used

p1 >> pads([0,2,[4,7]])

p1.stop()

# After we set the pitch, we use "keywords" to assign other instructions - like durations

p1 >> pads([0,1,2,3], dur=1)

p1 >> pads([0,1,2,3], dur=1/2)

p1 >> pads([0,1,2,3], dur=[1,1/2])

p1.stop()

# What happens when we use lists for pitch and durations that are not equal size?

p1 >> pads([0,1,2,3], dur=[1,1/2,1/2])

# Useful keywords are "amp", "dur", "sus", "pan", "oct"

p1 >> pads([0,1,2,3], dur=[1,1/2,1/2], amp=[1.5,0.5], sus=2, pan=[-1,1], oct=[5,5,5,(4,6)])

# Ok - lets stop that.

p1.stop()

# Lets play with some drum sounds. To trigger audio samples we use a special instrument called "play"
# and instead of giving a list of pitches to play, we give it a string of characters in quotes

d1 >> play("x-o-")

d1.stop()

# Each character is mapped to a folder of samples. "x" is a kick drum, "-" is a hi-hat, and "o" is a snare.
# To select a different file in the folder, we use the "sample" keyword:

d1 >> play("x-o-", sample=1)

d1 >> play("x-o-", sample=2)

d1 >> play("x-o-", sample=[0,1,2])

d1.stop()

# It can be a list of numbers too! We can make our drum pattern more complex by using brackets

d1 >> play("x-o[--]")

d1 >> play("x-o(-o)")

d1 >> play("x-o{-o*}")

d1.stop()

# Can you work out what the brackets are doing? The square bracket plays multiple samples in the
# space of one step:

d1 >> play("x-o[--]")

d1 >> play("x-o[---]")

d1 >> play("x-o[-------]")

d1.stop()

# The round brackets alternates the sound used:

d1 >> play("x-o(-o)")

d1 >> play("x-o(-[-o])")

d1 >> play("x-o(-[-(-o)])")

d1.stop()

# And the curly braces selects a sample at random for more variety

d1 >> play("x-o{-o}")

d1 >> play("x-o{-[--]o}")

d1.stop()

# Just like before we can use keyword arguments:

d1 >> play("x-(-[-o])", dur=[3/4,3/4,1/2], pan=[-1,1])

# You can also change the rate the audio is played 

d1 >> play("x-(-[-o])", dur=[3/4,3/4,1/2], pan=[-1,1], rate=1)

d1 >> play("x-(-[-o])", dur=[3/4,3/4,1/2], pan=[-1,1], rate=2)

d1 >> play("x-(-[-o])", dur=[3/4,3/4,1/2], pan=[-1,1], rate=0.5)

d1 >> play("x-(-[-o])", dur=[3/4,3/4,1/2], pan=[-1,1], rate=-1)

d1 >> play("x-(-[-o])", dur=[3/4,3/4,1/2], pan=[-1,1], rate=[1,2,0.5,-1])

d1.stop()

# To play things at the same time, just use multiple Players. Try changing the values and adding keyword
# arguments to the code below:

p1 >> pads([0,2,4,9,7], dur=1/4)

d1 >> play("x-x-")
d2 >> play("  * ")

# To stop everything, press "Cmd+." or run the line of code below.

Clock.clear()

# You're at the end of part 1. Nice work - let me know when you get to this point.

#######################################################################

# Part 2: Putting together a tune
# -------------------------------

# Ok, so we've got the basics, lets make a basic tune! So far we've only used the major 
# scale, which the default, but we can use a whole bunch and even make up our own!
# To see the list of scales, use:

print(Scale.names())

# Let's use the dorian scale!

Scale.default = "dorian"

# All of the timing is handled by "Clock" and we can change the tempo if we want

Clock.bpm = 144

# 1. Let's start with a basic drum beat

d1 >> play("x ")

# 2. Add a bassline

b1 >> sawbass([0,-1,3], dur=[4,4,8])

# 3. Let's add some chords - we can make sure they fit with the bass by setting the pitch relative
# to the pitch of the bass, b1, using the addition operator (+ sign).

p1 >> star(b1.pitch)

p1 >> star(b1.pitch + (0,2,4))

p1 >> star(b1.pitch + (0,2,4), dur=[3/4, 3/4, 1/2])

# 4. Create you own melody to go with it - pitch a SynthDef

print(SynthDefs) # e.g. blip

# e.g. p2 >> blip([0,7,6,4,2], dur=1/2, sus=1)

p2 >>

# 5. Let's add to our drums. Try making this more complex by using the different brackets

d1 >> play("x-")

d2 >> play("  * ")

# What happens to our chords if we change the bass?

b1 >> sawbass([2,3,4,6], dur=4)

# Very nice! Press Cmd+. to stop playing or

Clock.clear()

#######################################################################

# Part 3: Algorithmic music

# Sometimes we want to give instructions to the Players that don't happen straight away. We
# can use the "every" function to say "every 8 beats, do something". For example:

p1 >> pads([0,1,2,3,4,5,6,7])

p1.every(8, "reverse")

p1.stop()

# Every 8 beats, the Player began to play the notes in descending order and then change
# again every 8 beats. We can also "shuffle" the order of the notes!

p1 >> pads([0,1,2,3,4,5,6,7])

p1.every(8, "shuffle")

p1.stop()

# Instead of putting everything on a newline, it's possible to "chain" these functions together:

p1 >> pads([0,1,2,3]).every(4, "reverse")

p1 >> pads([0,1,2,3]).every(4, "reverse").stop()

# Another interesting function is "stutter", which plays multiple sounds. After we name the "stutter",
# we can supply more arguments in the brackets like we did with the SynthDef:

d1 >> play("x-o-").every(4, "stutter")

d1 >> play("x-o-").every(4, "stutter", 4)

d1 >> play("x-o-").every(4, "stutter", 16)

# We can use keywords like we did above with stutter, to change how the function works

d1 >> play("x-o-").every(4, "stutter", 4, pan=[-1,1])

d1 >> play("x-o-").every(4, "stutter", 4, dur=3)

d1.stop()

# For "melodic" players (where we play notes), we can use a cool function called "offadd"
# which will play a new note on the off-beat, a few steps in the scale higher than the original:

# Start off with a basic sequence

x1 >> blip([0,2,3,4])

# Every 3 beats, play a note on the off-beat that is 4 steps higher

x1 >> blip([0,2,3,4]).every(3, "offadd", 4) 

# You can "chain" more than one repeated function together, just like you did with "stop" earlier:

x1 >> blip([0,2,3,4]).every(3, "offadd", 4).every(7, "stutter", 4)

# Try changing some of the keywords

x1 >> blip([0,2,3,4]).every(3, "offadd", 4).every(7, "stutter", 4, dur=3, pan=[-1,1], oct=6)

# Chain together as many different functions as you like!

x1 >> blip([0,2,3,4]).every(3, "offadd", 4).every(7, "stutter", 4, dur=3, pan=[-1,1], oct=5).every(8, "reverse")

# Now, if you've got this far - try and go back to the "tune" we just played and
# see how you can add variety by using the functions. Feel free to copy and paste
# some of the code from this section over to your tune.

#######################################################################

# Part 4: Adding and sequencing effects

# We can also add effects to the players and sequence them just as we have done
# with durations and pitches. We can add reverb by specifying the room size and
# what percentage to mix the reverberated sound:

p1 >> blip(dur=4, sus=1)

p1 >> blip(dur=4, sus=1, room=1, mix=0.5)

p1 >> blip(dur=1, sus=1, room=[0,0.25,0.5,1], mix=[0, 0.1, 0.3, 0.5])

p1.stop()

# Could you hear the difference? Below are some other effects to try out. See if
# you can apply them to other SynthDefs, not just the ones written below. Remember
# Ctrl+. will stop all the sound.

# High Pass Filter - only lets frequencies *above* this value into the signal

d1 >> play("x-o-")

d1 >> play("x-o-", hpf=500)

d1 >> play("x-o-", hpf=5000)

d1 >> play("x-o-", hpf=[0,100,250,500,1000,2000,4000,8000])

d1.stop()

# Low pass filter - only lets frequences *below* this value into the signal

d1 >> play("x-o-")

d1 >> play("x-o-", lpf=5000)

d1 >> play("x-o-", lpf=500)

d1 >> play("x-o-", lpf=[50,100,200,400,800,1600,3200,6400])

d1.stop()

# Chop - chops the signal into "n" parts

p1 >> pluck([0,4], dur=4, chop=4)

p1 >> pluck([0,4], dur=4, chop=8)

p1 >> pluck([0,4], dur=4, chop=320)

p1.stop()

# -- What happens when you use a different sustain than duration?

p1 >> pluck([0,4], dur=[3/4,3/4,1/2], chop=4)

p1 >> pluck([0,4], dur=[3/4,3/4,1/2], chop=4, sus=2)

p1.stop()

# Shape - wave shape distortion

b1 >> bass(dur=8)

b1 >> bass(dur=8, shape=0.5)

b1 >> bass(dur=8, shape=[0.1,0.2,0.3,0.4,0.5,0.6,0.7,0.8,0.9,1.0])

# -- Try combining different effects in the same player:
    
b1 >> bass(dur=8, shape=[0.1,0.2,0.3,0.4,0.5,0.6,0.7,0.8,0.9,1.0], chop=16, room=0.5, mix=0.2)


# Challenge time! Use "room", "chop", "hpf", "lpf", and "shape" in the tune we
# worked on to customise your sound and add your own bit of flair.

#######################################################################

# Part 5: Patterns

# Python uses "lists" to store multiple items of data but they aren't often manipulated
# in a way that is useful for creating interesting music. That's why FoxDot uses data type
# called Pattern that is an extension of "lists"

# To create a simple pattern, just put an upper-case 'P' before a list:

l = [0, 1, 2, 3]
p = P[0, 1, 2, 3]

print(l, type(l))
print(p, type(p))

# Now we can do interesting things with 'p' that we can't do with 'l'. For example,
# if we want to double all the values in 'l', the shortest way to do that is like so:
    
print([x * 2 for x in l])

# This is a bit cumbersome, especially compared to how we do it with patterns:
    
print(p * 2)

# We can do any arithmetic we want, and even use lists/patterns:
    
print(P[0, 1, 2, 3] * [1, 4])

# Lists also come with a whole bunch of useful methods for manipulating order etc

print(p.reverse())

print(p.rotate())

print(p.palindrome())

print(p.stretch(6))

# We can chain these together:
    
print(p.reverse().palindrome().rotate() * 2)

# You can even "autofill" a pattern with numbers if you're feeling lazy. It is
# very similar to the 'range' function  in Python where you  specify the start,
# the end, and the step size of the range of numbers you want:
    
print(P[0:10])

print(P[10:0:-1])

print(P[0:10:2].shuffle()) # We can use methods on these autofilled series

# To see more information about Pattern methods, run

help(Pattern)

# Let's do a few more useful examples then see how we can use them in performance:
# To join two or more patterns together, use the "bar" symbol like so:
    
print(P[:4] | P[:4].shuffle()) # We get 0-4 in series, then in a random order

# To create groups of values, such as chords, in Patterns, you can use the & symbol
# to "zip" two patterns into one pattern of groups - don't worry if they're different sizes

print(P[:4] & P[9, 11])

# To get a subset of a pattern, we can use normal Python indexing. For example, if we
# just want one item from a pattern, we put square brackets at the end of the pattern
# and the  number of the item we want:
    
evens = P[2, 4, 6, 8]

print(evens[2]) # Get the item at index 2, which is 6 - indices start at 0!

# To get a subset, we supply range like we did to generate a series!

print(evens[0:3]) # We get the first three items in the list

# Even if the range goes past the end of the pattern, we'll get the size we asked for

print(evens[0:6])

# Let's create a neat melody using a pattern

p1 >> blip(P[:10:2][:8].rotate(-3), dur=1/2, sus=2)

# Combine with a "PStep" pattern

p1 >> blip(P[:10:2][:8].rotate(-3) + PStep(8,[0,3]).rotate(), dur=1/2, sus=2)

p1.stop()

# So what is PStep? Well, there are some functions that exist in FoxDot for generating
# patterns for you to save some typing. Let's look at a few useful ones:
    
print(PStep(5,4,0)) # Pattern of length 5, ending with a 4, filled with 0s

print(PDur(3,8)) # Euclidean rhythm, 3 pulses over 8 steps

print(PSine(8)) # n values representing a sine wave

# Let's put them into practice

p1 >> blip(P[:10:2][:8].rotate(-3) + PStep(8,[0,3]).rotate() | P[[9,11]], dur=PDur(3,8), sus=2, pan=PSine(16).shuffle())

d1 >> play("Xs")

b1 >> dbass([0, 2, 3, 4], dur=8)

Clock.clear()

# The Pattern methods, such as 'palindrome' and 'trim', can be called regularly, just like Player methods
# such as "stutter" to create patterns that change over time!

p1 >> blip(P[:10:2], dur=PDur(5,8)*2, sus=2, oct=PStep(7,5,6)).every(6, "reverse").often("trim", 3).every(9, "stutter", 4, dur=3)

d1 >> play("Xs")

b1 >> dbass([0, 2, 3, 4], dur=8)

Clock.clear()

#######################################################################

# Part 6: Using time to create extended sequences

# So far we've been using lists of numbers for things like pithes and durations
# but what if we want values to change depending on time instead of the sequence?
# Here's an example:

# Lets use a bass to play these notes for 8 beats each

b1 >> bass([0, 3], dur=8)

# What if we want to change the duration but keep playing the notes for 8 beats each?

b1 >> bass([0, 3], dur=PDur(3,8))

b1.stop()

# It doesn't work. This is where we use a tool called "var" which means "variable"
# and it varies depending on the beat:

b1 >> bass(var([0, 3], dur=8), dur=PDur(3,8))

b1.stop()

# It played each pitch for 8 beats each, even though the durations were less than 8.
# We create a "var" by using the code - var(list_of_values, dur=duration)

b1 >> bass(var([0, 3], dur=8), dur=PDur(3,8))

# Notice the difference between changing the duration in the bass and the duration in the var

b1 >> bass(var([0, 3], dur=8), dur=PDur(5,8))

b1 >> bass(var([0, 3], dur=[6, 2]), dur=PDur(5,8))

b1.stop()

# These are especially useful for creating chord sequences. Let's use it in our "tune" from earlier:
# Here was our bass to start with:

b1 >> sawbass([0,-1,3], dur=[4,4,8])

# Let's create a var called "chords" so we can use in more than player:

var.chords = var([0,-1,3], dur=[4,4,8])

b1 >> sawbass(var.chords, dur=1)

# We can now change the duration to whatever we want...

b1 >> sawbass(var.chords, dur=PDur(3,8)*2)

# ...and other instructions to create interesting patterns!

b1 >> sawbass(var.chords, dur=PDur(3,8)*2, oct=[5,5,[6,4],5], pan=[0,[-1,1]]) + [0,0,4,0,7]

# We can use the "var.chords" variable as a single note in a list:

p1 >> blip([var.chords,2,3,4], sus=2)

# Listen to the first note in the sequence, it changes with the chords. We can continue
# to add all sorts of functions to the sequence to make it more interesting

p1 >> blip([var.chords,2,3,4], sus=2).every(3, "offadd", 4)

p1 >> blip([var.chords,2,3,4], sus=2).every(3, "offadd", 4).every(7, "stutter", 4, dur=3, pan=[-1,1], oct=6)

p1 >> blip([var.chords,2,3,4], sus=2).every(3, "offadd", 4).every(7, "stutter", 4, dur=3, pan=[-1,1], oct=6).every(8, "reverse")

# Now let's introduce our triads again. This time we'll use "var.chords" instead
# of "b1.pitch" when adding (0, 2, 4).

p2 >> star(var.chords + (0, 2, 4), dur=PDur(3,8))

# Question: What happens if we do use b1.pitch? Why does it happen?

p2 >> star(b1.pitch + (0, 2, 4), dur=PDur(3,8))

# Let's introduce some percussion again!

d1 >> play("x-")

d2 >> play("  H ")

# Let's use a new "var" to apply a high pass filter to the drums for the last bar of an 8 bar cycle
# Set the filter to be 0 for 28 beats (7 bars x 4 beats) and then 4000 for 4 beats (1 bar x 4 beats)

var.filter = var([0,8000], dur=[28,4])

d1 >> play("x-", hpf=var.filter)
d2 >> play("  H ", hpf=var.filter)

# Try and add your elements to the mix - see if there are other interesting ways of
# combining the "var.chords" variable. 

# - Try applying the "var.filter" to p1, p2, and b1.
# - Try using brackets and .every to make the percussive sounds more complex
# - What happens when you change "var.chords"? e.g. 

var.chords = var([2,3,4,6], dur=4)

# When you're done, press Cmd+. or run:

Clock.clear()

#######################################################################

# Part 7: PGroups and complex patterns

#######################################################################

# So far we've referred to numbers in round brackets like this: (0, 2, 4)
# as groups of values. FoxDot treats these as a datatype called "PGroup"
# which is a type of Pattern. Look at the code below:
    
print(P[0, 1, 2, (3, 4)])

# We get P[0, 1, 2, P(3, 4)] - the last item is a PGroup. Like with
# Patterns, we can just put a "P" in front of the brackets to convert
# it to a PGroup and do some cool stuff with it:

print(P(0, 1, 2, 3, 4).reverse())

print(P(0, 1, 2, 3, 4).shuffle())

# Along with playing notes together like so:
    
p1 >> pads(P(0, 2, 4, 6), dur=4)

p1.stop()

# PGroups can also be used to play notes in quick succession by putting
# different symbols between the 'P' and the brackets:

p1 >> pads(P(0, 2, 4, 6), dur=4)    

p1 >> pads(P*(0, 2, 4, 6), dur=4)

p1 >> pads(P*(0, 2, 4, 6), dur=2)

p1.stop()

# Notice the difference? The P* plays all the notes across the note's
# duration - just like the square brackets in the "play" synth. You
# can use the + symbol to spread the notes over a note's sustain
# as opposed to the duration, which can be useful when using varying
# lengths of durations:
    
p1 >> pluck(P*(0, 4), dur=PDur(3,8), sus=1)

p1 >> pluck(P+(0, 4), dur=PDur(3,8), sus=1)

p1 >> pluck(P+(0, 4), dur=PDur(3,8), sus=2)

p1.stop()

# We use one of these PGroups when we use the Pattern "offadd" method
# which allows us to specify the durations between notes using the 
# ^ symbol and the duration as the last value in the group:
    
print(P[0, 1, 2, 3].offadd(4))
    
p1 >> pluck(P^(0, 2, 4, 0.5), dur=4) # delay of 0.5 beat

p1 >> pluck(P^(0, 2, 4, 0.75), dur=2) # delay of 0.75 beat

p1 >> pluck([P*(0, 3), P^(0, 2, 4, 0.75)], dur=2) # Combining multiple PGroups

p1.stop()

# So P[:4].offadd(4) is essentially just P[:4] + P^(0, 4, 0.5)!

p1 >> pluck(P[:4].offadd(4))

p1 >> pluck(P[:4] + (P^(0,4,0.5)))

p1.stop()

# These are useful to create variations in rhythm without having to create a
# complex "dur" argument. e.g. to create the simple melody below:
    
p1 >> pluck([[0, P*(0, 0)], 2, -3, 2])

# We would need to do this:
    
p1 >> pluck([0, 2, -3, 2, 0, 0, 2, -3, 2], dur=P[1,1/2,1].stutter([4,2,3]))

p1.stop()

# Which is a lot of typing and thinking - and we want to focus on making music!

#######################################################################

# Part 8: Advanced Sample Sequences

#######################################################################

# Let's create a very simple drum pattern

d1 >> play("xs", sample=3)
d2 >> play("  * ", sample=3)
d3 >> play("(d  )d( [( d)d])", sample=3)

Clock.clear()

# We've had to use three separate players for what is just one drum
# sequence. While this can make it easier to change attributes, such
# as durations or amplitude for individual parts of the sequence,
# it can also be useful to treat the sequence as a whole. We can "layer"
# several sample strings over one another by putting sequences next to
# one another but surrounded with <> arrows like so:
    
d1 >> play("<xs><  * ><(d  )d( [( d)d])>", sample=3)

d1.stop()

# Make sure there are no spaces between the different patterns! You
# can also use these brackets to play individual samples together in
# a sequence like this:
    
d1 >> play("x-<*><o>-")

# Although sometimes its easier to split them up into separate sequences:
    
d1 >> play("<x-*-><  o >")

d1.stop()

# The sequences don't need to be the same length, so try multiple
# sequences with different lengths!

# You can think of each sequence as layers on top of each other that
# are grouped together using PGroups. If you want to change attributes
# or effects for an individual layer, we need to use PGroups when
# doing so. So if we have 3 layers and we want to set the sample for 
# the first layer to 2 but the others as 0, we could use code that
# looks like this:
    
d1 >> play("<xs><  * ><(d  )d( [( d)d])>", sample=P(2, 0, 0))

d1.stop()

# Similarly, if I want to set the stereo panning of the last layer to
# alternate left then right (i.e. -1 and 1) then I could use code 
# that looks like this:
    
d1 >> play("<xs><  * ><(d  )d( [( d)d])>", sample=P(2, 0, 0), pan=P(0, 0, [-1, 1]))

d1.stop()

# This all comes in very useful when you want to use the "every"
# method with a more complex sequence:
    
d1 >> play("<xs><  * ><(d  )d( [( d)d])>", sample=P(2, 0, 0), pan=P(0, 0, [-1, 1])).every([12,4], "trim", 3)

d1.stop()

# When you create a complex sequence, you might want to use a specific
# sample which would take a separate value to the rest of the sequence.
# e.g. You want the '*' sample to be 2 but others to be 0, well you could 
# do it this way:
    
d1 >> play("x-*-", sample=[0,0,2,0])

d1.stop()

# But what happens when you change the sequence?

d1 >> play("x-*(-[-*])", sample=[0,0,2,0])

# You then need to *also* update the sample keyword argument to this:

d1 >> play("x-*(-[-*])", sample=[0,0,2,[0,(0,2)]])

d1.stop()

# That's a bit annoying. You can actually specify the sample number
# for a specific character by putting it in between bars || with the
# number you want:
    
d1 >> play("x-|*2|-")

d1 >> play("x-|*2|(-[-|*2|])")

d1.stop()

# You can also use sequences / patterns in this way too!

d1 >> play("x-o|n[01]|")

d1 >> play("x-|o(02)|-")

d1 >> play("x-|o(0[20])|-")

d1 >> play("x-o|a{0123}|")

d1.stop()

# Note: This overrides the sample keyword

d1 >> play("x-*-", sample=2)

d1 >> play("x-|*1|-", sample=2)

d1.stop()

# Put this all together for a funky beat in one line of text:

d1 >> play("<|x2|s><  |*(3[33])| ><(d  )d( [( d)d])>", pan=P(0, 0, [-1,1]))

d1.stop()

#######################################################################

# Ok, use this space below to use what you know and start a jam. Think of
# it as a template:
    
Clock.bpm = 120 # Pick your own bpm

print(Scale.names()) # Pick your own scale!

Scale.default = "minor"

print(SynthDefs) # Pick your own synths!

b1 >> sawbass(var([0, 2], 8), dur=1)

p1 >> keys(b1.pitch + (0, 2, 4), dur=8)

p2 >> blip(P[0, 2, 4].stretch(8), dur=1/2, sus=2) + var([0, 2], [6, 2])
    
d1 >> play("<xs><  * ><(d  )d( [( d)d])>", sample=3)

Clock.clear()

# Some ideas:
    
# Change the duration of b1
# Change the values in the "var" inside b1
# Change the SynthDef for p1
# Use the "every" method with p2 to reverse or shuffle the order of the melody
# Use pan=P*(-1,1) somewhere to shift sounds across the stereo
# Add effects like "hpf" to d1 to add some tension then take the effect away
# Add your own sequence
# Delete it all and start from scratch!

#######################################################################

# we've reached the end of the workshop! Now you have all the basic building 
# blocks required for sequencing notes and percussion, as well as adding effects
# to the sound and manipulating our sequences with algorithms.

# No one becomes an expert over night but with a little practice you can be
# throwing your own Algorave with your friends very soon!
