"""Reusable extraction helpers for the Game Dev Wiki deep-ingest passes."""
import pypdf, os, re, sys, json, glob

RAW = 'raw'

def reader(sid):
    f = glob.glob(os.path.join(RAW, f'{sid}-*.pdf'))[0]
    r = pypdf.PdfReader(f)
    if r.is_encrypted:
        r.decrypt('')
    return r, f

def pages(sid):
    r, f = reader(sid)
    out = []
    for i in range(len(r.pages)):
        try: out.append(r.pages[i].extract_text() or '')
        except: out.append('')
    return out

def fulltext(sid):
    """Cache full text per page to _work/sid.full.txt and return list of page strings."""
    cache = f'_work/{sid}.full.txt'
    ps = pages(sid)
    with open(cache, 'w', encoding='utf-8', errors='replace') as fh:
        for i, t in enumerate(ps):
            fh.write(f'\n===== PAGE {i+1} =====\n'); fh.write(t)
    return ps

if __name__ == '__main__':
    cmd = sys.argv[1]
    sid = sys.argv[2]
    if cmd == 'full':
        ps = fulltext(sid)
        print(f'{sid}: {len(ps)} pages cached to _work/{sid}.full.txt')
    elif cmd == 'slice':
        # slice PDF page range a-b (1-indexed inclusive) and print text
        a, b = int(sys.argv[3]), int(sys.argv[4])
        ps = pages(sid)
        for i in range(a-1, min(b, len(ps))):
            print(f'\n===== PAGE {i+1} =====')
            print(ps[i])
