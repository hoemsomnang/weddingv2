import math
import os
import random

def get_defs():
    return """
  <defs>
    <filter id="shadow-soft" x="-20%" y="-20%" width="140%" height="140%">
      <feDropShadow dx="1" dy="3" stdDeviation="3.5" flood-color="#3b1b22" flood-opacity="0.2"/>
    </filter>
    <filter id="shadow-deep" x="-25%" y="-25%" width="150%" height="150%">
      <feDropShadow dx="2" dy="5" stdDeviation="5" flood-color="#180e12" flood-opacity="0.32"/>
    </filter>
    <filter id="leaf-shadow" x="-20%" y="-20%" width="140%" height="140%">
      <feDropShadow dx="1" dy="2" stdDeviation="2.5" flood-color="#0e1f11" flood-opacity="0.25"/>
    </filter>
    <linearGradient id="trellis-stroke" x1="0%" y1="100%" x2="0%" y2="0%">
      <stop offset="0%" stop-color="#B88A7A" stop-opacity="0.3"/>
      <stop offset="50%" stop-color="#D4A798" stop-opacity="0.55"/>
      <stop offset="100%" stop-color="#ECC6BA" stop-opacity="0.2"/>
    </linearGradient>
    <linearGradient id="dark-shrub" x1="0%" y1="100%" x2="0%" y2="0%">
      <stop offset="0%" stop-color="#0E1E12"/>
      <stop offset="40%" stop-color="#1B3820"/>
      <stop offset="85%" stop-color="#2D5432"/>
      <stop offset="100%" stop-color="#3D6E44"/>
    </linearGradient>
    <linearGradient id="mid-foliage" x1="0%" y1="100%" x2="0%" y2="0%">
      <stop offset="0%" stop-color="#18361C"/>
      <stop offset="35%" stop-color="#2C5931"/>
      <stop offset="75%" stop-color="#467D4D"/>
      <stop offset="100%" stop-color="#629E69"/>
    </linearGradient>
    <linearGradient id="grass-stalk" x1="0%" y1="100%" x2="0%" y2="0%">
      <stop offset="0%" stop-color="#36543A"/>
      <stop offset="60%" stop-color="#5E8863"/>
      <stop offset="100%" stop-color="#8DB692"/>
    </linearGradient>
    <radialGradient id="coral-core-deep" cx="50%" cy="50%" r="50%">
      <stop offset="0%" stop-color="#8E2434"/>
      <stop offset="40%" stop-color="#B73548"/>
      <stop offset="80%" stop-color="#D94F63"/>
      <stop offset="100%" stop-color="#F26E80"/>
    </radialGradient>
    <linearGradient id="coral-petal-inner" x1="0%" y1="100%" x2="0%" y2="0%">
      <stop offset="0%" stop-color="#C23C50"/>
      <stop offset="35%" stop-color="#DE556A"/>
      <stop offset="75%" stop-color="#F2798C"/>
      <stop offset="100%" stop-color="#FCABB8"/>
    </linearGradient>
    <linearGradient id="coral-petal-mid" x1="0%" y1="100%" x2="0%" y2="0%">
      <stop offset="0%" stop-color="#D64D62"/>
      <stop offset="30%" stop-color="#EE6E82"/>
      <stop offset="70%" stop-color="#FA9BB0"/>
      <stop offset="100%" stop-color="#FED1DA"/>
    </linearGradient>
    <linearGradient id="coral-petal-outer" x1="0%" y1="100%" x2="0%" y2="0%">
      <stop offset="0%" stop-color="#E26578"/>
      <stop offset="25%" stop-color="#F58DA0"/>
      <stop offset="65%" stop-color="#FCBDCA"/>
      <stop offset="90%" stop-color="#FEEDF1"/>
      <stop offset="100%" stop-color="#FFFFFF"/>
    </linearGradient>
    <radialGradient id="blush-core-deep" cx="50%" cy="50%" r="50%">
      <stop offset="0%" stop-color="#9C3048"/>
      <stop offset="45%" stop-color="#B8445A"/>
      <stop offset="80%" stop-color="#D9687D"/>
      <stop offset="100%" stop-color="#EB889B"/>
    </radialGradient>
    <linearGradient id="blush-petal-inner" x1="0%" y1="100%" x2="0%" y2="0%">
      <stop offset="0%" stop-color="#C24F64"/>
      <stop offset="35%" stop-color="#E2788C"/>
      <stop offset="75%" stop-color="#F3A5B4"/>
      <stop offset="100%" stop-color="#FCD2DB"/>
    </linearGradient>
    <linearGradient id="blush-petal-mid" x1="0%" y1="100%" x2="0%" y2="0%">
      <stop offset="0%" stop-color="#D46A7F"/>
      <stop offset="30%" stop-color="#EB8B9E"/>
      <stop offset="70%" stop-color="#F7B8C5"/>
      <stop offset="100%" stop-color="#FDE8ED"/>
    </linearGradient>
    <linearGradient id="blush-petal-outer" x1="0%" y1="100%" x2="0%" y2="0%">
      <stop offset="0%" stop-color="#DF8295"/>
      <stop offset="25%" stop-color="#F1A7B7"/>
      <stop offset="65%" stop-color="#FBD0DA"/>
      <stop offset="90%" stop-color="#FDF0F3"/>
      <stop offset="100%" stop-color="#FFFFFF"/>
    </linearGradient>
    <linearGradient id="petal-curl" x1="0%" y1="0%" x2="0%" y2="100%">
      <stop offset="0%" stop-color="#FFFFFF" stop-opacity="0.95"/>
      <stop offset="50%" stop-color="#FFF0F3" stop-opacity="0.8"/>
      <stop offset="100%" stop-color="#EAA6B6" stop-opacity="0.3"/>
    </linearGradient>
    <linearGradient id="purple-floret-1" x1="0%" y1="100%" x2="0%" y2="0%">
      <stop offset="0%" stop-color="#452478"/>
      <stop offset="35%" stop-color="#653CA6"/>
      <stop offset="75%" stop-color="#8961CF"/>
      <stop offset="100%" stop-color="#B998FC"/>
    </linearGradient>
    <linearGradient id="purple-floret-2" x1="0%" y1="100%" x2="0%" y2="0%">
      <stop offset="0%" stop-color="#542B94"/>
      <stop offset="40%" stop-color="#7B4CC7"/>
      <stop offset="80%" stop-color="#A277ED"/>
      <stop offset="100%" stop-color="#D3B8FE"/>
    </linearGradient>
    <linearGradient id="lavender-floret" x1="0%" y1="100%" x2="0%" y2="0%">
      <stop offset="0%" stop-color="#68429B"/>
      <stop offset="45%" stop-color="#8B65C2"/>
      <stop offset="85%" stop-color="#B494E3"/>
      <stop offset="100%" stop-color="#E2D4F7"/>
    </linearGradient>
    <linearGradient id="fallen-petal-1" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#FFFFFF"/>
      <stop offset="30%" stop-color="#FCD2DA"/>
      <stop offset="70%" stop-color="#F28E9E"/>
      <stop offset="100%" stop-color="#DA5E70"/>
    </linearGradient>
    <linearGradient id="fallen-petal-2" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#FFFFFF"/>
      <stop offset="35%" stop-color="#FCE1E6"/>
      <stop offset="75%" stop-color="#F6A7B5"/>
      <stop offset="100%" stop-color="#E27384"/>
    </linearGradient>
    <linearGradient id="euc-grad-1" x1="0%" y1="100%" x2="0%" y2="0%">
      <stop offset="0%" stop-color="#3B5749"/>
      <stop offset="40%" stop-color="#557564"/>
      <stop offset="75%" stop-color="#739783"/>
      <stop offset="100%" stop-color="#9BBBAA"/>
    </linearGradient>
    <linearGradient id="euc-grad-2" x1="0%" y1="100%" x2="0%" y2="0%">
      <stop offset="0%" stop-color="#476856"/>
      <stop offset="45%" stop-color="#658874"/>
      <stop offset="80%" stop-color="#88AC97"/>
      <stop offset="100%" stop-color="#AFD0BC"/>
    </linearGradient>
    <linearGradient id="stem-grad" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" stop-color="#2B462C"/>
      <stop offset="50%" stop-color="#4B6E4C"/>
      <stop offset="100%" stop-color="#2B462C"/>
    </linearGradient>
  </defs>
"""

def generate_shrub_base(width):
    xml = '<g>\n'
    for x in range(0, width+1, 50):
        rx = random.randint(60,120); ry = random.randint(70,140)
        xml += f'<ellipse cx="{x}" cy="430" rx="{rx}" ry="{ry}" fill="url(#dark-shrub)"/>\n'
    xml += '</g>\n'
    return xml

def generate_meadow_grasses(width):
    xml = '<g>\n'
    r = random.Random(77)
    for x in range(460, width-460, 14):
        h = r.randint(100,165); bend = r.randint(-30,30); sw = r.uniform(1.1,2.2)
        c1x=x+bend*0.4; c1y=430-h*0.5; c2x=x+bend; c2y=430-h
        xml += f'<path d="M {x} 430 Q {c1x:.0f} {c1y:.0f}, {c2x:.0f} {c2y:.0f}" stroke="url(#grass-stalk)" stroke-width="{sw:.1f}" fill="none" stroke-linecap="round" opacity="0.7"/>\n'
        if r.random()>0.4:
            xml += f'<ellipse cx="{c2x:.0f}" cy="{c2y:.0f}" rx="2" ry="3.5" fill="#B9D4BD" opacity="0.75"/>\n'
    xml += '</g>\n'
    return xml

def generate_purple_cluster(cx, cy, scale, count, sx, sy, seed):
    xml = f'<g transform="translate({cx:.0f},{cy:.0f}) scale({scale:.2f})">\n'
    r = random.Random(seed)
    floret_types = ["purple-floret-1","purple-floret-2","lavender-floret"]
    for i in range(count):
        fx=r.gauss(0,sx*0.45); fy=-r.uniform(10,sy)+abs(fx)*0.25
        fs=r.uniform(0.75,1.15); grad=floret_types[i%3]
        np_=4 if r.random()>0.3 else 5; base=r.uniform(0,math.pi)
        xml += f'<g transform="translate({fx:.1f},{fy:.1f}) scale({fs:.2f})" filter="url(#shadow-soft)">\n'
        for p in range(np_):
            pa=base+p*(math.pi*2/np_); px=math.cos(pa)*8.5; py=math.sin(pa)*8.5
            xml += f'<ellipse cx="{px:.1f}" cy="{py:.1f}" rx="7" ry="5.5" transform="rotate({math.degrees(pa):.1f},{px:.1f},{py:.1f})" fill="url(#{grad})"/>\n'
        xml += '<circle cx="0" cy="0" r="1.8" fill="#FFF494"/>\n</g>\n'
    xml += '</g>\n'
    return xml

def generate_rose_petal(cx, cy, ri, ro, wr, ang, grad, curl=True):
    al=ang-wr/2; ar=ang+wr/2
    bx0=cx+math.cos(ang)*ri*0.7; by0=cy+math.sin(ang)*ri*0.7
    blx=cx+math.cos(al)*ri; bly=cy+math.sin(al)*ri
    brx=cx+math.cos(ar)*ri; bry=cy+math.sin(ar)*ri
    rm=(ri+ro)/2
    slx=cx+math.cos(al-0.12)*rm*1.08; sly=cy+math.sin(al-0.12)*rm*1.08
    srx=cx+math.cos(ar+0.12)*rm*1.08; sry=cy+math.sin(ar+0.12)*rm*1.08
    tx=cx+math.cos(ang)*ro; ty=cy+math.sin(ang)*ro
    tlx=cx+math.cos(ang-wr*0.22)*(ro*1.02); tly=cy+math.sin(ang-wr*0.22)*(ro*1.02)
    trx=cx+math.cos(ang+wr*0.22)*(ro*1.02); try_=cy+math.sin(ang+wr*0.22)*(ro*1.02)
    c1lx=cx+math.cos(al)*(ri*1.2); c1ly=cy+math.sin(al)*(ri*1.2)
    c2rx=cx+math.cos(ar+0.08)*(ro*0.85); c2ry=cy+math.sin(ar+0.08)*(ro*0.85)
    p = f'<path d="M {blx:.1f} {bly:.1f} C {c1lx:.1f} {c1ly:.1f},{slx:.1f} {sly:.1f},{tlx:.1f} {tly:.1f} Q {tx:.1f} {ty:.1f},{trx:.1f} {try_:.1f} C {srx:.1f} {sry:.1f},{c2rx:.1f} {c2ry:.1f},{brx:.1f} {bry:.1f} Q {bx0:.1f} {by0:.1f},{blx:.1f} {bly:.1f} Z" fill="url(#{grad})" filter="url(#shadow-soft)"/>\n'
    if curl:
        ch=(ro-rm)*0.35; ctx=cx+math.cos(ang)*(ro-ch); cty=cy+math.sin(ang)*(ro-ch)
        p += f'<path d="M {tlx:.1f} {tly:.1f} Q {tx:.1f} {ty:.1f},{trx:.1f} {try_:.1f} Q {ctx:.1f} {cty:.1f},{tlx:.1f} {tly:.1f} Z" fill="url(#petal-curl)" opacity="0.85"/>\n'
    return p

def generate_rose(cx, cy, scale, rot, style):
    xml = f'<g transform="translate({cx:.1f},{cy:.1f}) rotate({math.degrees(rot):.1f}) scale({scale:.2f})" filter="url(#shadow-deep)">\n'
    core=f"{style}-core-deep"; inn=f"{style}-petal-inner"; mid=f"{style}-petal-mid"; out=f"{style}-petal-outer"
    for i in range(7):
        ang=(i/7)*math.pi*2+0.15*math.sin(i*1.7); xml+=generate_rose_petal(0,0,46,110,(math.pi*2/7)*1.45,ang,out)
    for i in range(8):
        ang=(i/8)*math.pi*2+0.35; xml+=generate_rose_petal(0,0,30,85,(math.pi*2/8)*1.4,ang,mid)
    for i in range(8):
        ang=(i/8)*math.pi*2+0.18; xml+=generate_rose_petal(0,0,18,62,(math.pi*2/8)*1.35,ang,inn)
    for i in range(9):
        ang=(i/9)*math.pi*2+0.4; xml+=generate_rose_petal(0,0,10,42,(math.pi*2/9)*1.3,ang,inn,False)
    xml += f'<circle cx="0" cy="0" r="16" fill="url(#{core})"/>\n'
    for j in range(6):
        a=j*(math.pi*2/6); px1=math.cos(a)*4; py1=math.sin(a)*4; px2=math.cos(a+1.2)*12; py2=math.sin(a+1.2)*12; px3=math.cos(a+2.2)*14; py3=math.sin(a+2.2)*14
        xml += f'<path d="M {px1:.1f} {py1:.1f} Q {px2:.1f} {py2:.1f},{px3:.1f} {py3:.1f} Q {math.cos(a+1.5)*7:.1f} {math.sin(a+1.5)*7:.1f},{px1:.1f} {py1:.1f} Z" fill="url(#{inn})" opacity="0.92"/>\n'
    xml += '</g>\n'
    return xml

def generate_white_sprays(width):
    xml = '<g>\n'
    r = random.Random(101)
    spots = [(80,240,20,40),(180,210,22,45),(330,270,16,30),(width-330,270,16,30),(width-180,210,22,45),(width-80,240,20,40),(460,310,12,25),(width-460,310,12,25)]
    for scx,scy,n,sp in spots:
        for _ in range(n):
            bx=scx+r.gauss(0,sp*0.4); by=scy+r.gauss(0,sp*0.4); sz=r.uniform(2.5,4.5)
            xml += f'<g transform="translate({bx:.1f},{by:.1f})">\n'
            for p in range(5):
                ang=p*(math.pi*2/5); px=math.cos(ang)*sz; py=math.sin(ang)*sz
                xml += f'<circle cx="{px:.1f}" cy="{py:.1f}" r="{sz*0.65:.1f}" fill="#FFFFFF" opacity="0.95"/>\n'
            xml += f'<circle cx="0" cy="0" r="{sz*0.35:.1f}" fill="#E8B038"/>\n</g>\n'
    xml += '</g>\n'
    return xml

def generate_fallen_petals(width):
    xml = '<g>\n'
    petals = [(50,415,26,16,0.45,"fallen-petal-1"),(90,422,28,17,-0.3,"fallen-petal-2"),(140,428,30,18,0.15,"fallen-petal-1"),
              (200,420,25,15,0.6,"fallen-petal-2"),(250,426,28,17,-0.4,"fallen-petal-1"),
              (width-250,426,28,17,0.4,"fallen-petal-1"),(width-200,420,25,15,-0.6,"fallen-petal-2"),
              (width-140,428,30,18,-0.15,"fallen-petal-1"),(width-90,422,28,17,0.3,"fallen-petal-2"),(width-50,415,26,16,-0.45,"fallen-petal-1"),
              (480,432,18,11,0.3,"fallen-petal-2"),(600,430,20,12,-0.2,"fallen-petal-1"),(width//2,431,22,13,0.35,"fallen-petal-2"),
              (width-600,430,20,12,0.2,"fallen-petal-1"),(width-480,432,18,11,-0.3,"fallen-petal-2")]
    for px,py,pw,ph,rot,grad in petals:
        xml += f'<g transform="translate({px},{py}) rotate({math.degrees(rot):.1f})" filter="url(#shadow-soft)">\n'
        xml += f'<path d="M {-pw*0.5:.1f} 0 C {-pw*0.4:.1f} {-ph*0.9:.1f},{pw*0.4:.1f} {-ph*0.9:.1f},{pw*0.5:.1f} 0 C {pw*0.4:.1f} {ph*0.7:.1f},{-pw*0.4:.1f} {ph*0.7:.1f},{-pw*0.5:.1f} 0 Z" fill="url(#{grad})"/>\n'
        xml += f'<path d="M {-pw*0.3:.1f} {-ph*0.2:.1f} Q 0 {-ph*0.7:.1f},{pw*0.3:.1f} {-ph*0.2:.1f} Q 0 {-ph*0.1:.1f},{-pw*0.3:.1f} {-ph*0.2:.1f} Z" fill="#FFFFFF" opacity="0.7"/>\n'
        xml += '</g>\n'
    xml += '</g>\n'
    return xml

def build_bottom_meadow(w=1400, h=440):
    svg = f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {w} {h}" width="100%" height="100%">\n'
    svg += get_defs()
    svg += generate_shrub_base(w)
    svg += generate_meadow_grasses(w)
    svg += generate_purple_cluster(w*0.74, 310, 1.1, 55, 90, 140, 42)
    svg += generate_purple_cluster(w*0.16, 310, 0.9, 38, 75, 110, 88)
    svg += generate_purple_cluster(w*0.44, 375, 0.5, 16, 40, 55, 7)
    svg += generate_purple_cluster(w*0.55, 375, 0.5, 15, 38, 52, 13)
    svg += generate_rose(110, 360, 0.92, 0.25, "blush")
    svg += generate_rose(255, 340, 1.05, -0.2, "coral")
    svg += generate_rose(170, 270, 0.80, 0.4, "blush")
    svg += generate_rose(w-110, 360, 0.92, -0.25, "blush")
    svg += generate_rose(w-255, 340, 1.05, 0.2, "coral")
    svg += generate_rose(w-170, 270, 0.80, -0.4, "blush")
    svg += generate_rose(w*0.34, 385, 0.52, 0.3, "blush")
    svg += generate_rose(w*0.60, 390, 0.48, -0.25, "coral")
    svg += generate_white_sprays(w)
    svg += generate_fallen_petals(w)
    svg += '</svg>\n'
    return svg

def build_corner_spray(mirror=False, seed_offset=0):
    w, h = 500, 500
    svg = f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {w} {h}" width="100%" height="100%">\n'
    svg += get_defs()
    if mirror:
        svg += f'<g transform="scale(-1,1) translate(-{w},0)">\n'
    svg += '<path d="M 0 0 C 60 80, 120 180, 80 320" stroke="url(#stem-grad)" stroke-width="3" fill="none"/>\n'
    svg += '<path d="M 0 0 C 100 60, 220 100, 340 80" stroke="url(#stem-grad)" stroke-width="3" fill="none"/>\n'
    for ex,ey,rx,ry,tilt,grad in [
        (30,80,22,16,0.5,"euc-grad-1"),(60,150,25,18,-0.4,"euc-grad-2"),
        (50,220,28,20,0.55,"euc-grad-1"),(40,300,24,17,-0.3,"euc-grad-2"),
        (120,50,22,16,-0.4,"euc-grad-2"),(200,40,26,19,0.45,"euc-grad-1"),
        (290,50,24,17,-0.35,"euc-grad-2"),(360,65,20,15,0.4,"euc-grad-1"),
    ]:
        svg += f'<ellipse cx="{ex}" cy="{ey}" rx="{rx}" ry="{ry}" transform="rotate({math.degrees(tilt):.0f},{ex},{ey})" fill="url(#{grad})" filter="url(#leaf-shadow)"/>\n'
    for i in range(22):
        r = random.Random(i + 500 + seed_offset)
        fx=r.uniform(20,140); fy=r.uniform(20,140); fs=r.uniform(0.6,0.95)
        grad=["purple-floret-1","purple-floret-2","lavender-floret"][i%3]
        np_=4 if r.random()>0.3 else 5; base=r.uniform(0,math.pi)
        svg += f'<g transform="translate({fx:.0f},{fy:.0f}) scale({fs:.2f})" filter="url(#shadow-soft)">\n'
        for p in range(np_):
            pa=base+p*(math.pi*2/np_); px=math.cos(pa)*8; py=math.sin(pa)*8
            svg += f'<ellipse cx="{px:.1f}" cy="{py:.1f}" rx="7" ry="5.5" transform="rotate({math.degrees(pa):.1f},{px:.1f},{py:.1f})" fill="url(#{grad})"/>\n'
        svg += '<circle cx="0" cy="0" r="1.6" fill="#FFF494"/>\n</g>\n'
    svg += generate_rose(150, 200, 0.85, 0.3, "blush")
    r2 = random.Random(77+seed_offset)
    for _ in range(14):
        bx=r2.uniform(80,320); by=r2.uniform(80,320); sz=r2.uniform(2.5,4)
        svg += f'<g transform="translate({bx:.0f},{by:.0f})">\n'
        for p in range(5):
            ang=p*(math.pi*2/5); px=math.cos(ang)*sz; py=math.sin(ang)*sz
            svg += f'<circle cx="{px:.1f}" cy="{py:.1f}" r="{sz*0.65:.1f}" fill="#FFFFFF" opacity="0.95"/>\n'
        svg += f'<circle cx="0" cy="0" r="{sz*0.35:.1f}" fill="#E8B038"/>\n</g>\n'
    if mirror:
        svg += '</g>\n'
    svg += '</svg>\n'
    return svg

def main():
    base = r"d:\Learn\AI\02.Weeding\02._V2\public"
    os.makedirs(base, exist_ok=True)
    files = {
        "wedding_bottom_meadow.svg": build_bottom_meadow(1400, 440),
        "wedding_corner_left.svg":   build_corner_spray(False, 0),
        "wedding_corner_right.svg":  build_corner_spray(True, 1000),
    }
    for fn, content in files.items():
        path = os.path.join(base, fn)
        with open(path, "w", encoding="utf-8") as f:
            f.write(content)
        print(f"Generated public/{fn} ({len(content):,} bytes)")

if __name__ == "__main__":
    main()
