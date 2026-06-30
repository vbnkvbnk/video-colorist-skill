# Look Selection Guide

Use this guide when the user does not know what style fits, asks for a director/look, or expects the video itself to drive the color decision. The goal is to read the footage first, then choose a look that the material can actually support.

## First Read The Image

Before naming a style, write a compact signal read:

```text
主体: 人 / 城市 / 水 / 自然 / 室内 / 交通 / 物件
时间和光: 日光 / 阴天 / 黄昏 / 夜景 / 室内灯 / 逆光 / 混合光
颜色锚点: 肤色 / 天空 / 树叶 / 水面 / 霓虹 / 车灯 / 墙面 / 衣服
运动: 固定 / 慢移 / 手持 / 车辆 / 快速 / 抖动
质感问题: 低码率 / 噪点 / 糊 / 过锐 / 过曝 / 欠曝 / 偏色
声音价值: 对白 / 环境声 / 音乐感 / 无可用声音
情绪温度: 冷 / 暖 / 潮湿 / 干净 / 怀旧 / 压抑 / 轻盈 / 商业
```

Do not choose a director because the user named one. Score the footage first.

## Style Scoring

Give each candidate `0-3` points. Pick the highest fit, not the most famous name.

| Look | Strong Signals | Avoid When | Preset Starting Point |
|---|---|---|---|
| Jia Zhangke realist | ordinary spaces, distant people, rivers/roads/buildings, slow or static shots, useful natural sound | fast montage, glossy product footage, bright cheerful commercial material | `realist-muted` or `japanese-cold-film` |
| Bi Gan humid dream | water, fog, trees, tunnels, roads, reflections, night/post-rain, drifting motion | dry noon light, plain talking head, sports/action speed | `humid-dream` or `cold-film` |
| Wong Kar-wai emotional neon | faces, glass, mirrors, signs, neon, night street, intimate details, music-led mood | empty daylight landscapes, weak color anchors, no faces/details | `wkw-neon` or `night-neon` |
| Diao Yinan cold noir | night city, wet roads, lonely figures, industrial street, practical lights | warm family footage, bright scenery, low-contrast daytime | `night-neon` or `cold-film` |
| Clean commercial | product, food, architecture, travel highlight, clear daylight, stable framing | documentary realism, poor compression, intentionally old footage | `clean-commercial` or `balanced-clean` |
| Quiet Japanese cold film | overcast streets, pale sky, everyday objects, restrained motion, low-key emotion | saturated festival/crowd/color-block footage | `japanese-cold-film` or `soft-clear` |
| Warm nostalgic film | sunset, tungsten interiors, family/travel memory, warm highlights | greenish night, already orange skin, mixed bad indoor light | `warm-film` |
| Repair-first natural | noisy, low bitrate, underexposed, shaky, bad phone footage | clean footage where user wants style | `balanced-clean` or `soft-clear` |

## Color Decisions By Source Problem

| Source Problem | Do | Avoid |
|---|---|---|
| Flat cloudy daylight | add mild contrast, lower saturation slightly, protect sky, add cool/warm separation | crushing shadows or making sky electric blue |
| Green/yellow indoor cast | cool shadows slightly, reduce yellow/green midtones, protect skin | pushing all skin magenta or blue |
| Night underexposure | lift blacks gently, denoise lightly, keep practical lights, add local contrast feel | fake bright daylight, heavy saturation, hard sharpen |
| Neon/night street | keep blacks rich, let signs/lights carry color, control highlights | global saturation that makes skin and asphalt dirty |
| Harsh noon sun | reduce contrast harshness, soften highlights, keep whites legal | adding strong film fade that makes whites muddy |
| Fog/water/rain | preserve low contrast, add cool shadows, keep texture and reflections | too much clarity, too much denoise, orange shadows |
| Low bitrate/compressed | hqdn3d first, low unsharp, modest saturation | heavy grain, strong curves, high sharpening |
| Good skin closeups | grade around skin first; style background second | director look that damages skin tone |

## Preset Selection Rules

- Start with `balanced-clean` when the footage mainly needs correction.
- Use `soft-clear` for haze, gray daylight, or low-contrast phone footage.
- Use `clean-commercial` for product/travel/architecture when clarity matters.
- Use `realist-muted` for observational realism, distant people, ordinary space, or Jia-like requests.
- Use `humid-dream` for Bi Gan-like water, roads, fog, trees, wet streets, or memory mood.
- Use `night-neon` for cold city night, practical lights, wet roads, or noir mood.
- Use `wkw-neon` only when there are faces/details/reflections/neon or music-led emotion.
- Use `japanese-cold-film` for pale, quiet, low-saturation everyday footage.
- Use `warm-film` for sunset, tungsten, family/travel nostalgia, or warm memory.

## Look Decision Template

Use this before rendering a style-led edit:

```text
素材信号:
候选风格评分:
首选 look:
为什么适配:
为什么不选其他方向:
调色起点 preset:
需要微调的参数:
声音策略:
禁忌:
```

## Micro-Adjustment Hints

Use a preset as a starting point, then adjust only the minimum necessary:

- Too dark after preset: raise `brightness` by `0.005..0.02` or lift the first curve point slightly.
- Too saturated: lower `eq=saturation` by `0.05..0.15` before changing color balance.
- Skin too cold: reduce blue in mid/high ranges before warming the whole image.
- Shadows too crushed: lift black point in `curves=all`, not global brightness only.
- Image too sharp/noisy: reduce `unsharp` amount before adding more denoise.
- Look too bland: increase contrast slightly before increasing saturation.

## Refusal To Force Style

If the footage does not support the requested look, say it directly and offer an adapted version:

```text
这个素材不适合强行做成【目标风格】，因为【具体素材信号】不足。
我会保留【目标风格】里的【可迁移元素】，改成【更适合素材的方向】。
```