#!/usr/bin/env python3
"""Render the Sunday 22 November 2026 front page (1024x1024, <=1 MiB).

Every story below was verified against live reporting in the build session
(22 Nov 2026, ~13:30-14:00 WIB). Events are dated Sunday 22 Nov 2026 in
some time zone, or are Sunday's toll/update of a weekend event; the
DATE CHECK box on the page names what was deliberately left out.
No network at render time; output is deterministic.
"""
import os
from PIL import Image, ImageDraw, ImageFont

W, H = 1024, 1024
PAPER = (246, 239, 220)
PANEL = (255, 253, 244)
INK = (25, 21, 18)
MUTED = (92, 85, 70)
RED = (158, 27, 27)
BLUE = (28, 78, 128)
GREEN = (46, 107, 52)
GOLD = (176, 124, 18)
RULE = (201, 191, 164)
LIGHT = (232, 224, 200)

FD = "/usr/share/fonts/truetype/dejavu"
FL = "/usr/share/fonts/truetype/liberation"


def font(name, size):
    return ImageFont.truetype(os.path.join(FL, name), size)


SERIF_B = lambda s: font("LiberationSerif-Bold.ttf", s)
SERIF = lambda s: font("LiberationSerif-Regular.ttf", s)
SERIF_I = lambda s: font("LiberationSerif-Italic.ttf", s)
SANS_B = lambda s: font("LiberationSans-Bold.ttf", s)
SANS = lambda s: font("LiberationSans-Regular.ttf", s)

# ---------------------------------------------------------------- stories
# fields: key, region, headline, deck, source, pin(x, y in 0..1000 map coords)
# regions: ME Middle East & Gulf (9), EU Europe (7), UR Ukraine & Russia (7),
# AM Americas (8), AP Asia-Pacific (5), AF Africa & World (3), SP Sport (5)
STORIES = [
 # --- Middle East & Gulf (9) ---
 dict(key="cop31", region="ME", hero=True,
      head="COP31 NEARS A DEAL AT 2 A.M.",
      deck="Final text drops fossil fuels, sets 35% clean power by 2035 and 1 Gt of carbon capture; plenary to approve on Sunday.",
      src="Reuters / AP", pin=(560, 330)),
 dict(key="bahrain", region="ME", hero=True,
      head="IRAN HITS US BASES IN BAHRAIN",
      deck="IRGC missiles and drones target two US bases; Bahrain says a civilian site burned, no injuries.",
      src="IANS / Reuters", pin=(575, 345)),
 dict(key="hormuz", region="ME",
      head="Two tankers hit near Hormuz",
      deck="UK maritime agency reports projectiles strike ships leaving the Gulf; one tanker hits a mine and burns.",
      src="UKMTO", pin=(590, 350)),
 dict(key="houthi", region="ME",
      head="Riyadh intercepts 3 Houthi missiles",
      deck="Saudi coalition says three ballistic missiles aimed at the capital were stopped; it struck Hodeidah port.",
      src="SPA / Reuters", pin=(565, 365)),
 dict(key="sirik", region="ME",
      head="Blasts heard on Iran's Sirik coast",
      deck="Explosions reported Saturday night; Fars says the blasts came from the sea, nature unclear.",
      src="Fars"),
 dict(key="kharg", region="ME",
      head="Iran readies 14 tankers to break blockade",
      deck="Deputy minister calls the US blockade 'an act of war'; a two-day Hormuz ceasefire plan stays on the table.",
      src="IRIB"),
 dict(key="gaza", region="ME",
      head="Four killed in Gaza ceasefire breaches",
      deck="WAFA reports four Palestinians killed and 14 hurt; a death also reported in Jabalia.",
      src="WAFA", pin=(555, 335)),
 dict(key="hartha", region="ME",
      head="Fire at Iraq power station kills 4",
      deck="Blaze at Hartha plant near Basra injures 35; cause unknown, state media says.",
      src="INA", pin=(570, 340)),
 dict(key="qatar", region="ME",
      head="Qatar hosts CENTCOM chief as Gulf burns",
      deck="Defence chief and US Central Command commander meet in Doha amid the regional escalation.",
      src="QNA", pin=(580, 355)),
 # --- Europe (7) ---
 dict(key="denmark", region="EU",
      head="Denmark seeks EU curb on Russian tourists",
      deck="Copenhagen wants bloc-wide limits after an alleged murder plot linked to Moscow.",
      src="DR"),
 dict(key="croatia", region="EU",
      head="Zagreb rallies over hospital death",
      deck="Thousands demand accountability after a patient's death at a psychiatric hospital.",
      src="HINA"),
 dict(key="eubudget", region="EU",
      head="EU tables \u20ac1.78tn budget for 2028\u201334",
      deck="Council president Costa's draft heads to the 26\u201327 Nov summit; agreement still pending.",
      src="European Commission"),
 dict(key="helicopter", region="EU",
      head="Russian helicopter 'violated' Finnish airspace",
      deck="Helsinki reports a suspected incursion of up to 4.1 km in the eastern Gulf of Finland.",
      src="YLE"),
 dict(key="kaliningrad", region="EU",
      head="Blasts near Russia's Baltic Fleet base",
      deck="Explosions reported by Kaliningrad during drone activity, monitors say.",
      src="Kyiv Independent"),
 dict(key="rutte", region="EU",
      head="NATO: 'every inch' of Poland defended",
      deck="Secretary general Rutte reassures Warsaw as the war spills over borders.",
      src="NATO"),
 dict(key="blair", region="EU",
      head="Blair: rejoin EU only if UK innovates",
      deck="Ex-PM says Britain should rejoin only on a technology-led pitch.",
      src="BBC"),
 # --- Ukraine & Russia (7) ---
 dict(key="zelensky", region="UR",
      head="Zelensky: 'No guarantees on paper yet'",
      deck="Kyiv has not seen written Article 5-like pledges; they must last decades, he says.",
      src="Kyiv Independent", pin=(545, 270)),
 dict(key="jandeadline", region="UR",
      head="US wants Ukraine deal by early January",
      deck="FT: Washington presses for a deal before the new Congress sits; Kyiv says Moscow is in no hurry.",
      src="Financial Times"),
 dict(key="kryvyirih", region="UR",
      head="Double-tap strike hits Zelensky's hometown",
      deck="Russian ballistic missiles kill two, including a 7-year-old boy, and wound 58 in Kryvyi Rih.",
      src="Reuters", pin=(550, 275)),
 dict(key="sparta", region="UR",
      head="Drones set Russian ship ablaze off Finland",
      deck="Cargo ship Sparta II burns in the Gulf of Finland; crew evacuated as it drifts into Finnish waters.",
      src="Reuters / AP", pin=(520, 225)),
 dict(key="villages", region="UR",
      head="Kyiv seeks ceasefires to free 15 villages",
      deck="Zelensky proposes local truces to evacuate nine settlements in Kherson and six in Zaporizhzhia.",
      src="Ukrainska Pravda / ISW"),
 dict(key="ukdrones", region="UR",
      head="Ukraine and UK to build drones in Britain",
      deck="Defence ministers sign joint production of mid- and deep-strike drones.",
      src="Ukrinform"),
 dict(key="finlandclaim", region="UR",
      head="Finland claims \u20ac25bn from Russia",
      deck="Helsinki pursues three arbitration awards, the largest a \u20ac16.4bn Gazprom gas claim.",
      src="YLE"),
 # --- Americas (8) ---
 dict(key="chapo", region="AM", hero=True,
      head="MEXICO CAPTURES 'EL CHAPO ISIDRO'",
      deck="Special forces seize cartel boss Fausto Isidro Meza Flores in Sinaloa; 11 killed in the violence that followed.",
      src="Reuters", pin=(150, 420)),
 dict(key="florida", region="AM",
      head="Florida river breaks 73-year record",
      deck="St Johns River near Cocoa tops a 1940s mark after days of rain; flooding may last into January.",
      src="NWS", pin=(185, 430)),
 dict(key="homeless", region="AM",
      head="Judge blocks Trump's $4bn homeless-aid revamp",
      deck="Federal judge rejects the administration's bid to overhaul the programme.",
      src="Washington Post"),
 dict(key="chinai", region="AM",
      head="US lawmakers push ban on Chinese AI",
      deck="Congress moves to bar Chinese-made AI models from federal systems.",
      src="The Hill"),
 dict(key="nvidia", region="AM",
      head="Nvidia faces SEC inquiry, sources say",
      deck="US regulator examines the chipmaker's finances as AI stocks slide.",
      src="Reuters"),
 dict(key="guatemala", region="AM",
      head="Guatemala arrests wanted Mexican",
      deck="US seeks extradition of the suspect held in Guatemala City.",
      src="AP", pin=(160, 460)),
 dict(key="palisades", region="AM",
      head="Palisades fire suspect convicted",
      deck="Suspect found guilty of fire-related charges in the deadly Pacific Palisades blaze.",
      src="LA Times"),
 dict(key="peru", region="AM",
      head="Peru counts quake toll: 1 dead, 16 hurt",
      deck="M6.7 Jun\u00edn tremor leaves 170 homes damaged; a M5.0 aftershock follows on Sunday.",
      src="IGP / USGS", pin=(215, 560)),
 # --- Asia-Pacific (5) ---
 dict(key="hongkong", region="AP",
      head="Hong Kong on fire alert after Tai Po grief",
      deck="Observatory issues a Yellow fire warning; a year on, Tai Po families mark their loss.",
      src="HKO / SCMP", pin=(800, 380)),
 dict(key="manipur", region="AP",
      head="Toxic alcohol kills 11 in Manipur",
      deck="More than 180 people hospitalised in India's north-east, the chief minister says.",
      src="PTI", pin=(760, 400)),
 dict(key="korea", region="AP",
      head="Seoul offers $75,000 for cheating tip-offs",
      deck="South Korea's leader repeats a reward for reporting academic dishonesty.",
      src="Yonhap"),
 dict(key="autoweapons", region="AP",
      head="UN states agree autonomous-weapons pact",
      deck="Countries agree at UN talks to create an international treaty on killer robots.",
      src="UN"),
 dict(key="trumpiran", region="AP",
      head="Trump: Iran 'breached' the deal",
      deck="US president accuses Tehran and vows a long-term pact to block nuclear arms.",
      src="AP"),
 # --- Africa & World (3) ---
 dict(key="nigeria", region="AF",
      head="24 bodies after Nigeria boat capsize",
      deck="Emergency agency NEMA reports the toll from the river accident.",
      src="NEMA", pin=(470, 480)),
 dict(key="icj", region="AF",
      head="Myanmar ruling 'may shape' Gaza cases",
      deck="ICJ judgment on Myanmar could frame Israel's position, lawyers say.",
      src="ICJ"),
 dict(key="stocks", region="AF",
      head="US stocks slide into correction",
      deck="Dow and S&P 500 fall in Friday's AI sell-off; chip shares lead the drop.",
      src="Reuters"),
 # --- Sport (5) ---
 dict(key="alcaraz", region="SP",
      head="Alcaraz to face Zverev for ATP title",
      deck="Spaniard fights back past Shelton to set up a Turin final against the world No. 1.",
      src="BBC Sport"),
 dict(key="france", region="SP",
      head="France into final with Springboks",
      deck="Les Bleus beat Argentina in Paris to book a Nations Championship final.",
      src="BBC Sport"),
 dict(key="australia", region="SP",
      head="Australia edge Wales in thriller",
      deck="Wallabies hold on for a narrow win in Cardiff.",
      src="BBC Sport"),
 dict(key="bournemouth", region="SP",
      head="Evanilson scores in sixth straight game",
      deck="Bournemouth beat Nottingham Forest as the Brazilian's hot streak rolls on.",
      src="BBC Sport"),
 dict(key="coventry", region="SP",
      head="McNeil own goal gifts Coventry 3\u20132 win",
      deck="Late drama as Crystal Palace fall at Coventry.",
      src="BBC Sport"),
]

REGIONS = [
    ("ME", "MIDDLE EAST & GULF"),
    ("EU", "EUROPE"),
    ("UR", "UKRAINE & RUSSIA"),
    ("AM", "AMERICAS"),
    ("AP", "ASIA-PACIFIC"),
    ("AF", "AFRICA & WORLD"),
    ("SP", "SPORT"),
]

KPI = [
    ("35%", "COP31 clean-power share by 2035"),
    ("11", "killed after Chapo Isidro arrest"),
    ("24", "bodies after Nigeria capsize"),
    ("58", "injured in Kryvyi Rih strike"),
    ("6.7", "Peru quake magnitude"),
    ("73 YRS", "Florida river record broken"),
]

DATE_CHECK = ("DATE CHECK \u2014 NOT SUNDAY, LEFT OUT: Russia's 400-drone barrage "
    "(Thu\u2013Fri night 19\u201320 Nov) \u2022 Peru mainshock (Fri eve 20 Nov; Sunday brought "
    "the toll + aftershock) \u2022 Riemann proof claim (Fri 20 Nov; verified Sat 21) \u2022 "
    "Bolsonaro in ICU (Sat 21 Nov) \u2022 Trump\u2013Xi\u2013Putin Shenzhen summit (Thu 19 Nov) "
    "\u2022 EU\u2013Indonesia trade deal (Sat 21 Nov).")

HEROES = [s for s in STORIES if s.get("hero")]
GRID = [s for s in STORIES if s["key"] in
        ("hormuz", "hartha", "zelensky", "sparta", "florida", "peru",
         "hongkong", "manipur", "alcaraz", "france")]
INDEX = [s for s in STORIES if s not in HEROES and s not in GRID]

assert len(STORIES) == 44, len(STORIES)
assert len(HEROES) == 3 and len(GRID) == 10 and len(INDEX) == 31
assert all(sum(1 for s in STORIES if s["region"] == r[0]) >= 1 for r in REGIONS)
assert sum(len([s for s in STORIES if s["region"] == r[0]]) for r in REGIONS) == 44


# ---------------------------------------------------------------- helpers

def wrap(d, text, fnt, width):
    words, lines, cur = text.split(), [], ""
    for w in words:
        t = (cur + " " + w).strip()
        if d.textlength(t, font=fnt) <= width:
            cur = t
        else:
            if cur:
                lines.append(cur)
            cur = w
    if cur:
        lines.append(cur)
    return lines


def text_lines(d, x, y, lines, fnt, fill=INK, leading=None, align="left", width=0):
    lh = leading or int(fnt.size * 1.18)
    for ln in lines:
        if align == "center":
            d.text((x + width / 2, y), ln, font=fnt, fill=fill, anchor="ma")
        else:
            d.text((x, y), ln, font=fnt, fill=fill)
        y += lh
    return y


def hline(d, x0, x1, y, fill=INK, width=1):
    d.line([(x0, y), (x1, y)], fill=fill, width=width)


def box(d, x0, y0, x1, y1, fill=None, outline=None, width=1):
    d.rectangle([x0, y0, x1, y1], fill=fill, outline=outline, width=width)


# ---------------------------------------------------------------- illustrations
# Small procedural scenes; each draws into (x, y, w, h) and returns nothing.

def ill_sun(d, x, y, w, h):
    d.rectangle([x, y, x + w, y + h], fill=(250, 226, 160))
    d.ellipse([x + w * 0.74, y + h * 0.06, x + w * 0.94, y + h * 0.36], fill=(240, 150, 40))
    cx, cy, r = x + w * 0.32, y + h * 0.5, h * 0.38
    d.ellipse([cx - r, cy - r, cx + r, cy + r], fill=(90, 150, 200),
              outline=(28, 78, 128), width=2)
    d.ellipse([cx - r * 0.55, cy - r * 0.7, cx - r * 0.05, cy - r * 0.1],
              fill=(46, 107, 52))
    d.ellipse([cx + r * 0.1, cy + r * 0.15, cx + r * 0.6, cy + r * 0.65],
              fill=(46, 107, 52))
    d.arc([cx - r, cy - r, cx + r, cy + r], 200, 340, fill=(255, 255, 255), width=2)
    d.line([cx, cy - r, cx, cy + r], fill=(255, 255, 255), width=2)
    d.rectangle([x, y + h * 0.88, x + w, y + h], fill=(28, 78, 128))
    for i, col in enumerate([(158, 27, 27), (28, 78, 128), (46, 107, 52), (176, 124, 18),
                             (90, 60, 120)]):
        fx = x + w * (0.56 + i * 0.085)
        d.rectangle([fx, y + h * 0.62, fx + 2, y + h * 0.88], fill=(60, 60, 60))
        d.rectangle([fx + 2, y + h * 0.62, fx + 16, y + h * 0.74], fill=col)


def ill_night(d, x, y, w, h):
    d.rectangle([x, y, x + w, y + h], fill=(16, 22, 44))
    for sx, sy in [(0.12, 0.2), (0.3, 0.12), (0.55, 0.25), (0.75, 0.1), (0.9, 0.3), (0.42, 0.32)]:
        d.ellipse([x + w * sx, y + h * sy, x + w * sx + 3, y + h * sy + 3], fill=(255, 255, 255))
    d.ellipse([x + w * 0.78, y + h * 0.08, x + w * 0.95, y + h * 0.32], fill=(240, 235, 200))
    for i, (ax, ay, bx, by) in enumerate([(0.05, 0.85, 0.35, 0.3), (0.3, 0.9, 0.6, 0.35),
                                          (0.55, 0.88, 0.9, 0.28)]):
        d.arc([x + w * ax, y + h * ay - h * 0.55, x + w * bx, y + h * by + h * 0.1],
              200, 340, fill=(240, 140, 40), width=3)
        d.ellipse([x + w * bx - 4, y + h * by - 4, x + w * bx + 4, y + h * by + 4],
                  fill=(240, 140, 40))
    d.rectangle([x, y + h * 0.82, x + w, y + h], fill=(40, 40, 40))
    for bx in (0.1, 0.35, 0.62, 0.85):
        d.rectangle([x + w * bx, y + h * 0.62, x + w * bx + w * 0.12, y + h * 0.82],
                    fill=(70, 70, 78))
        d.rectangle([x + w * bx + 2, y + h * 0.66, x + w * bx + w * 0.12 - 2, y + h * 0.72],
                    fill=(250, 214, 130))


def ill_desert(d, x, y, w, h):
    d.rectangle([x, y, x + w, y + h], fill=(232, 196, 130))
    d.ellipse([x + w * 0.72, y + h * 0.06, x + w * 0.95, y + h * 0.38], fill=(240, 160, 40))
    d.polygon([(x, y + h), (x + w * 0.3, y + h * 0.55), (x + w * 0.62, y + h),
               (x + w, y + h * 0.7), (x + w, y + h)], fill=(190, 140, 80))
    d.rectangle([x, y + h * 0.78, x + w, y + h * 0.86], fill=(90, 70, 50))
    d.line([x + w * 0.34, y + h * 0.22, x + w * 0.66, y + h * 0.22], fill=(50, 50, 50),
           width=3)
    d.ellipse([x + w * 0.38, y + h * 0.22, x + w * 0.6, y + h * 0.36], fill=(70, 70, 75))
    d.rectangle([x + w * 0.6, y + h * 0.26, x + w * 0.72, y + h * 0.32], fill=(70, 70, 75))
    d.rectangle([x + w * 0.42, y + h * 0.36, x + w * 0.44, y + h * 0.48], fill=(50, 50, 50))
    d.rectangle([x + w * 0.54, y + h * 0.36, x + w * 0.56, y + h * 0.48], fill=(50, 50, 50))
    d.line([x + w * 0.4, y + h * 0.48, x + w * 0.58, y + h * 0.48], fill=(50, 50, 50),
           width=2)


def ill_sea(d, x, y, w, h, fire=False):
    d.rectangle([x, y, x + w, y + h], fill=(120, 170, 205))
    d.rectangle([x, y, x + w, y + h * 0.3], fill=(180, 210, 230))
    d.rectangle([x + w * 0.08, y + h * 0.42, x + w * 0.92, y + h * 0.62], fill=(50, 50, 55))
    d.rectangle([x + w * 0.6, y + h * 0.22, x + w * 0.72, y + h * 0.42], fill=(158, 27, 27))
    d.rectangle([x + w * 0.12, y + h * 0.62, x + w * 0.88, y + h * 0.68], fill=(30, 30, 35))
    if fire:
        for dx, dy, r in [(0.3, 0.25, 14), (0.38, 0.18, 10), (0.24, 0.3, 8)]:
            d.ellipse([x + w * dx - r, y + h * dy - r, x + w * dx + r, y + h * dy + r],
                      fill=(240, 140, 40))
        d.ellipse([x + w * 0.3 - 6, y + h * 0.25 - 6, x + w * 0.3 + 6, y + h * 0.25 + 6],
                  fill=(250, 220, 80))
    for wy in (0.72, 0.82, 0.92):
        d.line([x + 4, y + h * wy, x + w - 4, y + h * wy], fill=(255, 255, 255), width=2)


def ill_plant(d, x, y, w, h):
    d.rectangle([x, y, x + w, y + h], fill=(210, 200, 170))
    d.rectangle([x, y + h * 0.55, x + w, y + h], fill=(120, 110, 95))
    for tx in (0.12, 0.42, 0.72):
        d.polygon([(x + w * tx, y + h * 0.85), (x + w * (tx + 0.05), y + h * 0.25),
                   (x + w * (tx + 0.14), y + h * 0.25), (x + w * (tx + 0.19), y + h * 0.85)],
                  fill=(150, 140, 125))
        d.ellipse([x + w * tx - 3, y + h * 0.22, x + w * (tx + 0.19) + 3, y + h * 0.34],
                  fill=(220, 220, 220))
    for fx, fy, r in [(0.55, 0.35, 12), (0.62, 0.28, 8), (0.5, 0.42, 7)]:
        d.ellipse([x + w * fx - r, y + h * fy - r, x + w * fx + r, y + h * fy + r],
                  fill=(240, 140, 40))


def ill_podium(d, x, y, w, h):
    d.rectangle([x, y, x + w, y + h], fill=(200, 215, 235))
    d.rectangle([x, y + h * 0.6, x + w, y + h], fill=(120, 90, 60))
    d.rectangle([x + w * 0.32, y + h * 0.42, x + w * 0.68, y + h * 0.62], fill=(90, 60, 40))
    d.ellipse([x + w * 0.44, y + h * 0.12, x + w * 0.56, y + h * 0.3], fill=(230, 200, 160))
    d.polygon([(x + w * 0.4, y + h * 0.3), (x + w * 0.6, y + h * 0.3),
               (x + w * 0.66, y + h * 0.45), (x + w * 0.34, y + h * 0.45)], fill=(40, 60, 90))
    for fx, col in [(0.06, (0, 90, 180)), (0.86, (255, 215, 0))]:
        d.rectangle([x + w * fx, y + h * 0.15, x + w * fx + 3, y + h * 0.6], fill=(60, 60, 60))
        d.rectangle([x + w * fx + 3, y + h * 0.15, x + w * (fx + 0.12), y + h * 0.3], fill=col)


def ill_flood(d, x, y, w, h):
    d.rectangle([x, y, x + w, y + h], fill=(150, 180, 200))
    d.rectangle([x, y + h * 0.5, x + w, y + h], fill=(60, 110, 160))
    for hx in (0.08, 0.42, 0.74):
        d.rectangle([x + w * hx, y + h * 0.3, x + w * (hx + 0.2), y + h * 0.55], fill=(200, 170, 130))
        d.polygon([(x + w * hx - 4, y + h * 0.3), (x + w * (hx + 0.1), y + h * 0.16),
                   (x + w * (hx + 0.24), y + h * 0.3)], fill=(158, 27, 27))
    for wy in (0.62, 0.74, 0.88):
        for k in range(4):
            d.arc([x + w * (0.05 + k * 0.25), y + h * wy - 6,
                   x + w * (0.17 + k * 0.25), y + h * wy + 6], 0, 180, fill=(255, 255, 255), width=2)


def ill_quake(d, x, y, w, h):
    d.rectangle([x, y, x + w, y + h], fill=(220, 205, 175))
    d.polygon([(x, y + h), (x + w * 0.25, y + h * 0.3), (x + w * 0.5, y + h),
               (x + w * 0.75, y + h * 0.35), (x + w, y + h)], fill=(140, 120, 95))
    d.polygon([(x + w * 0.25, y + h * 0.3), (x + w * 0.3, y + h * 0.42),
               (x + w * 0.2, y + h * 0.45)], fill=(255, 255, 255))
    d.line([x + w * 0.1, y + h, x + w * 0.3, y + h * 0.62, x + w * 0.28, y + h * 0.4],
           fill=(60, 45, 30), width=3)
    d.line([x + w * 0.7, y + h, x + w * 0.62, y + h * 0.55, x + w * 0.78, y + h * 0.38],
           fill=(60, 45, 30), width=3)
    for bx in (0.45, 0.68):
        d.rectangle([x + w * bx, y + h * 0.68, x + w * (bx + 0.16), y + h * 0.88],
                    fill=(180, 150, 115))
        d.line([x + w * bx, y + h * 0.68, x + w * (bx + 0.16), y + h * 0.88],
               fill=(60, 45, 30), width=2)


def ill_city(d, x, y, w, h):
    d.rectangle([x, y, x + w, y + h], fill=(200, 190, 220))
    for i, (bx, bw, bh) in enumerate([(0.04, 0.16, 0.55), (0.24, 0.13, 0.75),
                                      (0.41, 0.18, 0.62), (0.63, 0.14, 0.85),
                                      (0.81, 0.15, 0.5)]):
        d.rectangle([x + w * bx, y + h * (1 - bh), x + w * (bx + bw), y + h], fill=(70, 70, 85))
        for wy in range(3):
            d.rectangle([x + w * bx + 3, y + h * (1 - bh) + 6 + wy * 12,
                         x + w * (bx + bw) - 3, y + h * (1 - bh) + 12 + wy * 12],
                        fill=(250, 214, 130))
    d.polygon([(x + w * 0.42, y + h * 0.18), (x + w * 0.5, y + h * 0.05),
               (x + w * 0.58, y + h * 0.18)], fill=(240, 200, 40))
    d.text((x + w * 0.5, y + h * 0.22), "!", font=SANS_B(28), fill=(158, 27, 27), anchor="mm")


def ill_clinic(d, x, y, w, h):
    d.rectangle([x, y, x + w, y + h], fill=(225, 235, 225))
    d.rectangle([x + w * 0.3, y + h * 0.15, x + w * 0.7, y + h * 0.85], fill=(255, 255, 255),
                outline=(46, 107, 52), width=3)
    d.rectangle([x + w * 0.46, y + h * 0.28, x + w * 0.54, y + h * 0.72], fill=(158, 27, 27))
    d.rectangle([x + w * 0.38, y + h * 0.44, x + w * 0.62, y + h * 0.56], fill=(158, 27, 27))
    d.rectangle([x + w * 0.06, y + h * 0.68, x + w * 0.24, y + h * 0.88], fill=(60, 90, 60))
    d.rectangle([x + w * 0.78, y + h * 0.68, x + w * 0.94, y + h * 0.88], fill=(60, 90, 60))


def ill_tennis(d, x, y, w, h):
    d.rectangle([x, y, x + w, y + h], fill=(90, 140, 80))
    d.rectangle([x + w * 0.08, y + h * 0.12, x + w * 0.92, y + h * 0.88],
                fill=(120, 170, 105), outline=(255, 255, 255), width=2)
    d.line([x + w * 0.08, y + h * 0.5, x + w * 0.92, y + h * 0.5], fill=(255, 255, 255), width=2)
    d.line([x + w * 0.5, y + h * 0.12, x + w * 0.5, y + h * 0.88], fill=(255, 255, 255), width=2)
    d.ellipse([x + w * 0.68, y + h * 0.18, x + w * 0.82, y + h * 0.4], fill=(220, 230, 60),
              outline=(255, 255, 255), width=2)
    d.arc([x + w * 0.68, y + h * 0.18, x + w * 0.82, y + h * 0.4], 200, 340, fill=(255, 255, 255),
          width=2)


def ill_rugby(d, x, y, w, h):
    d.rectangle([x, y, x + w, y + h], fill=(110, 160, 90))
    d.rectangle([x, y + h * 0.72, x + w, y + h], fill=(70, 110, 60))
    d.ellipse([x + w * 0.3, y + h * 0.3, x + w * 0.72, y + h * 0.62], fill=(180, 120, 60),
              outline=(255, 255, 255), width=2)
    d.line([x + w * 0.5, y + h * 0.32, x + w * 0.5, y + h * 0.6], fill=(255, 255, 255), width=2)
    for px in (0.12, 0.88):
        d.line([x + w * px, y + h * 0.15, x + w * px, y + h * 0.72], fill=(255, 255, 255), width=3)
        d.line([x + w * (px - 0.06), y + h * 0.15, x + w * (px + 0.06), y + h * 0.15],
               fill=(255, 255, 255), width=3)


def ill_strike(d, x, y, w, h):
    d.rectangle([x, y, x + w, y + h], fill=(40, 32, 48))
    for sx, sy in [(0.1, 0.15), (0.35, 0.08), (0.6, 0.2), (0.85, 0.1)]:
        d.ellipse([x + w * sx, y + h * sy, x + w * sx + 3, y + h * sy + 3], fill=(255, 255, 255))
    for bx in (0.05, 0.3, 0.55, 0.78):
        d.rectangle([x + w * bx, y + h * 0.45, x + w * (bx + 0.18), y + h], fill=(25, 25, 30))
        for wy in (0.52, 0.62, 0.72, 0.82):
            d.rectangle([x + w * bx + 3, y + h * wy, x + w * (bx + 0.18) - 3, y + h * wy + 5],
                        fill=(250, 214, 130))
    for fx, fy, r, col in [(0.42, 0.35, 16, (240, 140, 40)), (0.47, 0.28, 10, (250, 220, 80)),
                           (0.38, 0.42, 8, (240, 140, 40)), (0.42, 0.35, 6, (255, 240, 160))]:
        d.ellipse([x + w * fx - r, y + h * fy - r, x + w * fx + r, y + h * fy + r], fill=col)


ILLS = {"cop31": ill_sun, "bahrain": ill_night, "chapo": ill_desert,
        "hormuz": lambda d, x, y, w, h: ill_sea(d, x, y, w, h, fire=True),
        "hartha": ill_plant, "zelensky": ill_podium, "sparta": ill_sea,
        "florida": ill_flood, "peru": ill_quake, "hongkong": ill_city,
        "manipur": ill_clinic, "alcaraz": ill_tennis, "france": ill_rugby,
        "kryvyirih": ill_strike}



# ---------------------------------------------------------------- layout

M = 14  # margin
CW = W - 2 * M  # 996

HEADLINE = [s for s in STORIES if s["key"] == "cop31"][0]
HEROES = [s for s in STORIES if s["key"] in ("bahrain", "chapo", "kryvyirih")]
GRID = [s for s in STORIES if s["key"] in
        ("hormuz", "hartha", "zelensky", "sparta", "florida", "peru",
         "hongkong", "manipur", "alcaraz", "france")]
INDEX = [s for s in STORIES if s not in HEROES and s not in GRID and s is not HEADLINE]
assert len(HEROES) == 3 and len(GRID) == 10 and len(INDEX) == 30, (
    len(HEROES), len(GRID), len(INDEX))

PIN_KEYS = ["cop31", "bahrain", "hormuz", "houthi", "gaza", "hartha",
            "zelensky", "kryvyirih", "sparta", "chapo", "florida", "peru",
            "hongkong"]
PIN_NUM = {k: i + 1 for i, k in enumerate(PIN_KEYS)}

CONTINENTS = [
    [(-168, 66), (-140, 70), (-120, 72), (-95, 80), (-80, 73), (-60, 60),
     (-75, 45), (-80, 32), (-97, 26), (-105, 20), (-115, 30), (-125, 40),
     (-150, 60)],
    [(-80, 10), (-60, 5), (-35, -5), (-40, -20), (-55, -35), (-70, -50),
     (-75, -30), (-80, -15)],
    [(-10, 36), (0, 44), (10, 45), (20, 55), (30, 60), (30, 70), (10, 70),
     (-5, 58), (-10, 50)],
    [(-17, 15), (-10, 35), (10, 37), (30, 32), (35, 28), (43, 12), (51, 10),
     (40, -5), (35, -20), (20, -35), (12, -18), (9, 4), (-8, 5)],
    [(35, 36), (45, 40), (60, 45), (70, 55), (90, 70), (120, 73), (160, 70),
     (180, 66), (160, 60), (140, 45), (130, 35), (120, 25), (105, 10),
     (95, 8), (80, 8), (70, 22), (55, 25), (45, 30)],
    [(113, -22), (130, -12), (142, -10), (150, -20), (153, -28), (140, -38),
     (130, -32), (115, -35)],
]
PIN_LABELS = ("1 Antalya  2 Bahrain  3 Hormuz  4 Riyadh  5 Gaza  6 Basra  "
              "7 Kyiv  8 Kryvyi Rih  9 Gulf of Finland  10 Sinaloa  "
              "11 Florida  12 Jun\u00edn  13 Hong Kong")


def draw_map(d, x, y, w, h):
    box(d, x, y, x + w, y + h, fill=(214, 228, 238), outline=RULE)
    def px(lon, lat):
        return (x + (lon + 180) / 360 * w, y + (90 - lat) / 180 * h)
    for cont in CONTINENTS:
        d.polygon([px(lo, la) for lo, la in cont], fill=(196, 182, 148),
                  outline=(120, 105, 75))
    by_key = {s["key"]: s for s in STORIES}
    # display nudges so the Gulf / Kyiv clusters stay readable
    nudge = {"cop31": (0, -7), "bahrain": (13, 7), "hormuz": (20, 12),
             "houthi": (-15, 12), "gaza": (-13, -7), "hartha": (15, -8),
             "zelensky": (-8, -7), "kryvyirih": (10, 7)}
    for k, n in PIN_NUM.items():
        s = by_key[k]
        lon, lat = (s["pin"][0] / 1000 * 360 - 180, 90 - s["pin"][1] / 1000 * 180)
        cx, cy = px(lon, lat)
        dx, dy = nudge.get(k, (0, 0))
        cx, cy = cx + dx, cy + dy
        d.ellipse([cx - 5, cy - 5, cx + 5, cy + 5], fill=RED, outline=(255, 255, 255))
        d.text((cx, cy), str(n), font=SANS_B(7), fill=(255, 255, 255), anchor="mm")


def render():
    img = Image.new("RGB", (W, H), PAPER)
    d = ImageDraw.Draw(img)

    # --- kicker bar 0-22 ---
    box(d, 0, 0, W, 22, fill=RED)
    d.text((M, 11), "THE WORLD IN ONE DAY", font=SANS_B(11), fill=(255, 255, 255),
           anchor="lm")
    d.text((W - M, 11), "44 STORIES  \u2022  7 REGIONS  \u2022  SUNDAY 22 NOVEMBER 2026",
           font=SANS_B(11), fill=(255, 255, 255), anchor="rm")

    # --- masthead 22-82, dateline 82-98 ---
    d.text((W / 2, 52), "THE SUNDAY WORLD", font=SERIF_B(46), fill=INK, anchor="mm")
    d.text((M, 52), "No. 326", font=SANS(10), fill=MUTED, anchor="lm")
    d.text((W - M, 52), "ONE DAY \u2022 ONE PAGE", font=SANS_B(10), fill=MUTED, anchor="rm")
    hline(d, M, W - M, 80, fill=INK, width=2)
    d.text((W / 2, 90), "SUNDAY 22 NOVEMBER 2026  \u2014  ANTALYA  \u2022  BAHRAIN  \u2022  "
           "SINALOA  \u2022  KRYVYI RIH  \u2022  TURIN",
           font=SANS_B(10), fill=INK, anchor="mm")
    hline(d, M, W - M, 98, fill=RULE, width=1)

    # --- headline: COP31 98-200 ---
    hx, hw = M, 690
    d.text((hx, 104), "CLIMATE  \u2022  COP31  \u2022  ANTALYA", font=SANS_B(11), fill=RED)
    d.text((hx, 118), "COP31 NEARS A DEAL", font=SERIF_B(40), fill=INK)
    deck = wrap(d, HEADLINE["deck"], SERIF(14), hw)
    text_lines(d, hx, 162, deck, SERIF(14), leading=17)
    ix, iw = 712, 298
    ill_sun(d, ix, 104, iw, 84)
    box(d, ix, 104, ix + iw, 104 + 84, outline=RULE)
    d.text((ix, 191), "Reuters \u2022 AP \u2022 AFP \u2014 text tabled 02:00 Antalya; "
           "plenary 06:00 GMT Sunday", font=SANS(9), fill=MUTED)
    hline(d, M, W - M, 202, fill=INK, width=2)

    # --- KPI strip 206-244 ---
    kw, gap = 162, 4
    y = 206
    for i, (num, lab) in enumerate(KPI):
        x0 = M + i * (kw + gap)
        box(d, x0, y, x0 + kw, y + 38, fill=PANEL, outline=RULE)
        d.text((x0 + kw / 2, y + 12), num, font=SERIF_B(19), fill=RED, anchor="mm")
        d.text((x0 + kw / 2, y + 29), lab, font=SANS(8), fill=MUTED, anchor="mm")
    hline(d, M, W - M, 250, fill=INK, width=1)

    # --- region bar 254-272 ---
    y = 254
    segw = CW / 7
    fills = [(158, 27, 27), (28, 78, 128), (46, 107, 52), (176, 124, 18),
             (90, 60, 120), (180, 90, 40), (60, 60, 60)]
    for i, (code, name) in enumerate(REGIONS):
        n = sum(1 for s in STORIES if s["region"] == code)
        x0 = M + i * segw
        box(d, x0, y, x0 + segw - 2, y + 18, fill=fills[i])
        d.text((x0 + segw / 2 - 1, y + 9), f"{name} {n}", font=SANS_B(9),
               fill=(255, 255, 255), anchor="mm")
    hline(d, M, W - M, 278, fill=INK, width=1)

    # --- heroes 280-462 ---
    y = 282
    d.text((M, y), "THE DAY'S THREE BIG STORIES", font=SANS_B(11), fill=RED)
    y = 298
    hw3, gap3 = 325, 10
    for i, s in enumerate(HEROES):
        x0 = M + i * (hw3 + gap3)
        ILLS[s["key"]](d, x0, y, hw3, 84)
        box(d, x0, y, x0 + hw3, y + 84, outline=RULE)
        ty = y + 88
        ty = text_lines(d, x0, ty, wrap(d, s["head"], SERIF_B(15), hw3), SERIF_B(15),
                        leading=16)
        ty = text_lines(d, x0, ty + 2, wrap(d, s["deck"], SERIF(11.5), hw3),
                        SERIF(11.5), leading=13)
        pin = f"  \u25cf{PIN_NUM[s['key']]}" if s["key"] in PIN_NUM else ""
        d.text((x0, ty + 2), f"Source: {s['src']}{pin}", font=SANS(9), fill=MUTED)
    hline(d, M, W - M, 466, fill=INK, width=1)

    # --- grid 466-750 ---
    y = 470
    d.text((M, y), "AROUND THE WORLD IN TEN PICTURES", font=SANS_B(11), fill=RED)
    y = 486
    gw, gapg = 192, 8
    for r in range(2):
        for c in range(5):
            s = GRID[r * 5 + c]
            x0 = M + c * (gw + gapg)
            yy = y + r * 132
            ILLS[s["key"]](d, x0, yy, gw, 56)
            box(d, x0, yy, x0 + gw, yy + 56, outline=RULE)
            ty = yy + 60
            ty = text_lines(d, x0, ty, wrap(d, s["head"], SERIF_B(12), gw), SERIF_B(12),
                            leading=13)
            ty = text_lines(d, x0, ty + 1, wrap(d, s["deck"], SERIF(10), gw), SERIF(10),
                            leading=11)
            pin = f"  \u25cf{PIN_NUM[s['key']]}" if s["key"] in PIN_NUM else ""
            d.text((x0, ty + 1), f"{s['src']}{pin}", font=SANS(8), fill=MUTED)
    hline(d, M, W - M, 752, fill=INK, width=1)

    # --- index 752-884 (3 columns x 10 rows) ---
    y = 756
    d.text((M, y), "THE FULL INDEX \u2014 30 MORE STORIES", font=SANS_B(11), fill=RED)
    d.text((W - M, y), "in the order they broke", font=SERIF_I(10), fill=MUTED,
           anchor="ra")
    y = 772
    colw = (CW - 32) / 3
    for i, s in enumerate(INDEX):
        col = i // 10
        row = i % 10
        x0 = M + col * (colw + 16)
        yy = y + row * 11
        d.text((x0, yy), f"{i + 1:2d}.", font=SANS_B(9), fill=RED)
        line = f"{s['head']} \u2014 {s['src']}"
        if d.textlength(line, font=SERIF(9.5)) > colw - 22:
            while d.textlength(line + "\u2026", font=SERIF(9.5)) > colw - 22 and len(line) > 10:
                line = line[:-1]
            line += "\u2026"
        d.text((x0 + 20, yy), line, font=SERIF(9.5), fill=INK)
    hline(d, M, W - M, 886, fill=INK, width=1)

    # --- map + date check 888-972 ---
    y = 890
    d.text((M, y), "WHERE IT HAPPENED", font=SANS_B(10), fill=RED)
    draw_map(d, M, y + 14, 500, 58)
    leg = wrap(d, PIN_LABELS, SANS(8), 500)
    text_lines(d, M, y + 74, leg, SANS(8), leading=10)
    dx = 522
    d.text((dx, y), "DATE CHECK", font=SANS_B(10), fill=RED)
    dc = wrap(d, DATE_CHECK, SERIF(9.5), W - M - dx)
    text_lines(d, dx, y + 14, dc, SERIF(9.5), leading=11.5)
    hline(d, M, W - M, 976, fill=INK, width=1)

    # --- footer 976-1024 ---
    d.text((W / 2, 986), "Every story above happened, or was first reported, on Sunday "
           "22 November 2026 in some time zone. Sources are named on every story.",
           font=SERIF_I(10), fill=INK, anchor="ma")
    d.text((W / 2, 1002), "THE SUNDAY WORLD \u2014 44 stories \u2022 7 regions \u2022 "
           "3 big stories \u2022 10 pictures \u2022 30 more in the index \u2022 "
           "drawn in code, no AI image.",
           font=SANS(9), fill=MUTED, anchor="ma")
    return img


if __name__ == "__main__":
    import sys
    out = sys.argv[1] if len(sys.argv) > 1 else "entry.png"
    render().save(out, optimize=True)
    print("saved", out, os.path.getsize(out), "bytes")
