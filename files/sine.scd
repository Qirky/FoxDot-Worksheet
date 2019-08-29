(
SynthDef.new(\sine,
    {|amp=1, sus=1, pan=0, freq=0|
        var osc, env;
        osc=SinOsc.ar(freq, mul: amp);
        env=EnvGen.ar(Env.perc(attackTime: 0.01, releaseTime: sus), doneAction: 2);
        osc=(osc * env);
        osc = Pan2.ar(osc, pan);
        Out.ar(0, osc)}).add;
)