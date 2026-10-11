"""Check local links, image metadata and downloadable PDFs before publishing."""
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import urlsplit, unquote
import json

ROOT = Path(__file__).resolve().parents[1]


class Site(HTMLParser):
    def __init__(self):
        super().__init__()
        self.ids, self.links, self.assets = set(), [], set()
        self.h1_count = 0

    def handle_starttag(self, tag, attrs):
        a = dict(attrs)
        if 'id' in a:
            assert a['id'] not in self.ids, f"Duplicate ID: {a['id']}"
            self.ids.add(a['id'])
        if tag == 'h1':
            self.h1_count += 1
        if tag == 'img':
            assert all(k in a for k in ('alt', 'width', 'height')), 'Image metadata missing'
        if tag == 'a' and a.get('target') == '_blank':
            assert 'noopener' in a.get('rel', '').split(), 'Unsafe external tab'
        for key in ('href', 'src'):
            if key in a:
                self.links.append(a[key])


html = (ROOT / 'index.html').read_text(encoding='utf-8-sig')
site = Site()
site.feed(html)
assert site.h1_count == 1, 'Exactly one main heading required'
for link in site.links:
    parsed = urlsplit(link)
    if parsed.scheme or parsed.netloc:
        continue
    if parsed.path:
        file = (ROOT / unquote(parsed.path)).resolve()
        assert file.is_relative_to(ROOT) and file.is_file(), f'Missing local asset: {link}'
        site.assets.add(file.relative_to(ROOT).as_posix())
        if file.suffix == '.pdf':
            data = file.read_bytes()
            assert data.startswith(b'%PDF-') and b'%%EOF' in data[-1024:], 'Invalid PDF download'
    if parsed.fragment and not parsed.path:
        assert unquote(parsed.fragment) in site.ids, f'Broken anchor: {link}'
assert 'github.com/usjunior' not in html, 'Obsolete GitHub profile'
assert 'IntersectionObserver' not in html, 'Content must not depend on scroll scripts'
schema_start = html.index('<script type="application/ld+json">')
schema = html[schema_start:].split('>', 1)[1].split('</script>', 1)[0]
json.loads(schema)
print(f'Validated {len(site.links)} links, {len(site.assets)} assets, PDF and structured metadata.')

if __name__ == '__main__':
    import sys
    if '--build' in sys.argv:
        import shutil
        out = ROOT / '_site'
        out.mkdir(exist_ok=True)
        shutil.copy2(ROOT / 'index.html', out / 'index.html')
        for name in site.assets:
            dest = out / name
            dest.parent.mkdir(parents=True, exist_ok=True)
            shutil.copy2(ROOT / name, dest)
        (out / '.nojekyll').touch()
        print('Built _site with only public referenced assets.')
