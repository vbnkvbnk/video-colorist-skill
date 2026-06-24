---
name: video-colorist
description: Local video inspection, contact sheets, grading, clip assembly, BGM, Chinese director references, and Oscar Best Director style guidance.
metadata:
  short-description: Video editing and color grading helper
---

# Video Colorist

Preserve originals. Export new files.
Put every generated output in an `export` folder under the working media folder.

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

## Oscar Best Director Style Bank

When the user asks for `奥斯卡导演`, `Oscar director`, `Best Director`, `Academy Award`, or an international mainstream film direction, read `references/oscar-best-directors.md`.

Use that reference as a style bank, not a winner trivia list:

1. Match footage first: subject, movement, light, texture, and emotional temperature.
2. Pick 2-3 Oscar directions that actually fit, then choose one primary direction.
3. Translate the chosen direction into editing rhythm, color, contrast, texture, sound, and camera treatment.
4. If the user asks for "近30年", use the reference's latest verified 30-year span; verify newer ceremonies before extending it.
5. Verify the latest winner from a reliable source before claiming the list is current.
6. Do not promise exact imitation of a living artist; describe an adapted cinematic direction.

关键行：奥斯卡方向只作为审美坐标，最终剪辑必须服从素材本身。


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

## Bi Gan Trigger

When the user prompt mentions `毕赣`, `Bi Gan`, `路边野餐`, `地球最后的夜晚`, `凯里`, or asks for a dreamlike wandering film style, use this direction unless the user explicitly overrides it:

1. Treat the target as atmosphere and spatial memory, not a literal copy of a living director. Keep the original footage recognizable.
2. Prefer a drifting, humid, nocturnal or post-rain mood: water, wet roads, trees, fog, tunnels, streets, vehicles, reflections, and distant lights should become memory anchors.
3. Build rhythm around wandering continuity: longer holds, slow lateral movement, slow push-ins, and soft spatial transitions. Avoid MV rhythm, aggressive cutting, whip pans, speed ramps, template transitions, and flashy zooms.
4. Use BGM only as a low, nostalgic undertow unless the user asks otherwise. Natural ambience, traffic, rain, wind, and room tone should remain believable when present.
5. If the material lacks faces, dialogue, alleys, night, interiors, or strong human action, lean into "place dreaming about itself" instead of forcing plot.

执行要点:

- 风格判断：毕赣方向不是单纯青绿色滤镜；核心是潮湿、游荡、记忆感、现实空间变得像梦。
- 画面质感：保留一点旧数字影像的颗粒、轻微雾感和柔化边缘；不要过锐、过干净、过商业广告感。
- 调色方向：冷调为底，但不要把画面推成单一青绿。阴影可偏蓝青，树叶和墙面保留真实绿/灰，肤色和车灯不要脏掉；红色尾灯、招牌、暖光可作为少量情绪色。
- 亮度/对比：整体可比原片稍亮，黑位不要死黑；高光可以有一点发散感，但避免白树干、天空、水面全部过曝。
- 饱和度：中低饱和为主，局部红、蓝、暖黄可更鲜明；如果用户给参考图，先匹配参考图的明暗和肤色/树叶真实度，再加风格。
- 构图：优先选择纵深道路、湖面、树冠、桥、车窗、反光、门洞、楼梯、巷道；让人物或车辆处在环境里，不要一味大特写。
- 运镜方式：顺着素材已有运动做慢漂移、慢推、慢摇或稳定后的轻微呼吸感；只做修复性重构图，避免为了像导演而强行加大幅度运动。
- 剪辑结构：可按 `水/空镜 -> 路/树/车 -> 光/反射 -> 更空的余韵` 组织；剪点少而准，让镜头之间像记忆跳接。
- 不建议：不要重度 teal-orange、不要全片一层青绿、不要过度降噪磨皮、不要强暗角、不要把白天素材硬压成夜景。

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

