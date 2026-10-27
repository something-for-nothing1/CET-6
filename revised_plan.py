"""Rebuild dated lessons from the original bank and the advanced supplement."""
from pathlib import Path
from datetime import date, timedelta

PLAN_VERSION = 'advanced-20261027-v2'

def make_plan(original, root):
    groups = {f'O{i}': d['rows'] for i,d in enumerate(original,1)}
    extra_groups=[]
    for line in (Path(root)/'advanced_vocab.txt').read_text(encoding='utf-8').splitlines():
        if line.startswith('#'):
            extra_groups.append({'theme':line[1:].strip(),'rows':[]})
        elif line.strip():
            row=tuple(part.strip() for part in line.split('|'))
            assert len(row)==3
            extra_groups[-1]['rows'].append(row)
    assert len(extra_groups)==31 and all(len(d['rows'])==20 for d in extra_groups)
    groups.update({f'E{i}':d['rows'] for i,d in enumerate(extra_groups,1)})
    bank={r[0]:r for rows in groups.values() for r in rows}
    assert len(bank)==1460
    used={r[0] for r in original[0]['rows']}
    # 10/26 remains unchanged. 'reinforce' from the linked core list is already there.
    core='undermine inherent empirical ambiguous substantial inevitable compelling mitigate exacerbate facilitate foster constrain allocate derive attribute assess perceive contradict sustain'.split()
    choices=[
      ('抽象学术与精准表达', 'E1 O4 O41', 3),
      ('社会问题与教育机会', 'E2 E3 O2 O18', 2),
      ('科技、研究与数据', 'E4 E5 O3 O5', 5),
      ('写作论证与因果搭配', 'E6 O28 O29 O30', 28),
      ('环境、经济与发展', 'E7 E8 O11 O9', 12),
      ('文化、历史与传统', 'E9 O21 O22 E30', 21),
      ('教育进阶与职业能力', 'E2 E10 O2 O7', 7),
      ('数字生活与信息安全', 'E12 E4 O6 O5', 6),
      ('消费行为与经济判断', 'E17 E8 O10 O9', 10),
      ('生态治理与能源转型', 'E7 E20 O12 O13', 13),
      ('健康、医疗与心理', 'E11 O14 O15 O16', 14),
      ('文化传播与国际交流', 'E13 E23 O24 O23', 24),
      ('生命科学与自然系统', 'E21 E22 O37', 37),
      ('认知、记忆与行为', 'E16 O38 O1', 38),
      ('社会公平与人口变迁', 'E3 E19 O17 O18', 18),
      ('城乡规划与农业升级', 'E15 E14 O19 O20', 20),
      ('职场管理与协作沟通', 'E10 E24 O8 O26', 8),
      ('论证态度与程度判断', 'E29 E25 O32 O33', 32),
      ('宏观经济与产业升级', 'E8 E17 O9 O24', 9),
      ('社区生活与乡村发展', 'E14 E15 O20 O19', 19),
      ('公共政策与制度执行', 'E18 O39 O18', 39),
      ('媒体识读与数字伦理', 'E12 O25 O6', 25),
      ('艺术审美与文化表达', 'E23 E9 O22 O23', 22),
      ('学术研究与证据评价', 'E5 E21 E31 O3 O4', 4),
      ('绿色产业与环境风险', 'E20 E28 O13 O11 O40', 40),
      ('身心健康与压力应对', 'E11 E16 O16 O15', 16),
      ('家庭、老龄化与社会支持', 'E19 E3 O17 O18', 17),
      ('技术应用与科研沟通', 'E4 E5 O35 O36', 35),
      ('熟词僻义与动词搭配', 'E26 O41 O31', 31),
      ('逻辑衔接与写作表达', 'E27 O34 O30', 34),
      ('综合查漏①：科技与自然', 'E21 E22 E4 O37 O5', 5),
      ('综合查漏②：经济与职场', 'E8 E10 E17 O7 O8 O36', 8),
      ('综合查漏③：文化与翻译', 'E30 E9 E13 O21 O24', 21),
      ('综合查漏④：抽象学术概念', 'E31 E1 O42 O4', 42),
      ('综合查漏⑤：论证与判断', 'E29 E25 E6 O28 O32', 28),
      ('综合查漏⑥：搭配与语境', 'E26 E27 E24 O26 O31', 26),
    ]
    assert len(choices)==36
    # Advanced items are preferred when filling a topic with fewer than 40 remaining entries.
    fallback=[r for g in list(groups)[42:]+list(groups)[:42] for r in groups[g]]
    plan=[dict(original[0],kind='learn',active_count=5,review_rows=[],source_days=[])]
    cursor=0
    for number in range(2,43):
        if (number-2)%7==6:
            source_days=[n for n in range(max(2,number-6),number) if plan[n-1]['rows']]
            plan.append(dict(theme='每周总复习与错词回收',rows=[],kind='weekly',active_count=0,
                             source_days=source_days,review_rows=[],en='',zh=''))
            continue
        theme,prefs,example=choices[cursor]
        chosen=[]
        if cursor==0:
            chosen=[bank[w] for w in core if w not in used]
            used.update(r[0] for r in chosen)
        candidates=[r for g in prefs.split() for r in groups[g]]+fallback
        for row in candidates:
            if len(chosen)==40:break
            if row[0] in used:continue
            chosen.append(row);used.add(row[0])
        assert len(chosen)==40
        # Bring six useful expression words forward, not six random dictionary items.
        preferred=[r for r in chosen if ' ' not in r[0] and '-' not in r[0]]
        active=([bank[w] for w in ['undermine','mitigate','exacerbate','facilitate','foster','allocate']] if cursor==0 else preferred[:6])
        chosen=active+[r for r in chosen if r not in active]
        plan.append(dict(theme=theme,rows=chosen,kind='learn',active_count=6,
                         source_days=[],review_rows=[],en=original[example-1]['en'],zh=original[example-1]['zh']))
        cursor+=1
    assert len(plan)==42 and cursor==36 and len(used)==1460
    # A reproducible 30-word schedule: 10 each from roughly 1, 3 and 7 days ago.
    # When an interval lands on a weekly review, use the most recent learning day before it.
    for n,lesson in enumerate(plan,1):
        sources=[]
        for gap in (1,3,7):
            target=n-gap
            while target>=1 and not plan[target-1]['rows']:target-=1
            if target>=1 and target not in sources:sources.append(target)
        if lesson['kind']=='weekly':sources=lesson['source_days']
        lesson['source_days']=sources
        picked=[];seen=set()
        if lesson['kind']=='weekly':
            candidates=[r for d in sources for r in plan[d-1]['rows'][:5]]
        else:
            candidates=[]
            for source in sources:
                rows=plan[source-1]['rows']
                offset=(n*7)%len(rows)
                candidates.extend((rows+rows)[offset:offset+10])
            candidates += [r for source in sources for r in plan[source-1]['rows']]
        for row in candidates:
            if row[0] not in seen:
                picked.append(row);seen.add(row[0])
            if len(picked)==30:break
        lesson['review_rows']=picked
    return plan

def final_review_groups(plan):
    learned=[i for i,d in enumerate(plan,1) if d['rows']]
    sizes=[8,8,7,7,7]
    result=[];offset=0
    for day,size in zip(range(43,48),sizes):
        source=learned[offset:offset+size];offset+=size
        result.append((day,source[0],source[-1],f'考前回顾：第{day-42}批'))
    assert offset==len(learned)
    return result
