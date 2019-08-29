# FoxDot Advanced Workshop
# ========================

# This worksheet is a direct follow on from the FoxDot introduction
# worksheet and assumes that you understand most of the key concepts
# it introduces. If you haven't completed the introduction first,
# it is advised that you do so before continuing.

# Part 5: Player Keys
# -------------------

# Player Keys are the easiest way to create relationships between your Player objects. 
# They let you share data in a reactive and dynamic way. They are accessed as you would 
# any Python object attribute, by typing the name of the object, a dot, then the name 
# of the attribute e.g. p1.pitch. The neat thing about Player Keys is that, if the 
# original Player is updated, so is the Player Key, so you don’t need to worry about 
# re-evaluating any code.

p1 >> pads([0, 4, 5, 3], dur=4)
p2 >> pluck(p1.pitch, dur=1/2)

Clock.clear()

# These work for all Player attributes:

p1 >> pluck(dur=1/2, amp=PRand([0, 1]))

p2 >> play("*", amp=p1.amp)

Clock.clear()

# You can also use a player key within a sequence:

p1 >> sawbass([0, 4, 5, 3], dur=4)

p2 >> star([p1.pitch, 7, 6, 7], dur=1/2, sus=1)

# You can create relationships in your music by combining simple maths and Player
# Keys. For example, adding +2 to a player's pitch will usually create a "harmony":

p1 >> sawbass([0, 4, 5, 3], dur=2)

p2 >> star(p1.pitch + 2, dur=PDur(3,8))

Clock.clear()

# You can add groups of values in round brackets to create chord relationships:

p1 >> sawbass([0, 4, 5, 3], dur=2)

p2 >> star(p1.pitch + (0, 2, 4), dur=PDur(3,8))

Clock.clear()

# Or use a series of values in a list or a Pattern:

p1 >> sawbass([0, 4, 5, 3], dur=2)

p2 >> star(p1.pitch + P[:6:2].palindrome(), dur=PDur(3,8))

Clock.clear()

# Of course, you can always multiply and divide values. For example, you can
# put two players in opposite channels using .pan and multiplying by -1 even
# when using random values:

p1 >> play("*", dur=PDur(3,8), pan=PRand([-1, 1]))

p2 >> play("+", dur=1/4, amp=PRand([0,1]), pan=p1.pan*-1)

Clock.clear()

# If you have some experience with computer programming, you might have come
# across logic operators, such as "is not equal to", which looks like '!='.

# This can be used to create some cool relationships, such as "play a note
# when one player *isn't* playing a note":

p1 >> pluck(amp=PRand([0,1]), dur=1/2)

p2 >> play("x", amp=p1.amp != 1)

Clock.clear()

# Sometimes we don't want one-to-one relationships and we can make FoxDot make
# a decision about appropriate notes to play. To do this with pitch, we can
# use the '.accompany()' method like so:

b1 >> sawbass(var([0, 1, 5, 3]), dur=PDur(3,8))

p1 >> star(b1.pitch.accompany())

Clock.clear()

# Try using it in a jam:

b1 >> sawbass(var([0, 1, 5, 3]), dur=PDur(3,8))

p1 >> star(b1.pitch.accompany(), delay=0.5)

d1 >> play("(x )( x)i( [ i])")
d2 >> play("[--]")

Clock.clear()


# Part 6: Playing loops
# ---------------------

# The 'loop' synth is designed to let you play longer audio files (>1 sec) and manipulate them. 
# To get started, just supply the filename you want to play and the duration you want to play in beats:

# e.g. p1 >> loop("path/to/my/my_file.wav", dur=32)

# You can put files in a special folder located in FoxDot/snd/_loop_ which can be opened by going 
# to "Help & Settings" and then "Open Samples Folder" from the FoxDot menu. You don’t need to supply 
# the full path (or extension) for files in this folder:

# For example, there is a file called 'foxdot.wav' in this folder.

p1 >> play("foxdot", dur=4)

# To see all the files in this folder use:

print(Samples.loops)

# If you want to play with the play back order, you can supply a "position" argument after the file 
# name that FoxDot will iterate through based on the duration. So to play the first 4 beats of audio 
# in order:

p1 >> loop("foxdot", P[:4], dur=1)
 
# Or play the first 4 beats in random order:

p1 >> loop("foxdot", P[:4].shuffle(), dur=1)

# Or play a random selection of snippets quickly:

p1 >> loop("foxdot", PRand(32)[:16], dur=1/4)

d1 >> play("<(X )( X)O ><[--]>< + + ( [ +])>")

Clock.clear()

# Let's use some drum loops now to see how to use them in a song. Copy the file "drums135.wav" from
# the worksheet folder into the FoxDot loops file (Help & Settings -> Open samples folder -> _loop_)

# Then run:

p1 >> loop("drums135")

p1.stop()

# By default it only plays the first beat, let's play the first 4:

p1 >> loop("drums135", P[:4])

p1.stop()

# Sounded weird didn't it? That's because we're playing through the loop at 120bpm (or whatever
# the current tempo is) and not the tempo of the loop, which is 135. We can tell FoxDot what
# tempo to loop through the audio by using the 'tempo' keyword:

p1 >> loop("drums135", P[:4], tempo=135)

p1.stop()

# When changing the duration, the position needs to updated too. So when the duration is 1/2 beat,
# the position argument needs to be in steps of 1/2 also, then can be done easily but requires
# some thought:

p1 >> loop("drums135", P[:8]/2, dur=1/2, tempo=135)

p1.stop()

# We can use pattern methods to do some cool stuff with simple sequences:

p1 >> loop("drums135", P[:4].offadd(1, 0.25), tempo=135)

p1 >> loop("drums135", P[:4], tempo=135).every(4, "offadd", 1.5, 0.25)

p1 >> loop("drums135", P[:4], tempo=135).every(4, "offadd", 1.5, 0.25).every(5, "stutter", 4, dur=3)

p1 >> loop("drums135", P[:4], tempo=135).every(4, "offadd", 1.5, 0.25).every(5, "stutter", 4, dur=3).every(8, "shuffle")

p1.stop()

# And, of course, you can apply filters:

p1 >> loop("drums135", P[:4], tempo=135, lpf=2000, lpr=0.2).every(4, "offadd", 1.5, 0.25).every(5, "stutter", 4, dur=3)

p1 >> loop("drums135", P[:4], tempo=135, slide=PStep(7,-2)).every(4, "offadd", 1.5, 0.25).every(5, "stutter", 4, dur=3)

p1.stop()

# One of the issues with this technique is that there the audio is "pitch shifted", you 
# can stretch the whole file without changing pitch using the 'stretch' synth and without
# knowing the tempo beforehand. Let's look at an example. Copy the file 'kano.wav' from 
# the worksheet folder in the loops folder like you  did with 'drums135.wav'. Now, let's
# try using it with 'loop'

Clock.bpm=140

p1 >> loop("kano", dur=4)

d1 >> play("x-o-")

# Ouch, not very good so far as we don't know the tempo!

p1 >> stretch("kano", dur=4)

# Sound better?

Clock.clear()

# Note: you can't use the "position" argument with stretch, and it stretches the whole audio file.

# Part 7: Advanced time-vars
# --------------------------

# You can supply a TimeVar as an input to many FoxDot functions, such as PDur, to create Patterns
# that change over time:

d1 >> play("X", dur=PDur(3, 8))

d1 >> play("X", dur=PDur(var([3,5], [6,2]), 8))

d1 >> play("X", dur=PDur(var([3,5], [6,2]), 8, var([0,1])))

d2 >> play(" -H-")

Clock.clear()

# You can see a full list of Pattern functions here: https://foxdot.org/docs/pattern-functions/

# Try with some of the other functions:

p1 >> pluck(oct=PStep(4, var([4,6], [6,2]), 5), dur=1/4)

p1 >> pluck(oct=PStep(4, var([4,6], [6,2]), 5), dur=1/4, formant=PRand(5))

d1 >> play("X", dur=PDur(var([3,5], [6,2]), 8, var([0,1])))

d2 >> play(" -H-")

Clock.clear()

# As well as using TimeVars to create values that change over time, you can use them to 
# change *gradually* over time. To do this, you can use a 'linvar':

# Run this line a few times:

print(var([0,1]), linvar([0,1]))

# You can see how the 'var' only returns 0 or 1, but the 'linvar' increases/decreases in value
# over time. Let's look at some useful examples:

p1 >> dirt([0, 6, 4, 2], dur=1/4, hpf=linvar([0, 4000], 16))

p1.stop()

# The duration argument relates to how long it should take to change value, so, for the following
# linvar, it takes 12 beats to reach 4000, then 4 beats to return to 0.

linvar([0, 4000],[12, 4])

# We can even use a duration of 0 to instantly reset the linvar:

p1 >> dirt([0, 6, 4, 2], dur=1/4, hpf=linvar([0, 4000], 16))

p1.stop()

# Here are some more examples to play with:

p1 >> dirt([0, 6, 4, 2], dur=1/4, hpf=linvar([0, 4000], [16, 0]), hpr=linvar([1,0.1],12), pan=linvar([-1,1], 4))

d1 >> play("<X:><  O >", lpf=linvar([0, 0, 4000, 100],[12, 0, 4, 0]))

b1 >> bass(var([0,2],8), dur=PDur(3,8), drive=0.5, formant=linvar([0,8],[16,0]), amp=1/2)

Clock.clear()

# Part 8: Scheduling events
# -------------------------

# So far we've been using player objects to schedule musical events, but what about
# scheduling custom events that aren't necessarily playing notes? We can define functions
# and tell FoxDot to activate them later in the future.

# Here's a really simple example; first, run this code to create the function, "hello"

def hello():
    print("Hello, the current beat is", Clock.now())

# This function prints a message to the console saying hello and the current clock beat.
# Activate (aka 'call') the function by running:

hello()

# To call it, 4 beats in the future, you can use Clock.future(). Note there are no
# brackets following 'hello'

Clock.future(4, hello)

# We can also use Clock.schedule to call the function at the start of the next bar:

Clock.schedule(hello)

# Let's look at a musical example:

p1 >> pluck(P[:8], dur=1/4)

b1 >> sawbass(var([0, 2, 3, 4]))

d1 >> play("x-")

def change():
    Root.default += 4
    Scale.default = "minor"
    d1 >> play("<X-><  O >")

# Before the start of the next cycle, schedule the change

Clock.schedule(change)

# Stop the clock at the start of the next bar:

Clock.schedule(Clock.clear)

# Now let's use this opportunity to combine player-keys, linvars and scheduling
# to create a jam below:

# This is to fit with the 'kano' loop
Root.default=-3.5; Scale.default="minor"

p1 >> loop("drums135", P[:4], tempo=135).every(4, "offadd", 1.5, 0.25).every(5, "stutter", 4, dur=3)

p2 >> stretch("kano", dur=4, amp=.8)

b1 >> sawbass(var([0,2,-1],[8,4,4]), dur=PDur(3,8))

b2 >> dirt(b1.pitch + P[0, 2, 4, 7].palindrome(), dur=1/4, oct=var([5,6],1), hpf=linvar([0,4000],16), drive=0.5)

d1 >> play("+", dur=PDur(var([3,5],[6,2]),8,var([0,1])), pan=linvar([-1,1],8), amp=1.5)

Clock.schedule(Clock.clear)

######################################
#            Lunch break             #
######################################

# Part 9: Collaborating with FoxDot
# ---------------------------------

# When you want to play with friends, you'll probably want to synchronise
# your FoxDot clocks. The easiest way to do this is to decide who will be
# the 'master'. That person should go to the menu in the FoxDot interface:

# Language -> Listen for connections

# They will be shown a message in the console like so:

# Listening for connections on 192.168.1.10 on port 57999

# Make note of the IP address (the number similar to 192.168.1.10). Any one 
# who wants to synchronise should then run the code:

Clock.connect("192.168.1.10") # Use the IP address of the 'master' clock

# Provided there are no issues with firewalls etc, you should be connected!
# Let's try it out and make some noise!

# Part 10: Sending OSC messages to Processing
# -------------------------------------------

# If you want to send FoxDot messages to an application other than SuperCollider
# then it's very simple. The application must be a valid OSC server; this stands
# for Open Sound Control and is a very common protocol for music applications
# these days. For instance, Processing (http://processing.org/) has a library
# called oscP5. 

# If you have Processing installed, you can open a very basic file courtest of
# FoxDot user, noisk8, called 'noisk8.pde'. Press "run" and you should see
# a grey square. The application is running on your local machine and on port
# 12345. We can use the 'Server.add_forward' method to give FoxDot this
# information:

Server.add_forward("localhost", 12345)

# This tells FoxDot to forward all messages it is sending to another address,
# i.e. our Processing sketch.

# The sketch reacts to 'bass', 'dirt', 'blip', 'space', and 'bell' notes.

b1 >> bass([0, 1, -2], dur=[4, 4, 8])

b2 >> dirt(b1.pitch + [7, 4, 2, 0,], amp=PRand([0,1])[:16], dur=1/4, hpf=linvar([0,2000],16), hpr=linvar([1,0.1],12))

p1 >> blip(dur=PDur(3,8)*2, sus=4) + (0,9)

p2 >> space([b1.pitch + 2, 4], dur=[6, 2], sus=8)

p3 >> bell(P[b1.pitch,2,4,2][:6], dur=PDur(3,8), oct=6)

d1 >> play("X:")

Clock.clear()

# Part 11: Adding your own SynthDefs
# ----------------------------------

# FoxDot comes packaged with a few SynthDefs but you can add your own at any 
# time, even during a performance. Let's open 'sine.scd' in SuperCollider
# and take a look. 

# Once opened, press Ctrl+Enter to run the code and create a new SynthDef
# called 'sine' on the SuperCollider server. Now we need to give FoxDot a
# reference to it:

sine = SynthDef("sine")

# The name in brackets must be the same as the name on the SuperCollider server.
# You can trigger it like any normal FoxDot synth:

p1 >> sine([0, 1, 3, 4], dur=1/4)

p1 >> sine([0, 1, 3, 4], dur=1/4, drive=0.1)

p1 >> sine([0, 1, 3, 4], dur=1/4, drive=0.1, pan=linvar([-1,1],8))

p1 >> sine([0, 1, 3, 4], dur=1/4, drive=0.1, pan=linvar([-1,1],8), vib=12)

p1 >> sine([0, 1, 3, 4], dur=1/4, drive=0.1, pan=linvar([-1,1],8), vib=12, oct=[4,5,6])

p1.stop()

# etc etc

# Make sure you use 'ReplaceOut' instead of just 'Out' in your SynthDef to apply effects

# Part 12: Setting up MIDI
# ------------------------

# The first thing to do is connect your laptop to your MIDI device and make sure the 
# correct drivers are installed – this usually happens automatically but not always. 
# Next, make sure that SuperCollider can “see” the device. To do this, open SuperCollider
# and run this line of code:

# FoxDot.midi 

# You should then see a message in the "post window" with MIDI sources and destinations.
# To select a midi destination to use, run FoxDot.midi() with the index of the destination
# in SuperCollider, e.g.

# FoxDot.midi(1)

# Now you can use the 'midi' SynthDef like any normal SynthDef

p1 >> midi([0,1,2,3,4,5], dur=PDur(3,8), amp=[1,1/2,1/2]).every(6, "stutter", 4, dur=3, oct=6)

p1.stop()

# Functionality for other control arguments are limited but you can select the channel by
# using the 'channel' keyword argument:

p1 >> midi([0,1,2,3], channel = 1)

p1.stop()

# You may find that midi notes and FoxDot notes are out of sync a little. To adjust this,
# you need to change the Clock.midi_nudge value to 'nudge' the onset of midi notes by a 
# small amount.

# An easy way to do this is to play a simple sequence and change the value by small
# increments until the notes are synchronised.

p1 >> midi([0, 4])
 
p2 >> play("x * ")
 
# Value is usually between 0.15 and 0.25
Clock.midi_nudge = 0.2
