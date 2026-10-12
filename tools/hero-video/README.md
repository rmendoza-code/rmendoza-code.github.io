# Video del hero (`assets/site/video/hero-wave.mp4`)

1. Cuadros inicial/final 16:9, figura al ~68 % del ancho, fondo con degradado (paleta `azul-noche` = la publicada; también `cobalto`, `lima`, `amarillo-neon`):
   `python tools/hero-video/frames.py . <carpeta_salida>` → `<paleta>-start.png` (hero.webp), `<paleta>-end.png` (wave.webp) y `<paleta>-poster.webp`.
2. Generar en Higgsfield (plan Starter: Kling 3.0 `std` (720p); Seedance 2.0/2.5 y Kling `pro` piden plan Pro):

```
higgsfield generate create kling3_0 --mode std --sound off --start-image azul-noche-start.png --end-image azul-noche-end.png \
  --duration 5 --aspect_ratio 16:9 --wait --prompt "Single continuous shot, locked-off static camera, no cuts, no zoom, no camera movement. A stylized 3D animated character (white shirt with rolled sleeves, black trousers, watch with cobalt blue strap) stands on the right side of the frame against a smooth deep navy-to-cobalt blue studio gradient background with a soft glow behind him. He starts with his arms crossed and a friendly smile, then smoothly and continuously uncrosses his arms: one hand slides into his trouser pocket while the other rises into a calm open-palm wave at shoulder height, ending in a held friendly wave. One smooth, steady, one-directional motion, no repeated waving, no extra gestures. Identity, face, clothing and lighting stay consistent. Background gradient stays perfectly static and empty."
```

3. Escalar a 2K (2 créditos; acepta el id del trabajo anterior):
   `higgsfield generate create bytedance_video_upscale --video <job_id> --resolution 2k --model_version standard --preset aigc --wait`
4. Recodificar con keyframe cada 4 cuadros (scrub fluido, ~3 MB) y sacar el póster:

```
ffmpeg -i raw2k.mp4 -an -vf scale=2560:-2:flags=lanczos -c:v libx264 -preset slow -crf 20 -tune animation -pix_fmt yuv420p -g 4 -x264-params keyint=4:scenecut=0 -movflags +faststart assets/site/video/hero-wave.mp4
ffmpeg -i raw2k.mp4 -frames:v 1 f0.png   # → 1920×1080 → assets/site/img/hero-poster.webp
```

Sin ffmpeg en el sistema: `pip install imageio-ffmpeg` y usar `imageio_ffmpeg.get_ffmpeg_exe()`.
