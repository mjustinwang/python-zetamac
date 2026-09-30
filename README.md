# python-zetamac

A command-line recreation of [Zetamac](https://arithmetic.zetamac.com/), the timed mental-math arithmetic game, written in Python.

This project has two goals:

1. Build a small, working arithmetic game.
2. Get hands-on practice collaborating with Git and GitHub as a two-person team (feature branches, commits, merges, pull requests, and issues).

## How it works

You choose the difficulty up front, then answer as many arithmetic problems as you can before the clock runs out.

1. Pick the **maximum number of digits** per number.
2. Pick which **operations** to include: `+`, `-`, `*`, `/`.
3. Pick a **time limit** in seconds.
4. Answer problems as they appear. Each correct answer scores a point.
5. When time is up, you get a summary: total correct, average time per question, and your fastest answer.

Division problems are always generated so the answer is a whole number.

### Example session

```
Max digits per number: 2
Do you want this operation: "+"? y/n: y
Do you want this operation: "-"? y/n: y
Do you want this operation: "*"? y/n: y
Do you want this operation: "/"? y/n: n
Total time in sec: 60
TOTAL TIME LEFT: 60
47 + 82 = 
```

## Getting started

### Run it

```bash
git clone https://github.com/mjustinwang/python-zetamac.git
cd python-zetamac
python run.py
```

Press `Ctrl+C` at any time to quit.

## Project structure

| File | Purpose |
| --- | --- |
| `run.py` | Entry point. Calls `run_game()`. |
| `game.py` | Game loop, settings prompts, answer input, timing, and the end-of-game summary. |
| `generator.py` | `problem_gen()` creates a random problem and its answer for a given digit length and operation. |


## Our Git and GitHub workflow

Since learning Git collaboration was a main goal, here is how we worked. You can see all of it in the repo's [commit history](https://github.com/mjustinwang/python-zetamac/commits/main/), [issues](https://github.com/mjustinwang/python-zetamac/issues), and [pull requests](https://github.com/mjustinwang/python-zetamac/pulls).

- **Issues:** bugs and to-dos were written up as issues before we started on them.
- **Feature branches:** each piece of work lived on its own branch instead of committing straight to `main`.
- **Commits:** small, focused commits with descriptive messages.
- **Pull requests:** changes were merged into `main` through PRs.
- **Merging:** we practiced merging branches and resolving conflicts when our work overlapped.

### Contributing flow (what we did)

```bash
git checkout main
git pull
git checkout -b feature/short-description
# make changes, then:
git add .
git commit -m "Describe what changed and why"
git push -u origin feature/short-description
# open a pull request on GitHub, get a review, then merge
```

## Authors

- Justin Wang ([@mjustinwang](https://github.com/mjustinwang))
- Ryan Ho ([@cm-ryanho](https://github.com/cm-ryanho))
