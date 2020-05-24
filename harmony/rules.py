"""
Rules introduced in "Harmonic Practice" book.
The goal is to describe them computiationaly and then use them as an
exercise verifier.
"""
import music21
import itertools

VOICES = ["bass", "tenor", "alt", "soprano"]

class Rule:

    def __init__(self, rule, desc):
        self.desc = desc
        self.rule = rule

    def __repr__(self):
        return str(desc)

    def __call__(self, st):
        return self.rule(st)


def _doubleRoot(st):
    for c in st:
        pnames = c.pitchNames
        if pnames.count(c.third.name) > 1 or pnames.count(c.fifth.name) > 1:
            print(c.offset, c)

def _parallel(st):
    p5 = lambda n1, n2: music21.interval.Interval(n1, n2).name == 'P5'
    p8 = lambda n1, n2: music21.interval.Interval(n1, n2).simpleName == 'P1'
    for c1, c2 in zip(st, st[1:]):
        suspects = []
        for i1, i2 in itertools.combinations(range(4), 2):
            n1, n2 = c1.pitches[i1], c1.pitches[i2]
            if p5(n1, n2) or p8(n1, n2):
                suspects.append((i1, i2, music21.interval.Interval(n1, n2)))
        for sus in suspects:
            i1, i2 = sus[0], sus[1]
            second_interval = music21.interval.Interval(c2.pitches[i1], c2.pitches[i2])
            if second_interval.name == sus[2].name and \
                second_interval.noteStart != sus[2].noteStart:
                print(c1.offset, sus[2].name, VOICES[i1], VOICES[i2])
        #suspects = [interval.Interval(n1, n2) for n1, n2 in
        #        itertools.combinations(c1.pitches, 2) if p5(n1, n2) or p8(n1, n2)]


