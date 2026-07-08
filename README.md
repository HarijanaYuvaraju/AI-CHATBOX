# Password Strength Analyzer

A browser-based tool that evaluates the strength of a password in real time and suggests stronger alternatives. Built with plain HTML, CSS, and JavaScript — no frameworks, no backend, no dependencies.

## Live Demo
Open `index.html` in any browser, or enable GitHub Pages on this repo to get a live link.

## Features

- **Real-time checklist** — checks password length, uppercase/lowercase mix, digits, symbols, repeated or sequential characters (e.g. `aaa`, `123`), and matches against a list of commonly leaked passwords.
- **Strength dial** — visual score (0–100) with a strength label (Very Weak → Very Strong), estimated entropy in bits, and an estimated crack time.
- **Stronger password suggestions** — one button patches the current password with missing character types; another generates a random passphrase (e.g. `Copper-Willow-Harbor-Ember42!`).
- **Reuse check (session-only)** — a lightweight "vault" that remembers passwords entered during the current browser session and flags duplicates. This simulates the "prevent reuse of old passwords" requirement without needing a real database or backend.

## How It Works

- **Entropy estimate**: `E = L × log2(N)`, where `L` is password length and `N` is the size of the character set used (lowercase ≈26, uppercase ≈26, digits ≈10, symbols ≈32).
- **Crack time estimate**: assumes an attacker can attempt 10 billion guesses/second against an offline, unsalted hash — a common worst-case benchmark used in password strength tools.
- **Penalties**: passwords matching a known leaked-password list, or containing repeated/sequential runs, have their entropy score reduced, since attackers try these patterns first.

## Why No Real Database?

This is a static, client-side tool (HTML/CSS/JS only), so there's no backend to store password history. The reuse check uses in-memory JavaScript state to simulate the concept — it resets when the page is reloaded. A production version would replace this with a server storing **salted hashes** of previous passwords (never plaintext) and comparing new submissions against that hash history.

## Tech Stack

- HTML5
- CSS3 (no frameworks)
- Vanilla JavaScript (no libraries)
- Fonts: Fraunces, Inter, IBM Plex Mono (via Google Fonts)

## What I Learned

- How password entropy is calculated and why character variety matters more than simple length alone.
- Why passphrases can offer better security-to-memorability trade-offs than complex short passwords.
- Basic principles of secure password storage (hashing + salting) and why plaintext reuse-checking is a bad practice.

## Run Locally

No build step required. Just download `index.html` and open it in a browser.
