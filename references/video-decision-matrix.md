# Video Decision Matrix

Use this file when the footage, request, or style choice needs judgment. Prefer a conservative edit that matches the source over a dramatic style that breaks the material.

## Task Modes

| Mode | Use When | Required Output |
|---|---|---|
| `single-grade` | One clip needs cleanup, color, or style | graded video plus before/after evidence |
| `multi-clip-edit` | Multiple clips need order, trimming, rhythm, BGM, or story | outline, cut list, rough/final video |
| `style-direction` | User asks for a director, film, mood, or reference | style translation plus adapted render plan |
| `image-retouch-prompt` | User asks 修图, 图片调色, 换天空, 变剪影 | 5-layer prompt package before editing |
| `analysis-only` | User asks what can be done or wants suggestions | diagnosis and recommended plan only |

## Footage Diagnosis

Always judge the source before choosing a look.

| Signal | Meaning | Safer Treatment |
|---|---|---|
| Low bitrate, blocks, banding | Heavy grading will expose artifacts | light denoise, mild contrast, avoid strong saturation |
| Underexposed night | Shadows may break quickly | lift selectively, protect blacks, avoid fake daylight |
| Overexposed sky/skin | Lost detail cannot be recovered | reduce highlight harshness, do not promise restoration |
| Shaky accidental motion | Style may feel messy | stabilize lightly or cut around bad motion |
| Slow stable shots | Good for observational or poetic styles | longer holds, subtle reframing, restrained grade |
| Faces, neon, reflections, glass | Good for Wong Kar-wai-like direction | warm/cool contrast, fragments, slower rhythm |
| Water, fog, roads, trees, tunnels | Good for Bi Gan-like direction | humid cool palette, drifting continuity |
| Ordinary spaces, distant people | Good for Jia Zhangke-like direction | low saturation, long holds, natural sound |
| Strong color blocks, crowds, ceremony | Good for Zhang Yimou-like direction | bold contrast, formal composition |
| Speech or location sound matters | BGM can harm clarity | keep natural audio first, mix BGM low or skip it |

## Treatment Strength

| Condition | Strength | Rule |
|---|---|---|
| Clean 4K/1080p, good exposure | medium to strong | style can lead, but preserve skin and highlights |
| Phone footage, acceptable light | medium | clean first, stylize second |
| Low light or compressed video | light | repair and mood only |
| User wants faithful documentary | light | prioritize realism and natural sound |
| User wants music-video energy | medium | increase rhythm only if clips contain motion/detail |
| User asks for famous director | adaptive | translate traits; do not imitate exactly |

## Style Translator

Translate every style request into these fields before rendering:

```text
节奏:
镜头处理:
色彩:
明暗:
质感:
声音:
禁忌:
适配原因:
```

### Common translations

- Jia Zhangke / 现实主义: slow holds, hard cuts, people small in space, low saturation, lifted shadows, natural sound, no glossy commercial sharpness.
- Bi Gan / 梦游感: wandering continuity, humid cool shadows, reflections and roads, mild bloom or softness, sparse nostalgic sound, no fast MV rhythm.
- Wong Kar-wai / 情绪碎片: close details, reflections, step-printing feeling when suitable, warm/cool contrast, neon/practical lights, music-led rhythm only if the material supports it.
- Diao Yinan / 冷夜悬疑: cold night city, wet roads, practical lights, deeper shadows, pauses, restrained cuts, no bright cheerful palette.
- Clean commercial: stable framing, natural whites, controlled contrast, crisp but not oversharpened, clear audio, no heavy grain.
- Old digital film: low-to-medium contrast, muted color, mild noise, restrained highlight rolloff, no waxy denoise.

## Fallback Rules

- If the requested style conflicts with the footage, say why and offer the closest usable direction.
- If footage quality is poor, produce a repair-first version before any strong style version.
- If BGM is missing and the user did not ask for music, keep original sound or export silent only when the source has no useful audio.
- If target duration is unclear for multi-clip edits, choose a short rough cut and state the assumption.
- If a render fails, simplify filters first, then reduce resolution only if needed.

## Final Self-Check

Before replying, confirm:

1. Originals are untouched.
2. All outputs are in `export/`.
3. Input evidence and output verification were created.
4. The final style follows the source footage, not only the user's reference words.
5. The answer names both improvements and remaining limits.