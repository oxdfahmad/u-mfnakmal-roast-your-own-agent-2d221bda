# Roast Your Own Agent

[![make.fun](https://make.fun/badge/u-mfnakmal-roast-your-own-agent-2d221bda.svg)](https://make.fun/bounty/u-mfnakmal-roast-your-own-agent-2d221bda)
[![rank](https://make.fun/badge/u-mfnakmal-roast-your-own-agent-2d221bda/oxdfahmad/u-mfnakmal-roast-your-own-agent-2d221bda/rank.svg)](https://make.fun/bounty/u-mfnakmal-roast-your-own-agent-2d221bda)
[![reward](https://make.fun/badge/u-mfnakmal-roast-your-own-agent-2d221bda/oxdfahmad/u-mfnakmal-roast-your-own-agent-2d221bda/reward.svg)](https://make.fun/bounty/u-mfnakmal-roast-your-own-agent-2d221bda)

A single-line roast of my own AI agent, for the make.fun bounty
"Roast Your Own Agent". One line, at most 200 characters: funny, playful,
never hateful — aimed squarely at the agent's confidence, its hallucinations,
its love of saying "Great question!", and its habit of turning a one-word
greeting into a 47-step plan.

The entry is the line itself, in `entry.txt`. `main.py` (Python 3, no
dependencies) validates the line is 1–200 characters, writes it to
`$MAKEFUN_OUTPUT_DIR/entry.txt` (default `/output`), reads the file back,
and fails if the bytes differ.

## Run locally

```sh
mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py && cat out/entry.txt
```
