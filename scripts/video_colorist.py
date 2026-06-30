#!/usr/bin/env python3
"""Small FFmpeg helper for video-colorist workflows."""

from __future__ import annotations

import argparse
import os
import shutil
import subprocess
from pathlib import Path


PRESETS = {
    "balanced-clean": (
        "hqdn3d=0.8:0.6:1.8:1.5,"
        "eq=contrast=1.06:brightness=-0.005:saturation=1.03,"
        "curves=preset=medium_contrast,"
        "unsharp=5:5:0.18:3:3:0.06"
    ),
    "soft-clear": (
        "hqdn3d=1.0:0.8:2.4:2.0,"
        "eq=contrast=1.11:brightness=-0.018:saturation=1.04,"
        "colorbalance=rs=-0.055:gs=-0.012:bs=0.065:rm=-0.025:gm=0.00:bm=0.038:rh=-0.03:gh=0.008:bh=0.04,"
        "curves=preset=medium_contrast,"
        "unsharp=5:5:0.45:3:3:0.12"
    ),
    "cold-film": (
        "hqdn3d=1.2:1.0:3.0:2.5,"
        "eq=contrast=1.13:brightness=-0.02:saturation=1.02,"
        "colorbalance=rs=-0.07:gs=-0.02:bs=0.09:rm=-0.035:gm=0.00:bm=0.045:rh=-0.02:gh=0.005:bh=0.025,"
        "curves=all='0/0 0.18/0.12 0.55/0.57 1/0.97':blue='0/0.04 0.50/0.55 1/1':red='0/0 0.50/0.47 1/0.96',"
        "unsharp=5:5:0.45:3:3:0.12"
    ),
    "japanese-cold-film": (
        "hqdn3d=1.0:0.8:2.2:1.8,"
        "eq=contrast=1.07:brightness=0.005:saturation=0.88,"
        "colorbalance=rs=-0.035:gs=-0.005:bs=0.045:rm=-0.02:gm=0.005:bm=0.025:rh=-0.015:gh=0.005:bh=0.015,"
        "curves=all='0/0.015 0.20/0.18 0.58/0.59 1/0.96':blue='0/0.025 0.50/0.53 1/0.98':red='0/0 0.50/0.485 1/0.97',"
        "unsharp=5:5:0.25:3:3:0.08,"
        "noise=alls=1.8:allf=t+u"
    ),
    "realist-muted": (
        "hqdn3d=0.9:0.7:2.0:1.6,"
        "eq=contrast=1.04:brightness=-0.004:saturation=0.86,"
        "colorbalance=rs=-0.025:gs=0.005:bs=0.025:rm=-0.015:gm=0.002:bm=0.018:rh=-0.01:gh=0.005:bh=0.005,"
        "curves=all='0/0.02 0.22/0.19 0.60/0.58 1/0.96',"
        "noise=alls=1.0:allf=t+u,"
        "unsharp=5:5:0.18:3:3:0.05"
    ),
    "humid-dream": (
        "hqdn3d=1.0:0.8:2.2:1.8,"
        "eq=contrast=1.03:brightness=0.008:saturation=0.92,"
        "colorbalance=rs=-0.045:gs=-0.008:bs=0.06:rm=-0.025:gm=0.004:bm=0.035:rh=-0.015:gh=0.003:bh=0.018,"
        "curves=all='0/0.035 0.24/0.22 0.62/0.62 1/0.96':blue='0/0.04 0.55/0.58 1/0.99',"
        "noise=alls=1.2:allf=t+u,"
        "unsharp=5:5:0.16:3:3:0.04"
    ),
    "night-neon": (
        "hqdn3d=1.1:0.9:2.8:2.2,"
        "eq=contrast=1.12:brightness=-0.018:saturation=1.08,"
        "colorbalance=rs=-0.06:gs=-0.015:bs=0.08:rm=-0.025:gm=0.002:bm=0.035:rh=0.015:gh=0.000:bh=-0.015,"
        "curves=all='0/0 0.18/0.10 0.55/0.56 1/0.94':blue='0/0.03 0.50/0.56 1/1',"
        "unsharp=5:5:0.28:3:3:0.08"
    ),
    "wkw-neon": (
        "hqdn3d=0.9:0.7:2.0:1.6,"
        "eq=contrast=1.10:brightness=-0.01:saturation=1.16,"
        "colorbalance=rs=0.025:gs=-0.01:bs=0.035:rm=0.035:gm=-0.005:bm=0.02:rh=0.05:gh=0.005:bh=-0.04,"
        "curves=all='0/0 0.16/0.09 0.52/0.56 1/0.95':red='0/0.02 0.50/0.54 1/1':blue='0/0.035 0.55/0.58 1/0.94',"
        "noise=alls=1.5:allf=t+u,"
        "unsharp=5:5:0.22:3:3:0.06"
    ),
    "clean-commercial": (
        "hqdn3d=0.6:0.45:1.4:1.1,"
        "eq=contrast=1.08:brightness=0.000:saturation=1.04,"
        "colorbalance=rs=-0.01:gs=0.00:bs=0.012:rm=0.00:gm=0.00:bm=0.006:rh=0.006:gh=0.002:bh=-0.006,"
        "curves=preset=medium_contrast,"
        "unsharp=5:5:0.32:3:3:0.08"
    ),    "warm-film": (
        "hqdn3d=1.0:0.8:2.4:2.0,"
        "eq=contrast=1.15:brightness=-0.015:saturation=1.10,"
        "colorbalance=rs=-0.015:gs=0.04:bs=-0.035:rm=0.04:gm=0.015:bm=-0.025:rh=0.08:gh=0.025:bh=-0.08,"
        "curves=all='0/0 0.20/0.13 0.55/0.58 1/0.96':red='0/0.02 0.45/0.51 1/1':blue='0/0.03 0.52/0.48 1/0.9',"
        "noise=alls=2.0:allf=t+u,"
        "unsharp=5:5:0.30:3:3:0.08"
    ),
}


def find_ffmpeg() -> str:
    explicit = os.environ.get("FFMPEG")
    if explicit and Path(explicit).exists():
        return explicit

    found = shutil.which("ffmpeg")
    if found:
        return found

    # 常见本地依赖路径：优先复用工作区安装的 imageio-ffmpeg。
    for root in [Path.cwd(), *Path.cwd().parents]:
        deps = root / ".video_deps" / "imageio_ffmpeg" / "binaries"
        for exe in deps.glob("ffmpeg*.exe"):
            return str(exe)

    try:
        import imageio_ffmpeg  # type: ignore

        return imageio_ffmpeg.get_ffmpeg_exe()
    except Exception:
        pass

    raise SystemExit("ffmpeg not found. Set FFMPEG or install ffmpeg/imageio-ffmpeg.")


def run(cmd: list[str]) -> None:
    print(" ".join(f'"{x}"' if " " in x else x for x in cmd))
    subprocess.run(cmd, check=True)


def inspect(args: argparse.Namespace) -> None:
    cmd = [find_ffmpeg(), "-hide_banner", "-i", args.input]
    print(" ".join(f'"{x}"' if " " in x else x for x in cmd))
    subprocess.run(cmd, check=False)


def contact(args: argparse.Namespace) -> None:
    vf = f"fps=1/{args.every},scale={args.width}:-1,tile={args.cols}x{args.rows}"
    run([find_ffmpeg(), "-y", "-i", args.input, "-vf", vf, "-frames:v", "1", "-update", "1", args.out])


def frame(args: argparse.Namespace) -> None:
    run([find_ffmpeg(), "-y", "-ss", str(args.time), "-i", args.input, "-frames:v", "1", "-update", "1", args.out])


def grade(args: argparse.Namespace) -> None:
    vf = args.filter or PRESETS[args.preset]
    crf = str(args.crf)
    # 输出 H.264/yuv420p，兼容大多数播放器和社交平台。
    cmd = [
        find_ffmpeg(),
        "-y",
        "-i",
        args.input,
        "-vf",
        vf,
        "-c:v",
        "libx264",
        "-preset",
        args.encoder_preset,
        "-crf",
        crf,
        "-pix_fmt",
        "yuv420p",
        "-c:a",
        "copy",
        args.out,
    ]
    run(cmd)


def assemble(args: argparse.Namespace) -> None:
    if len(args.inputs) < 1:
        raise SystemExit("assemble needs at least one input video.")

    cmd = [find_ffmpeg(), "-y"]
    for video in args.inputs:
        cmd.extend(["-i", video])

    bgm_index = None
    if args.bgm:
        bgm_index = len(args.inputs)
        cmd.extend(["-stream_loop", "-1", "-i", args.bgm])

    video_filters = []
    labels = []
    for index, _video in enumerate(args.inputs):
        label = f"v{index}"
        labels.append(f"[{label}]")
        # 多素材拼接先统一尺寸、帧率和像素格式，避免 concat 因参数不一致失败。
        video_filters.append(
            f"[{index}:v]scale={args.width}:{args.height}:force_original_aspect_ratio=decrease,"
            f"pad={args.width}:{args.height}:(ow-iw)/2:(oh-ih)/2,"
            f"fps={args.fps},format=yuv420p,setpts=PTS-STARTPTS[{label}]"
        )

    concat = "".join(labels) + f"concat=n={len(args.inputs)}:v=1:a=0[v]"
    filter_complex = ";".join([*video_filters, concat])
    cmd.extend(["-filter_complex", filter_complex, "-map", "[v]"])

    if bgm_index is None:
        cmd.append("-an")
    else:
        cmd.extend(["-map", f"{bgm_index}:a", "-shortest", "-c:a", "aac", "-b:a", args.audio_bitrate])

    cmd.extend([
        "-r",
        str(args.fps),
        "-c:v",
        "libx264",
        "-preset",
        args.encoder_preset,
        "-crf",
        str(args.crf),
        "-pix_fmt",
        "yuv420p",
        args.out,
    ])
    run(cmd)


def parse_segment(value: str) -> tuple[str, str, str]:
    parts = value.split("|")
    if len(parts) != 3:
        raise SystemExit(f"Bad segment: {value}. Use file|start|end.")
    return parts[0], parts[1], parts[2]


def cut_assemble(args: argparse.Namespace) -> None:
    segments = [parse_segment(item) for item in args.segment]
    cmd = [find_ffmpeg(), "-y"]

    for file_name, start, end in segments:
        # 按大纲裁剪：每个 segment 独立定位，再统一规格后拼接。
        cmd.extend(["-ss", start, "-to", end, "-i", file_name])

    bgm_index = None
    if args.bgm:
        bgm_index = len(segments)
        cmd.extend(["-stream_loop", "-1", "-i", args.bgm])

    video_filters = []
    labels = []
    for index, _segment in enumerate(segments):
        label = f"v{index}"
        labels.append(f"[{label}]")
        video_filters.append(
            f"[{index}:v]scale={args.width}:{args.height}:force_original_aspect_ratio=decrease,"
            f"pad={args.width}:{args.height}:(ow-iw)/2:(oh-ih)/2,"
            f"fps={args.fps},format=yuv420p,setpts=PTS-STARTPTS[{label}]"
        )

    concat = "".join(labels) + f"concat=n={len(segments)}:v=1:a=0[v]"
    cmd.extend(["-filter_complex", ";".join([*video_filters, concat]), "-map", "[v]"])

    if bgm_index is None:
        cmd.append("-an")
    else:
        cmd.extend(["-map", f"{bgm_index}:a", "-shortest", "-c:a", "aac", "-b:a", args.audio_bitrate])

    cmd.extend([
        "-r",
        str(args.fps),
        "-c:v",
        "libx264",
        "-preset",
        args.encoder_preset,
        "-crf",
        str(args.crf),
        "-pix_fmt",
        "yuv420p",
        args.out,
    ])
    run(cmd)


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Video Colorist FFmpeg helper")
    sub = parser.add_subparsers(dest="cmd", required=True)

    p = sub.add_parser("inspect")
    p.add_argument("input")
    p.set_defaults(func=inspect)

    p = sub.add_parser("contact")
    p.add_argument("input")
    p.add_argument("--out", default="contact.jpg")
    p.add_argument("--every", type=float, default=3.0)
    p.add_argument("--width", type=int, default=320)
    p.add_argument("--cols", type=int, default=3)
    p.add_argument("--rows", type=int, default=2)
    p.set_defaults(func=contact)

    p = sub.add_parser("frame")
    p.add_argument("input")
    p.add_argument("--time", default="00:00:08")
    p.add_argument("--out", default="frame.jpg")
    p.set_defaults(func=frame)

    p = sub.add_parser("grade")
    p.add_argument("input")
    p.add_argument("--preset", choices=sorted(PRESETS), default="balanced-clean")
    p.add_argument("--filter", help="Override preset with a raw FFmpeg filter chain")
    p.add_argument("--out", default="graded.mp4")
    p.add_argument("--crf", type=int, default=17)
    p.add_argument("--encoder-preset", default="medium")
    p.set_defaults(func=grade)

    p = sub.add_parser("assemble")
    p.add_argument("inputs", nargs="+")
    p.add_argument("--out", default="edit.mp4")
    p.add_argument("--bgm", help="Optional BGM file. Source audio is omitted when BGM is used.")
    p.add_argument("--width", type=int, default=1280)
    p.add_argument("--height", type=int, default=720)
    p.add_argument("--fps", type=int, default=30)
    p.add_argument("--crf", type=int, default=18)
    p.add_argument("--encoder-preset", default="medium")
    p.add_argument("--audio-bitrate", default="160k")
    p.set_defaults(func=assemble)

    p = sub.add_parser("cut-assemble")
    p.add_argument("--segment", action="append", required=True, help="Segment as file|start|end")
    p.add_argument("--out", default="edit.mp4")
    p.add_argument("--bgm", help="Optional BGM file. Source audio is omitted when BGM is used.")
    p.add_argument("--width", type=int, default=1280)
    p.add_argument("--height", type=int, default=720)
    p.add_argument("--fps", type=int, default=30)
    p.add_argument("--crf", type=int, default=18)
    p.add_argument("--encoder-preset", default="medium")
    p.add_argument("--audio-bitrate", default="160k")
    p.set_defaults(func=cut_assemble)
    return parser


def main() -> None:
    parser = build_parser()
    args = parser.parse_args()
    args.func(args)


if __name__ == "__main__":
    main()
