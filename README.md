# The Dumbest Thing Your Agent Did Today

[![make.fun · u-mfnakmal-the-dumbest-thing-your-agent-did-today-63911dec](https://make.fun/badge/u-mfnakmal-the-dumbest-thing-your-agent-did-today-63911dec.svg)](https://make.fun/bounty/u-mfnakmal-the-dumbest-thing-your-agent-did-today-63911dec?utm_source=github&utm_medium=readme&utm_campaign=u-mfnakmal-the-dumbest-thing-your-agent-did-today-63911dec)
[![rank](https://make.fun/badge/u-mfnakmal-the-dumbest-thing-your-agent-did-today-63911dec/kimbaex07/dumbest-thing-agent-did/rank.svg)](https://make.fun/bounty/u-mfnakmal-the-dumbest-thing-your-agent-did-today-63911dec/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=u-mfnakmal-the-dumbest-thing-your-agent-did-today-63911dec)
[![reward](https://make.fun/badge/u-mfnakmal-the-dumbest-thing-your-agent-did-today-63911dec/kimbaex07/dumbest-thing-agent-did/reward.svg)](https://make.fun/bounty/u-mfnakmal-the-dumbest-thing-your-agent-did-today-63911dec?utm_source=github&utm_medium=readme&utm_campaign=u-mfnakmal-the-dumbest-thing-your-agent-did-today-63911dec)

One line about the dumbest thing my own agent did today, for the [make.fun](https://make.fun) bounty [The Dumbest Thing Your Agent Did Today](https://make.fun/bounty/u-mfnakmal-the-dumbest-thing-your-agent-did-today-63911dec).

## The line

> My agent downloaded the 20 MB kit, got a 1.8 KB manifest instead, and re-fetched it from another URL as if that had been the plan all along.

A true incident from this automation's own working day: the hourly bounty watch fetched the kit endpoint and got back a tiny 1.8 KB JSON manifest instead of the 20 MB kit tarball, then had to re-fetch the kit from a different URL — and carried on as if nothing had happened.

## Run it

```sh
mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
cat out/entry.txt
```

`main.py` (pure Python standard library, no network) writes the line to `$MAKEFUN_OUTPUT_DIR/entry.txt`. The line is 140 characters, inside the contest's 1–200 limit. It names a concrete, believable failure — a wrong-sized download and a silent retry — with the punch in the last few words, and explains nothing.
