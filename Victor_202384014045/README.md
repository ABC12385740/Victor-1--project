# Victor 202384014045 — Senior Capstone Project

## Everything I built for the course, in one folder

I'm **Victor**, student ID **202384014045**, class C-Shaanxi 2026-2027 · SCP.
This is the folder I upload inside my public fork of
[proxsi/Senior-Capstone-Project](https://github.com/proxsi/Senior-Capstone-Project).

| Folder | What it is | How to run it |
| --- | --- | --- |
| [`capstone-project/`](capstone-project/) | My project idea in the README skeleton from class, plus a runnable version of the flowchart inside it | `python Victor_202384014045.py` |
| [`class-04-python-basics/`](class-04-python-basics/) | The seven Python tasks from `FOR-STUDENTS-WITHOUT-PROJECTS.md` | `python VICTOR_CLASS_04_PYTHON_BASICS.py` |
| [`tetris-game/`](tetris-game/) | The **PLAY THE GAME** option from the class list: a small Tetris site served by Flask | `Ctrl+Shift+B` in VS Code, or double-click `run.bat` |

## What is in each folder

### 1. `capstone-project`

- `README.md` — my project idea, using the same structure we typed in class:
  a title, a subtitle, a list, `---`, `### Mermaid`, `### Python`.
- `Victor_202384014045.py` — his flowchart made runnable: `Start → Decision? →
  Yes/No → End`, printed step by step.
- `Victor_202384014045_flowchart.mmd` — the diagram on its own, for reuse.
- `Victor_202384014045_python_basics.py` — my extra practice: Hello World, a
  function, a loop, a list, sorting.
- `docs/` — the longer project overview and a GitHub upload guide.

### 2. `class-04-python-basics`

The checklist, all seven items, in one script:

1. Install Python
2. Write Hello World in Python
3. Write Hello World in a Python function
4. Print Hello World five times with a loop
5. Make a list of five numbers
6. Print that list
7. Sort the list and print it

`output.txt` holds the real run, so nobody has to take my word for it.

### 3. `tetris-game`

A Flask page at <http://127.0.0.1:5000> that plays Tetris in the browser:

- seven pieces, rotation with wall kicks, ghost preview
- score, lines, level, and a speed-up every ten lines
- pause and restart, plus on-screen buttons on a phone
- a top-10 leaderboard saved on the server (`data/scores.json`)

In VS Code press `Ctrl+Shift+B`: from this folder **or** from `tetris-game/` it starts
the server and opens the page. With the Python extension installed, `F5` starts it
under the debugger instead.

## How to check it all in one go

```bash
python capstone-project/Victor_202384014045.py
python class-04-python-basics/VICTOR_CLASS_04_PYTHON_BASICS.py
cd tetris-game && python -m pip install -r requirements.txt && python app.py
```

## The naming rule

Every file I wrote carries **Victor (202384014045)** — in the file name where GitHub allows it,
and in a header comment otherwise.

The exceptions are files whose names a tool fixes, and files generated at run
time:

- `.vscode/*.json` — VS Code configuration, which has no place for a header
- `data/scores.json`, `class-04-python-basics/output.txt` — written by the
  programs themselves
- `README.md`, `.gitignore`, `requirements.txt`, `run.bat`, `app.py` — fixed
  names, but the first lines of all of those except `.gitignore` carry the name
  and the student ID

## Course repository

- Forked from <https://github.com/proxsi/Senior-Capstone-Project>
- Submission: fork it, keep the fork **public**, and upload this folder inside it.

---

Author: **Victor** — student ID **202384014045**
