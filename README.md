# hermes-the-firm
### *An entire legal practice, stuffed into your computer.*

---

Somewhere right now — it's always right now — a first-year associate is on hour nine of highlighting boxes of documents for a case that will settle anyway. That's called "billable hours." There are entire skyscrapers full of people doing this.

And somewhere else, somebody with a real legal problem — an eviction, a denied claim, a contract written specifically to be misunderstood — is going to type their question into one of those chatty AI helpers. And that helper is going to do what they all do: hem, hedge, apologize, and serve up something that sounds like law but isn't. It read the brochure. It didn't read the law.

**This is the other thing.**

hermes-the-firm is a legal practice — the whole organism — loaded into [Hermes Agent](https://github.com/NousResearch/hermes-agent), an AI that runs on *your* machine and works for *you*. Not a chatbot with a lawyer costume. A firm. With departments, and a library, and rules, and — this is the part nobody else does — the actual text of the actual law, sitting on your disk, quotable.

Here's the breakdown, in plain English:

---

## The five layers (or: how the sausage is legitimately made)

### 1. The lawyers — twelve departments

Commercial contracts. Privacy. Product. Corporate deals. Employment. Litigation. Regulatory. AI governance. IP. Law school. Legal clinics. And a department whose whole job is installing more skills, because even firms need a guy.

Each department comes loaded with real workflows: how to triage an NDA, how to run an investigation, how to draft board minutes, how to not commit malpractice while doing it. Each department also interviews you first — an hour of questions about *your* shop — and then it stops being generic. Forever. Answer the questions once, and every skill in that department works from your playbook, your risk tolerance, your jurisdiction. Skip the interview, and it refuses to guess at you. Imagine that. Software that admits when it doesn't know you.

### 2. The live wires — federal research, on tap

Four connectors you flip on when you want them: the federal regulations (eCFR), the Federal Register (what the government is *doing* this week), CourtListener (case law — the stuff courts actually decided), and govinfo (the official paper trail). These talk straight to the source. No librarian, no login portal, no "seats."

### 3. The vault — the actual law, on disk

This is the one that matters. A project called open-us-law took essentially the entire statutory law of the United States — three million sections, all fifty states, from official government sources — and gave it away. We bolted it in.

So when you ask about, say, **Michigan workers' comp**, this thing doesn't riff. It pulls **MCL 418** — the Workers' Disability Compensation Act — off your own disk and shows you the words. All 40,658 sections of Michigan law are there, verified complete by actual humans who counted. Fifty-one jurisdictions like that.

And here's my favorite part, the part I'd put on the letterhead: the vault keeps a manifest of exactly what's verified and what isn't, and the firm **reads it before it answers**. If a state's law is thin in the collection, it tells you it's thin. It will not dress up a guess as a statute. Most software lies to you politely. This one tattles on itself.

### 4. The rulebook — rules for the robot

A firm needs policies. So there's a layer of skills about the AI itself: a model firm AI policy, privilege handling (what's protected and what only pretends to be), vendor security questionnaires, the anti-patterns that blow up legal teams in production. The machine comes with its own employee handbook. Somebody had to do it.

### 5. The stacks — 1,155 skills, five layers deep

A whole library of craft — 982 skills in the Louis collection alone: drafting agreements, running reviews, simulating opposing counsel, coaching students through IRAC. Built originally with a Middle-East-first lens — Lebanon, Saudi Arabia, UAE, Egypt, the DIFC and ADGM free zones — because most legal AI assumes everybody practices in Delaware. Yours doesn't have to.

And the stacks now reach across the Atlantic without losing the accent. Layer 4 wires you into the live federal machinery — eCFR, the Federal Register, CourtListener's case law, govinfo's paper trail (§2). Layer 5 is the vault: four skills that read the actual statutory law of all fifty states off your own disk — look up a statute, verify a citation round-trip, check what jurisdiction coverage is human-verified before anything quotes it. Michigan to Maine, MENA to federal register. One library, every court that'll have you.

---

## The math

**1,155 skills. Five layers. One command.**

And here's the trick nobody pulls anymore: **it costs nothing until you ask for it.** No background daemon whispering into every conversation. No token tax while you're doing something unrelated. You type `/hermes-the-firm`, you pick a department, and *then* the relevant brains wake up. Everything runs locally. Nothing phones home. Your client's secrets stay in your building — which, in this profession, isn't a feature, it's the bar admission.

## Getting it

```bash
git clone <this-repo> ~/hermes-the-firm
mkdir -p ~/.hermes/plugins
ln -s ~/hermes-the-firm ~/.hermes/plugins/hermes-the-firm
hermes plugins enable hermes-the-firm
```

Restart Hermes. Type `/hermes-the-firm`. Pick a department. Answer its questions honestly — it's the last time it'll ever have to guess about you.

(The multi-gigabyte law vault is a separate download, because we figured you'd rather choose that yourself. One skill walks you through it. Keep reading — it's below.)

## One firm, several offices — installing into a profile

Here's a thing about Hermes nobody warns you about: plugins are discovered **per home**. A profile session looks in its *own* plugin drawer and nowhere else. You installed the firm in your main office? Congratulations — your legal-work profile can't see it. It's not a bug. It's more like each office having its own mail room. Secure, if you enjoy that sort of thing. Annoying, if you just wanted your mail.

So if you run a separate profile for legal work (and you should — you don't wear the same shoes to court and to the beach), you install it twice:

```bash
# 1. hang the firm in that profile's closet
ln -s ~/hermes-the-firm \
      ~/.hermes/profiles/<profile>/plugins/hermes-the-firm

# 2. flip the switch from inside THAT home
HERMES_HOME=~/.hermes/profiles/<profile> hermes plugins enable hermes-the-firm
```

When it asks about replacing built-in tools, say **N**. This plugin registers one command and read-only skills. It doesn't want your tools. It wants to work.

Then restart any sessions already running under that profile — discovery happens at session start, not mid-sentence. And since every skill is explicit-load, enabling costs nothing until you actually ask for the firm. Same trick as before. Free until used. Radical concept.

## Stocking the vault — pulling the law off Hugging Face

Remember the vault? The actual law, on disk? Here's where it comes from, and here's how you go get it yourself, because depending on somebody else's download button is how you end up with somebody else's rules.

The whole corpus lives on [Hugging Face](https://huggingface.co/datasets/vaquill/open-us-law) as parquet files — one file per state, one per topic. `us_mi_statutes.parquet` is Michigan's entire statutory code. Twenty megabytes. The state of Michigan charges law publishers money for this. Vaquill gives it away. Pick whichever business model smells better to you.

First, get yourself an account token and do this once:

```bash
hf auth login
```

That's it. That's authentication. No SSO portal. No "verify you are not a law firm."

Now — and this is the part I want you to actually hear — **you don't have to download all of it.** Three and a half gigabytes of law sounds impressive at parties, but the federal regulations alone are 2.7 gigs of that (the CFR is *enormous*, which tells you something about what your government has been up to). If you practice in Michigan and occasionally touch federal employment law, grab exactly that:

```bash
# everything for one state
hf download vaquill/open-us-law --repo-type dataset \
    us_mi_statutes.parquet us_mi_constitutions.parquet \
    us_mi_court_rules.parquet us_mi_guidance.parquet \
    --local-dir ~/hermes-the-firm/data/

# plus the federal statutes (ADA, FMLA — the usual suspects)
hf download vaquill/open-us-law --repo-type dataset \
    us_federal_statutes.parquet us_federal_constitutions.parquet \
    us_federal_court_rules.parquet \
    --local-dir ~/hermes-the-firm/data/
```

Swap `<state postal code>` into those filenames for any other state. Want everything? Drop the filenames and it'll pull the whole shelf. Your disk, your funeral, your three million sections.

Two pieces of housekeeping that separate adults from tourists:

1. **Verify what you downloaded.** The repo ships a `SHA256SUMS.json` — a manifest of checksums, which is a fancy way of saying "the seller keeps a receipt." Check yours against theirs:

```bash
python3 tools/verify-corpus.py --data-dir ~/projects/open-us-law/data/
```

(That tool ships with this repo — no other checkout needed. Point `--data-dir` wherever you pulled the files. Want to prove a specific citation actually resolves before you rely on it? Add `--cite "MCL 418"` and it'll count the sections.)

If a hash doesn't match, the file changed somewhere between Virginia and your disk, and you do NOT want to cite a statute that got mangled in transit. This is legal work. Trust, but verify the checksum.

2. **Don't commit the data.** It's public-domain law; the repo is for code. The data directory stays local, like good silverware.

And that's the whole ceremony. `hf auth login` once, `hf download` with the files you want, verify against the manifest. The entire statutory law of the United States, delivered to your machine, for free, in about the time it takes to explain to a client why their invoice has four decimal points on it.

## The fine print, in large type

This is a practice, not a license. (The license is Apache-2.0 — see LICENSE.) It drafts, it checks, it verifies citations against primary sources, it flags what needs a human eyeball. It does not replace your lawyer, your judgment, or your jurisdiction's bar exam. It makes the person using it dangerous — in the good way.

Built by standing on some tall shoulders: Anthropic's claude-for-legal (Apache-2.0), Vaquill's open-us-law corpus (CC BY 4.0 — data wants to be free, and here, it finally is), Beshkenadze's us-legal-tools (MIT), and HAQQ Legal AI's master and mini packs (MIT). Ported to Hermes by rJ9. Licenses and attributions live in THIRD-PARTY-NOTICES.md, because credit is another thing that shouldn't be paywalled.

---

*It's pronounced "Hermes: The Firm." Like the movie. Like Kermit. Say it out loud once and you'll never call it anything else.*
