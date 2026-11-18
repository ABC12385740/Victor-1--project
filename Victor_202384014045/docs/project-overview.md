# Project Overview — Campus Second-hand Textbook Exchange

**Author:** Victor (202384014045)
**Course:** C-Shaanxi 2026-2027 · SCP — Senior Capstone Project
**Status:** idea + plan, first working version not started yet

## The problem

Textbooks are bought once and used for one semester, then they sit on a shelf.
The students who need that same book next semester are in the same building, but
they have no easy way to find each other:

- the WeChat group scrolls too fast, and old messages are gone in a week;
- the campus notice board is only for *selling*, and there is no search;
- a listing has no course code, so a buyer cannot tell whether the book is the
  right edition for *their* class.

The result: used books stay unused, and the next student pays full price.

## The idea

One small web app where a student posts a book **with its course code**, and the
next student searches by that code and finds it in one step.

The important design choice is the course code. It is what the buyer actually
knows ("I am taking CS203 next term"), and it is what the WeChat group is
missing. Everything else — photos, price, condition — is secondary.

## Who it is for

| User | What they need | What they get |
| ---- | -------------- | ------------- |
| Seller | Get rid of a book fast, get some money back | Post in under a minute, mark as sold |
| Buyer | Find the right book for a specific course | Search by course code, see price and condition |
| Course staff | Stop answering "where do I buy the book?" | One link to share at the start of term |

## User stories

1. As a seller, I want to post a book with a photo so a buyer can judge the
   condition before messaging me.
2. As a buyer, I want to search by course code so I do not buy the wrong edition.
3. As a buyer, I want to filter by price so I do not waste time on books I cannot
   afford.
4. As a seller, I want to mark a book as sold so people stop messaging me.
5. As an admin, I want to hide a spam listing so the list stays useful.

## Version 1 scope (what I will actually build)

| # | Feature | Must have? |
| - | ------- | ---------- |
| 1 | Sign up / sign in with an e-mail address and password | yes |
| 2 | Create a listing: title, course code, condition, price, photo | yes |
| 3 | List + search by course code, sort by price or newest | yes |
| 4 | Listing detail page | yes |
| 5 | Mark listing as sold | yes |
| 6 | Message thread between buyer and seller | nice to have |
| 7 | Admin page to hide spam | nice to have |
| 8 | Payment / delivery | **out of scope** |

Cut line: if I run out of time, features 6 and 7 go, and the app is still a
working marketplace for features 1–5.

## Data model (first draft)

```text
User        id, email, password_hash, display_name, created_at
Listing     id, seller_id, course_code, title, condition, price_cents,
            photo_path, status (open | sold), created_at
Message     id, listing_id, sender_id, body, created_at
```

Two decisions worth writing down:

- **Price in integer cents**, not a float. Floating point money is a classic bug
  and I do not want to explain rounding in the report.
- **`status` instead of deleting a listing.** A sold book should disappear from
  search but stay in the database, so the seller can see their own history.

## Pages

```text
/                 -> list + search (the only page most people use)
/listing/<id>     -> detail + "message seller"
/new              -> create listing (login required)
/mine             -> my listings + mark as sold
/login, /signup   -> auth
```

## Stack and why

| Layer | Choice | Reason |
| ----- | ------ | ------ |
| Back end | Python 3.14 + Flask | Python is the language of this course; Flask keeps routing explicit |
| Templates | Jinja2 (comes with Flask) | No separate front-end build step |
| Front end | Plain HTML / CSS / vanilla JS | One small form and one search box; a framework is overkill |
| Database | SQLite (`sqlite3` module), PostgreSQL later | Zero setup for the demo, and the SQL is the same |
| Auth | Flask session cookie + `werkzeug` password hashing | Understandable, no third-party service |
| Photos | Save to `static/uploads`, store the filename | Simplest thing that works on a free host |
| Hosting | Render free tier | Gives a public URL for the demo |

## Timeline

| Week | Goal | Deliverable |
| ---- | ---- | ----------- |
| 1 | Python basics, install the toolchain | this folder |
| 2 | Schema + page sketches + Flask skeleton | `/` page prints a hard-coded list |
| 3 | Auth | sign up, sign in, sign out working |
| 4 | Listings | create, list, search by course code |
| 5 | Photos + messages | upload works, one thread per listing |
| 6 | Testing + report | fixed bugs, written report, screenshots |
| 7 | Deploy + demo | public URL, 3-minute demo video |

## Risks and what I will do about them

| Risk | Likelihood | Plan |
| ---- | ---------- | ---- |
| Empty marketplace (no listings) | high | Seed with 10 books from my own class before the demo |
| Photo upload abuse / size | medium | Limit to 2 MB, accept only jpg/png, one photo per listing |
| Running out of time | medium | The cut line above; features 1–5 are the demo |
| SQLite on a free host | low | It works on Render; move to PostgreSQL only if needed |
| Losing work | low | Everything in git, committed at the end of each session |

## How I will know it worked

- A classmate who did **not** see me build it can post a book and find it again
  by course code in under two minutes.
- The search returns the right book when I type only the course code.
- `python -m pytest` (or a plain test script) passes for the price formatting and
  the search filter.

## What I want to learn from it

1. How a request actually becomes a page (routing, templates, a database read).
2. How to design a schema that survives a feature change without a rewrite.
3. How to cut a project down when the deadline is closer than the plan.

## Next step

Design the four tables on paper and draw the four pages, before writing any
Flask code. Then build `/` with a hard-coded list, so there is something on
screen on day one.
