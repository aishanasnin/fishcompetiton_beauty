# model/fish_analysis.py
from PIL import Image, ImageStat
import os, random

def analyze(image_paths, names):
    out = []
    for i, p in enumerate(image_paths):
        name = (names[i] if i < len(names) and names[i].strip() else f"Fish #{i+1}")
        try:
            im = Image.open(p).convert('RGB')
            stat = ImageStat.Stat(im)
            brightness = sum(stat.mean)/3
            vibrancy = sum(stat.stddev)/3
            sexy = min(100, int(vibrancy/2 + brightness/2) + random.randint(-6,6))
            scales_count = max(1, int((vibrancy/20.0) * (im.width * im.height / 10000.0)) + random.randint(5, 30))
            shape = int(50 + (vibrancy % 50))
            eye = int(50 + (brightness % 50))
            beauty = int((vibrancy * 0.4 + brightness * 0.6) / 2)
            total_score = beauty + shape + eye + sexy
            out.append({
                'name': name,
                'image': os.path.basename(p),
                'beauty': int(beauty),
                'shape': int(shape),
                'eye': int(eye),
                'scales_count': int(scales_count),
                'vibrancy': int(vibrancy),
                'sexy': int(sexy),
                'total_score': int(total_score)
            })
        except Exception as e:
            out.append({'name': name, 'image': '', 'beauty':0, 'shape':0, 'eye':0, 'scales_count':0, 'vibrancy':0, 'sexy':0, 'total_score':0})
    return out
