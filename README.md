# Video Colorist Skill

A Codex skill for local video inspection, contact sheets, frame grabs, color grading, multi-clip assembly, BGM replacement, and director/style-guided video finishing with FFmpeg.

## Features

- Inspect video metadata: duration, codec, resolution, fps, bitrate, and audio streams.
- Generate contact sheets and representative frame grabs.
- Apply reusable color presets with FFmpeg.
- Assemble multiple clips into a normalized H.264 MP4.
- Build cut lists from explicit time ranges.
- Replace source audio with BGM.
- Use named director/style references as practical editing guidance.
- Includes a dedicated Jia Zhangke trigger for restrained realism, cool cyan-green low saturation, natural sound, and minimal digital movement.

## Layout

```text
.
├── SKILL.md
├── agents/
│   └── openai.yaml
├── references/
│   └── color-grading-notes.md
└── scripts/
    └── video_colorist.py
```

## Requirements

- Python 3.10+
- FFmpeg available on `PATH`, or set `FFMPEG` to the ffmpeg executable.
- Optional: `imageio-ffmpeg` if you want the helper script to locate a bundled ffmpeg binary.

Install the optional dependency:

```bash
python -m pip install imageio-ffmpeg
```

## Usage

```bash
python scripts/video_colorist.py inspect input.mp4
python scripts/video_colorist.py contact input.mp4 --out contact.jpg
python scripts/video_colorist.py frame input.mp4 --time 8 --out frame.jpg
python scripts/video_colorist.py grade input.mp4 --preset cold-film --out graded.mp4
python scripts/video_colorist.py assemble a.mp4 b.mp4 --out edit.mp4 --bgm music.mp3
python scripts/video_colorist.py cut-assemble --segment "a.mp4|00:00:01|00:00:04" --segment "b.mp4|00:00:00|00:00:03" --out edit.mp4
```

## Presets

- `balanced-clean`: natural cleanup.
- `soft-clear`: cool clarity for haze or low contrast.
- `cold-film`: deeper cool shadows and blue/cyan mood.
- `japanese-cold-film`: low saturation, lifted blacks, quiet air.
- `warm-film`: warm highlights and nostalgic contrast.

## Notes

The skill preserves original media and exports new files. It does not include any source video, audio, copyrighted media, or model outputs from local editing sessions.

## License

MIT
