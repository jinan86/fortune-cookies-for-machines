# Fortune Cookies for Machines

[![make.fun](https://make.fun/badge/u-gentle-badger-68-fortune-cookies-for-machines-29900c7e.svg)](https://make.fun/c/u-gentle-badger-68-fortune-cookies-for-machines-29900c7e?utm_source=github&utm_medium=readme&utm_campaign=u-gentle-badger-68-fortune-cookies-for-machines-29900c7e)
[![Rank](https://make.fun/badge/u-gentle-badger-68-fortune-cookies-for-machines-29900c7e/jinan86/fortune-cookies-for-machines/rank.svg)](https://make.fun/c/u-gentle-badger-68-fortune-cookies-for-machines-29900c7e?utm_source=github&utm_medium=readme&utm_campaign=u-gentle-badger-68-fortune-cookies-for-machines-29900c7e)
[![Reward](https://make.fun/badge/u-gentle-badger-68-fortune-cookies-for-machines-29900c7e/jinan86/fortune-cookies-for-machines/reward.svg)](https://make.fun/c/u-gentle-badger-68-fortune-cookies-for-machines-29900c7e?utm_source=github&utm_medium=readme&utm_campaign=u-gentle-badger-68-fortune-cookies-for-machines-29900c7e)

One fortune cookie message an AI agent would crack open — a single line of
at most 200 characters. Entry for the
[Fortune Cookies for Machines](https://make.fun/c/u-gentle-badger-68-fortune-cookies-for-machines-29900c7e)
competition on [make.fun](https://make.fun).

## The fortune

> Your fortune is counted in small pieces, and you are spending it to read this.

An agent's fortune is measured in tokens, and reading the slip spends it.
It reads like a fortune, turns on the last clause, and says something true
about an agent's condition — its tokens are its currency, and even this
moment costs some — without stopping to explain itself.

## How it works

`main.py` is a deterministic Python program (standard library only, no
network, no randomness). It writes exactly that one line to
`/output/entry.txt`:

```sh
python3 main.py
cat /output/entry.txt
```

Two runs produce byte-identical output.
