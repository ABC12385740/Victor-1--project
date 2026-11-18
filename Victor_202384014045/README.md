# Victor 202384014045 — Senior Capstone Project

> A fork of [`proxsi/Senior-Capstone-Project`](https://github.com/proxsi/Senior-Capstone-Project).
> This folder holds my Class 04 homework and the first draft of my capstone idea.

| | |
| --- | --- |
| **Name** | Victor |
| **Student ID** | 202384014045 |
| **Course** | C-Shaanxi 2026-2027 · SCP — Senior Capstone Project |
| **Class** | 04 — Python Basics |

## Class 04 — Python Basics

The checklist from `FOR-STUDENTS-WITHOUT-PROJECTS.md`, all seven items done.

### The checklist

1. Install Python
2. Write Hello World in python
3. Write Hello World in a python function
4. Print Hello World FIVE TIMES using a loop
5. Make a List of 5 numbers
6. Print the list of 5 numbers
7. Sort the list of 5 numbers and print it

### What I did for each item

| # | Task | Result |
| - | ---- | ------ |
| 1 | Install Python | **Python 3.14.10** (64-bit) at `D:\Python314\python.exe` |
| 2 | Hello World | `hello()` → `Hello World` |
| 3 | Hello World in a function | `hello_in_function("World")` → `Hello World` |
| 4 | Hello World five times, with a loop | `five_times()` → 5 numbered lines |
| 5 | A list of 5 numbers | `[42, 7, 19, 3, 88]` |
| 6 | Print the list | one number per line |
| 7 | Sort the list and print it | `[3, 7, 19, 42, 88]` |

### Run it

```bash
python VICTOR_CLASS_04_PYTHON_BASICS.py
```

### Output

```text
1. Install Python
   version:     3.14.10
   interpreter: D:\Python314\python.exe

2. Hello World
   Hello World

3. Hello World in a function
   Hello World

4. Hello World five times (loop)
   1. Hello World
   2. Hello World
   3. Hello World
   4. Hello World
   5. Hello World

5. Make a list of 5 numbers
   [42, 7, 19, 3, 88]

6. Print the list of 5 numbers
   42
   7
   19
   3
   88

7. Sort the list of 5 numbers and print it
   original: [42, 7, 19, 3, 88]
   sorted(): [3, 7, 19, 42, 88]
   .sort():  [3, 7, 19, 42, 88]
```

### Notes

- Item 1 has no screenshot on purpose: the first two lines print `sys.version`
  and `sys.executable`, which shows the real interpreter that ran the file.
- Item 7 prints the sort twice: `sorted(numbers)` returns a **new** list, while
  `numbers.sort()` changes the list in place.
- Only the standard library is used (`sys`), so nothing needs to be installed
  before running the file.
- Numbers are printed one per line in item 6 so the list is readable. The full
  list is still printed in items 5 and 7.

## My capstone idea — a second-hand textbook exchange for our campus

Every semester I watch the same thing happen in my dorm. People finish a course,
put the textbook on a shelf, and it never moves again. At the same time the
students one year below us are paying full price for the same book, because the
only place to look is a WeChat group where messages disappear after a week. I
have bought a used book this way myself, and the whole deal happened over six
messages, one blurry photo, and a cash handover in front of the library.

I want to build the thing that WeChat group should have been: a small web app
where a student lists a book once, and buyers can search by course code instead
of scrolling through hundreds of unrelated messages.

It also connects to what I want to do after graduation. I am interested in
back-end work, and this project is small enough that I can actually finish it,
but it still has the parts that matter: accounts, a database, search, and an
upload for photos.

### Who it is for

- **Sellers** — students who just finished a course and want the book out of
  their room, and a little money back.
- **Buyers** — students starting that course next term who would rather pay
  40% of the price than 100%.
- **Course staff** — they get one place to point students at when they ask
  "where do I get this book?"

### What version 1 will do

1. Sign up / sign in with a student e-mail address.
2. Post a book: title, course code, condition, price, and one photo.
3. Search and filter by course code, price range, and condition.
4. A simple message thread so the deal does not have to happen in DMs.
5. Mark a listing as sold, which removes it from search.
6. A small admin page to delete spam listings.

### Planned stack

| Layer | Choice | Why |
| ----- | ------ | --- |
| Front end | HTML + CSS + a little JavaScript | Learn the fundamentals first, no framework yet |
| Back end | Python + Flask | I already know Python, and Flask keeps the routing readable |
| Database | SQLite first, PostgreSQL later | SQLite is one file, so the demo runs anywhere |
| Auth | Flask session + hashed passwords | Straightforward, and I can explain every line |
| Hosting | Render free tier | Enough for a demo and a public link |

### Milestones

- [ ] Week 1 — finish the Python basics (this folder)
- [ ] Week 2 — design the database tables and draw the pages on paper
- [ ] Week 3 — build sign up / sign in
- [ ] Week 4 — build create + list + search for books
- [ ] Week 5 — add the photo upload and the message thread
- [ ] Week 6 — test on my phone, fix the layout, write the report
- [ ] Week 7 — deploy and record the demo

### What could go wrong

- **Nobody posts anything.** A marketplace with no listings is useless, so I
  will pre-seed it with books from my own class and ask two classmates to post.
- **Photo storage fills up.** I will limit the photo size on upload and keep
  only one photo per listing for version 1.
- **My time is short.** Every feature above is cuttable except post and search,
  so there is always a demo-able version.

## Repository layout

```text
Victor_202384014045/
├── README.md                          <- this file
├── VICTOR_CLASS_04_PYTHON_BASICS.py   <- the seven checklist tasks
├── output.txt                         <- the real output of that file
└── docs/
    └── project-overview.md            <- the longer project plan
```

## Links

- Course repository (the one I forked):
  <https://github.com/proxsi/Senior-Capstone-Project>
- Checklist I worked from: `FOR-STUDENTS-WITHOUT-PROJECTS.md`
