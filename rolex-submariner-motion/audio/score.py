"""Offline score + sound design for the Submariner film.

100 BPM, bar = 2.4 s, eighth = 0.3 s. Every timestamp below is taken from the
same stage table as index.html (STAGES bars: 3,2,2,2,2,3,3,2,5 -> 57.6 s).
Writes a 48 kHz stereo WAV: python3 score.py out.wav
"""
import sys
import numpy as np

SR = 48000
BAR, BEAT, E8, E16 = 2.4, 0.6, 0.3, 0.15
DUR = 57.6
N = int(DUR * SR)
rng = np.random.default_rng(11)

music = np.zeros((N, 2))
sfx = np.zeros((N, 2))


def mtof(m):
    return 440.0 * 2 ** ((m - 69) / 12)


def t_axis(d):
    return np.arange(int(d * SR)) / SR


def put(bus, sig, at, pan=0.0, gain=1.0):
    i = int(at * SR)
    if i >= N:
        return
    sig = sig[: N - i] * gain
    l, r = np.cos((pan + 1) * np.pi / 4), np.sin((pan + 1) * np.pi / 4)
    bus[i:i + len(sig), 0] += sig * l * 1.414
    bus[i:i + len(sig), 1] += sig * r * 1.414


def fft_filter(x, lo=None, hi=None):
    X = np.fft.rfft(x)
    f = np.fft.rfftfreq(len(x), 1 / SR)
    m = np.ones_like(f)
    if lo:
        m *= 1 / (1 + (lo / np.maximum(f, 1)) ** 4)
    if hi:
        m *= 1 / (1 + (f / hi) ** 4)
    return np.fft.irfft(X * m, len(x))


def env_ad(d, a, decay):
    t = t_axis(d)
    e = np.minimum(1, t / max(a, 1e-4)) * np.exp(-np.maximum(0, t - a) / decay)
    fade = np.minimum(1, (d - t) / 0.02)
    return e * fade


# ---------- instruments ----------
def musicbox(m, d=1.6):
    t = t_axis(d)
    f = mtof(m)
    s = np.sin(2 * np.pi * f * t) + .35 * np.sin(2 * np.pi * f * 3.01 * t) * np.exp(-t * 9) \
        + .18 * np.sin(2 * np.pi * f * 5.43 * t) * np.exp(-t * 18)
    return s * env_ad(d, .002, .45)


def bell(m, d=4.0):
    t = t_axis(d)
    f = mtof(m)
    parts = [(1, 1, 1.6), (2.76, .5, .9), (5.4, .3, .5), (8.93, .15, .3), (.5, .25, 2.4)]
    s = sum(a * np.sin(2 * np.pi * f * r * t) * np.exp(-t / dcy) for r, a, dcy in parts)
    return s * np.minimum(1, t / .003)


def pad(notes, d, bright=900):
    t = t_axis(d)
    s = np.zeros_like(t)
    for m in notes:
        for det in (-0.08, 0.0, 0.07):
            f = mtof(m + det)
            ph = (f * t) % 1.0
            s += (2 * ph - 1) * .25
    s = fft_filter(s, lo=180, hi=bright)
    att = np.minimum(1, t / .5)
    rel = np.minimum(1, (d - t) / .4)
    return s * att * rel / len(notes)


def bass(m, d):
    t = t_axis(d)
    f = mtof(m + 12)
    s = np.sin(2 * np.pi * f * t) + .35 * np.sin(2 * np.pi * 2 * f * t)
    s = np.tanh(1.4 * s) * .5
    return s * np.minimum(1, t / .008) * np.minimum(1, (d - t) / .05) * np.exp(-t * 1.2)


def kick():
    t = t_axis(.45)
    f = 48 + 110 * np.exp(-t * 32)
    ph = 2 * np.pi * np.cumsum(f) / SR
    return np.sin(ph) * np.exp(-t * 7) + .3 * np.exp(-t * 300) * rng.standard_normal(len(t))


def clap():
    t = t_axis(.3)
    n = fft_filter(rng.standard_normal(len(t)), lo=900, hi=6000)
    e = np.exp(-t * 18) * (1 + .6 * (np.sin(2 * np.pi * 90 * t) > .3) * (t < .03))
    return n * e * .6


def tick(accent=False):
    t = t_axis(.05)
    n = fft_filter(rng.standard_normal(len(t)), lo=5000, hi=12000)
    clickf = 3200 if accent else 4100
    return (n * .5 + np.sin(2 * np.pi * clickf * t)) * np.exp(-t * 160)


def noise_sweep(d, f0, f1, shape='rise'):
    t = t_axis(d)
    n = rng.standard_normal(len(t))
    out = np.zeros_like(n)
    seg = int(SR * .05)
    for k in range(0, len(n), seg):
        u = k / len(n)
        fc = f0 * (f1 / f0) ** u
        out[k:k + seg] = fft_filter(n[k:k + seg + 64], lo=fc * .5, hi=fc * 1.6)[: len(n[k:k + seg])]
    if shape == 'rise':
        e = (t / d) ** 2.2
    elif shape == 'fall':
        e = (1 - t / d) ** 2
    else:  # whoosh
        e = np.sin(np.pi * t / d) ** 2
    return out * e


def metal_ring(m, d=1.6):
    t = t_axis(d)
    f = mtof(m)
    s = sum(a * np.sin(2 * np.pi * f * r * t) * np.exp(-t * dd) for r, a, dd in
            [(1, 1, 3), (2.41, .6, 5), (3.87, .4, 7), (5.6, .25, 10)])
    return s * np.minimum(1, t / .001)


# ---------- harmony ----------
CH = {
    'Dmaj7': [62, 66, 69, 73], 'Bm7': [59, 62, 66, 69], 'Gmaj7': [55, 59, 62, 66],
    'A': [57, 61, 64, 69], 'Asus': [57, 62, 64, 69],
}
ROOT = {'Dmaj7': 38, 'Bm7': 35, 'Gmaj7': 31, 'A': 33, 'Asus': 33}
PROG = ['Dmaj7', 'Bm7', 'Gmaj7',            # 1-3 pencil
        'A', 'Dmaj7',                       # 4-5 paper
        'Bm7', 'Gmaj7',                     # 6-7 neon
        'Dmaj7', 'A',                       # 8-9 2D
        'Bm7', 'Gmaj7',                     # 10-11 2.5D
        'Dmaj7', 'A', 'Bm7',                # 12-14 3D
        'Gmaj7', 'Dmaj7', 'A',              # 15-17 explode
        'Bm7', 'Asus',                      # 18-19 assemble
        'Gmaj7', 'A', 'Bm7', 'Dmaj7', 'Dmaj7']  # 20-24 logo

ARP = [0, 1, 2, 3, 2, 1, 2, 3]
for b, ch in enumerate(PROG):
    t0 = b * BAR
    notes = CH[ch]
    # music box arpeggio: eighths in the sketch, sixteenths once the watch is built
    step = E8 if b < 3 or b >= 22 else E16
    count = int(BAR / step)
    if b == 23:
        count = 0
    for k in range(count):
        n = notes[ARP[k % 8]] + 12 + (12 if (k // 8) % 2 and step == E16 else 0)
        vel = .32 if k % 4 == 0 else .2
        if 17 <= b <= 18:
            vel *= .7
        put(music, musicbox(n), t0 + k * step, pan=.35 * np.sin(k), gain=vel)
    # pad from paper onward
    if b >= 3:
        bright = 700 if b < 5 else 1500 if b < 7 else 1100 if b < 11 else 2200 if b < 17 else 1300
        d = BAR + (2.6 if b == 23 else .35)
        if b < 23:
            put(music, pad(notes, d, bright), t0, gain=.42 if b < 11 else .5)
    # bass
    if 3 <= b <= 10:
        for q in range(4):
            put(music, bass(ROOT[ch], BEAT * .95), t0 + q * BEAT, gain=.45)
    elif 11 <= b <= 16:
        for q in range(8):
            m = ROOT[ch] + (12 if q in (3, 7) else 0)
            put(music, bass(m, E8 * .9), t0 + q * E8, gain=.5)
    elif b in (17, 18):
        put(music, bass(ROOT[ch], BAR * .95), t0, gain=.45)
    elif b >= 19:
        put(music, bass(ROOT[ch], BAR * (2.2 if b == 22 else .98)), t0, gain=.45 if b < 23 else 0)
    # drums
    if 7 <= b <= 10:
        for q in (0, 2):
            put(music, kick(), t0 + q * BEAT, gain=.6)
    if 11 <= b <= 16:
        for q in range(4):
            put(music, kick(), t0 + q * BEAT, gain=.7)
        for q in (1, 3):
            put(music, clap(), t0 + q * BEAT, pan=.1, gain=.35)
    # the mechanism: sixteenth ticks under the whole film
    if b < 23:
        for q in range(16):
            g = .05 if b < 3 else .08
            put(music, tick(q % 4 == 0), t0 + q * E16, pan=-.2, gain=g * (1.4 if q % 4 == 0 else 1))

# final chord: Dmaj9 voiced wide, rings out to the end
final = pad([50, 57, 62, 66, 69, 73, 76], 4.8, 1600)
put(music, final, 52.8, gain=.6)
put(music, bass(38, 4.8), 52.8, gain=.5)

# logo melody: one note per letter as R-O-L-E-X lands (stage 9 starts 45.6 s)
for i, m in enumerate([74, 78, 81, 85, 86]):
    put(music, bell(m, 2.5), 45.6 + 2.7 + i * E8, pan=-.4 + i * .2, gain=.16)

# ---------- sound design ----------
# 1 pencil: graphite strokes while the outline draws (0.3–4.5 s)
t = 0.3
while t < 4.6:
    d = rng.uniform(.12, .38)
    n = fft_filter(rng.standard_normal(int(d * SR)), lo=1800, hi=6500)
    tt = t_axis(d)
    grain = 1 + .6 * np.sin(2 * np.pi * rng.uniform(18, 35) * tt)
    put(sfx, n * np.sin(np.pi * tt / d) ** .7 * grain, t, pan=rng.uniform(-.3, .3), gain=.11)
    t += d + rng.uniform(.02, .12)
# hatch strokes as the shading fills in
for k in range(10):
    tt = t_axis(.07)
    put(sfx, fft_filter(rng.standard_normal(len(tt)), lo=2500, hi=7000) * np.sin(np.pi * tt / .07), 3.0 + k * .15, gain=.08)

# 2 paper: one card lands on every eighth (7.5–10.2 s)
for i in range(10):
    tt = t_axis(.25)
    thud = fft_filter(rng.standard_normal(len(tt)), lo=80, hi=900) * np.exp(-tt * 28)
    rust = fft_filter(rng.standard_normal(len(tt)), lo=2000, hi=8000) * np.exp(-tt * 40) * .3
    put(sfx, thud + rust, 7.2 + (i + 1) * E8 - .01, pan=-.4 + i * .08, gain=.55)
# lights out
put(sfx, tick(True) * 2.5, 11.72, gain=.35)
put(sfx, noise_sweep(.3, 900, 120, 'fall'), 11.72, gain=.25)

# 3 neon: ignition buzz with flicker, then a low hum
tt = t_axis(1.0)
buzz = np.sign(np.sin(2 * np.pi * 120 * tt)) * .3 + np.sin(2 * np.pi * 240 * tt) * .3
flick = (rng.random(len(tt) // 2400 + 1) > .45).repeat(2400)[: len(tt)]
put(sfx, fft_filter(buzz, hi=2500) * flick * np.minimum(1, tt / .05), 12.0, gain=.18)
put(sfx, noise_sweep(1.2, 300, 3000, 'rise'), 11.0, gain=.12)
tt = t_axis(4.6)
put(sfx, np.sin(2 * np.pi * 120 * tt) * .3 * np.minimum(1, tt / .5) * np.minimum(1, (4.6 - tt) / .4), 12.2, gain=.12)

# 4 2D: soft shimmer as colour floods in
put(sfx, noise_sweep(.8, 2000, 9000, 'whoosh'), 16.6, gain=.12)

# 5 2.5D: camera tilts away
put(sfx, noise_sweep(1.4, 250, 2500, 'whoosh'), 21.5, pan=-.2, gain=.32)

# 6 3D: metal arrives, then the fly-around
put(sfx, kick() * 1.2, 26.4, gain=.7)
put(sfx, metal_ring(81, 2.0), 26.4, pan=.2, gain=.12)
put(sfx, noise_sweep(1.6, 300, 3200, 'whoosh'), 28.9, pan=.3, gain=.3)
put(sfx, noise_sweep(2.4, 200, 6000, 'rise'), 31.2, gain=.25)

# 7 explode: separation hit, then a tick per label (bottom part first)
put(sfx, kick() * 1.3, 33.6, gain=.8)
put(sfx, metal_ring(69, 2.4), 33.6, pan=-.2, gain=.14)
put(sfx, noise_sweep(.9, 3000, 300, 'fall'), 33.6, gain=.2)
for i in range(10):
    put(sfx, metal_ring(86 + i, .25), 33.6 + 1.2 + i * E8, pan=.5, gain=.07)
    put(sfx, tick(True), 33.6 + 1.2 + i * E8, pan=.5, gain=.12)

# 8 assemble: reverse rise, then the snap as everything locks at 43.2 s
put(sfx, noise_sweep(2.4, 400, 5000, 'rise'), 40.8, gain=.28)
put(sfx, tick(True), 43.2, gain=1.2)
put(sfx, metal_ring(93, .6), 43.2, gain=.4)
put(sfx, kick(), 43.2, gain=.55)

# 9 logo: dive through the dial crown, chime as the crown fills, sparkle with the sweep, glint
put(sfx, noise_sweep(1.0, 400, 7000, 'rise'), 45.5, gain=.3)
put(sfx, noise_sweep(.7, 6000, 500, 'fall'), 46.5, gain=.18)
put(sfx, bell(86, 4.0), 48.0, gain=.3)
put(sfx, bell(74, 4.0), 48.0, gain=.2)
for k in range(14):
    put(sfx, musicbox(98 + (k * 5) % 12, .5), 51.6 + k * .09, pan=-.6 + k * .09, gain=.06)
put(sfx, bell(93, 4.5), 52.8, gain=.28)
put(sfx, bell(81, 4.5), 52.8, gain=.18)


# ---------- reverb + mix ----------
def reverb(x, secs=2.2, mix=.25):
    L = int(secs * SR)
    ir = rng.standard_normal((L, 2)) * np.exp(-np.arange(L) / SR * 3.2)[:, None]
    ir[:, 0] = fft_filter(ir[:, 0], hi=6000)
    ir[:, 1] = fft_filter(ir[:, 1], hi=6000)
    ir /= np.sqrt((ir ** 2).sum(0))
    out = np.zeros_like(x)
    n = len(x) + L
    nfft = 1 << (n - 1).bit_length()
    for c in range(2):
        y = np.fft.irfft(np.fft.rfft(x[:, c], nfft) * np.fft.rfft(ir[:, c], nfft), nfft)[: len(x)]
        out[:, c] = y
    return x * (1 - mix) + out * mix * 3


mixd = reverb(music, 2.4, .28) + reverb(sfx, 1.4, .15)
# gentle end fade over the final second
fade = np.ones(N)
fade[-int(1.0 * SR):] = np.linspace(1, 0, int(1.0 * SR)) ** 1.5
mixd *= fade[:, None]
mixd = np.tanh(mixd / np.max(np.abs(mixd)) * 1.05) / np.tanh(1.05) * .7

out = sys.argv[1] if len(sys.argv) > 1 else 'score.wav'
pcm = (np.clip(mixd, -1, 1) * 32767).astype('<i2')
import wave
with wave.open(out, 'wb') as w:
    w.setnchannels(2)
    w.setsampwidth(2)
    w.setframerate(SR)
    w.writeframes(pcm.tobytes())
print('wrote', out, len(pcm) / SR, 's')
