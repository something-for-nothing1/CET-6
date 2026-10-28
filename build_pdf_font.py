"""Subset the OFL Noto font to the site's vocabulary and export labels."""
from pathlib import Path
import sys,base64

ROOT=Path(__file__).resolve().parent
sys.path.insert(0,str(ROOT/'.qa-python'))
from fontTools import subset
from fontTools.ttLib import TTFont
from fontTools.fontBuilder import FontBuilder
from fontTools.pens.ttGlyphPen import TTGlyphPen
from fontTools.pens.cu2quPen import Cu2QuPen
from fontTools.varLib.instancer import instantiateVariableFont

font=TTFont(ROOT/'tmp/pdfs/NotoSansSC-Regular.otf')
text=(ROOT/'index.html').read_text(encoding='utf-8')+(ROOT/'assets/export-pdf.js').read_text(encoding='utf-8')
characters=set(range(32,127))|{ord(ch) for ch in text}
options=subset.Options()
options.hinting=False
options.layout_features=[]
subsetter=subset.Subsetter(options=options)
subsetter.populate(unicodes=characters)
subsetter.subset(font)
order=font.getGlyphOrder()
glyph_set=font.getGlyphSet()
glyphs={}
for name in order:
    pen=TTGlyphPen(glyph_set)
    glyph_set[name].draw(Cu2QuPen(pen,max_err=1.0,reverse_direction=True))
    glyphs[name]=pen.glyph()
builder=FontBuilder(font['head'].unitsPerEm,isTTF=True)
builder.setupGlyphOrder(order)
builder.setupCharacterMap(font.getBestCmap())
builder.setupGlyf(glyphs)
builder.setupHorizontalMetrics(font['hmtx'].metrics)
builder.setupHorizontalHeader(ascent=font['hhea'].ascent,descent=font['hhea'].descent)
builder.setupNameTable({'familyName':'CET6 PDF Sans','styleName':'Regular',
    'fullName':'CET6 PDF Sans Regular','psName':'CET6PDFSans-Regular',
    'uniqueFontIdentifier':'CET6PDFSans-Regular-v1','version':'Version 1.0',
    'copyright':font['name'].getDebugName(0) or '',
    'licenseDescription':font['name'].getDebugName(13) or 'SIL Open Font License 1.1',
    'licenseInfoURL':'https://openfontlicense.org/'})
builder.setupOS2(sTypoAscender=font['OS/2'].sTypoAscender,
    sTypoDescender=font['OS/2'].sTypoDescender,usWinAscent=font['OS/2'].usWinAscent,
    usWinDescent=font['OS/2'].usWinDescent)
builder.setupPost()
target=ROOT/'tmp/pdfs/CET6-PDF-Sans.ttf'
builder.save(target)
encoded=base64.b64encode(target.read_bytes()).decode('ascii')
ipa_font=TTFont(ROOT/'tmp/pdfs/NotoSans-Latin.ttf')
instantiateVariableFont(ipa_font,{'wght':400,'wdth':100},inplace=True)
ipa_text=''.join(__import__('json').loads((ROOT/'phonetics.json').read_text(encoding='utf-8')).values())
ipa_chars={ord(ch) for ch in ipa_text}
ipa_options=subset.Options();ipa_options.hinting=False;ipa_options.layout_features=[]
ipa_subsetter=subset.Subsetter(options=ipa_options)
ipa_subsetter.populate(unicodes=ipa_chars)
ipa_subsetter.subset(ipa_font)
assert all(code in font.getBestCmap() or code in ipa_font.getBestCmap() for code in ipa_chars)
ipa_target=ROOT/'tmp/pdfs/CET6-IPA-Sans.ttf';ipa_font.save(ipa_target)
ipa_encoded=base64.b64encode(ipa_target.read_bytes()).decode('ascii')
(ROOT/'assets/pdf/font-data.js').write_text('/* Noto font subsets; SIL Open Font License, see OFL.txt and OFL-LATIN.txt. */\nwindow.CET6PdfFontBase64="'+encoded+'";\nwindow.CET6IpaFontBase64="'+ipa_encoded+'";\n',encoding='utf-8')
print(f'PDF font: {target.stat().st_size} bytes; {len(font.getBestCmap())} characters')
