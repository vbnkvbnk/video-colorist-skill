---
name: video-colorist
description: "Use for local video work: inspect footage, make contact sheets/frame grabs, color grade, sharpen/denoise, compare exports, assemble multiple clips, cut/delete/reorder material, add BGM, and adapt mood/director/cinematographer/film references into edits or grades. Before invoking an edit/grade on provided footage, first inspect the material and recommend fitting director/style directions, especially when the user asks about `导演`, `风格`, `剪辑`, or `运镜`. If a named visual reference is requested, research that style online before editing unless the user says not to."
---

# Video Colorist

Preserve originals. Export new files.

## Default Flow

1. Inspect media: duration, resolution, fps, codec, bitrate, audio.
2. Make evidence: contact sheet plus representative frame grabs.
3. Recommend director/style directions from the actual footage before editing unless the user already made a firm choice.
4. Diagnose: exposure, contrast, white balance, noise/compression, sharpness, color separation.
5. If director/style is named, web-search reliable sources and extract usable traits: editing rhythm, palette, contrast, texture, lighting, sound/music.
6. Adapt traits to the actual footage; do not claim exact replication of a living artist.
7. Render, then verify with output metadata and frames/contact sheet.
8. Final: link output, say what changed, mention source limits.

## Director Recommendation Gate

When raw footage or a folder of clips is provided, give a short style recommendation before running the final edit:

1. Identify subject matter: people, city, nature, water, traffic, interiors, night, weather, objects.
2. Identify motion language: locked-off, handheld drift, slow pan/tilt, tracking, vehicle movement, fast movement, shaky accidental movement.
3. Identify image mood: clean/commercial, documentary, humid/hazy, nostalgic, cold, warm, high contrast, low contrast.
4. Match 2-4 possible Chinese director directions and choose one primary recommendation.
5. Explain why it fits the footage and name what to avoid.

Brief output template:

```text
素材判断:
可选导演方向:
首推:
运镜建议:
剪辑/调色要点:
不建议:
```

Common Chinese director directions:

- 侯孝贤/贾樟柯 direction: fixed or slow observational camera, long holds, people small in environment, natural sound, low saturation, avoid flashy transitions.
- 王家卫 direction: step-printing/slow motion feeling, fragments, reflections, neon or warm-cool contrast, intimate close-ups; use only when there are faces, night, glass, signs, or emotionally charged details.
- 张艺谋 direction: strong color blocks, formal composition, ritualized movement, bold contrast; use only when footage has clear color fields, crowds, architecture, costume, or staged gestures.
- 刁亦男 direction: cold night city, wet roads, practical lights, suspenseful pauses, sharp shadow contrast; use when there is night traffic, rain, industrial streets, or lonely figures.
- 毕赣 direction: drifting camera, dreamlike geography, long takes, voice/music memory, green-blue shadows; use when footage has wandering paths, water, fog, caves/streets, or surreal continuity.
- 顾长卫/摄影诗方向: soft natural light, lyrical faces/landscape, gentle lateral movement, muted warm-cool palette; use when footage is everyday but emotionally tender.

运镜判断关键行：先顺着素材本来的运动走，不为了像导演而强行加推拉摇移。


## Jia Zhangke Trigger

When the user prompt mentions `贾樟柯`, `Jia Zhangke`, `山河故人`, `三峡好人`, or `Still Life`, use this as the default editing direction unless the user explicitly overrides it:

1. Treat the reference as film-content style, not short-video app UI; ignore platform chrome, buttons, captions, status bars, and repost overlays in reference videos.
2. Build the cut around realism and ordinary space: restrained pacing, hard cuts, longer-held shots, distant human figures, empty environments, water/roads/buildings/fire/light as memory anchors.
3. Prefer natural sound or lightly mixed diegetic audio. Add BGM only when the user provides it or explicitly asks; if using `Go West`, treat it as nostalgic/emotional memory rather than fast MV rhythm.
4. Use a cool cyan-green, low-saturation, old digital-film feel: lifted shadows, restrained highlights, mild grain/noise, low-to-medium contrast, and no glossy commercial look.
5. Keep camera movement minimal. Use digital reframing only for subtle slow push-in, stabilization, or composition repair; avoid flashy transitions, heavy zooms, whip pans, speed ramps, and template effects.
6. For multiple clips, start from a simple spatial/emotional structure such as `empty place -> person in space -> light/fire/event -> aftermath`, then make a concise cut list before rendering.

简化执行分支：

- 画面质感：旧、潮、钝、沉；保留水汽、灰尘、噪点和轻微糊感，避免通透锐利的商业质感。
- 调色风格：低饱和、低对比、偏灰绿/青蓝；肤色压淡，高光收住，用红、橙、蓝做少量现实杂色点缀。
- 构图风格：人小环境大，多拍江面、码头、旧墙、楼梯、船、桥和晾晒物；人物以背影、侧影、沉默停留为主。
- 运动方式：固定机位、慢推、慢摇、远景观察；少快切，少炫技，避免重变焦、甩镜、速度变化和模板转场。

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

