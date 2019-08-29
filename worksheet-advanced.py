# FoxDot Advanced Workshop
# ========================

# This worksheet is a direct follow on from the FoxDot introduction
# worksheet and assumes that you understand most of the key concepts
# it introduces. If you haven't completed the introduction first,
# it is advised that you do so before continuing.

# Part 1: Scales, roots, and tempo
# --------------------------------

# There are a number of existing scales in FoxDot that can be used:

print(Scale.names())

# To set the "default scale", just assign the scale name to Scale.default,
# and all the players will updated immediately:

p1 >> pluck((0, 2, 4))

p2 >> blip(P[:8], dur=1/2)

Scale.default = "minor"

Clock.clear()

# Each scale has a subset scale, called its pentatonic, that can be accessed
# by using the .pentatonic attribute:

print(Scale.major, Scale.major.pentatonic)

# You can specify a player object to use a different scale to the default
# by using the 'scale' keyword like so:

p1 >> pluck((0, 2, 4))

p2 >> blip(P[:8], dur=1/2)

p2 >> blip(P[:8], dur=1/2, scale=Scale.minor.pentatonic)

Clock.clear()

# A short-hand method for using the pentatonic scale as default is .penta()
# and will update the scale even if the defautl scale changes.

p1 >> pluck((0, 2, 4))

p2 >> blip(P[:8], dur=1/2).penta()

Scale.default = "major"

Clock.clear()

# As well as changing the scale, we can change the "key", or "root". 
# By default this is 0, which is equal to middle C. You can set the root
# in the same way as the scale, but using Root.default with a number (of
# semitones above/below middle C) or a note letter:

p1 >> pluck((0, 2, 4))
p2 >> blip(P[:8], dur=1/2).penta()

Root.default = 2

Root.default = -2

Root.default = "F#"

Root.default = "Eb"

Root.default = var([0, 2], 8)

Clock.clear()

# You can even use a TimeVar to change it automatically! Just as you
# can specify a player object's scale explicitly, you can specify the 
# root too: 

Root.default = 0

p2 >> blip([0, 7, 6, 4, 2], dur=1/4, sus=2, root=var([0, 2], 8))

Clock.clear()

# Tempo works in a very similar way to root and scale; you just need
# to update the Clock.bpm value, which starts off at 120 beats per minute
# by default:

p1 >> pluck(P[:4])

Clock.bpm = 130

Clock.bpm = 145

Clock.bpm = 100

Clock.clear()

# Unlike changing the scale and root, changing the tempo doesn't happen
# immediately, but at the start of the next bar. This helps keep FoxDot
# running in time better, especially when synchronised to something else.

# You might find you want to udpate tempo immediately, however. If, for
# example, you set the tempo to 10 instead of 100, you will have to wait 
# until the next bar to update the tempo, which will take nearly 30 seconds!
# To update the tempo immediately, use Clock.update_tempo_now()

p1 >> pluck(P[:4])

Clock.bpm = 10

Clock.update_tempo_now(100)

Clock.clear()

# You can also use a TimeVar for the tempo to change the bpm at certain
# times, but beware, the clock is more likely to drift when this happens
# so isn't advised when synchronised to an external application:

p1 >> pluck((0, 2, [4, 6, 7]), dur=PDur(3,8), sus=2, chop=4)
d1 >> play("x-o-")

Clock.bpm = var([120, 60, 30], [12, 2, 2])

Clock.clear()

# Similar to root and scale, player object's can have their own tempo!
# This can be set using the 'bpm' keyword:

Clock.bpm = 120

p1 >> pluck([0, 2, 3, 4, 5], pan=-1)
p2 >> pluck([0, 2, 3, 4], pan=1, bpm=180)


# Part 2: Groups of players
# -------------------------

# When you have multiple players playing at once, it can be useful
# to stop/start or apply effects to groups of players in one command.
# FoxDot allows you to group players together by simply wrapping them
# in a Group() object:

p1 >> play("X-O-")
p2 >> sawbass(var([0, 5], 8), dur=1/2, amp=[0,1])
p3 >> star([0, 4], dur=PDur(3,8), sus=2, chop=4)

Group(p1, p2, p3).lpf = 400

Group(p1, p2, p3).lpf = 0

Group(p1, p2, p3).stop()

# This can be combined well with the 'amplify' attribute (different to 'amp')
# to create "drops" in your music (amplify is discussed in more depth in the
# next part)

p1 >> play("X-O-")
p2 >> sawbass(var([0, 5], 8), dur=1/2, amp=[0,1])
p3 >> star([0, 4], dur=PDur(3,8), sus=2, chop=4)
p4 >> play("#", dur=32, amp=2)

Group(p1, p2, p3, p4).amplify=var([1, 0],[28, 4])

Clock.clear()

# FoxDot has some short-hand ways of accessing group of similarly named
# player objects. For example, to access a group of all the players 
# beginning with 'p' (p1 - p9) you can use 'p_all':

p1 >> play("X-O-")
p2 >> sawbass(var([0, 5], 8), dur=1/2, amp=[0,1])
p3 >> star([0, 4], dur=PDur(3,8), sus=2, chop=4)
p4 >> play("#", dur=32, amp=2)

p_all.amplify=var([1, 0],[28, 4])

p_all.stop()

# You should name your player objects appropriately, e.g. starting
# with 'd' for drums and 'p' for players. This allows you to control
# groups of players easily using the _all groups:

d1 >> play("X-O-")
d2 >> play("#", dur=32, amp=2)
d3 >> play("{ +[ +]}")

p1 >> sawbass(var([0, 5], 8), dur=1/2, amp=[0,1])
p2 >> star([0, 4], dur=PDur(3,8), sus=2, chop=4)

d_all.lpf = 400

p_all.hpf = 1000

d_all.lpf = p_all.hpf = 0

Group(p_all, d_all).amplify = var([1,0], [28,4])

Clock.clear()

# Note that you can use Group() with groups, which makes it easy
# to combine groups if you need to!

# Part 3: effects and attributes in detail
# ----------------------------------------

# We're going to go through all of the attributes that you can use 
# FoxDot player objects one by one on the FoxDot documentation site
# which has example code you can copy and paste here. 

# The keywords you have been using inside player objects relate to
# player object attributes and effects. Attributes affect player 
# objects behaviour and effects alter the sound. Let's start with
# the attributes. These are (in no particular order):

# degree, oct, dur, amp, sample, delay, amplify, scale, root, and bpm.

# We have covered most of these already, but will look at 'delay' 
# and 'amplify' now.

# Delay
# -----

# In music (and especially electronic music) delay often refers to a 
# sort of "echo" effect where a sound is played again a short period 
# after it begins, but a little quieter. In FoxDot, however, it literally 
# refers to an amount of time, in beats, to delay a sound from being
# played. Here, we’ll delay every third note by half a beat:

p1 >> pluck([0, 1, 2, 3], delay=[0, 0, 0.5])

p1.stop()

# If you want to play the note and play it with a delay, you can use 
# a tuple or PGroup with the first value being 0, meaning no delay. 
# The second value will indicate how long to delay the second note:

# "Stutter" every third note

p1 >> pluck([0, 1, 2, 3], delay=[0, 0, (0, 0.5)])
 
# Delay a note to play *after* the following one

p1 >> pluck([0, 1, 2, 3], delay=[0, 0, (0, 1.5)])

p1.stop()

# Amplify
# -------

# Before a sound gets triggered by a player, the 'amp' value is multiplied
# by 'amplify' so that you can use things like TimeVar to set an amplitude
# to be 1 or 0 (i.e. on and off) for certain amount of time:

d1 >> play("X:")
p1 >> pluck(dur=1/4, amp=[1,1,1,1,1,0], amplify=var([1,0],[6,2])) 

Clock.clear()

# This is useful if you want to set Groups to be "on" or "off" at the same time:

d1 >> play("X:")
p1 >> pluck(dur=1/4, amp=[1,1,1,1,1,0])
p2 >> bass(var([0, 3], 8), dur=1/2)
 
p_all.amplify = var([1,0], [14,2])

Clock.clear()

# Now let's take a look at what effects we can use with our players. You can 
# view all of the effects by simply running:

print(Effects)

# Let's break down what this returns: it's a list of all of the effects and 
# the arguments used to apply them. The full name of the effect is on the 
# left, followed by it's "parent" argument and "child" arguments. 

# The parent argument is the main keyword used, the child arguments are
# supplementary keywords that are also used in the effect. When the parent
# argument is set to 0, the effect is no longer applied. However, child
# arguments can be set to 0 while the effect *is* applied.


# Let's look at some examples:

# <Fx 'wavesShapeDistortion' -- args: shape>

p1 >> pluck([0, 1, 2, 3], shape=var([0, 0.25, 0.5, 1]))

p1.stop()

# <Fx 'vibrato' -- args: vib, vibdepth>

p1 >> pluck([0, 1, 2, 3], vib = var([0, 4, 12, 25]))

p1 >> pluck([0, 1, 2, 3], vib = var([0, 4, 12, 25]), vibdepth=var([0.01, 0.05, 0.1, 0.5], 32))

p1.stop()

# <Fx 'tremolo' -- args: tremolo, beat_dur>

p1 >> pluck((0, 2, 4), dur=4, tremolo=[0, 2, 4, 8])

p1.stop()

# The 'beat_dur' argument is automatically supplied by FoxDot and is equal to the 
# duration of 1 beat in seconds.

# Let's go through the rest of the effects in-depth now. Open your preferred browser
# and navigate to the following URL:
#
#    https://foxdot.org/docs/player-effects/
#

# Part 4: Pattern methods in detail
# ---------------------------------

# Let's look at a few Pattern methods in detail and useful ways to implement them
# in a live coding performance.

# Offadd / Offmul
# ---------------

# These methods add / multiply the values in a Pattern and then use PGroups to
# play them with a slight delay

p1 >> pluck(P[0, 1, 2, 3])

p1 >> pluck(P[0, 1, 2, 3].offadd(2))

p1 >> pluck(P[0, 1, 2, 3], pan=P[-1,1])

p1 >> pluck(P[0, 1, 2, 3], pan=P[-1,1].offmul(-1))

p1.stop()

# This can be really useful when combined with the "every" method

p1 >> pluck([0, 4], dur=PDur(3,8)).every(3, "offadd", 2)

p1.stop()

# You can use the 'every' method with an attribute other than pitch, by
# specifying it's name followed by a dot then the method, like so:

p1 >> pluck([0, 4, 6, 7], lpf=4000, lpr=0.2).every(3, "lpf.offmul", 1/2)

p1.stop()

# We can also specify the duration to delay the note by, which defaults
# to half a beat, by specifying an extra argument, either named or un-named

p1 >> pluck(P[0, 1, 2, 3].offadd(2, dur=0.75))

p1 >> pluck(P[0, 1, 2, 3].offadd(2, 0.75))

p1 >> pluck(P[0, 1, 2, 3]).every(4, "offadd", 2, dur=0.25)

p1.stop()

# Also works for 'offmul' too.

p1 >> pluck([0, 4, 6, 7], lpf=4000, lpr=0.2).every(3, "lpf.offmul", 1/2, dur=0.75)

p1.stop()

# Trim
# ----

# This is a very simple method that shortens a Pattern to the length you supply:

print(P[:8].trim(3))

p1 >> pluck(P[:8])

p1 >> pluck(P[:8].trim(3))

p1.stop()

# Like most Pattern methods, most arguments can be supplied as a list to return
# extended Patterns like so:

print(P[:8].trim([3, 2]))

p1 >> pluck(P[:8])

p1 >> pluck(P[:8].trim([3, 2]))

p1.stop()

# This also works for play-strings, when wrapped in P[]

p1 >> play(P["x-o-"].trim([3, 2]))

p1.stop()

# And, of course, can be used with the 'every' method:

p1 >> play("x-o-").every([12, 4], "trim", 3)

p1 >> play("x-o-").every([12, 4], "trim", [3, 2])

# Add some bass and percussion and it sounds like an organic drum fill

b1 >> bass(var([0, 1, 5, 3]), dur=1/2, drive=0.2)

b2 >> play("#", dur=16)

Clock.clear()

# Amen
# ----

# Yes, there's even a method for replicating the  famous "amen break"!

print(P["x-i-"].amen())

# It doesn't look like much, but here is what it sounds like:

Clock.bpm=140

p1 >> play(P["x-i-"].amen())

p1 >> play("x-i-").every(8, "amen")

# Add some bass and percussion again...

b1 >> bass(var([0, 1, 5, 3]), dur=1/2, drive=0.2)

b2 >> play("#", dur=16)

Clock.clear()

# Let's go through some of the other methods now. Open your preferred browser
# and navigate to the following URL:
#
#    https://foxdot.org/docs/pattern-methods/
#
# Try some out and see what happens!