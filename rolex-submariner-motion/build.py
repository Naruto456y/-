"""Build the self-contained page: embeds audio/score.m4a into index.html."""
import base64, pathlib
root = pathlib.Path(__file__).parent
html = (root / 'index.html').read_text()
b64 = base64.b64encode((root / 'audio' / 'score.m4a').read_bytes()).decode()
(root / 'dist').mkdir(exist_ok=True)
(root / 'dist' / 'rolex-submariner.html').write_text(html.replace('AUDIO_DATA_URI', 'data:audio/mp4;base64,' + b64))
print('built dist/rolex-submariner.html')
