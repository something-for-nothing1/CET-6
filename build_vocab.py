from pathlib import Path
from datetime import date, timedelta
import html, json, re, calendar

ROOT = Path(__file__).resolve().parent
DAYS = []
def add(theme, entries, en, zh):
    rows = [tuple(x.strip() for x in line.split('|')) for line in entries.strip().splitlines() if line.strip()]
    assert len(rows) == 20, (theme, len(rows))
    assert all(len(r) == 3 for r in rows), theme
    DAYS.append(dict(theme=theme, rows=rows, en=en, zh=zh))

add('学习与教育①：能力和学习过程', '''
acquire|获得；习得|acquire knowledge
cultivate|培养；培育|cultivate critical thinking
enhance|提高；增强|enhance learning efficiency
competence|能力；胜任|professional competence
motivation|动力；动机|learning motivation
curriculum|课程体系|a balanced curriculum
discipline|学科；纪律；自律|self-discipline
literacy|读写能力；某领域素养|digital literacy
proficiency|熟练程度|language proficiency
comprehension|理解；理解力|reading comprehension
retention|保持；记忆保持|knowledge retention
memorize|记住；熟记|memorize key terms
concentrate|集中注意力|concentrate on a task
distract|使分心|distract students from study
reinforce|加强；巩固|reinforce understanding
revise|修订；复习（英式）|revise an essay
assessment|评估；考核|continuous assessment
feedback|反馈（通常不可数）|constructive feedback
aptitude|天资；才能|an aptitude for languages
mastery|精通；掌握|mastery of a subject
''', 'Regular practice helps students acquire knowledge and enhance their competence.', '经常练习有助于学生获取知识、提升能力。')

add('学习与教育②：教学和机会', '''
access|获得或使用的机会；进入|access to education
equitable|公平的；公正的|equitable access
allocate|分配；划拨|allocate educational resources
promote|促进；推广；晋升|promote lifelong learning
participate|参与|participate in discussions
enroll|注册入学；招收|enroll in a course
tuition|学费；教学|tuition fees
scholarship|奖学金；学术研究|win a scholarship
compulsory|强制的；义务的|compulsory education
vocational|职业的|vocational training
academic|学术的；学业的|academic performance
instructor|教师；指导员|a qualified instructor
lecture|讲座；讲课|attend a lecture
seminar|研讨课；研讨会|a research seminar
tutorial|辅导课|a small-group tutorial
assignment|作业；任务|complete an assignment
deadline|截止时间|meet a deadline
qualification|资格；学历|professional qualifications
dropout|辍学者|school dropouts
undergraduate|本科生；本科的|undergraduate education
''', 'Schools should allocate resources fairly to promote equitable access to education.', '学校应公平分配资源，促进教育机会公平。')

add('研究与证据①：调查和分析', '''
conduct|开展；实施；行为|conduct a survey
investigate|调查；研究|investigate the causes
evidence|证据（通常不可数）|provide evidence
indicate|表明；指出|indicate a trend
establish|建立；确定；证实|establish a connection
hypothesis|假设|test a hypothesis
variable|变量；可变的|control a variable
sample|样本；抽样|a representative sample
respondent|调查应答者|survey respondents
questionnaire|问卷|complete a questionnaire
observation|观察；观察结果|direct observation
experiment|实验|carry out an experiment
empirical|以观察或实验为依据的|empirical evidence
statistical|统计的|statistical analysis
correlation|相关性|a correlation between two factors
causation|因果关系|correlation and causation
interpret|解释；口译|interpret the findings
verify|核实；验证|verify the results
replicate|重复；复制|replicate a study
conclusion|结论|draw a conclusion
''', 'Researchers conduct surveys to investigate problems, but correlation alone does not establish causation.', '研究人员开展调查来研究问题，但仅有相关性不能确立因果关系。')

add('研究与证据②：可信度和局限', '''
reliable|可靠的|reliable information
valid|有效的；有根据的|a valid argument
objective|客观的；目标|an objective assessment
bias|偏差；偏见|selection bias
limitation|局限；限制|acknowledge a limitation
accuracy|准确性|improve accuracy
precision|精确性|measurement precision
consistent|一致的；持续的|consistent with the evidence
contradict|与……矛盾；反驳|contradict a claim
ambiguous|有歧义的；模棱两可的|an ambiguous statement
arbitrary|任意的；武断的|an arbitrary decision
assumption|假定；假设|a reasonable assumption
infer|推断|infer from the data
deduce|推导；演绎|deduce a conclusion
substantial|大量的；实质性的|substantial evidence
preliminary|初步的|preliminary findings
comprehensive|全面的|a comprehensive review
relevant|相关的|relevant to the topic
significant|重要的；统计上显著的|a significant difference
uncertainty|不确定性|reduce uncertainty
''', 'Reliable conclusions require objective evidence and an explicit discussion of bias and limitations.', '可靠的结论需要客观证据，并明确讨论偏差和局限。')

add('科技与数字生活①：创新和应用', '''
innovation|创新|technological innovation
adopt|采用；收养|adopt a new approach
facilitate|促进；使便利|facilitate communication
transform|改变；使转变|transform daily life
efficiency|效率|improve efficiency
automate|使自动化|automate routine tasks
algorithm|算法|a search algorithm
artificial|人工的；人造的|artificial intelligence
intelligence|智力；智能；情报|human intelligence
digital|数字的|digital technology
device|设备；装置|a mobile device
platform|平台|an online platform
database|数据库|a research database
integrate|整合；融入|integrate theory with practice
upgrade|升级|upgrade a system
breakthrough|突破|a scientific breakthrough
patent|专利；专利权|apply for a patent
prototype|原型；样机|develop a prototype
application|应用；申请|practical applications
accessible|可获得的；易使用的|accessible to everyone
''', 'Technological innovation can transform education and facilitate access to learning resources.', '技术创新可以改变教育，并使学习资源更容易获取。')

add('科技与数字生活②：风险和规范', '''
privacy|隐私|protect personal privacy
security|安全；保障|data security
regulate|监管；调节|regulate online platforms
ethical|伦理的；合乎道德的|ethical concerns
transparency|透明度|increase transparency
surveillance|监视；监控|electronic surveillance
consent|同意；许可|informed consent
confidential|保密的|confidential information
vulnerable|易受伤害的；脆弱的|vulnerable to attack
exposure|接触；暴露|exposure to harmful content
fraud|欺诈|online fraud
deceptive|欺骗性的|deceptive advertising
manipulate|操纵；操作|manipulate public opinion
addiction|成瘾|internet addiction
excessive|过度的|excessive screen time
distraction|使人分心的事；分心|a source of distraction
virtual|虚拟的；事实上的|virtual reality
anonymous|匿名的|anonymous users
copyright|版权|copyright protection
accountability|问责；承担责任|ensure accountability
''', 'Clear rules are needed to protect privacy and ensure transparency in the use of personal data.', '需要明确的规则来保护隐私，并确保个人数据使用的透明度。')

add('工作与职业①：就业和能力', '''
employment|就业；雇用|employment opportunities
recruit|招聘；招募|recruit new employees
adapt|适应；改编|adapt to change
collaborate|合作|collaborate with colleagues
initiative|主动性；倡议|take the initiative
occupation|职业；占领|choose an occupation
candidate|候选人；应聘者|a suitable candidate
resume|简历（美式）；重新开始|submit a resume
interview|面试；采访|a job interview
internship|实习|complete an internship
expertise|专业知识或技能|technical expertise
teamwork|团队合作|effective teamwork
leadership|领导能力|leadership skills
responsibility|责任|take responsibility for a task
commitment|投入；承诺|commitment to work
flexible|灵活的|flexible working hours
versatile|多才多艺的；多用途的|a versatile employee
competent|能胜任的|a competent manager
promotion|晋升；推广|career promotion
prospect|前景；可能性|career prospects
''', 'Employers value candidates who take the initiative and adapt to new challenges.', '雇主重视能够主动行动、适应新挑战的应聘者。')

add('工作与职业②：劳动和组织', '''
productivity|生产率|labour productivity
incentive|激励；诱因|financial incentives
retain|保留；留住|retain skilled workers
negotiate|谈判；协商|negotiate a contract
well-being|身心健康；福祉|employee well-being
workforce|全体劳动者；员工总数|an ageing workforce
wage|工资（常按时或周计）|a minimum wage
salary|薪水（常指固定月薪或年薪）|an annual salary
benefit|好处；福利；使受益|employee benefits
compensation|补偿；薪酬|fair compensation
workload|工作量|a heavy workload
burnout|身心耗竭；职业倦怠|prevent burnout
redundant|多余的；被裁减的|be made redundant
layoff|裁员|mass layoffs
turnover|人员流动率；营业额|staff turnover
hierarchy|等级体系|an organizational hierarchy
supervise|监督；管理|supervise a team
delegate|委派；代表|delegate tasks
coordinate|协调|coordinate activities
morale|士气|boost staff morale
''', 'Reasonable workloads and fair incentives can improve productivity and employee well-being.', '合理的工作量与公平的激励可以提高生产率、改善员工福祉。')

add('经济与消费①：市场和增长', '''
economy|经济；节约|the global economy
stimulate|刺激；促进|stimulate economic growth
investment|投资|investment in infrastructure
demand|需求；要求|consumer demand
consumption|消费；消耗|household consumption
recession|经济衰退|an economic recession
inflation|通货膨胀|rising inflation
revenue|收入；财政收入|tax revenue
profit|利润；获益|make a profit
expenditure|支出|public expenditure
budget|预算|a limited budget
deficit|赤字；不足|a budget deficit
surplus|盈余；过剩|a trade surplus
asset|资产；有用的人或物|financial assets
liability|负债；不利因素|assets and liabilities
capital|资本；首都|human capital
loan|贷款；借出|a bank loan
currency|货币|foreign currency
fluctuate|波动|prices fluctuate
prosperity|繁荣|economic prosperity
''', 'Investment can stimulate demand, but policymakers must also consider inflation and public expenditure.', '投资可以刺激需求，但政策制定者也必须考虑通胀和公共支出。')

add('经济与消费②：购物和决策', '''
affordable|负担得起的|affordable products
rational|理性的；合理的|rational decisions
prioritize|优先处理；确定优先次序|prioritize essential needs
alternative|替代选择；替代的|an affordable alternative
evaluate|评估|evaluate product quality
consumer|消费者|consumer behaviour
purchase|购买|make a purchase
retail|零售|retail sales
discount|折扣；低估|offer a discount
bargain|便宜货；讨价还价|a good bargain
impulse|冲动；推动力|impulse buying
advertisement|广告|a misleading advertisement
brand|品牌|brand loyalty
loyalty|忠诚|customer loyalty
preference|偏好|consumer preferences
durable|耐用的|durable goods
warranty|保修；担保|a one-year warranty
refund|退款|request a refund
transaction|交易|an online transaction
subscription|订阅；订购费|a monthly subscription
''', 'Rational consumers evaluate alternatives and prioritize essential needs before making a purchase.', '理性的消费者在购买前会评估不同选择，并优先考虑基本需求。')

add('环境与气候①：问题和影响', '''
environment|环境|protect the environment
emission|排放；排放物|carbon emissions
consequence|后果|environmental consequences
deteriorate|恶化|air quality deteriorates
urgent|紧迫的|an urgent need
climate|气候|climate change
greenhouse|温室|greenhouse gases
pollution|污染|air pollution
contaminate|污染；使受污染|contaminate drinking water
drought|干旱|a prolonged drought
flood|洪水；淹没|severe flooding
habitat|栖息地|habitat loss
biodiversity|生物多样性|preserve biodiversity
ecosystem|生态系统|a fragile ecosystem
extinction|灭绝|on the brink of extinction
deforestation|毁林；森林砍伐|prevent deforestation
degradation|退化；恶化|soil degradation
toxic|有毒的|toxic waste
irreversible|不可逆的|irreversible damage
disruption|扰乱；中断|ecosystem disruption
''', 'Rising emissions can have serious consequences, making environmental protection an urgent priority.', '排放增加可能造成严重后果，因此环境保护成为紧迫的优先事项。')

add('环境与气候②：保护和治理', '''
sustainable|可持续的|sustainable development
conserve|保护；节约|conserve natural resources
mitigate|减轻；缓解|mitigate climate change
implement|实施|implement environmental policies
awareness|意识；认识|raise environmental awareness
recycle|回收利用|recycle household waste
reuse|再次使用|reuse packaging
biodegradable|可生物降解的|biodegradable materials
conservation|保护；节约|wildlife conservation
restoration|修复；恢复|ecological restoration
preserve|保护；保存|preserve natural habitats
rehabilitate|修复；使康复|rehabilitate damaged land
offset|抵消；弥补|offset carbon emissions
footprint|足迹；占用或影响范围|a carbon footprint
neutral|中立的；中性的|carbon-neutral production
legislation|法律；立法|environmental legislation
enforce|执行；强制实施|enforce regulations
compliance|遵守；合规|compliance with standards
monitor|监测；监督|monitor air quality
stewardship|管理和保护责任|environmental stewardship
''', 'Governments should implement sustainable policies and raise public awareness to conserve resources.', '政府应实施可持续政策并提高公众意识，以保护资源。')

add('能源与资源', '''
renewable|可再生的|renewable energy
transition|转变；过渡|the energy transition
dependence|依赖|dependence on fossil fuels
deplete|消耗；使枯竭|deplete natural resources
efficient|高效的|energy-efficient appliances
fossil|化石；化石的|fossil fuels
coal|煤|coal consumption
petroleum|石油|petroleum production
solar|太阳的|solar power
wind|风；风力|wind energy
nuclear|核的|nuclear energy
hydroelectric|水力发电的|hydroelectric power
grid|电网；网格|the power grid
storage|储存|energy storage
battery|电池|battery technology
reserve|储备；保留|oil reserves
scarcity|稀缺；不足|water scarcity
abundant|丰富的；充足的|abundant resources
extract|提取；开采|extract minerals
utilize|利用|utilize resources effectively
''', 'The transition to renewable energy can reduce dependence on fossil fuels.', '向可再生能源转型可以减少对化石燃料的依赖。')

add('健康与医疗①：预防和生活方式', '''
maintain|维持；保养；主张|maintain a healthy lifestyle
prevent|预防；阻止|prevent disease
moderate|适度的；温和的|moderate exercise
balanced|均衡的|a balanced diet
beneficial|有益的|beneficial to health
nutrition|营养|adequate nutrition
nutrient|营养物质|essential nutrients
obesity|肥胖|childhood obesity
sedentary|久坐的|a sedentary lifestyle
intake|摄入量|daily calorie intake
metabolism|新陈代谢|the body's metabolism
immune|免疫的；不受影响的|the immune system
chronic|慢性的；长期的|chronic disease
symptom|症状|common symptoms
diagnose|诊断|diagnose an illness
treatment|治疗；对待|medical treatment
therapy|疗法|physical therapy
recover|恢复；康复|recover from an illness
screening|筛查|cancer screening
hygiene|卫生|personal hygiene
''', 'A balanced diet and moderate exercise are beneficial to health and help prevent disease.', '均衡饮食与适度运动有益健康，有助于预防疾病。')

add('健康与医疗②：服务和公共卫生', '''
healthcare|医疗保健|access to healthcare
afford|负担得起；抽得出|afford medical treatment
adequate|足够的；适当的|adequate medical care
intervention|干预|early intervention
priority|优先事项|a public health priority
physician|医生；内科医生|consult a physician
surgeon|外科医生|an experienced surgeon
patient|病人；有耐心的|patient care
prescription|处方|prescription drugs
antibiotic|抗生素|antibiotic resistance
vaccine|疫苗|develop a vaccine
infection|感染|prevent infection
contagious|有传染性的|a contagious disease
epidemic|流行病；流行|a flu epidemic
pandemic|大流行病；大流行的|a global pandemic
mortality|死亡；死亡率|infant mortality
longevity|长寿|increased longevity
insurance|保险|medical insurance
coverage|覆盖范围；保险保障|insurance coverage
burden|负担|the burden of disease
''', 'Early intervention and adequate healthcare should be public health priorities.', '早期干预与充足的医疗服务应成为公共卫生的优先事项。')

add('心理与情绪', '''
resilience|韧性；恢复能力|build emotional resilience
cope|应对；处理|cope with stress
anxiety|焦虑|reduce anxiety
confidence|信心|build confidence
supportive|给予支持的|a supportive environment
depression|抑郁；萧条|clinical depression
distress|痛苦；忧虑|emotional distress
frustration|挫败；沮丧|a sense of frustration
isolation|孤立；隔离|social isolation
loneliness|孤独|feelings of loneliness
optimistic|乐观的|optimistic about the future
pessimistic|悲观的|a pessimistic outlook
self-esteem|自尊|low self-esteem
empathy|共情；同理心|show empathy
sympathy|同情；赞同|express sympathy
mindfulness|正念；专注当下|mindfulness practice
counselling|心理咨询；辅导|psychological counselling
relieve|缓解；解除|relieve stress
overwhelm|使不堪重负|feel overwhelmed
trauma|创伤|psychological trauma
''', 'A supportive environment helps people cope with anxiety and build resilience.', '支持性的环境有助于人们应对焦虑、增强心理韧性。')

add('人口与老龄化', '''
demographic|人口的；人口统计的|demographic change
ageing|老龄化；变老的|an ageing population
decline|下降；衰退；婉拒|a decline in birth rates
proportion|比例|a growing proportion
challenge|挑战；质疑|address a challenge
fertility|生育能力；肥沃|the fertility rate
birthrate|出生率|a falling birthrate
lifespan|寿命|the average lifespan
elderly|年老的|elderly people
retirement|退休|the retirement age
pension|养老金|a pension system
dependency|依赖；依存|the dependency ratio
caregiver|照护者|family caregivers
intergenerational|代际的|intergenerational support
household|家庭；住户|household income
migration|迁移；移民|rural-to-urban migration
immigrant|移民|immigrant families
emigrant|移居国外的人|emigrants from rural regions
population|人口|population growth
density|密度|population density
''', 'Demographic change and an ageing population create challenges for pension systems.', '人口结构变化与人口老龄化给养老金制度带来挑战。')

add('社会公平与公共服务', '''
inequality|不平等|income inequality
inclusive|包容的；兼收并蓄的|an inclusive society
distribute|分配；分发|distribute resources fairly
welfare|福利；福祉|social welfare
disadvantaged|处境不利的|disadvantaged groups
poverty|贫困|reduce poverty
deprivation|匮乏；剥夺|material deprivation
discrimination|歧视；辨别|racial discrimination
prejudice|偏见|gender prejudice
equality|平等|equality of opportunity
equity|公平；权益|social equity
privilege|特权；优待|social privilege
entitlement|应有权利；应得福利|benefit entitlement
subsidy|补贴|a housing subsidy
subsidize|补贴；资助|subsidize public transport
assistance|帮助；援助|financial assistance
charity|慈善；慈善组织|a charitable organization
volunteer|志愿者；自愿做|volunteer work
solidarity|团结；相互支持|social solidarity
justice|公正；司法|social justice
''', 'An inclusive society distributes resources fairly and supports disadvantaged groups.', '包容的社会公平分配资源，并支持弱势群体。')

add('城市与交通', '''
urbanization|城市化|rapid urbanization
infrastructure|基础设施|urban infrastructure
congestion|拥堵|traffic congestion
commute|通勤|commute to work
convenient|方便的|convenient public transport
metropolitan|大都市的|a metropolitan area
municipal|市政的|municipal services
residential|住宅的|a residential area
commercial|商业的|a commercial district
pedestrian|行人；步行的|pedestrian safety
vehicle|车辆；载体|electric vehicles
transit|运输；通行|public transit
railway|铁路|high-speed railway networks
route|路线|a bus route
capacity|容量；能力|transport capacity
expansion|扩张；扩建|urban expansion
renovation|翻新；修缮|building renovation
sanitation|环境卫生|sanitation services
sewage|污水|sewage treatment
amenity|便利设施（常用复数）|public amenities
''', 'Investment in public transport can reduce congestion and make commuting more convenient.', '投资公共交通可以缓解拥堵，使通勤更加便利。')

add('乡村与农业', '''
rural|乡村的|rural development
revitalize|使恢复活力；振兴|revitalize rural communities
agriculture|农业|sustainable agriculture
output|产量；输出|agricultural output
livelihood|生计|improve farmers’ livelihoods
cultivation|种植；培养|rice cultivation
irrigation|灌溉|an irrigation system
fertilizer|肥料|organic fertilizer
pesticide|农药|reduce pesticide use
harvest|收获；收成|a good harvest
crop|农作物|food crops
grain|谷物；颗粒|grain production
livestock|牲畜（集合名词）|raise livestock
fertile|肥沃的；多产的|fertile soil
arable|可耕作的|arable land
erosion|侵蚀；削弱|soil erosion
mechanization|机械化|agricultural mechanization
cooperative|合作社；合作的|a farming cooperative
organic|有机的|organic farming
vegetation|植被|natural vegetation
''', 'Better irrigation can increase crop yields and improve rural livelihoods.', '更好的灌溉设施可以提高作物产量、改善乡村生计。')

add('文化与传统①：保护和传承', '''
heritage|遗产；传统|cultural heritage
inherit|继承|inherit a tradition
diversity|多样性|cultural diversity
identity|身份；认同|cultural identity
transmit|传递；传播|transmit knowledge
intangible|非物质的；难以触知的|intangible cultural heritage
tangible|有形的；可感知的|tangible benefits
custom|风俗；习惯|local customs
ritual|仪式；惯例|a traditional ritual
festival|节日|a traditional festival
craftsmanship|工艺；技艺|traditional craftsmanship
artisan|工匠|skilled artisans
legacy|遗产；遗留影响|a lasting legacy
ancestral|祖先的；祖传的|an ancestral home
indigenous|本土的；原住民的|indigenous knowledge
authentic|真实的；正宗的|authentic local culture
conventional|传统的；常规的|conventional methods
contemporary|当代的；同时代的|contemporary culture
revival|复兴；恢复|a cultural revival
continuity|连续性；延续|cultural continuity
''', 'Protecting cultural heritage helps communities maintain their identity and transmit traditions.', '保护文化遗产有助于社区保持文化认同、传承传统。')

add('文化与传统②：艺术和表达', '''
appreciate|欣赏；感激；理解|appreciate traditional art
exhibit|展出；表现出|exhibit works of art
represent|代表；表现|represent cultural values
inspire|激励；启发|inspire creativity
distinctive|独特的；有辨识度的|a distinctive style
calligraphy|书法|Chinese calligraphy
porcelain|瓷；瓷器|blue-and-white porcelain
ceramic|陶瓷的；陶瓷制品|ceramic art
embroidery|刺绣|traditional embroidery
sculpture|雕塑|a stone sculpture
architecture|建筑；建筑风格|traditional architecture
aesthetic|审美的|aesthetic value
masterpiece|杰作|an artistic masterpiece
literature|文学；文献|classical literature
poetry|诗；诗歌（集合称谓）|classical poetry
narrative|叙事；故事|a historical narrative
symbol|象征；符号|a symbol of unity
symbolize|象征|symbolize good fortune
exhibition|展览|an art exhibition
creativity|创造力|encourage creativity
''', 'Museums exhibit distinctive works of art that inspire visitors to appreciate cultural diversity.', '博物馆展出独具特色的艺术作品，启发参观者欣赏文化多样性。')

add('旅游与历史地理', '''
destination|目的地|a popular tourist destination
attract|吸引|attract visitors
historical|历史的|historical records
magnificent|壮丽的|magnificent scenery
reputation|名声；声誉|an international reputation
scenic|风景优美的|a scenic area
landscape|风景；地貌|a rural landscape
monument|纪念碑；历史遗迹|an ancient monument
relic|遗物；遗迹|cultural relics
dynasty|朝代|the Tang dynasty
imperial|帝国的；皇帝的|an imperial palace
ancient|古代的|ancient civilization
civilization|文明|Chinese civilization
archaeological|考古的|archaeological discoveries
excavation|挖掘；发掘|an archaeological excavation
itinerary|行程|a travel itinerary
accommodation|住宿（英式通常不可数）|tourist accommodation
hospitality|好客；接待服务|local hospitality
souvenir|纪念品|buy souvenirs
ecotourism|生态旅游|develop ecotourism
''', 'The city attracts visitors with its magnificent landscape and rich historical heritage.', '这座城市以壮丽的风景和丰富的历史遗产吸引游客。')

add('发展与对外交流', '''
cooperation|合作|international cooperation
mutual|相互的；共同的|mutual understanding
exchange|交流；交换|cultural exchange
contribute|贡献；促成；捐助|contribute to development
achievement|成就|scientific achievements
globalization|全球化|economic globalization
bilateral|双边的|bilateral relations
multilateral|多边的|multilateral cooperation
diplomatic|外交的|diplomatic relations
partnership|伙伴关系|a strategic partnership
dialogue|对话|promote dialogue
consensus|共识|reach a consensus
interdependence|相互依存|economic interdependence
integration|融合；一体化|regional integration
reform|改革|economic reform
opening-up|对外开放|reform and opening-up
modernization|现代化|agricultural modernization
manufacturing|制造业；制造|advanced manufacturing
logistics|物流|modern logistics
connectivity|互联互通；连通性|regional connectivity
''', 'International cooperation and cultural exchange can promote mutual understanding.', '国际合作与文化交流可以促进相互理解。')

add('媒体与信息', '''
credible|可信的|credible sources
disseminate|传播；散布|disseminate information
misleading|误导的|misleading claims
analytical|分析的；善于分析的|analytical thinking
distinguish|区分；辨别|distinguish fact from opinion
journalism|新闻业；新闻工作|responsible journalism
outlet|媒体机构；出口；销售点|a news outlet
headline|新闻标题|a newspaper headline
editorial|社论；编辑的|an editorial decision
broadcast|广播；播出|a live broadcast
circulation|发行量；流通|newspaper circulation
audience|受众；观众|a global audience
source|来源|a reliable source
rumour|谣言；传闻|spread a rumour
misinformation|错误信息|combat misinformation
propaganda|宣传；鼓动性信息|political propaganda
sensational|耸人听闻的；轰动的|sensational headlines
censorship|审查制度|media censorship
impartial|公正的；不偏不倚的|impartial reporting
scrutiny|仔细审查|public scrutiny
''', 'Critical readers check credible sources and distinguish evidence from misleading claims.', '有批判意识的读者会核查可信来源，区分证据和误导性说法。')

add('人际关系与沟通', '''
communicate|交流；传达|communicate effectively
resolve|解决；决心|resolve a conflict
respect|尊重|mutual respect
trust|信任|build trust
constructive|建设性的|constructive criticism
interaction|互动|face-to-face interaction
relationship|关系|maintain relationships
conflict|冲突|a conflict of interest
compromise|妥协；折中|reach a compromise
dispute|争议；争论|settle a dispute
persuade|说服|persuade someone to act
convince|使确信；说服|convince someone of the value
assertive|自信坚定的|assertive communication
aggressive|好斗的；激进的|aggressive behaviour
passive|被动的|a passive response
intimate|亲密的|an intimate friendship
reciprocal|相互的；互惠的|reciprocal support
alienate|使疏远|alienate potential supporters
reconcile|使和解；调和|reconcile different interests
rapport|融洽关系|establish rapport
''', 'Constructive communication helps people resolve conflicts and build trust.', '建设性的沟通有助于人们解决冲突、建立信任。')

add('个人成长与时间管理', '''
pursue|追求；从事|pursue a goal
persist|坚持；持续存在|persist in one's efforts
self-regulation|自我调节；自律|develop self-regulation
reflect|反思；反映|reflect on experience
fulfil|实现；履行|fulfil one's potential
aspiration|志向；愿望|career aspirations
ambition|抱负；雄心|achieve an ambition
determination|决心；确定|strong determination
perseverance|毅力|patience and perseverance
setback|挫折|overcome a setback
obstacle|障碍|remove an obstacle
procrastination|拖延|avoid procrastination
routine|惯例；常规|a daily routine
habit|习惯|form a habit
potential|潜力；潜在的|realize one's potential
autonomy|自主权；自主性|learner autonomy
independence|独立|financial independence
maturity|成熟|emotional maturity
fulfilment|满足感；履行|personal fulfilment
aspire|渴望；立志|aspire to become a teacher
''', 'People who persist through setbacks are more likely to fulfil their potential.', '能够在挫折中坚持的人更有可能发挥自身潜力。')

add('论证核心动词①：影响和改变', '''
affect|影响|affect daily life
influence|影响；影响力|influence decisions
undermine|削弱；损害|undermine public trust
strengthen|加强|strengthen cooperation
alleviate|减轻；缓解|alleviate poverty
accelerate|加速|accelerate development
hinder|阻碍|hinder progress
impair|损害；削弱|impair memory
disrupt|扰乱；中断|disrupt normal activity
reshape|重塑|reshape the economy
modify|修改；改变|modify a plan
adjust|调整；适应|adjust to a new environment
reverse|逆转；颠倒|reverse a trend
restore|恢复；修复|restore confidence
sustain|维持；支撑|sustain economic growth
intensify|增强；加剧|intensify competition
exacerbate|加剧；使恶化|exacerbate inequality
jeopardize|危及|jeopardize safety
impede|妨碍；阻碍|impede development
trigger|引发|trigger a debate
''', 'Excessive pressure may undermine confidence, while timely support can alleviate stress.', '过度的压力可能削弱信心，而及时的支持可以缓解压力。')

add('论证核心动词②：解决和推进', '''
remedy|纠正；补救；补救办法|remedy a problem
tackle|着手解决|tackle unemployment
overcome|克服|overcome difficulties
ensure|确保|ensure equal opportunities
enable|使能够|enable students to learn independently
empower|赋能；给予权力|empower local communities
foster|促进；培养|foster cooperation
boost|促进；提高|boost confidence
encourage|鼓励|encourage participation
advocate|提倡；支持|advocate equal rights
propose|提出；提议|propose a solution
recommend|推荐；建议|recommend practical measures
devise|设计；想出|devise a strategy
formulate|制定；系统阐述|formulate a policy
execute|执行；实施|execute a plan
accomplish|完成|accomplish a task
attain|达到；获得|attain a goal
optimize|优化|optimize resource use
safeguard|保护；保障|safeguard public interests
eliminate|消除；淘汰|eliminate barriers
''', 'Practical measures can tackle inequality and enable more people to access education.', '切实可行的措施可以应对不平等，让更多人获得教育机会。')

add('阅读核心动词①：表达和判断', '''
acknowledge|承认；致谢|acknowledge the limitations
emphasize|强调|emphasize the importance
attribute|把……归因于；属性|attribute success to effort
justify|证明……合理|justify a decision
assess|评估|assess the risks
claim|声称；主张；索赔|claim that something is true
assert|断言；维护|assert one's rights
contend|主张；争取|contend that change is needed
argue|论证；争论|argue for a policy
imply|暗示；意味着|imply a connection
suggest|建议；表明；暗示|suggest a possible explanation
reveal|揭示|reveal a pattern
demonstrate|证明；展示|demonstrate the benefits
illustrate|说明；举例说明|illustrate a point
highlight|突出；强调|highlight the risks
underline|强调；在……下画线|underline the need for action
question|质疑；问题|question an assumption
rebut|反驳|rebut a misleading claim
refute|反驳；驳斥|refute an argument
reject|拒绝接受；否定|reject a proposal
''', 'The findings highlight the risks, but they do not justify every proposed restriction.', '这些发现凸显了风险，但不能证明所有拟议的限制都合理。')

add('阅读核心动词②：过程和关系', '''
involve|涉及；包含；使参与|involve local residents
require|需要；要求|require careful planning
depend|依赖；取决于|depend on the context
derive|获得；源自|derive benefits from exercise
constitute|构成|constitute a major obstacle
comprise|包括；由……组成|the report comprises five sections
consist|由……组成；在于|consist of three parts
incorporate|包含；纳入|incorporate feedback into a plan
exclude|排除|exclude irrelevant information
entail|涉及；必然需要|entail additional costs
undergo|经历；经受|undergo major changes
emerge|出现；显现|new problems emerge
arise|出现；发生|arise from a misunderstanding
occur|发生；出现|occur frequently
coincide|同时发生；一致|coincide with a change
precede|先于|precede an event
follow|跟随；接着发生；遵循|follow the instructions
accompany|伴随；陪同|accompany economic growth
correspond|相符；对应；通信|correspond to a category
interact|相互作用；交流|interact with others
''', 'Effective reform requires planning and involves changes that may entail additional costs.', '有效的改革需要规划，也涉及可能带来额外成本的变化。')

add('评价与态度形容词', '''
feasible|可行的|a feasible solution
essential|必不可少的|essential skills
inevitable|不可避免的|an inevitable consequence
controversial|有争议的|a controversial policy
appropriate|适当的|appropriate measures
plausible|看似合理的|a plausible explanation
convincing|有说服力的|convincing evidence
questionable|可疑的；有争议的|a questionable assumption
skeptical|怀疑的|skeptical of the claims
reluctant|不情愿的|reluctant to change
enthusiastic|热情的|enthusiastic about the project
indifferent|漠不关心的|indifferent to criticism
favorable|有利的；赞同的|favorable conditions
adverse|不利的|adverse effects
desirable|值得拥有的；理想的|a desirable outcome
practical|实际的；实用的|practical advice
viable|可行的；能存活的|a viable alternative
crucial|至关重要的|a crucial factor
trivial|琐碎的；不重要的|a trivial detail
inherent|固有的|inherent limitations
''', 'A feasible solution should be appropriate to local conditions and address essential needs.', '可行的解决方案应适合当地条件，并回应基本需求。')

add('趋势、程度与比较', '''
trend|趋势|a long-term trend
increase|增加|a steady increase
decrease|减少|a sharp decrease
gradual|逐渐的|a gradual improvement
considerable|相当大的|considerable progress
dramatic|急剧的；戏剧性的|a dramatic change
steady|稳定的；持续的|steady growth
marginal|微小的；边缘的|a marginal improvement
slight|轻微的|a slight decline
steep|陡峭的；急剧的|a steep rise
peak|峰值；达到顶峰|reach a peak
plateau|平台期；趋于稳定|reach a plateau
stagnant|停滞的；不流动的|a stagnant economy
approximately|大约|approximately half
roughly|大约；粗略地|roughly equal
respectively|分别；各自|10 and 20 percent respectively
relatively|相对地|relatively stable
comparatively|比较而言|comparatively low
predominantly|主要地；占主导地位地|predominantly rural
increasingly|越来越|increasingly important
''', 'The data show a gradual increase in participation and considerable differences between regions.', '数据显示参与度逐渐上升，不同地区之间存在较大差异。')

add('逻辑衔接与论证名词', '''
therefore|因此|therefore require further study
nevertheless|然而；尽管如此|nevertheless remain important
whereas|然而；鉴于|whereas others disagree
despite|尽管（后接名词等）|despite the difficulties
consequently|因此；结果|consequently face new challenges
moreover|此外；而且|moreover provide support
furthermore|此外；而且|furthermore reduce costs
nonetheless|尽管如此；然而|nonetheless remain useful
conversely|相反地|conversely increase the risk
otherwise|否则；在其他方面|otherwise lose the opportunity
whereby|凭此；借以|a system whereby people cooperate
thereby|从而；借此|thereby improving efficiency
hence|因此；由此|hence the need for reform
likewise|同样地|likewise benefit from training
accordingly|因此；相应地|adjust the plan accordingly
rationale|理由；基本原理|the rationale for a policy
premise|前提|a basic premise
implication|可能的影响；含意|policy implications
paradox|悖论；矛盾现象|an apparent paradox
dilemma|两难处境|face a dilemma
''', 'The policy may reduce costs; nevertheless, its long-term implications require careful assessment.', '这项政策可能降低成本；然而，其长期影响仍需认真评估。')

add('听力场景①：校园与研究', '''
appointment|预约；任命|make an appointment
reschedule|重新安排时间|reschedule a meeting
extension|延期；延伸|an extension of the deadline
clarify|澄清；说明|clarify the requirements
available|可获得的；有空的|available resources
advisor|导师；顾问|an academic advisor
supervisor|导师；主管|a research supervisor
lecturer|讲师；演讲者|a university lecturer
department|系；部门|the physics department
laboratory|实验室|a laboratory experiment
equipment|设备（不可数）|laboratory equipment
facility|设施；能力|research facilities
reference|参考；提及|reference materials
citation|引用；引文|a citation in an essay
plagiarism|剽窃；抄袭|avoid plagiarism
draft|草稿；起草|a first draft
proofread|校对|proofread a paper
presentation|报告；展示|give a presentation
conference|会议|an academic conference
workshop|研习班；车间|a writing workshop
''', 'Please make an appointment with your advisor to clarify the requirements before requesting an extension.', '申请延期前，请预约导师，弄清任务要求。')

add('听力场景②：商业和日常事务', '''
reservation|预订；保留意见|make a reservation
confirm|确认；证实|confirm a booking
inquiry|询问；调查|a customer inquiry
complaint|投诉；抱怨|make a complaint
inconvenience|不便|cause inconvenience
receipt|收据；收到|keep the receipt
invoice|发票；账单|pay an invoice
deposit|押金；存款；沉积物|pay a deposit
installment|分期付款的一期|pay in installments
overdue|逾期的|an overdue payment
cancel|取消|cancel an order
postpone|推迟|postpone a meeting
notify|通知|notify customers of a change
dispatch|派遣；发出|dispatch an order
delivery|递送；交付|delivery charges
shipment|装运；货物|a delayed shipment
inventory|库存；清单|check inventory levels
merchandise|商品（集合称谓）|return defective merchandise
defective|有缺陷的|a defective product
replacement|替换；替代品|request a replacement
''', 'Please confirm your reservation and notify us of any changes to avoid inconvenience.', '请确认预订，如有变动请通知我们，以免造成不便。')

add('自然科学与生命', '''
species|物种（单复数同形）|endangered species
evolution|进化；演变|biological evolution
adaptation|适应；改编|adaptation to climate change
survival|生存；存活|survival in the wild
mechanism|机制；机械装置|a biological mechanism
organism|生物；有机体|a living organism
gene|基因|gene expression
genetic|遗传的；基因的|genetic variation
inheritance|遗传；继承|genetic inheritance
mutation|突变|a genetic mutation
cell|细胞；小室|a nerve cell
tissue|组织；纸巾|muscle tissue
molecule|分子|a water molecule
compound|化合物；复合的|a chemical compound
substance|物质；实质|a harmful substance
chemical|化学的；化学物质|a chemical reaction
reproduce|繁殖；复制|reproduce rapidly
predator|捕食者|a natural predator
prey|猎物；捕食|birds of prey
instinct|本能|a survival instinct
''', 'Adaptation helps species survive, while genetic variation provides a basis for evolution.', '适应有助于物种存活，而遗传变异为进化提供基础。')

add('认知、记忆与行为', '''
perception|感知；看法|public perception
attention|注意力；关注|sustain attention
cognitive|认知的|cognitive ability
conscious|有意识的；察觉到的|a conscious decision
recognize|认出；承认；意识到|recognize a pattern
perceive|感知；认为|perceive a threat
recall|回忆；召回|recall information
retrieve|检索；取回|retrieve memories
encode|编码|encode information
stimulus|刺激；刺激物|respond to a stimulus
response|反应；回应|an emotional response
behaviour|行为|human behaviour
tendency|倾向|a tendency to hesitate
intuition|直觉|rely on intuition
reasoning|推理|logical reasoning
judgment|判断；判断力|make a judgment
consciousness|意识；知觉|lose consciousness
concentration|专注；浓度|improve concentration
fatigue|疲劳|mental fatigue
alertness|警觉；清醒|maintain alertness
''', 'Sleep affects cognitive ability and helps people sustain attention and recall information.', '睡眠影响认知能力，并有助于人们保持注意力、回忆信息。')

add('公共政策与法律', '''
policy|政策|public policy
authority|权力；当局；权威|local authorities
obligation|义务；责任|a legal obligation
protect|保护|protect individual rights
prohibit|禁止|prohibit discrimination
regulation|规定；监管|safety regulations
restriction|限制|impose restrictions
ban|禁止；禁令|a ban on smoking
penalty|处罚|a financial penalty
violation|违反；侵犯|a violation of the law
offence|违法行为；冒犯|a criminal offence
legitimate|合法的；正当的|legitimate concerns
legal|法律的；合法的|legal protection
illegal|非法的|illegal activities
right|权利；正确的|the right to education
liberty|自由|individual liberty
citizen|公民|citizen participation
governance|治理|effective governance
bureaucracy|官僚体制；官僚作风|reduce bureaucracy
petition|请愿；请愿书|sign a petition
''', 'Public policy should protect individual rights while ensuring that legal obligations are met.', '公共政策应保护个人权利，同时确保法律义务得到履行。')

add('风险、危机与应对', '''
risk|风险；冒……风险|assess a risk
precaution|预防措施|take precautions
prepare|准备|prepare for emergencies
respond|回应；应对|respond to a crisis
rebound|恢复；反弹|rebound after a crisis
hazard|危险；危害|a safety hazard
threat|威胁|pose a threat to health
crisis|危机（复数crises）|a financial crisis
emergency|紧急情况|an emergency response
disaster|灾难|a natural disaster
catastrophe|大灾难|an environmental catastrophe
contingency|意外情况；应急安排|a contingency plan
evacuate|撤离；疏散|evacuate residents
rescue|营救|a rescue operation
relief|救济；缓解；宽慰|disaster relief
rehabilitation|康复；修复|post-disaster rehabilitation
fragile|脆弱的|a fragile economy
robust|强健的；稳健的|a robust system
susceptible|易受影响的|susceptible to disease
precautionary|预防性的|precautionary measures
''', 'Communities should take precautions and prepare contingency plans to respond to emergencies.', '社区应采取预防措施，制定应急预案以应对紧急情况。')

add('熟词生义：阅读中的常见转换', '''
account|解释；账户；叙述|account for the difference
issue|问题；期号；发布|issue a statement
subject|主题；受试者；使遭受|subject to change
term|术语；学期；期限|in the long term
charge|收费；指控；负责；充电|be in charge of a project
spring|春天；泉水；突然出现|spring from experience
novel|新颖的；小说|a novel approach
fine|罚款；精细的；好的|pay a fine
address|处理；地址；演说|address public concerns
faculty|能力；全体教师；院系|mental faculties
interest|利益；利息；兴趣|in the public interest
critical|关键的；批判的；批评的|a critical stage
minute|极小的；分钟（形容词与名词读音不同）|minute differences
sound|可靠的；声音|sound judgment
mean|意味着；平均值；吝啬的|the mean score
bear|承担；忍受；熊|bear the cost
yield|产量；产生；让步|yield to pressure
volume|体积；数量；音量；卷|a large volume of data
scale|规模；刻度；等级|on a large scale
range|范围；一系列；变化|range from A to B
''', 'A sound explanation should account for the evidence rather than merely repeat a familiar claim.', '可靠的解释应说明证据，而不是仅重复熟悉的说法。')

add('抽象名词与易混词：考前收束', '''
factor|因素|a key factor
approach|方法；接近|an effective approach to learning
strategy|策略|a long-term strategy
outcome|结果|a positive outcome
impact|影响；冲击|have an impact on society
aspect|方面|an important aspect
dimension|维度；方面|the social dimension
context|背景；语境|in a different context
framework|框架|a theoretical framework
criterion|标准（复数criteria）|meet the criteria
principle|原则；原理|a basic principle
principal|主要的；校长；本金|the principal cause
effect|影响；结果；实现|a positive effect
extent|程度；范围|to some extent
constraint|约束；限制|time constraints
resource|资源|limited resources
perspective|视角；观点|from a different perspective
phenomenon|现象（复数phenomena）|a common phenomenon
procedure|程序；步骤|a standard procedure
process|过程；处理|the learning process
''', 'An effective strategy considers the context, available resources and the principal constraints.', '有效的策略会考虑背景、可用资源和主要约束。')

START = date(2026, 10, 26)
from revised_plan import make_plan, final_review_groups, PLAN_VERSION
ORIGINAL_DAYS = DAYS
DAYS = make_plan(ORIGINAL_DAYS, ROOT)
TOTAL_WORDS = sum(len(d['rows']) for d in DAYS)
LEARN_DAYS = sum(bool(d['rows']) for d in DAYS)
TITLE = '六级高频词汇｜48天逐日复习资料'
INTRO = '''适用：四级571分、六级目标550分；侧重词汇补基础、写作翻译输出，同时支持阅读和听力。
周期：2026年10月26日—12月12日。10月26日保留原20词；10月27日至12月6日安排36个40词学习日、5个周复习日，共1460个不同词条（含固定搭配）。12月7—11日集中复习，12月12日轻量回顾。
选词说明：这是围绕六级常见主题、学术阅读、听力场景和写译表达编写的实用核心词表，不是依据某一真题语料库统计的频次榜，也不替代完整考纲词表。例句与小练习均为自编，不是真题引文。
学习边界：优先掌握表内词义和搭配，不要求一次记住所有义项。词组内少量辅助词不另计新词。已经熟悉的词快速测过，将省下的时间用于真题生词。'''
METHOD = '''词汇学习约40分钟：10分钟主动回忆约30个旧词，25分钟识记当天40词及搭配，5分钟检查理解。当天学习页已列出具体复习词，首次衔接日10月27日只有20个已学旧词，不虚构额外旧词。
★表示当天6个优先运用词（10月26日保留5个）：每词独立造一个句子，尽量用表内搭配，并检查语法和语义。将这6个词的造句、改写或翻译融入每天30分钟的写译训练，不要求40词全部默写。另留30分钟听力、20分钟阅读或复盘。
普通日优先从约1、3、7天前的学习日各抽10词；间隔落在复习日时，回溯至最近的新词日。已有标黄词可优先替换同数量的熟词。每周一（11月2、9、16、23、30日）只总复习，不安排40个新词；12月7日起进入考前回顾。
40词是目标而非硬指标：前25—30词先掌握，后10—15词可按记忆情况选学。如果连续几天旧词回忆不足一半，先降至25—30词并处理错词。识义按当天完整词表计分，未学部分不算会；例如会25词就填25/40。
高阶不等于生僻。抽象学术词、熟词僻义、论证词和主题搭配交叉安排，原词表中的基础词作为快速查漏。每周回看真题，实际识别和造句情况比接触词数更重要。
搭配提醒：access to、contribute to、adapt to等中的to是介词；enable / persuade someone to do中的to引出不定式。尽量整块记忆，不能把同义词在所有语境中直接互换。'''
TRAPS = [
('affect / effect', 'affect通常作动词“影响”；effect通常作名词“影响、结果”，也可作动词“实现”，如effect change。'),
('economic / economical', 'economic指“经济的”；economical指“节约的、经济实惠的”。后者为对比拓展词。'),
('principal / principle', 'principal：主要的、校长、本金；principle：原则、原理。'),
('infer / imply', '作者或证据imply（暗示）；读者infer（推断）。'),
('rise / raise / arise', 'rise是不及物动词“上升”；raise通常带宾语“提高、筹集”；arise指“出现、发生”。rise、raise为对比拓展。'),
('considerable / considerate', 'considerable：相当大的；considerate：体贴的。considerate为对比拓展。'),
('conserve / preserve / reserve', 'conserve侧重保护、节约资源；preserve侧重保存、保护免受破坏；reserve可指预留、储备。'),
('credible / reliable / valid', 'credible侧重可信；reliable侧重可靠；valid侧重有效或论据成立。'),
('efficient / effective', 'efficient侧重效率；effective侧重有效果。effective为对比拓展。'),
('species / criterion / phenomenon', 'species单复数同形；criterion的复数是criteria；phenomenon的复数是phenomena。'),
('evidence / information / equipment / feedback', '这些词在所列常见含义下通常不可数；不要写an evidence、equipments、feedbacks。information为搭配辅助词。'),
('despite / although', 'despite后接名词、代词或动名词；although后接从句。不要写despite of；不要把despite直接接完整从句。although为对比拓展。'),
]

def label(i):
    dt = START + timedelta(days=i-1)
    return f'Day {i:02d}｜{dt.month}月{dt.day}日'

def due(i):
    return DAYS[i-1]['source_days']

def due_text(i):
    return '、'.join(f'Day {j:02d}（{(START+timedelta(days=j-1)).strftime("%m/%d")}）' for j in due(i)) or '无指定旧词；可用四级易忘词热身'

REVIEW = final_review_groups(DAYS)
EXAM = ['acquire knowledge','access to education','allocate resources','enhance efficiency',
        'sustainable development','cultural heritage','contribute to development',
        'account for the difference','to some extent','from a different perspective']

def validate():
    assert len(DAYS) == 42
    words = [row[0] for d in DAYS for row in d['rows']]
    assert len(words) == 1460 and len(set(words)) == 1460, 'duplicate headwords'
    assert [i for i,d in enumerate(DAYS,1) if not d['rows']] == [8,15,22,29,36]
    assert all(len(d['rows'])==(20 if i==1 else 40) for i,d in enumerate(DAYS,1) if d['rows'])
    assert all(len(d['review_rows'])==(0 if i==1 else 20 if i==2 else 30) for i,d in enumerate(DAYS,1))
    assert (START + timedelta(days=41)) == date(2026,12,6)
    assert (START + timedelta(days=47)) == date(2026,12,12)
    covered = [x for _, a, b, _ in REVIEW for x in range(a,b+1)]
    assert covered == list(range(1,43))
    assert all(1<=j<i for i in range(1,43) for j in due(i))
    assert not any('待去重' in str(d) for d in DAYS)

def markdown():
    out = [f'# {TITLE}', INTRO, '## 怎么使用', METHOD,
           '## 日期导航', '| 日期 | 组别 | 主题 |', '|---|---|---|']
    for i,d in enumerate(DAYS,1):
        dt = START+timedelta(days=i-1)
        out.append(f'| {dt:%m/%d} | Day {i:02d} | {d["theme"]} |')
    for i,a,b,t in REVIEW:
        dt=START+timedelta(days=i-1)
        out.append(f'| {dt:%m/%d} | Day {i:02d} | 集中复习 Day {a:02d}—{b:02d}：{t} |')
    out += ['| 12/12 | Day 48 | 考试日：不加新词，回顾10个熟悉搭配 |', '## 逐日新词与回忆任务']
    for i,d in enumerate(DAYS,1):
        out += [f'### {label(i)}｜{d["theme"]}', f'旧词来源：{due_text(i)}。']
        if d['rows']:
            out += [f'本日{len(d["rows"])}词；识义 __/{len(d["rows"])}。★词各造一句。',
                    '| 序号 | 英文（★优先运用） | 核心意思 | 常用搭配 |', '|---|---|---|---|']
        else:
            out += ['今天不加新词。复盘本周6个学习日，重点检查下列30个旧词。']
        for k,(w,z,p) in enumerate(d['rows'],1):
            out.append(f'| {k:02d} | {"★ " if k<=d["active_count"] else ""}{w} | {z} | {p} |')
        if d['review_rows']:
            out += [f'**本日旧词复习：{len(d["review_rows"])}词**', '| 英文 | 核心意思 | 常用搭配 |','|---|---|---|']
            out += [f'| {w} | {z} | {p} |' for w,z,p in d['review_rows']]
        if d['rows']:
            out += ['**主动运用：**']+[f'- 用 **{w}** 造一句；可用搭配：{p}。' for w,z,p in d['rows'][:d['active_count']]]
            out += [f'**主题中译英：** {d["zh"]}', f'完成后核对文末「Day {i:02d}参考表达」。不同的正确译法也可以。']
        else:
            out += ['从上表选6个易错词各造一句；重译本周2句旧练习。']
    out += ['## 最后六天：集中回顾']
    for i,a,b,t in REVIEW:
        n=sum(len(DAYS[j-1]['rows']) for j in range(a,b+1))
        out += [f'### {label(i)}｜{t}',
                f'复习范围：Day {a:02d}—{b:02d}，共{n}词。没有新词。',
                '快速扫描全批词，可分两次完成；重点复习30个最不熟的词，选6词造句，重译2句旧练习。',
                f'具体回看：'+ '；'.join(f'Day {j:02d} {DAYS[j-1]["theme"]}' for j in range(a,b+1) if DAYS[j-1]['rows'])+'。']
    out += [f'### {label(48)}｜考试日', '只用5—10分钟回顾下面10个已经学过的搭配及个人易错词，不再安排35分钟新词任务。',
            '\n'.join(f'- {p}' for p in EXAM), '## 易混词和使用提醒']
    out += [f'- **{a}：**{b}' for a,b in TRAPS]
    out += ['## 每日中译英：参考表达', '以下都是自编参考句。不同的正确译法也可以；核查信息完整、搭配和语法，不追求与参考句一字不差。']
    out += [f'**Day {i:02d}参考表达：** {d["en"]}' for i,d in enumerate(DAYS,1) if d['rows']]
    out += ['## 个人真题错词补充页', '每天最多补3—5个真正影响理解的真题词，不额外强求背完；若当天已超时，用这些词替换已熟练的新词。',
            '| 日期 | 词或搭配 | 真题中的意思/原句出处 | 次日回忆 | 第3天 | 第7天 |',
            '|---|---|---|---|---|---|']
    out += ['| | | | □ | □ | □ |']*10
    content = '\n\n'.join(out) + '\n'
    return re.sub(r'(?m)(^\|[^\n]*\|)\n\n(?=\|)', r'\1\n', content)

def review_html(lesson):
    esc=html.escape
    rows=lesson['review_rows']
    if not rows:return '<p class="meta">首日没有指定旧词任务。</p>'
    sources='、'.join(f'<a href="#d{i}">Day {i:02d}</a>' for i in lesson['source_days'])
    out=[f'<details class="daily-review"><summary>复习旧词 · {len(rows)}词</summary><p class="meta">来源：{sources}。先遮释义回忆，再核查；标黄旧词可优先替换已熟练词。</p><div class="tablewrap"><table><thead><tr><th>序号</th><th>英文</th><th>核心意思</th><th>常用搭配</th></tr></thead><tbody>']
    for k,(w,z,p) in enumerate(rows,1):
        out.append(f'<tr data-review-word="{esc(w)}"><td><button type="button" class="word-toggle" data-word="{esc(w)}" aria-pressed="false" aria-label="标记生词 {esc(w)}">{k:02d}</button></td><td class="word">{esc(w)}</td><td class="meaning" tabindex="0"><span>{esc(z)}</span></td><td class="phrase" tabindex="0"><span>{esc(p)}</span></td></tr>')
    out.append('</tbody></table></div></details>')
    return '\n'.join(out)

def webpage():
    esc = html.escape
    chunks = [f'''<!doctype html><html lang="zh-CN"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1"><title>{TITLE}</title>
<style>
:root{{color-scheme:light;--ink:#213047;--muted:#52627a;--accent:#156b67;--line:#d9e2e8}}
*{{box-sizing:border-box}}body{{margin:0;background:#edf2f5;color:var(--ink);font:16px/1.7 "Microsoft YaHei","Segoe UI",sans-serif}}
main{{max-width:1080px;margin:30px auto;padding:34px;background:white;border-radius:14px}}h1{{font-size:30px;line-height:1.4}}h2{{margin-top:32px}}h3{{margin-top:0;color:var(--accent)}}p{{margin:10px 0}}.muted{{color:var(--muted)}}
.tools{{position:sticky;top:0;background:#fffef6;padding:10px;display:flex;gap:10px;flex-wrap:wrap;border-bottom:1px solid var(--line);z-index:2}}button,select{{font:inherit;padding:6px 12px;border:1px solid #a7bfc0;border-radius:6px;background:white;color:var(--ink)}}button{{cursor:pointer}}
.nav{{display:grid;grid-template-columns:repeat(auto-fit,minmax(145px,1fr));gap:7px}}.nav a{{padding:6px 10px;border:1px solid var(--line);border-radius:5px;text-decoration:none;color:var(--accent);font-size:14px}}
.day{{border:1px solid var(--line);padding:22px;border-radius:10px;margin:24px 0;scroll-margin-top:85px}}.meta{{font-size:14px;color:var(--muted)}}.tablewrap{{overflow:auto}}table{{border-collapse:collapse;width:100%;font-size:15px}}th,td{{padding:8px 10px;border-bottom:1px solid var(--line);text-align:left;vertical-align:top}}th{{background:#eff7f6}}td:first-child{{width:48px}}td.word{{width:185px;font-weight:600}}.star{{color:#b67700}}.quiz{{background:#f3f7fa;padding:12px;border-radius:6px;margin-top:16px}}details{{margin-top:8px}}summary{{cursor:pointer;color:var(--accent)}}
.word-toggle{{min-width:36px;min-height:36px;padding:3px 7px;border:1px solid #bdc9d4;background:transparent;font-variant-numeric:tabular-nums}}.word-toggle:hover{{background:#fff3c4}}.word-toggle:focus-visible,.score:focus-visible{{outline:3px solid #156b67;outline-offset:2px}}tr.marked>td{{background:#fff0a8;print-color-adjust:exact;-webkit-print-color-adjust:exact}}tr.marked .word-toggle{{border-color:#9b6b00;color:#624400}}.score{{width:66px;padding:4px 6px;border:1px solid #8da4b5;border-radius:5px;font:inherit;background:white;color:var(--ink);text-align:center}}.vocab-panel{{border:1px solid var(--line);padding:20px;border-radius:10px;margin-top:24px;scroll-margin-top:85px}}.vocab-panel h2{{margin-top:0}}.vocab-count{{font-size:15px;color:var(--muted);font-weight:normal}}#vocab-empty{{padding:18px;background:#f3f7fa;border-radius:6px}}[hidden]{{display:none!important}}.save-warning{{color:#945000}}
body.test .meaning span{{visibility:hidden}}body.test .meaning:hover span,body.test .meaning:focus span{{visibility:visible}}
body.test .phrase span{{visibility:hidden}}body.test .phrase:hover span,body.test .phrase:focus span{{visibility:visible}}
@media(max-width:650px){{main{{margin:0;padding:18px;border-radius:0}}.day{{padding:12px}}table{{min-width:660px}}h1{{font-size:25px}}}}
@media print{{@page{{size:A4;margin:13mm}}body{{background:white;font-size:10pt}}main{{max-width:none;margin:0;padding:0}}.tools,.nav,.noprint{{display:none}}.day{{break-before:page;border:0;padding:0;margin:0}}table{{font-size:10pt}}th,td{{padding:5px 7px}}tr{{break-inside:avoid}}h3{{font-size:15pt}}body.test .meaning span,body.test .phrase span{{visibility:visible}}details{{display:none}}.answerbook{{break-before:page}}.answers p{{break-inside:avoid}}}}
</style><style>
:root{{--ink:#24352f;--muted:#78847c;--accent:#34725d;--line:#e5e9e3}}html{{scroll-behavior:smooth}}body{{background:#f3f4ef;font-size:15px}}main{{max-width:1120px;background:transparent;margin:32px auto;padding:0 28px;border-radius:0}}h1{{font-size:38px;letter-spacing:-1.5px;margin:10px 0}}h2{{font-size:22px;letter-spacing:-.5px}}a{{color:var(--accent)}}.hero{{padding:18px 0 24px}}.eyebrow{{font-size:12px;letter-spacing:2.5px;color:var(--accent);font-weight:700}}.hero-sub{{color:#68766b;margin:4px 0 24px}}.hero-stats{{display:flex;gap:32px}}.hero-stats strong{{font-size:23px;letter-spacing:-.5px;margin-right:7px}}.hero-stats span{{font-size:12px;color:var(--muted)}}.tools{{background:#f3f4eff2;backdrop-filter:blur(12px);border:0;padding:10px 0;gap:8px}}button,select{{border-color:#dce3da;border-radius:9px;padding:8px 13px;font-size:13px}}button:hover{{border-color:#92b29d}}.calendar{{background:#fff;border:1px solid #e0e6dc;border-radius:20px;padding:26px;margin:16px 0 28px;box-shadow:0 8px 36px #263c2a05;scroll-margin-top:75px}}.cal-heading{{display:flex;align-items:center;justify-content:space-between;gap:18px;margin-bottom:20px}}.cal-heading h2{{margin:0;font-size:23px}}.cal-sub{{font-size:12px;color:var(--muted);margin:4px 0 0}}.month-tabs{{display:flex;background:#f1f4ee;padding:4px;border-radius:11px;gap:3px}}.month-tabs button{{border:0;background:transparent;white-space:nowrap;padding:7px 16px;color:#738073}}.month-tabs button[aria-selected="true"]{{background:white;color:#2c604b;box-shadow:0 2px 7px #2b482512;font-weight:700}}.weekdays,.month-grid{{display:grid;grid-template-columns:repeat(7,minmax(0,1fr))}}.weekdays div{{padding:9px 0 14px;text-align:center;font-size:12px;color:#8c968e}}.weekdays div:nth-last-child(-n+2){{color:#b38d77}}.month-grid{{gap:7px}}.cal-date{{min-height:108px;padding:10px 11px;border:1px solid #e8ece5;border-radius:10px;text-decoration:none;color:var(--ink);position:relative;transition:background .16s,border-color .16s,transform .16s}}a.cal-date:hover{{background:#f3f8f1;border-color:#8eae99;transform:translateY(-2px)}}a.cal-date:focus-visible{{outline:3px solid #34725d;outline-offset:2px}}.cal-date.inactive{{background:#fafbf8;color:#c9cec6;border-color:transparent;min-height:108px}}.cal-date.blank{{background:transparent;border:0}}.date-top{{display:flex;justify-content:space-between;align-items:center;gap:4px}}.date-number{{font-size:19px;line-height:1.2;font-weight:600}}.day-label{{font-size:10px;color:#98a393}}.date-topic{{font-size:11px;line-height:1.5;color:#66725f;height:33px;margin-top:8px;display:-webkit-box;-webkit-line-clamp:2;-webkit-box-orient:vertical;overflow:hidden}}.date-state{{font-size:10px;color:#94a08c;display:flex;gap:6px;margin-top:5px;flex-wrap:wrap}}.cal-date.recorded{{background:#edf5ec;border-color:#cadfc7}}.cal-date.recorded .date-state{{color:#39714e}}.cal-date.today{{border:2px solid #34725d;padding:9px 10px}}.cal-date.today .date-number{{color:#34725d}}.cal-date.selected{{box-shadow:inset 0 0 0 2px #8bae92}}.cal-date.review-day{{background:#f8f4eb;border-color:#ece2ce}}.cal-date.exam-day{{background:#b75936;color:white;border-color:#b75936}}.exam-day .date-topic,.exam-day .date-state,.exam-day .day-label{{color:#ffe9db}}.cal-footer{{display:flex;justify-content:space-between;gap:14px;flex-wrap:wrap;padding-top:19px;font-size:11px;color:#84907e}}.cal-legend{{display:flex;gap:15px;align-items:center;flex-wrap:wrap}}.dot{{display:inline-block;width:8px;height:8px;border-radius:50%;margin-right:5px;background:#d3e7cf}}.dot.review{{background:#e5d7b9}}.dot.exam{{background:#b75936}}.guide{{background:#eaf0e5;border:1px solid #dfe8d7;border-radius:14px;padding:17px 21px;margin:0 0 22px}}.guide summary{{color:#3d5d42;font-weight:600}}.guide p{{font-size:13px;color:#687660;line-height:1.85}}.vocab-panel,.day{{background:white;border-radius:16px;border-color:#e1e7dc;padding:24px}}.vocab-panel h2{{font-size:21px}}#vocab-empty{{background:#f5f7f1;color:#8a9582;padding:24px;text-align:center;font-size:13px}}.day h3{{font-size:18px}}th{{background:#f4f6f0;color:#718069;font-size:12px;font-weight:500}}td{{padding-top:11px;padding-bottom:11px}}.word-toggle{{border-color:#e2e7dc;color:#7d8c74}}.quiz{{background:#f4f6f0}}.about{{font-size:12px;color:#899381;margin:24px 0}}.about summary{{font-size:12px;color:#899381}}.vocab-count{{font-size:13px}}.meta{{color:#8a9484;font-size:12px}}
@media(max-width:650px){{main{{padding:0 12px;margin:16px auto}}h1{{font-size:30px}}.hero{{padding:10px 6px 18px}}.hero-stats{{gap:22px}}.calendar{{padding:15px 10px;border-radius:15px}}.cal-heading{{align-items:flex-start;gap:8px}}.cal-heading h2{{font-size:19px}}.month-tabs button{{padding:5px 9px;font-size:12px}}.cal-sub{{font-size:10px}}.month-grid{{gap:3px}}.cal-date,.cal-date.inactive{{min-height:95px;padding:7px 4px;border-radius:6px}}.cal-date.today{{padding:6px 3px}}.date-number{{font-size:16px}}.day-label{{display:none}}.date-topic{{font-size:9px;height:28px;margin-top:7px}}.date-state{{font-size:9px;gap:2px}}.date-state .weak-count{{display:none}}.cal-footer{{font-size:10px}}.day,.vocab-panel{{padding:15px}}.tools{{gap:5px}}.tools button,.tools select{{font-size:11px;padding:7px 9px}}.calendar table{{min-width:0}}}}
@media(prefers-reduced-motion:reduce){{html{{scroll-behavior:auto}}*{{transition:none!important}}}}
@media print{{main{{padding:0}}.hero-stats,.calendar,.about,.guide{{display:none}}.day,.vocab-panel{{border:0;background:white}}body{{background:white}}}}
 .site-nav{{display:flex;align-items:center;gap:8px;padding:12px 0;position:sticky;top:0;background:#f3f4eff5;backdrop-filter:blur(12px);z-index:3}}.site-nav a{{padding:8px 15px;border-radius:9px;text-decoration:none;color:#78847c;font-size:13px}}.site-nav a.active{{background:#e2ecdf;color:#315f45;font-weight:600}}body:not([data-view="calendar"]) .hero{{display:none}}.tools{{position:static;margin-top:8px}}.day{{margin-top:14px}}.day h3:focus{{outline:none}}.day-switch{{display:flex;justify-content:space-between;gap:10px;padding:12px 0 26px}}.day-switch a{{text-decoration:none;padding:9px 14px;border:1px solid #dce3da;border-radius:9px;font-size:13px}}.calendar{{margin-top:8px}}.route-tip{{font-size:12px;color:var(--muted)}}
@media print{{.site-nav,.day-switch{{display:none}}body[data-view="day"] .day{{break-before:auto}}}}
</style></head><body data-view="calendar"><main><header class="hero"><div class="eyebrow">CET–6 · STUDY PLANNER</div><h1>每天一点，离目标更近。</h1><p class="hero-sub">六级词汇进阶 · 2026.10.27 起调整</p><div class="hero-stats"><div><strong>40</strong><span>词 / 学习日</span></div><div><strong>1460</strong><span>词与搭配</span></div><div><strong>550</strong><span>目标分数</span></div></div></header><nav class="site-nav" aria-label="主导航"><a href="#calendar" data-view-link="calendar">学习日历</a><a href="#vocabulary" data-view-link="vocabulary">我的生词</a><a href="#guide" data-view-link="guide">学习方法</a></nav><noscript><p>请开启浏览器 JavaScript，点击日历日期后查看学习内容。</p></noscript>''']
    chunks += ['<div class="tools" id="study-tools" hidden><button id="mask" type="button" aria-pressed="false">遮住释义和搭配 · 自测</button><button type="button" id="print">打印 / 存为 PDF</button><select id="jump" aria-label="跳转日期"><option value="">跳到某一天…</option>']
    chunks += [f'<option value="d{i}">{esc(label(i))}</option>' for i in range(1,49)]
    chunks += ['</select><button type="button" id="back-calendar">回到日历</button></div>', '<section class="calendar" id="calendar" aria-label="备考日历"><div class="cal-heading"><div><h2>学习日历</h2><p class="cal-sub">40词学习日 · 约30词复习 · 每周一次总复习</p></div><div class="month-tabs" role="tablist" aria-label="选择月份">']
    for month in (10,11,12):
        chunks += [f'<button type="button" role="tab" id="tab-{month}" data-month="{month}" aria-selected="{str(month==10).lower()}" aria-controls="month-{month}" tabindex="{0 if month==10 else -1}">{month}月</button>']
    chunks += ['</div></div><div class="weekdays" aria-hidden="true">'+''.join(f'<div>{day}</div>' for day in '一二三四五六日')+'</div>']
    for month in (10,11,12):
        chunks += [f'<div id="month-{month}" role="tabpanel" aria-labelledby="tab-{month}" class="month-grid"'+(' hidden' if month!=10 else '')+'>']
        _, count = calendar.monthrange(2026,month)
        start_number = START.day if month == START.month else 1
        end_number = min(count,12) if month == 12 else count
        first = date(2026,month,start_number).weekday()
        chunks += ['<div class="cal-date blank" aria-hidden="true"></div>']*first
        for number in range(start_number,end_number+1):
            dt = date(2026,month,number)
            i = (dt-START).days+1
            if 1<=i<=48:
                topic = DAYS[i-1]['theme'].split('：')[0] if i<=42 else ('考前集中复习' if i<48 else '六级笔试 · 加油')
                learning = i<=42 and bool(DAYS[i-1]['rows'])
                kind = '' if learning else (' review-day' if i<48 else ' exam-day')
                state = '<span class="cal-score">待填写</span><span class="weak-count"></span>' if learning else ('回顾旧词' if i<48 else '15:00 开考')
                chunks += [f'<a href="#d{i}" class="cal-date{kind}" data-cal-day="{i}" data-date="{dt.isoformat()}" aria-label="{dt.month}月{number}日，Day {i:02d}，{esc(topic)}"><div class="date-top"><span class="date-number">{number}</span><span class="day-label">DAY {i:02d}</span></div><div class="date-topic">{esc(topic)}</div><div class="date-state">{state}</div></a>']
            else:
                chunks += [f'<div class="cal-date inactive"><span class="date-number">{number}</span></div>']
        chunks += ['<div class="cal-date blank" aria-hidden="true"></div>']*((-(first+end_number-start_number+1))%7)
        chunks += ['</div>']
    chunks += ['<div class="cal-footer"><div class="cal-legend"><span><i class="dot"></i>已记分</span><span><i class="dot review"></i>集中复习</span><span><i class="dot exam"></i>考试日</span></div><span id="calendar-progress" aria-live="polite">已记录 0 / 37 个学习日</span></div></section>', '<details class="guide" id="guide" hidden><summary>每天怎么学 · 40词进阶安排</summary>']
    chunks += [f'<p>{esc(p)}</p>' for p in METHOD.splitlines()]
    chunks += ['<p><a href="#resources">查看易混词、参考表达与补充资料</a></p></details>',
               '<p id="save-warning" class="save-warning" role="status" hidden>当前浏览器无法保存记录；本次仍可填写和标记，但刷新后可能丢失。</p>',
               '<section id="vocabulary" class="vocab-panel" hidden><h2>生词 <span id="vocab-count" class="vocab-count" aria-live="polite">（0词）</span></h2><p class="meta">汇总所有标黄的单词，按英文字母顺序排列。在这里点击序号也可取消标记，原表会同步更新。</p><p id="plan-migration" class="meta" hidden>已保留旧版生词标记与10月26日分数。其余日期已换词，旧分数保留在浏览器原记录中，不换算为新版分数。</p><p id="vocab-empty">还没有生词。先从日历选择日期，再点击每日词表中的序号。</p><div id="vocab-table" class="tablewrap" hidden><table><thead><tr><th>序号</th><th>英文</th><th>核心意思</th><th>常用搭配</th><th>学习日</th></tr></thead><tbody id="vocab-body"></tbody></table></div></section>',
               '<details class="about" id="about" hidden><summary>关于这份复习资料</summary>'+''.join(f'<p>{esc(p)}</p>' for p in INTRO.splitlines())+'</details>']
    for i,d in enumerate(DAYS,1):
        if not d['rows']:
            links='、'.join(f'<a href="#d{j}">Day {j:02d}</a>' for j in d['source_days'])
            chunks += [f'<section class="day" id="d{i}" hidden><h3 tabindex="-1">{esc(label(i))}｜{esc(d["theme"])}</h3><p>今天不加新词。先检查本周6个学习日，再重点回忆下面30词。</p><p class="meta">本周词表：{links}。</p>',review_html(d),'<div class="quiz">从本页旧词中选6个易错词，各造一句；核查搭配、语法和含义。对本周最差的2句翻译重新作答。</div></section>']
            continue
        maximum=len(d['rows'])
        review_links = '、'.join(f'<a href="#d{j}">Day {j:02d}</a>' for j in due(i)) or '无指定旧词；可用四级易忘词热身'
        chunks += [f'<section class="day" id="d{i}" hidden><h3 tabindex="-1">{esc(label(i))}｜{esc(d["theme"])}</h3>',
                   f'<p class="meta">旧词复习：{review_links}。</p><p class="route-tip">点击序号标黄生词，再点取消；分数与标记自动保存。</p>',
                   f'<p class="meta">{maximum}词 · '+('优先完成前25—30词；' if maximum==40 else '原安排保留；')+'★词各造一句。</p>'+review_html(d),
                   f'<p class="meta"><label for="score-{i}">识义 </label><input class="score" id="score-{i}" data-day="{i}" type="number" min="0" max="{maximum}" step="1" inputmode="numeric" placeholder="—" aria-label="Day {i:02d} 识义分数，0到{maximum}分"> /{maximum}</p>',
                   '<div class="tablewrap"><table><thead><tr><th>序号</th><th>英文</th><th>核心意思</th><th>常用搭配</th></tr></thead><tbody>']
        for k,(w,z,p) in enumerate(d['rows'],1):
            star='<span class="star">★ </span>' if k<=d['active_count'] else ''
            chunks += [f'<tr data-word-row="{esc(w)}"><td><button type="button" class="word-toggle" data-word="{esc(w)}" aria-pressed="false" aria-label="标记生词 {esc(w)}">{k:02d}</button></td><td class="word">{star}{esc(w)}</td><td class="meaning" tabindex="0"><span>{esc(z)}</span></td><td class="phrase" tabindex="0"><span>{esc(p)}</span></td></tr>']
        tasks=''.join(f'<li>用 <strong>{esc(w)}</strong> 造一句，建议搭配：{esc(p)}。</li>' for w,z,p in d['rows'][:d['active_count']])
        chunks += [f'</tbody></table></div><details class="quiz"><summary>主动运用 · {d["active_count"]}词各造一句</summary><ol>{tasks}</ol><p class="meta">这些是开放造句任务，没有唯一答案；先独立写，再检查搭配、主谓一致和信息是否合理。</p></details><div class="quiz"><strong>主题中译英：</strong>{esc(d["zh"])}<details><summary>完成后查看参考表达</summary><p>{esc(d["en"])}</p><p class="meta">自编例句；其他准确、自然的译法也可以。</p></details></div></section>']
    for i,a,b,t in REVIEW:
        total=sum(len(DAYS[j-1]['rows']) for j in range(a,b+1))
        chunks += [f'<section class="day" id="d{i}" hidden><h3 tabindex="-1">{esc(label(i))}｜集中复习</h3><p><strong>{esc(t)}</strong></p><p>范围：Day {a:02d}—{b:02d}，共{total}词；没有新词。快速扫描全批词，重点复习标黄词和最不熟的30词。</p>',
                   '<p>全批快测可分两次完成；当天重点处理30个易忘词，选6词造句，重译2句旧练习。</p><ul>']
        chunks += [f'<li><a href="#d{j}">Day {j:02d}：{esc(DAYS[j-1]["theme"])}</a></li>' for j in range(a,b+1) if DAYS[j-1]['rows']]
        chunks += ['</ul><p class="meta">不加新词；优先复习个人生词，再处理本批30个弱词、6词造句和2句重译。</p></section>']
    chunks += [f'<section class="day" id="d48" hidden><h3 tabindex="-1">{esc(label(48))}｜考试日</h3><p>只用5—10分钟回顾以下10个熟悉搭配及个人易错词，不加新词。</p><ul>']
    chunks += [f'<li>{esc(p)}</li>' for p in EXAM]
    chunks += ['</ul></section><nav id="day-switch" class="day-switch" aria-label="切换学习日" hidden><a id="previous-day" href="#d1">← 前一天</a><a href="#calendar">返回日历</a><a id="next-day" href="#d2">后一天 →</a></nav><section id="resources" hidden><h2>易混词和使用提醒</h2><ul>']
    chunks += [f'<li><strong>{esc(a)}：</strong>{esc(b)}</li>' for a,b in TRAPS]
    chunks += ['</ul><section class="answerbook"><h2>每日中译英参考表达</h2><p>以下均为自编例句。打印时在本节集中核对；不同的正确译法也可以。</p><div class="answers">']
    chunks += [f'<p><strong>Day {i:02d}：</strong>{esc(d["en"])}</p>' for i,d in enumerate(DAYS,1) if d['rows']]
    chunks += ['</div></section><h2>个人真题错词补充页</h2><p>每天最多补3—5个影响理解的真题词；超时则替换已熟练的新词。</p><div class="tablewrap"><table><thead><tr><th>日期</th><th>词 / 搭配</th><th>语境与意思 / 出处</th><th>次日 / 第3天 / 第7天</th></tr></thead><tbody>']
    chunks += ['<tr><td>____</td><td>____________</td><td>____________________</td><td>□　□　□</td></tr>']*10
    chunks += ['''</tbody></table></div><p class="muted">学习资料编写日期：2026年10月26日。词汇训练服务于理解和表达，不以背词数量代替真题检验。</p></section></main><script>
document.getElementById('mask').addEventListener('click',function(){const on=document.body.classList.toggle('test');this.setAttribute('aria-pressed',String(on));this.textContent=on?'显示释义和搭配':'遮住释义和搭配 · 自测';});
document.getElementById('print').addEventListener('click',()=>window.print());
document.getElementById('jump').addEventListener('change',function(){if(this.value)location.hash=this.value;});
document.getElementById('back-calendar').addEventListener('click',()=>{location.hash='calendar';});
const monthTabs = Array.from(document.querySelectorAll('[role="tab"][data-month]'));
function showMonth(month) {
  monthTabs.forEach(tab => {
    const active = Number(tab.dataset.month) === month;
    tab.setAttribute('aria-selected', String(active)); tab.tabIndex = active ? 0 : -1;
    document.getElementById(tab.getAttribute('aria-controls')).hidden = !active;
  });
}
monthTabs.forEach((tab,index) => {
  tab.addEventListener('click',()=>showMonth(Number(tab.dataset.month)));
  tab.addEventListener('keydown',event=>{
    let next;
    if(event.key==='ArrowRight') next=(index+1)%monthTabs.length;
    if(event.key==='ArrowLeft') next=(index+monthTabs.length-1)%monthTabs.length;
    if(event.key==='Home') next=0;
    if(event.key==='End') next=monthTabs.length-1;
    if(next===undefined)return;
    event.preventDefault();showMonth(Number(monthTabs[next].dataset.month));monthTabs[next].focus();
  });
});
const today = new Date();
const todayISO = `${today.getFullYear()}-${String(today.getMonth()+1).padStart(2,'0')}-${String(today.getDate()).padStart(2,'0')}`;
const todayCell = document.querySelector(`[data-date="${todayISO}"]`);
if(todayCell) {todayCell.classList.add('today');todayCell.setAttribute('aria-current','date');showMonth(today.getMonth()+1);}
function syncCalendarSelection() {
  const match = /^#d([1-9]|[1-3][0-9]|4[0-8])$/.exec(location.hash);
  const day = match ? Number(match[1]) : null;
  const view = day ? 'day' : (['#vocabulary','#guide','#resources'].includes(location.hash) ? location.hash.slice(1) : 'calendar');
  document.body.dataset.view = view;
  document.querySelectorAll('.day').forEach(section=>{section.hidden=section.id!==`d${day}`;});
  ['calendar','vocabulary','guide','resources'].forEach(id=>{document.getElementById(id).hidden=view!==id;});
  document.getElementById('about').hidden=view!=='guide';
  document.getElementById('guide').open=view==='guide';
  document.getElementById('study-tools').hidden=!['day','vocabulary'].includes(view);
  document.getElementById('jump').hidden=view!=='day';
  document.getElementById('jump').value=day ? `d${day}` : '';
  document.getElementById('day-switch').hidden=!day;
  if(day) {
    const previous=document.getElementById('previous-day'),next=document.getElementById('next-day');
    previous.hidden=day===1;previous.href=`#d${day-1}`;
    next.hidden=day===48;next.href=`#d${day+1}`;
    document.title=document.querySelector(`#d${day} h3`).textContent+'｜六级词汇';
  } else document.title='六级词汇｜'+({'calendar':'学习日历','vocabulary':'我的生词','guide':'学习方法','resources':'参考资料'}[view]);
  document.querySelectorAll('[data-view-link]').forEach(link=>{
    const active=link.dataset.viewLink===view || (view==='day'&&link.dataset.viewLink==='calendar') || (view==='resources'&&link.dataset.viewLink==='guide');
    link.classList.toggle('active',active);
    if(active)link.setAttribute('aria-current','page');else link.removeAttribute('aria-current');
  });
  const cell = Array.from(document.querySelectorAll('[data-cal-day]')).find(link=>link.getAttribute('href')===location.hash);
  document.querySelectorAll('.cal-date.selected').forEach(link=>link.classList.remove('selected'));
  if(cell) {cell.classList.add('selected');showMonth(Number(cell.dataset.date.slice(5,7)));}
  requestAnimationFrame(()=>{
    if(day)document.querySelector(`#d${day} h3`).focus({preventScroll:true});
    window.scrollTo({top:0,behavior:'instant'});
  });
}
window.addEventListener('hashchange',syncCalendarSelection);syncCalendarSelection();
''']
    words = [{'word':w, 'meaning':z, 'phrase':p, 'day':i, 'priority':k<=d['active_count']}
             for i,d in enumerate(DAYS,1) for k,(w,z,p) in enumerate(d['rows'],1)]
    chunks += ['const scoreLimits = '+json.dumps({i:len(d['rows']) for i,d in enumerate(DAYS,1) if d['rows']})+';']
    chunks += ['const vocabularyData = '+json.dumps(words,ensure_ascii=False).replace('<','\\u003c')+';', '''
(() => {
  const storageKey = 'cet6-study-progress-v2';
  const byWord = new Map(vocabularyData.map(item => [item.word, item]));
  const originalRows = new Map();
  document.querySelectorAll('[data-word-row],[data-review-word]').forEach(row=>{
    const word=row.dataset.wordRow||row.dataset.reviewWord;
    if(!originalRows.has(word))originalRows.set(word,[]);
    originalRows.get(word).push(row);
  });
  const scoreInputs = Array.from(document.querySelectorAll('.score'));
  const selected = new Set();
  const scores = {};
  const warning = document.getElementById('save-warning');
  let migrated = false;
  try {
    const current = localStorage.getItem(storageKey);
    let saved = JSON.parse(current || '{}');
    if(!current) {
      const legacy = JSON.parse(localStorage.getItem('cet6-study-progress-v1') || '{}');
      if(legacy && (legacy.selected || legacy.scores)) {
        saved={selected:legacy.selected||[],scores:{1:legacy.scores?.['1']},migrated:true};
      }
    }
    migrated=!!saved?.migrated;
    document.getElementById('plan-migration').hidden=!migrated;
    if (saved && Array.isArray(saved.selected)) saved.selected.forEach(word => { if (byWord.has(word)) selected.add(word); });
    if (saved && saved.scores && typeof saved.scores === 'object') {
      scoreInputs.forEach(input => {
        const value = saved.scores[input.dataset.day];
        if (Number.isInteger(value) && value >= 0 && value <= Number(input.max)) scores[input.dataset.day] = value;
      });
    }
  } catch (_) { warning.hidden = false; }
  function save() {
    try { localStorage.setItem(storageKey, JSON.stringify({selected:Array.from(selected), scores, migrated})); }
    catch (_) { warning.hidden = false; }
    updateCalendar();
  }
  function updateCalendar() {
    const counts = {};
    selected.forEach(word => {const day=byWord.get(word).day;counts[day]=(counts[day]||0)+1;});
    document.querySelectorAll('[data-cal-day]').forEach(link=>{
      const day=link.dataset.calDay;
      const score=link.querySelector('.cal-score');
      if(!score)return;
      const recorded=Object.hasOwn(scores,day);
      link.classList.toggle('recorded',recorded);
      score.textContent=recorded ? `识义 ${scores[day]}/${scoreLimits[day]}` : `${scoreLimits[day]}词`;
      link.querySelector('.weak-count').textContent=counts[day] ? `生词 ${counts[day]}` : '';
    });
    document.getElementById('calendar-progress').textContent=`已记录 ${Object.keys(scores).length} / ${Object.keys(scoreLimits).length} 个学习日`;
  }
  function syncRow(row, word) {
    const marked = selected.has(word);
    row.classList.toggle('marked', marked);
    const button = row.querySelector('.word-toggle');
    button.setAttribute('aria-pressed', String(marked));
    button.setAttribute('aria-label', `${marked ? '取消生词标记' : '标记生词'} ${word}`);
  }
  function cell(row, text, className) {
    const td = document.createElement('td');
    if (className) td.className = className;
    const span = document.createElement('span');
    span.textContent = text;
    td.append(span);
    if (className === 'meaning' || className === 'phrase') td.tabIndex = 0;
    row.append(td);
    return td;
  }
  const collator = new Intl.Collator('en', {sensitivity:'base'});
  function renderVocabulary() {
    const list = Array.from(selected, word => byWord.get(word)).sort((a,b) => collator.compare(a.word,b.word));
    const body = document.getElementById('vocab-body');
    const focusedWord = body.contains(document.activeElement) ? document.activeElement.dataset.word : null;
    const oldIndex = focusedWord ? Array.from(body.querySelectorAll('.word-toggle')).findIndex(button => button.dataset.word === focusedWord) : -1;
    const fragment = document.createDocumentFragment();
    list.forEach((item,index) => {
      const row = document.createElement('tr');
      row.className = 'marked';
      const numberCell = document.createElement('td');
      const button = document.createElement('button');
      button.type = 'button'; button.className = 'word-toggle'; button.dataset.word = item.word;
      button.textContent = String(index+1).padStart(2,'0');
      button.setAttribute('aria-pressed','true');
      button.setAttribute('aria-label',`取消生词标记 ${item.word}`);
      numberCell.append(button); row.append(numberCell);
      cell(row, (item.priority ? '★ ' : '') + item.word, 'word');
      cell(row, item.meaning, 'meaning'); cell(row, item.phrase, 'phrase');
      const link = document.createElement('a'); link.href = `#d${item.day}`;
      link.textContent = `Day ${String(item.day).padStart(2,'0')}`;
      const dayCell = document.createElement('td'); dayCell.append(link); row.append(dayCell);
      fragment.append(row);
    });
    body.replaceChildren(fragment);
    document.getElementById('vocab-count').textContent = `（${list.length}词）`;
    document.getElementById('vocab-empty').hidden = list.length > 0;
    document.getElementById('vocab-table').hidden = list.length === 0;
    if (oldIndex >= 0) {
      const buttons = body.querySelectorAll('.word-toggle');
      (buttons[Math.min(oldIndex, buttons.length-1)] || document.getElementById('mask')).focus({preventScroll:true});
    }
  }
  document.addEventListener('click', event => {
    const button = event.target.closest('button[data-word]');
    if (!button || !byWord.has(button.dataset.word)) return;
    const word = button.dataset.word;
    if (selected.has(word)) selected.delete(word); else selected.add(word);
    originalRows.get(word).forEach(row=>syncRow(row,word));
    renderVocabulary(); save();
  });
  scoreInputs.forEach(input => {
    if (Object.hasOwn(scores, input.dataset.day)) input.value = scores[input.dataset.day];
    input.addEventListener('input', () => {
      input.setCustomValidity('');
      if (input.value === '' && !input.validity.badInput) {
        delete scores[input.dataset.day]; save(); return;
      }
      const value = input.valueAsNumber;
      if (!Number.isInteger(value) || value < 0 || value > Number(input.max)) {
        input.setCustomValidity(`请输入0到${input.max}的整数`); return;
      }
      scores[input.dataset.day] = value; save();
    });
    input.addEventListener('change', () => input.reportValidity());
  });
  originalRows.forEach((rows,word) => rows.forEach(row=>syncRow(row,word)));
  renderVocabulary();
  updateCalendar();
})();
</script></body></html>''']
    return '\n'.join(chunks)

if __name__ == '__main__':
    validate()
    md = ROOT / '六级高频词汇_48天逐日复习资料.md'
    page = ROOT / '六级高频词汇_48天逐日复习资料.html'
    md.write_text(markdown(), encoding='utf-8')
    page.write_text(webpage(), encoding='utf-8')
    (ROOT / 'index.html').write_text(webpage(), encoding='utf-8')
    print(json.dumps({'days':48, 'new_word_days':LEARN_DAYS, 'unique_headwords':TOTAL_WORDS, 'priority_output_words':sum(d['active_count'] for d in DAYS),
                      'files':[str(md),str(page)]}, ensure_ascii=False))
