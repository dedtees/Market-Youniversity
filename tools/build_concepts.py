#!/usr/bin/env python3
"""Generates the static homepage concept pages for Market Youniversity."""
import os, sys

ROOT = sys.argv[1]

CONCEPTS = [
    ("concept-1", "1 · Two doors"),
    ("concept-2", "2 · Own the room"),
    ("concept-3", "3 · Your training team"),
    ("concept-4", "4 · Learning path"),
]

LOCK = '<svg viewBox="0 0 24 24" aria-label="locked"><path d="M17 9h-1V7a4 4 0 0 0-8 0v2H7a2 2 0 0 0-2 2v9a2 2 0 0 0 2 2h10a2 2 0 0 0 2-2v-9a2 2 0 0 0-2-2Zm-7-2a2 2 0 0 1 4 0v2h-4Z"/></svg>'

def head(title, desc):
    return f"""<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{title}</title>
<meta name="description" content="{desc}">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Roboto+Slab:wght@500;700;800&family=Roboto:wght@400;500;700&display=swap" rel="stylesheet">
<link rel="stylesheet" href="/assets/site.css">
</head>
<body>
"""

HEADER = """<header class="site-header">
  <div class="wrap">
    <a class="logo" href="#top" aria-label="Market Youniversity home"><b>MARKET</b><span><em>You</em>niversity</span></a>
    <button class="menu-toggle" aria-label="Menu" onclick="document.querySelector('.nav').classList.toggle('open')">Menu</button>
    <nav class="nav">
      <a href="#individuals">For Individuals</a>
      <a href="#organizations">For Organizations</a>
      <a href="#community">Community</a>
      <a href="#about">About</a>
      <a class="btn btn-primary" href="#contact">Talk to us</a>
    </nav>
  </div>
</header>
<main id="top">
"""

def footer(current):
    links = "".join(
        f'<a href="/{slug}/" class="{"on" if slug == current else ""}">{name}</a>'
        for slug, name in CONCEPTS
    )
    return f"""</main>
<footer class="site-footer" id="about">
  <div class="wrap">
    <div class="footer-grid">
      <div>
        <a class="logo" href="#top" style="color:#fff"><b>MARKET</b><span><em style="color:#9fb6ff">You</em>niversity</span></a>
        <p style="margin-top:16px">Presentation, facilitation and workplace training for individuals and organizations. Based in Colonia, NJ.</p>
        <form class="newsletter" onsubmit="return false">
          <input type="email" placeholder="Email address" aria-label="Email address">
          <button class="btn btn-green" type="submit">Get updates</button>
        </form>
        <p class="small" style="margin-top:8px">Be first to hear about new workshop dates and courses.</p>
      </div>
      <div>
        <h4>Market Youniversity</h4>
        <ul>
          <li><a href="#individuals">For individuals</a></li>
          <li><a href="#organizations">For organizations</a></li>
          <li><a href="#community">Community</a></li>
          <li><a href="#contact">Contact</a></li>
        </ul>
      </div>
      <div>
        <h4>Our family of companies</h4>
        <ul>
          <li><a href="https://pinpointmypromotions.com" target="_blank" rel="noopener">Pinpoint Promotions &amp; Marketing</a><br><span class="small">Branding and marketing</span></li>
          <li><a href="#">Eric Duchin Consulting</a><br><span class="small">Business consulting</span></li>
        </ul>
      </div>
    </div>
    <div class="footer-base"><span>&copy; 2026 Market Youniversity</span><span>Colonia, NJ</span></div>
  </div>
</footer>
<div class="concept-bar" role="navigation" aria-label="Homepage concepts"><span>Concepts</span><a href="/">All</a>{links}</div>
</body>
</html>
"""

CLIENTS = """<section class="section tight">
  <div class="wrap">
    <p class="clients-label">{label}</p>
    <div class="clients"><span>Regeneron</span><span>BCB Bank</span><span>GS1</span></div>
  </div>
</section>
"""

def courses(heading_html, intro):
    return f"""<section class="section" id="individuals">
  <div class="wrap">
    <span class="eyebrow">For individuals</span>
    {heading_html}
    <p class="lead">{intro}</p>
    <div class="grid-3" style="margin-top:32px">
      <article class="card course">
        <span class="tag">Live · 1 day</span>
        <h3>Pitch Perfect Presentations</h3>
        <p>One focused day to build a clear, confident presentation you can deliver anywhere. Built for teams at Regeneron and BCB Bank who needed results fast.</p>
        <div class="meta"><div>Next session<strong>Colonia, NJ · dates soon</strong></div><a class="btn btn-ghost" href="#contact">Join the list</a></div>
      </article>
      <article class="card course big">
        <span class="tag">Live · 2 days · video-recorded</span>
        <h3>Powerful Presentations</h3>
        <p>Two days. Several presentations each. Every one recorded and reviewed with feedback from the room. The fastest way to see yourself the way your audience does.</p>
        <div class="meta"><div>Next session<strong>Colonia, NJ · dates soon</strong></div><a class="btn btn-ghost" href="#contact">Join the list</a></div>
      </article>
      <article class="card">
        <span class="tag soon">Coming soon</span>
        <h3>Self-paced courses</h3>
        <p>Learn the same methods on your own schedule, then bring your practice talks to the community for feedback.</p>
        <div class="meta"><div>Online<strong>Get notified at launch</strong></div><a class="btn btn-ghost" href="#contact">Notify me</a></div>
      </article>
    </div>
  </div>
</section>
"""

ENGAGEMENTS = """<div class="grid-3" style="margin-top:32px">
      <article class="card"><span class="tag org">Workshops</span><h3>Workshops for your team</h3><p>Pitch Perfect, Powerful Presentations or another program, delivered privately for your people, on site or online.</p></article>
      <article class="card"><span class="tag org">Extended team</span><h3>Your extra training team</h3><p>Launching a product or updating material and your trainers are stretched? We work beside them to build and deliver it, as we do for GS1.</p></article>
      <article class="card"><span class="tag org">Custom programs</span><h3>Custom program design</h3><p>Needs assessment, curriculum, facilitator guides and onboarding, built around your goals from a blank page.</p></article>
    </div>"""

CHEVRONS = """<div class="chevrons">
      <div class="chev c1"><b>Analyze</b><small>Find the real skill gap</small></div>
      <div class="chev c2"><b>Design</b><small>Plan the learning</small></div>
      <div class="chev c3"><b>Develop</b><small>Build the material</small></div>
      <div class="chev c4"><b>Implement</b><small>Deliver and coach</small></div>
      <div class="chev c5"><b>Evaluate</b><small>Measure what stuck</small></div>
    </div>"""

TOPICS = """<div class="pills">
      <span class="pill">Presentation skills</span><span class="pill">Facilitation and train-the-trainer</span><span class="pill">Leadership</span><span class="pill">Customer service</span><span class="pill">Sales and marketing communication</span><span class="pill">Branding</span><span class="pill">Onboarding and SOP training</span>
    </div>
    <p class="small muted" style="margin-top:12px">Don't see your topic? Ask us. We build new programs all the time.</p>"""

def discord(active="eye-contact"):
    def ch(name, state):
        cls = {"on": "ch on", "open": "ch", "locked": "ch locked"}[state]
        icon = LOCK if state == "locked" else ""
        return f'<div class="{cls}"><span># {name}</span>{icon}</div>'
    return f"""<div class="discord" aria-label="Preview of the Market Youniversity Discord">
        <div class="server">Market Youniversity Community</div>
        <div class="group">Open to everyone</div>
        {ch("welcome", "open")}{ch("ask-a-coach", "open")}{ch("upcoming-workshops", "open")}
        <div class="group">Unlocked with a course</div>
        {ch("eye-contact", "on")}{ch("voice-and-pace", "locked")}{ch("structure", "locked")}{ch("handling-q-and-a", "locked")}
        <div class="group">Unlocked when you finish</div>
        {ch("showcase", "locked")}{ch("alumni", "locked")}
      </div>"""

def community(title, text):
    return f"""<section class="section alt" id="community">
  <div class="wrap hero-grid">
    <div>
      <span class="eyebrow">Community</span>
      <h2>{title}</h2>
      <p class="lead">{text}</p>
      <ul class="ticks">
        <li>Upload a practice talk and get feedback from coaches and peers</li>
        <li>New skill channels, like Eye Contact, unlock as you take and finish courses</li>
        <li>Stay sharp between workshops with people working on the same thing</li>
      </ul>
      <a class="btn btn-primary" href="#">Join the Discord free</a>
    </div>
    {discord()}
  </div>
</section>
"""

TESTIMONIAL = """<section class="section band-grad">
  <div class="wrap center">
    <p class="quote">"I used to dread public speaking. The techniques were practical, the sessions were engaging, and I recently got a standing ovation at work."</p>
    <p class="quote-by">Participant name, role, company</p>
    <span class="placeholder-note">Placeholder: replace with a real testimonial</span>
  </div>
</section>
"""

def family(title="Need more than training?"):
    return f"""<section class="section">
  <div class="wrap">
    <h2 class="center">{title}</h2>
    <p class="lead center">Market Youniversity is one of three companies working together. When the need is bigger than training, we bring in the right team.</p>
    <div class="family" style="margin-top:32px">
      <article class="card here"><span class="tag">You are here</span><h3>Market Youniversity</h3><p>Training for individuals and organizations.</p></article>
      <article class="card"><span class="tag">Branding</span><h3>Pinpoint Promotions &amp; Marketing</h3><p>Build the brand and marketing your people are trained to deliver.</p><a href="https://pinpointmypromotions.com" target="_blank" rel="noopener">pinpointmypromotions.com</a></article>
      <article class="card"><span class="tag">Consulting</span><h3>Eric Duchin Consulting</h3><p>Strategy and business consulting when you need help beyond training.</p><a href="#">Visit Eric Duchin Consulting</a></article>
    </div>
  </div>
</section>
"""

def contact(title, text):
    return f"""<section class="section alt" id="contact">
  <div class="wrap hero-grid">
    <div>
      <span class="eyebrow">Talk to us</span>
      <h2>{title}</h2>
      <p class="lead">{text}</p>
    </div>
    <form class="form form-card" onsubmit="return false">
      <h3>Book a free consultation</h3>
      <label>Name<input type="text" autocomplete="name"></label>
      <label>Email<input type="email" autocomplete="email"></label>
      <label>Company (optional)<input type="text" autocomplete="organization"></label>
      <label>I'm interested in
        <select><option>A workshop for myself</option><option>Training for my team</option><option>Help building a training program</option><option>Something else</option></select>
      </label>
      <button class="btn btn-green" type="submit">Send</button>
    </form>
  </div>
</section>
"""

def org_section(eyebrow_h2, intro, extra=""):
    return f"""<section class="section alt" id="organizations">
  <div class="wrap">
    <span class="eyebrow">For organizations</span>
    {eyebrow_h2}
    <p class="lead">{intro}</p>
    {ENGAGEMENTS}
    <h3 style="margin-top:56px">How we work</h3>
    {CHEVRONS}
    <h3 style="margin-top:56px">What we train</h3>
    {TOPICS}
    {extra}
    <div class="btn-row"><a class="btn btn-primary" href="#contact">Book a free consultation</a></div>
  </div>
</section>
"""

# ---------------- Concept 1: Two doors ----------------
c1 = head("Market Youniversity · Concept 1: Two doors", "Training for people who present and teams that perform.") + HEADER + """
<section class="hero">
  <div class="wrap center">
    <span class="eyebrow">Presentation and workplace training</span>
    <h1>Training for people who present<br>and teams that perform.</h1>
    <p class="lead">Build your own skills in a live workshop, or bring us in to train your whole team. Choose your door.</p>
    <div class="doors" style="text-align:left">
      <a class="door ind" href="#individuals">
        <span class="eyebrow">For individuals</span>
        <h3>I'm building my own skills</h3>
        <ul><li>Live presentation workshops in Colonia, NJ</li><li>A free community for practice and feedback</li><li>Self-paced courses, coming soon</li></ul>
        <span class="go">Explore courses &rarr;</span>
      </a>
      <a class="door org" href="#organizations">
        <span class="eyebrow" style="color:var(--magenta)">For organizations</span>
        <h3>I'm training a team</h3>
        <ul><li>Private workshops for your people</li><li>An extra training team when yours is stretched</li><li>Custom programs built from scratch</li></ul>
        <span class="go" style="color:var(--magenta)">See how we work &rarr;</span>
      </a>
    </div>
  </div>
</section>
""" + CLIENTS.format(label="Trusted by teams at") + courses(
    '<h2>Want to be a <span class="strike">good</span> great presenter?</h2>',
    "Good presenters get their message across. Great presenters connect, persuade and move people to act. Learn how in a day, in a two-day workshop, or soon at your own pace.",
) + org_section(
    "<h2>Your training team, without the hiring.</h2>",
    "We design, build and deliver training that sticks, from one-day workshops to full programs, working beside your people or in their place.",
) + community("Keep practicing after the workshop ends.", "Our Discord is where participants share practice talks, get feedback and keep improving together.") + TESTIMONIAL + family() + contact(
    "Not sure where to start?", "Tell us what you or your team need. We'll recommend the right workshop or program, no strings attached."
) + footer("concept-1")

# ---------------- Concept 2: Own the room ----------------
skills = """<section class="section">
  <div class="wrap">
    <span class="eyebrow">What you'll learn</span>
    <h2>What great presenters do differently</h2>
    <div class="grid-4" style="margin-top:32px">
      <article class="card"><h3>Structure</h3><p>A message people remember, built around what your audience needs to hear.</p></article>
      <article class="card"><h3>Eye contact</h3><p>Connect with one person at a time so the whole room feels spoken to.</p></article>
      <article class="card"><h3>Voice and pace</h3><p>Use pauses, volume and pace to keep attention and land your key points.</p></article>
      <article class="card"><h3>Handling Q&amp;A</h3><p>Stay calm and credible when the questions get tough.</p></article>
    </div>
  </div>
</section>
"""
team_band = """<section class="section alt" id="organizations">
  <div class="wrap hero-grid">
    <div>
      <span class="eyebrow">For organizations</span>
      <h2>Bring the workshop to your team.</h2>
      <p class="lead">Regeneron, BCB Bank and GS1 have trusted us to train their people. We run private sessions on site or online, and build training beyond presentations when you need it.</p>
      <div class="btn-row"><a class="btn btn-primary" href="#contact">Plan a team workshop</a></div>
    </div>
    <div>
      <h3>More than presentations</h3>
      """ + TOPICS + """
      <h3 style="margin-top:32px">Need a whole training team?</h3>
      <p class="muted">When your trainers are stretched, we step in to build and deliver material beside them, like we do for GS1.</p>
    </div>
  </div>
</section>
"""
c2 = head("Market Youniversity · Concept 2: Own the room", "Presentation skills training for individuals and teams.") + HEADER + """
<section class="hero hero-dark">
  <div class="wrap hero-grid">
    <div>
      <span class="eyebrow">Presentation skills training</span>
      <h1>Want to be a <span class="strike" style="color:#8f9bd0">good</span> great presenter?</h1>
      <p class="lead">For years we've trained professionals at Regeneron, BCB Bank and more to present with clarity and confidence. Join a public workshop, or bring it to your team.</p>
      <div class="btn-row"><a class="btn btn-green" href="#individuals">See upcoming workshops</a><a class="btn btn-white" href="#organizations">Bring it to my team</a></div>
    </div>
    <div class="card" style="color:var(--ink)">
      <span class="tag">Good vs great</span>
      <p><strong>Good presenters</strong> get their message across, leave a mark and speak clearly.</p>
      <p><strong>Great presenters</strong> connect deeply, spark emotion and inspire action.</p>
      <p class="muted small" style="margin:0">We teach the difference.</p>
    </div>
  </div>
</section>
""" + CLIENTS.format(label="Trusted by teams at") + skills + courses(
    "<h2>Two ways to train live</h2>",
    "Every workshop is hands-on. You present, you get feedback, you present again.",
) + team_band + community("Your practice room between workshops.", "Join the Discord to share talks, get feedback and unlock new skill channels as you learn.") + TESTIMONIAL + family() + contact(
    "Ready to own the room?", "Join the list for the next workshop in Colonia, NJ, or ask about a private session for your team."
) + footer("concept-2")

# ---------------- Concept 3: Your training team ----------------
pains = """<section class="section">
  <div class="wrap">
    <span class="eyebrow">Sound familiar?</span>
    <h2>When training can't wait, we step in.</h2>
    <div class="grid-3" style="margin-top:32px">
      <article class="card"><h3>A launch is coming</h3><p>A new product or process is rolling out and the training material isn't ready.</p></article>
      <article class="card"><h3>Your trainers are stretched</h3><p>Your team knows the content but doesn't have the hours to build and deliver it all.</p></article>
      <article class="card"><h3>A skill gap needs closing</h3><p>Managers need presentation, facilitation or customer service skills, and they need them this quarter.</p></article>
    </div>
  </div>
</section>
"""
case = """<div class="card" style="margin-top:40px;border-left:6px solid var(--magenta)">
      <span class="tag org">Client story</span>
      <h3>GS1: extra hands for a product launch</h3>
      <p>GS1 was releasing a new product and needed updated training material. Their training staff was on it but needed help, so we joined as an extension of their team to build and update the material with them.</p>
    </div>"""
indiv_band = """<section class="section" id="individuals">
  <div class="wrap hero-grid">
    <div>
      <span class="eyebrow">For individuals</span>
      <h2>Building your own skills?</h2>
      <p class="lead">Our public presentation workshops are open to anyone. Join Pitch Perfect (1 day) or Powerful Presentations (2 days, video-recorded) in Colonia, NJ.</p>
      <div class="btn-row"><a class="btn btn-primary" href="#contact">Get workshop dates</a><a class="btn btn-ghost" href="#community">Join the free community</a></div>
    </div>
    <div class="grid-2">
      <article class="card course"><span class="tag">1 day</span><h3>Pitch Perfect Presentations</h3><p>One focused day to build a clear, confident presentation.</p></article>
      <article class="card course big"><span class="tag">2 days</span><h3>Powerful Presentations</h3><p>Present several times, on video, with feedback from the room.</p></article>
    </div>
  </div>
</section>
"""
c3 = head("Market Youniversity · Concept 3: Your training team", "Outsourced training for organizations, plus public presentation workshops.") + HEADER + """
<section class="hero hero-grad">
  <div class="wrap hero-grid">
    <div>
      <span class="eyebrow">Outsourced training for organizations</span>
      <h1>Your training team, without the hiring.</h1>
      <p class="lead">We design, build and deliver training that sticks, working beside your trainers or in their place. Trusted by Regeneron, BCB Bank and GS1.</p>
      <div class="btn-row"><a class="btn btn-white" href="#contact">Book a free consultation</a></div>
      <p class="small" style="margin-top:16px">Looking for a course for yourself? <a href="#individuals" style="color:#fff;font-weight:700">See public workshops</a></p>
    </div>
    <div class="card" style="color:var(--ink)">
      <h3>What we train</h3>
      <ul class="ticks">
        <li>Presentation skills</li><li>Facilitation and train-the-trainer</li><li>Leadership</li><li>Customer service</li><li>Branding and marketing communication</li><li>Onboarding and SOP training</li>
      </ul>
    </div>
  </div>
</section>
""" + CLIENTS.format(label="Trusted by teams at") + pains + org_section(
    "<h2>Three ways to work with us</h2>",
    "Start with a single workshop or hand us the whole program. Either way you get a proven process and trainers who have done this for years.",
    case,
) + indiv_band + community("A community for the people you train.", "Participants keep practicing in our Discord after the workshop, so the skills stick long after the session ends.") + TESTIMONIAL + family() + contact(
    "Let's talk about your team.", "Tell us what's coming up and who needs training. We'll come back with a plan."
) + footer("concept-3")

# ---------------- Concept 4: Learning path ----------------
path = """<section class="section" id="individuals">
  <div class="wrap">
    <span class="eyebrow">Your path</span>
    <h2>Start free. Go as far as you want.</h2>
    <p class="lead">Every step builds on the last, and each one opens new channels in the community.</p>
    <div class="ladder" style="margin-top:32px">
      <div class="rung"><div><h3>Join the community</h3><p>Free. Meet other learners, ask a coach, see upcoming workshops.</p></div><a class="btn btn-ghost" href="#community">Join free</a></div>
      <div class="rung"><div><h3>Learn at your own pace <span class="tag soon" style="margin:0 0 0 8px">Coming soon</span></h3><p>Self-paced lessons on structure, eye contact, voice and Q&amp;A.</p></div><a class="btn btn-ghost" href="#contact">Notify me</a></div>
      <div class="rung"><div><h3>Pitch Perfect Presentations</h3><p>One live day in Colonia, NJ. Build and deliver a clear, confident presentation.</p></div><a class="btn btn-ghost" href="#contact">Get dates</a></div>
      <div class="rung"><div><h3>Powerful Presentations</h3><p>Two live days. Present several times on video with feedback from the room.</p></div><a class="btn btn-primary" href="#contact">Get dates</a></div>
    </div>
  </div>
</section>
"""
starts = """<div class="grid-3" style="margin-top:40px;text-align:left">
      <a class="door ind" href="#individuals"><h3>I have a big presentation coming up</h3><p class="muted">Get ready fast with a one-day workshop.</p><span class="go">Pitch Perfect &rarr;</span></a>
      <a class="door ind" href="#individuals"><h3>I want to become a confident presenter</h3><p class="muted">Build lasting skill with practice and video feedback.</p><span class="go">Powerful Presentations &rarr;</span></a>
      <a class="door org" href="#organizations"><h3>My team needs training</h3><p class="muted">Workshops, custom programs or an extra training team.</p><span class="go" style="color:var(--magenta)">For organizations &rarr;</span></a>
    </div>"""
c4 = head("Market Youniversity · Concept 4: Learning path", "Learn it. Practice it. Own the room.") + HEADER + """
<section class="hero">
  <div class="wrap center">
    <span class="eyebrow">A training hub for presenters and teams</span>
    <h1>Learn it. Practice it. Own the room.</h1>
    <p class="lead">Start free in our community, go deeper in a live workshop, and keep improving with people working on the same skills.</p>
    <h3 style="margin-top:40px">Where are you starting?</h3>
    """ + starts + """
  </div>
</section>
""" + CLIENTS.format(label="Our workshops have trained teams at") + path + community(
    "Skills unlock as you grow.", "Our Discord is the practice room. Finish a course and new channels open, like Eye Contact and Showcase, where you post a talk and get coached."
) + org_section(
    "<h2>Training your whole team?</h2>",
    "Bring the workshops in-house, or hire us as your training team for presentation, facilitation, leadership, customer service and more.",
) + TESTIMONIAL + family() + contact(
    "Questions about where to start?", "Tell us your goal and we'll point you to the right step."
) + footer("concept-4")

pages = {"concept-1": c1, "concept-2": c2, "concept-3": c3, "concept-4": c4}
for slug, html in pages.items():
    os.makedirs(os.path.join(ROOT, slug), exist_ok=True)
    with open(os.path.join(ROOT, slug, "index.html"), "w") as f:
        f.write(html)

# ---------------- Index: compare concepts ----------------
rows = [
    ("concept-1", "Two doors", "Training for people who present and teams that perform.", "Both audiences equally. The hero asks visitors to pick a door.", "Clearest split between individuals and organizations."),
    ("concept-2", "Own the room", "Want to be a good great presenter?", "Presentation skills first, for individuals and teams.", "Strongest emotional hook. Other topics sit lower on the page."),
    ("concept-3", "Your training team", "Your training team, without the hiring.", "Organizations first. Individuals get a smaller section.", "Best if most revenue will come from corporate work."),
    ("concept-4", "Learning path", "Learn it. Practice it. Own the room.", "A hub: free community, then workshops, step by step.", "Best showcases Discord and the future self-paced courses."),
]
cards = "".join(f"""
      <a class="door {'org' if slug == 'concept-3' else 'ind'}" href="/{slug}/">
        <span class="eyebrow">Concept {slug[-1]}</span>
        <h3>{name}</h3>
        <p class="slab" style="font-size:1.15rem">"{headline}"</p>
        <p class="muted"><strong>Leads with:</strong> {leads}</p>
        <p class="muted"><strong>Why pick it:</strong> {why}</p>
        <span class="go">Open concept &rarr;</span>
      </a>""" for slug, name, headline, leads, why in rows)
index = head("Market Youniversity · Homepage concepts", "Four homepage concepts for the new Market Youniversity.") + f"""
<main>
<section class="hero">
  <div class="wrap">
    <span class="eyebrow">Market Youniversity · for review</span>
    <h1>Four homepage concepts</h1>
    <p class="lead">Same site structure, four different ways to position it. Open each one, then tell us which headline and order feels right. Pieces can be mixed.</p>
    <div class="doors" style="grid-template-columns:repeat(auto-fit,minmax(260px,1fr))">{cards}
    </div>
    <p class="small muted" style="margin-top:32px">Placeholders: prices and dates are not set, testimonials are samples, forms don't send yet, and the Eric Duchin Consulting link needs its URL.</p>
  </div>
</section>
</main>
</body>
</html>
"""
with open(os.path.join(ROOT, "index.html"), "w") as f:
    f.write(index)
print("built")
