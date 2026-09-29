import json, re, yaml, sys, os
SECRET_KEYS = {'token','api_key','apikey','openai_api_key','secret','password','authorization','access_token','refresh_token','client_secret','private_key'}
EMAIL = re.compile(r'[\w.+-]+@[\w-]+\.[\w.]+')
PHONE = re.compile(r'(?<![\w-])(?:\+?52[\s-]?)?(?:\(?\d{2,3}\)?[\s-]?)\d{3,4}[\s-]?\d{4}(?![\w-])')
URL_RULES = [
    (re.compile(r'https://[0-9a-f-]{36}-[a-z0-9-]+\.apps\.astra\.datastax\.com[^\s"]*'), 'https://<ASTRA_DB_ENDPOINT>'),
    (re.compile(r'https://astra\.datastax\.com/org/[^\s"]+'), 'https://astra.datastax.com/<ORG>'),
    (re.compile(r'https://[a-z0-9-]+\.app\.n8n\.cloud/[^\s"]*'), 'https://<N8N_INSTANCE>/webhook/<path>'),
    (re.compile(r'https://www\.notion\.so/[^\s"]+'), 'https://www.notion.so/<PAGE_ID>'),
    (re.compile(r'https://docs\.google\.com/spreadsheets/d/[^\s"]+'), 'https://docs.google.com/spreadsheets/d/<SHEET_ID>'),
    (re.compile(r'https://hook\.[a-z0-9.]*make\.com/[^\s"]+'), 'https://hook.make.com/<WEBHOOK>'),
]
LONGID = re.compile(r'(?<![A-Za-z0-9_./-])(?=[A-Za-z0-9_-]*\d)(?=[A-Za-z0-9_-]*[A-Za-z])[A-Za-z0-9_-]{28,64}(?![A-Za-z0-9_./-])')
UUID = re.compile(r'\b[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}\b')

def clean_str(s, key=''):
    for rx, rep in URL_RULES: s = rx.sub(rep, s)
    s = EMAIL.sub('correo@ejemplo.com', s)
    s = PHONE.sub('<TELEFONO>', s)
    if key not in ('code','type','module','id','name','display_name','description','template','info'):
        s = LONGID.sub('<ID>', s)
    return s

def clean(o, key=''):
    if isinstance(o, dict):
        out = {}
        if o.get('password') is True and 'value' in o:
            o = dict(o); o['value'] = ''
        for k, v in o.items():
            lk = k.lower()
            if lk == 'credentials': out[k] = {kk: {'id': '<CREDENTIAL>', 'name': '<CREDENTIAL>'} for kk in (v or {})} if isinstance(v, dict) else '<CREDENTIAL>'; continue
            if lk in ('webhookid',): out[k] = '<WEBHOOK_ID>'; continue
            if k in ('__IMTCONN__','__IMTHOOK__','__IMTKEY__'): out[k] = '<CONNECTION>'; continue
            if lk in ('instanceid',): out[k] = '<INSTANCE>'; continue
            if lk in SECRET_KEYS and isinstance(v, str) and v: out[k] = '<REDACTED>'; continue
            out[k] = clean(v, lk)
        return out
    if isinstance(o, list): return [clean(v, key) for v in o]
    if isinstance(o, str): return clean_str(o, key)
    return o

src, dst = sys.argv[1], sys.argv[2]
if src.endswith(('.yml', '.yaml')):
    d = yaml.safe_load(open(src, encoding='utf-8'))
    yaml.safe_dump(clean(d), open(dst, 'w', encoding='utf-8'), allow_unicode=True, sort_keys=False, width=120)
else:
    d = json.load(open(src, encoding='utf-8'))
    d = clean(d)
    if isinstance(d, dict): d.pop('pinData', None); d.pop('meta', None)
    json.dump(d, open(dst, 'w', encoding='utf-8'), ensure_ascii=False, indent=2)
