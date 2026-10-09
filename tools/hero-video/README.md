# Video del hero (`assets/site/video/hero-wave.mp4`)

1. Cuadros inicial/final 16:9 sobre `#111214`, figura al ~68 % del ancho:
   `python tools/hero-video/frames.py . <carpeta_salida>` → `start.png` (hero.webp) y `end.png` (wave.webp).
2. Generar en Higgsfield (plan Starter: Kling 3.0 `std`; Seedance 2.5 y Kling `pro` piden plan Pro):

```
higgsfield generate create kling3_0 --mode std --sound off --start-image start.png --end-image end.png \
  --duration 5 --aspect_ratio 16:9 --wait --prompt "Single continuous shot, locked-off static camera, no cuts, no zoom, no camera movement. A stylized 3D animated character (white shirt with rolled sleeves, black trousers, watch with cobalt blue strap) stands on the right side of the frame against a plain dark charcoal studio background. He starts with his arms crossed and a friendly smile, then smoothly and continuously uncrosses his arms: one hand slides into his trouser pocket while the other rises into a calm open-palm wave at shoulder height, ending in a held friendly wave. One smooth, steady, one-directional motion, no repeated waving, no extra gestures. Identity, face, clothing and lighting stay consistent. Background stays static and empty."
```

3. Recodificar todo-intra (cada cuadro es keyframe → el scrub con el mouse es fluido) y sacar el póster:

```
ffmpeg -i raw.mp4 -an -c:v libx264 -preset slow -crf 24 -pix_fmt yuv420p -g 1 -x264-params keyint=1:scenecut=0 -movflags +faststart assets/site/video/hero-wave.mp4
ffmpeg -i raw.mp4 -frames:v 1 f0.png   # → convertir a assets/site/img/hero-poster.webp
```

Sin ffmpeg en el sistema: `pip install imageio-ffmpeg` y usar `imageio_ffmpeg.get_ffmpeg_exe()`.
