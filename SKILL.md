---
name: video-colorist
description: "Use for local video work: inspect footage, make contact sheets/frame grabs, color grade, sharpen/denoise, compare exports, assemble multiple clips, cut/delete/reorder material, add BGM, and adapt mood/director/cinematographer/film references into edits or grades. If the request mentions `导演` or a named visual reference, research that style online before editing unless the user says not to."
---

# Video Colorist

Preserve originals. Export new files.

## Default Flow

1. Inspect media: duration, resolution, fps, codec, bitrate, audio.
2. Make evidence: contact sheet plus representative frame grabs.
3. Diagnose: exposure, contrast, white balance, noise/compression, sharpness, color separation.
4. If director/style is named, web-search reliable sources and extract usable traits: editing rhythm, palette, contrast, texture, lighting, sound/music.
5. Adapt traits to the actual footage; do not claim exact replication of a living artist.
6. Render, then verify with output metadata and frames/contact sheet.
7. Final: link output, say what changed, mention source limits.


## Jia Zhangke Trigger

When the user prompt mentions `贾樟柯`, `Jia Zhangke`, `山河故人`, `三峡好人`, or `Still Life`, use this as the default editing direction unless the user explicitly overrides it:

1. Treat the reference as film-content style, not short-video app UI; ignore platform chrome, buttons, captions, status bars, and repost overlays in reference videos.
2. Build the cut around realism and ordinary space: restrained pacing, hard cuts, longer-held shots, distant human figures, empty environments, water/roads/buildings/fire/light as memory anchors.
3. Prefer natural sound or lightly mixed diegetic audio. Add BGM only when the user provides it or explicitly asks; if using `Go West`, treat it as nostalgic/emotional memory rather than fast MV rhythm.
4. Use a cool cyan-green, low-saturation, old digital-film feel: lifted shadows, restrained highlights, mild grain/noise, low-to-medium contrast, and no glossy commercial look.
5. Keep camera movement minimal. Use digital reframing only for subtle slow push-in, stabilization, or composition repair; avoid flashy transitions, heavy zooms, whip pans, speed ramps, and template effects.
6. For multiple clips, start from a simple spatial/emotional structure such as `empty place -> person in space -> light/fire/event -> aftermath`, then make a concise cut list before rendering.

## Multi-Clip Rule

When multiple materials are provided:

1. Decide or ask for target duration and output platform/aspect ratio when unclear.
2. Build an outline from the footage first.
3. Convert outline to a cut list: `file | start | end | purpose`.
4. Cut/delete/reorder by the outline and requested style.
5. Set sound priority: speech, natural sound, or BGM.
6. Add BGM only if provided or explicitly requested; prefer licensed/royalty-free/public-domain music.
7. Preserve natural sound when realism/documentary feeling matters.
8. For complex edits, export `rough_cut.mp4` before final grade/audio polish.

Brief template:

```text
Reference:
Target duration/platform:
Outline:
Cut list:
BGM/natural sound:
Output:
```

## Script

Use `scripts/video_colorist.py`:

```powershell
python C:\Users\Administrator\.codex\skills\video-colorist\scripts\video_colorist.py inspect input.mp4
python C:\Users\Administrator\.codex\skills\video-colorist\scripts\video_colorist.py contact input.mp4 --out contact.jpg
python C:\Users\Administrator\.codex\skills\video-colorist\scripts\video_colorist.py frame input.mp4 --time 8 --out frame.jpg
python C:\Users\Administrator\.codex\skills\video-colorist\scripts\video_colorist.py grade input.mp4 --preset japanese-cold-film --out graded.mp4
python C:\Users\Administrator\.codex\skills\video-colorist\scripts\video_colorist.py assemble a.mp4 b.mp4 --out edit.mp4 --bgm music.mp3
python C:\Users\Administrator\.codex\skills\video-colorist\scripts\video_colorist.py cut-assemble --segment "a.mp4|00:00:01|00:00:04" --segment "b.mp4|00:00:00|00:00:03" --out edit.mp4
```

Presets: `balanced-clean`, `soft-clear`, `cold-film`, `japanese-cold-film`, `warm-film`.

## Notes

Use light `hqdn3d` before sharpening on low-bitrate video. Keep `unsharp` restrained. Prefer H.264 MP4 with `-crf 17..20`, `-pix_fmt yuv420p`, and `-c:a copy` unless changing audio.

