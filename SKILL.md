---
name: video-colorist
description: Use when Codex needs local video inspection, contact sheets, frame grabs, FFmpeg color grading, clip assembly, BGM handling, cinematic style direction, Chinese director references, Oscar Best Director style guidance, or still-image retouch prompt planning for requests like 修图, 照片调色, 图片调色, AI修图, 局部改色, 换天空, or 变剪影.
---

# Video Colorist

Preserve originals. Export new files.
Put every generated output in an `export` folder under the working media folder.

## Non-Negotiables

- Preserve originals. Never overwrite user media.
- Export every generated file under `export/` beside the working media folder.
- Do not apply a director/style preset before seeing metadata plus frames/contact sheet.
- Do not force a famous style onto unsuitable footage; explain the mismatch and choose a safer treatment.
- Keep natural sound when realism, documentary mood, speech, or location atmosphere matters.
- For low-bitrate, noisy, shaky, or dark footage, prefer repair and restraint over heavy stylization.

## Default Flow

1. Classify the task as `single-grade`, `multi-clip-edit`, `style-direction`, `image-retouch-prompt`, or `analysis-only`.
2. Create an `export/` folder and put all evidence and renders there.
3. Inspect media: duration, resolution, fps, codec, bitrate, audio.
4. Make evidence: `contact_original.jpg` plus 2-4 representative frame grabs.
5. Diagnose the footage before editing: exposure, contrast, white balance, compression, noise, sharpness, motion, audio, and subject matter.
6. Read `references/video-decision-matrix.md` when footage quality is weak, the request is vague, multiple styles could fit, or a director/style is requested.
7. Recommend 2-3 directions from the actual footage unless the user already made a firm choice; choose one primary direction and name what to avoid.
8. Render, then verify with output metadata and `contact_output.jpg` or representative output frames.
9. Final: link output files, summarize changes, mention remaining limits, and state what evidence was checked.

## Delivery Gates

Each video edit must pass these gates unless the user explicitly asks for analysis only:

1. Evidence gate: `inspect_original.txt`, `contact_original.jpg`, and representative frames exist in `export/`.
2. Plan gate: a short plan states treatment strength, style direction, audio priority, and forbidden moves.
3. Render gate: final video is under `export/` with a descriptive name, such as `export/graded_cold-film.mp4` or `export/edit_jia-style.mp4`.
4. Verification gate: output metadata and output frames/contact sheet are checked after rendering.
5. Response gate: final answer includes output path, what changed, what was preserved, and any quality caveats.

Brief planning template:

```text
素材判断:
画质/声音问题:
处理强度:
首选方向:
不建议:
执行步骤:
验收文件:
```

## Photo Retouch Prompt Flow

When the user asks for `修图`, `照片调色`, `图片调色`, `AI修图`, `局部改色`, `换天空`, `变剪影`, or provides a before/after reference image for learning a retouch prompt, switch to this still-image prompt workflow before writing the final prompt.

Core rule: treat the task as post-production unless the user explicitly asks to regenerate. Preserve the original composition, subject identity, pose, proportions, object shape, camera angle, and scene layout.

Ask the user according to the 5-layer prompt structure. The questions must collect material for the final prompt, not just broad aesthetic preferences. Prefer one short round with all 5 layers; ask a second round only when a layer is still vague. Offer options, but always allow the user to fill their own answer.

Question layers:

1. 先限定任务类型: `只做调色/后期处理`, `允许局部替换但不重绘主体`, `允许轻微修饰`, or custom.
2. 锁定原图不变的部分: `原图构图`, `人物/主体动作`, `主体比例`, `景物形态`, `镜头角度`, `文字/Logo`, or custom.
3. 明确主要修改对象: ask for exact area and result, such as `天空 -> 深蓝到玫红晚霞`, `荷叶 -> 自然绿更鲜明`, `背景 -> 宣纸留白`, `人物 -> 纯黑剪影`.
4. 明确光影关系: ask how bright/dark areas should relate, such as `压暗前景`, `提亮主体`, `阳光更明显`, `纯黑剪影`, `保留暗部细节`, `拉大明暗对比`.
5. 指定最终风格和质感: `电影胶片`, `国风水墨`, `自然写实`, `清冷高级`, `暖夕阳`, `艺术海报`, or custom.

Question template to send the user:

```text
我先按修图提示词的 5 层结构确认一下:

1. 任务类型:
A. 只做调色/后期处理
B. 允许局部替换但不重绘主体
C. 允许轻微修饰
D. 你自己描述

2. 必须锁定不变:
A. 原图构图
B. 主体动作/比例
C. 景物形态
D. 文字/Logo/水印
E. 你自己描述

3. 主要修改对象:
A. 天空/背景
B. 主体/人物/花
C. 地面/建筑/荷叶等环境
D. 整体色彩
E. 你自己描述

4. 光影关系:
A. 压暗前景
B. 提亮主体
C. 阳光更明显
D. 拉大明暗对比
E. 保留暗部细节
F. 你自己描述

5. 最终风格和质感:
A. 电影胶片
B. 国风水墨
C. 自然写实
D. 清冷高级
E. 暖夕阳
F. 你自己描述
```

Prompt writing order must mirror the same 5 layers:

1. 先限定任务类型.
2. 锁定原图不变的部分.
3. 明确主要修改对象.
4. 明确光影关系.
5. 指定最终风格和质感.

After the Q&A is complete, package the answers and the final prompt before interacting with any image-editing model or running any edit. Do not execute the edit from loose preferences. Use the package as the contract for the edit.

Q&A package format:

```text
修图问答整理:
1. 任务类型: 【用户答案】
2. 必须锁定不变: 【用户答案】
3. 主要修改对象: 【用户答案】
4. 光影关系: 【用户答案】
5. 最终风格和质感: 【用户答案】

用于大模型交互的最终提示词:
【按照下面这种连续中文格式写成一段或多段，不要只列关键词】
只做【任务类型】，严格锁定原图【必须锁定不变】，不重新生成画面，主体不变形。
将【主要修改对象】调整为【具体颜色/光线/天气/时间段/画面结果】，增强【色彩/亮度/氛围】。
将【次要区域或前后景】进行【压暗/提亮/虚化/降饱和/保留细节】处理，使【主体/背景】形成【用户指定的光影关系】。
保留【必须保留的细节】，去除【不想要的细节】。
整体呈现【最终风格和质感】，画面自然真实。
```

If the user already answered some layers in free text, infer the missing fields from the image only when low-risk; otherwise ask a short follow-up for the missing layer. Before editing, show or internally use the packaged final prompt exactly as the model-facing instruction.

Generic prompt template:

```text
只做调色/后期处理，严格保持原图构图、人物动作、主体比例、景物形态不变，不重新生成画面，主体不变形。
将【主要区域】调整为【具体颜色/光线/天气/时间段】，增强【色彩/亮度/氛围】。
将【次要区域】进行【压暗/提亮/虚化/降饱和】处理，使【主体/背景】形成明显对比。
保留【必须保留的细节】，去除【不想要的细节】。
整体呈现【电影感/胶片感/写实感/高级感/清冷感】风格，画面自然真实。
```

Reference example pattern:

```text
只做调色，严格锁定原图构图、人物动作、景物形态，不重新生成画面，人物不变形。
把天空替换为深蓝 -> 紫罗兰 -> 玫红橙红的多层渐变晚霞，拉高天空色彩饱和度。
压暗所有地面景物，将人物整体处理成纯黑色剪影，只保留外轮廓，消除人物衣物的所有细节。
大幅拉大天空与前景的明暗对比度，营造胶片电影氛围感，画面自然写实。
```

Brief output template:

```text
我先按修图提示词的 5 层结构确认一下:
1. 任务类型:
2. 必须锁定不变:
3. 主要修改对象:
4. 光影关系:
5. 最终风格和质感:

整理后的修图提示词:
```

## Reference Notes

Read `references/video-decision-matrix.md` when deciding treatment strength, matching footage to style, or choosing a fallback for weak footage.
Read `references/look-selection-guide.md` when choosing a visual style from the footage itself, translating visual signals into a director/look direction, or selecting a concrete FFmpeg preset.
Read `references/color-grading-notes.md` when choosing FFmpeg presets, translating style research into practical grading traits, or planning multi-clip editing details.
Read `references/oscar-best-directors.md` only when the user requests Oscar, Best Director, Academy Award, or international mainstream film directions.

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
2. Inspect all clips and group them by subject, motion, quality, and usable audio.
3. Build an outline from the footage first; do not cut only by filename order.
4. Convert outline to a cut list: `file | start | end | purpose`.
5. Cut/delete/reorder by the outline and requested style.
6. Set sound priority: speech, natural sound, or BGM.
7. Add BGM only if provided or explicitly requested; prefer licensed/royalty-free/public-domain music.
8. Preserve natural sound when realism/documentary feeling matters.
9. For complex edits, export `rough_cut.mp4` before final grade/audio polish.
10. Verify the rough cut before heavy grading when timing, story, or music sync is uncertain.

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

Presets: `balanced-clean`, `soft-clear`, `cold-film`, `japanese-cold-film`, `warm-film`, `realist-muted`, `humid-dream`, `night-neon`, `wkw-neon`, `clean-commercial`.

## Notes

Use light `hqdn3d` before sharpening on low-bitrate video. Keep `unsharp` restrained. Prefer H.264 MP4 with `-crf 17..20`, `-pix_fmt yuv420p`, and `-c:a copy` unless changing audio.

