"""Build the site's General American IPA map from an open lexicon and checked additions."""
from pathlib import Path
import json,re
import build_vocab as book

ROOT=Path(__file__).resolve().parent
lex=dict(line.split('\t',1) for line in (ROOT/'tmp/ipa/en_US.txt').read_text(encoding='utf-8').splitlines() if '\t' in line)
checked=json.loads((ROOT/'tmp/ipa/cambridge-us.json').read_text(encoding='utf-8'))
additions={word:'/'+item['ipa'][0]+'/' for word,item in checked.items() if item['ipa']}
# Reviewed dictionary gaps and contextual readings. Phrase entries use citation
# pronunciations of their constituent words, not connected-speech transcription.
additions.update({
 'afforestation':'/əˌfɔrəˈsteɪʃən/', 'attentional':'/əˈtenʃənəl/',
 'baseload':'/ˈbeɪsloʊd/', 'counterargument':'/ˈkaʊntərˌɑrɡjəmənt/',
 'densification':'/ˌdensɪfɪˈkeɪʃən/', 'digitization':'/ˌdɪdʒɪtəˈzeɪʃən/',
 'dispatchable':'/dɪˈspætʃəbəl/', 'employability':'/ɪmˌplɔɪəˈbɪləti/',
 'impulsivity':'/ˌɪmpʌlˈsɪvəti/', 'livability':'/ˌlɪvəˈbɪləti/',
 'reproducibility':'/ˌriːprəˌduːsəˈbɪləti/', 'salinization':'/ˌsælɪnəˈzeɪʃən/',
 'traceability':'/ˌtreɪsəˈbɪləti/', 'walkability':'/ˌwɔkəˈbɪləti/',
})
contextual={
 'minute':'形 /maɪˈnuːt/；名 /ˈmɪnɪt/',
 'resume':'简历 /ˈrezəmeɪ/；继续 /rɪˈzuːm/',
 'subject to':'形 /ˈsʌbdʒekt tuː/；动 /səbˈdʒekt tuː/',
 'live up to':'/lɪv ʌp tuː/',
 'wind':'/wɪnd/',
}
def normalize(value):
    value=value.replace('ɹ','r').replace('ɫ','l').replace('t̬','t').replace('·','.').replace('.','')
    # The source encodes CMU AH as ə in both positions. Use conventional ʌ
    # under lexical stress and ɚ for unstressed r-coloured schwa.
    vowels=set('aeiouɑɐæɒɔəɛɜɞɝɚɪʊʌ')
    output=[];stressed=False
    for char in value:
        if char in 'ˈˌ':stressed=True
        elif char in vowels:
            if char=='ə' and stressed:char='ʌ'
            elif char=='ɝ' and not stressed:char='ɚ'
            stressed=False
        elif char in '/,;； ':stressed=False
        output.append(char)
    return ''.join(output)
def lookup(word):
    if word in contextual:return contextual[word]
    if word in additions:return normalize(additions[word])
    if word in lex:return normalize(lex[word])
    parts=re.findall(r"[A-Za-z]+(?:'[a-z]+)?",word)
    readings=[]
    for part in parts:
        value=additions.get(part.lower()) or lex.get(part.lower())
        if not value:raise ValueError('Missing pronunciation: '+part)
        readings.append(normalize(value).split(',')[0].strip('/'))
    return '/'+' '.join(readings)+'/'
mapping={row[0]:lookup(row[0]) for day in book.DAYS for row in day['rows']}
assert len(mapping)==1460 and all('/' in value for value in mapping.values())
(ROOT/'phonetics.json').write_text(json.dumps(mapping,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
print('Built',len(mapping),'IPA entries')
