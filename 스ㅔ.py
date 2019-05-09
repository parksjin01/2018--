# -*- encoding:utf-8 -*-

import urllib2
import json

# f1 = """War is inconceivable without some image, or concept, of the enemy. It is the presence of the enemy that gives meaning and justification to war. ‘War follows from feelings of hatred’, wrote Carl Schmitt. ‘War has its own strategic, tactical, and other rules and points of view, but they all presuppose that the political decision has already been made as to who the enemy is’. The concept of the enemy is fundamental to the moral assessment of war: ‘The basic aim of a nation at war in establishing an image of the enemy is to distinguish as sharply as possible the act of killing from the act of murder’. However, we need to be cautious about thinking of war and the image of the enemy that informs it in an abstract and uniform way. Rather, both must be seen for the cultural and contingent phenomena that they are"""
# f2 = """Heritage is concerned with the ways in which very selective material artefacts, mythologies, memories and traditions become resources for the present. The contents, interpretations and representations of the resource are selected according to the demands of the present; an imagined past provides resources for a heritage that is to be passed onto an imagined future. It follows too that the meanings and functions of memory and tradition are defined in the present. Further, heritage is more concerned with meanings than material artefacts. It is the former that give value, either cultural or financial, to the latter and explain why they have been selected from the near infinity of the past. In turn, they may later be discarded as the demands of present societies change, or even, as is presently occurring in the former Eastern Europe, when pasts have to be reinvented to reflect new presents."""
# f3 = """We argue that the ethical principles of justice provide an essential foundation for policies to protect unborn generations and the poorest countries from climate change. Related issues arise in connection with current and persistently inadequate aid for these nations, in the face of growing threats to agriculture and water supply, and the rules of international trade that mainly benefit rich countries. Increasing aid for the world’s poorest peoples can be an essential part of effective mitigation. With 20 percent of carbon emissions from (mostly tropical) deforestation, carbon credits for forest preservation would combine aid to poorer countries with one of the most cost-effective forms of abatement. Perhaps the most cost-effective but politically complicated policy reform would be the removal of several hundred billions of dollars of direct annual subsidies from the two biggest recipients in the OECD ― destructive industrial agriculture and fossil fuels. Even a small amount of this money would accelerate the already rapid rate of technical progress and investment in renewable energy in many areas, as well as encourage the essential switch to conservation agriculture."""
# # f4 = """A defining element of catastrophes is the magnitude of their harmful consequences. To help societies prevent or reduce damage from catastrophes, a huge amount of effort and technological sophistication are often employed to assess and communicate the size and scope of potential or actual losses. This effort assumes that people can understand the resulting numbers and act on them appropriately. However, recent behavioral research casts doubt on this fundamental assumption. Many people do not understand large numbers. Indeed, large numbers have been found to lack meaning and to be underestimated in decisions unless they convey affect (feeling). This creates a paradox that rational models of decision making fail to represent. On the one hand, we respond strongly to aid a single individual in need. On the other hand, we often fail to prevent mass tragedies or take appropriate measures to reduce potential losses from natural disasters."""
# # f5 = """Marjorie Kinnan Rawlings, an American author born in Washington, D.C. in 1896, wrote novels with rural themes and settings. While she was young, one of her stories appeared in The Washington Post. After graduating from university, Rawlings worked as a journalist while simultaneously trying to establish herself as a fiction writer. In 1928, she purchased an orange grove in Cross Creek, Florida. This became the source of inspiration for some of her writings which included The Yearling and her autobiographical book, Cross Creek. In 1939, The Yearling, which was about a boy and an orphaned baby deer, won the Pulitzer Prize for Fiction. Later, in 1946, The Yearling was made into a film of the same name. Rawlings passed away in 1953, and the land she owned at Cross Creek has become a Florida State Park honoring her achievements"""
#
# k = {}
# for f in f1.split(" "):
#     k[f.lower()] = 1
# for f in f2.split(" "):
#     k[f.lower()] = 1
# for f in f3.split(" "):
#     k[f.lower()] = 1
# for f in f4.split(" "):
#     k[f.lower()] = 1
# for f in f5.split(" "):
#     k[f.lower()] = 1

# idx = 0
# print len(k.keys())
# print k.keys()[176:]
# for word in k.keys():
#     print idx/float(len(k.keys())), word
#     input = ""
#     while input != 'n' and input != 'N':
#         input = raw_input().strip()
#         print input
#     k[word] = input
#     idx += 1
#
# with open("temp_dict.json", "wt") as f:
#     f.write(f.dumps(k))

with open("meaning.json", "wt") as f:
    word = {
    "current":"현재의, 지금의, 통용되는, 흐름, 해류, 기류, 통화, 통용",
    "encourage":"격려하다, 용기를 북돋우다, 권장하다, 부추기다, 조장하다, 용기",
    "strategic":"전략상 중요한, 전략적인, 책략, 술수, 전략적",
    "provides":"제공하다, 주다, 규정하다",
    "new":"새, 새로운, 새 것, 새로 산, 새",
    "foundation":"토대, 재단",
    "increasing":"증대하는, 증가적인, 증가의",
    "emissions":"배출, 배출물, 배기가스",
    "be":"있다, 존재하다",
    "we":"우리",
    "justification":"타당한 이유, 옳음을 보여 주다, 정당화시키다, 해명하다, 행의 끝을 나란히 맞추다",
    "meanings":"뜻, 의미",
    "contingent":"대표단, 분견대, 파견대, 여부에 따라",
    "image":"이미지, 영상, 그림",
    "destructive":"파괴적인",
    "past":"지나간, 지난, 최근의, 이전의",
    "mythologies":"신화, 신화론",
    "killing":"살해, 살인, 기진맥진하게 만드는",
    "water":"물",
    "credits":"신용 거래, 외상, 융자, 신용도",
    "selective":"선택적인, 조심해서 고르는, 까다로운, 선별적인",
    "complicated":"복잡한",
    "distinguish":"구별하다, 구별 짓다, 차이를 보이다, 식별하다, 알아듣다",
    "carbon":"탄소",
    "poorer":"가난한, 빈곤한, 가난한 사람들, 불쌍한, 가련한",
    "both":"둘 다(의), …뿐만 아니라 …도",
    "about":"약, –쯤, –경, 거의, 이리저리",
    "cautious":"조심스러운, 신중한",
    "abatement":"감소, 감퇴; 경감, 완화, 경감액, 폐지, 금지, 제거, 배제, 중지, 각하, 실효",
    "most":"최대(의), 가장 많음, 대부분(의), 가장",
    "technical":"과학 기술의, 기술적인, 기술의, 전문적인, 기법, 기술",
    "of":"…의",
    "dollars":"달러",
    "politically":"정치적으로, 정치와 관련된, 정치적인, 정당의, 정파의, 정치에 관심이 있는, 정치적으로 활발한",
    "according":"…에 따라서; 일치하여.",
    "nations":"국민,민족, 나라,국가 , 족,종족",
    "justice":"공평성, 공정성, 정당성, 사법; 재판",
    "connection":"관련성, 연결, 접속(부)",
    "way":"방법, 방식, 식, 투, 태도, 양식, 길, 도로, 가로, 가도, 코스, 진로, 저쪽으로, 훨씬, 멀리",
    "act":"행동, 법률, 가식",
    "however":"아무리 …해도, 하지만, 그러나",
    "argue":"언쟁을 하다, 다투다, 주장하다, 논증하다, 분명히 보여주다, 입증하다",
    "onto":"…(위)로,  …쪽으로",
    "or":"아니면, 또는, 혹은, …이나, …도, 안 그러면, …보다 먼저, …에 앞서서",
    "this":"이; 이것",
    "own":"… 자신의, 직접 …한, 소유하다, 쉽게 이기다, 패배시키다",
    "war":"전쟁, 무찌르다, 정복하다",
    "presence":"있음, 존재(함), 참석, 주둔하는 사람들; 주둔군",
    "unborn":"아직 태어나지 않은, 태중의",
    "preservation":"보존, 지키기",
    "feelings":"느낌, 의견, 태도, 생각",
    "countries":"국가, 나라, 지역, 국민; 국가",
    "explain":"설명하다, 이유를 대다, 해명하다",
    "moral":"도덕과 관련된, 도덕상의, 도의상의, 도의적인, 도덕적으로 옳은, 도덕적인",
    "removal":"없애기, 제거, 제거, 철폐, 해고",
    "artefacts":"인공물",
    "from":"…에서(부터), …부터, …에게서 (온/받은)",
    "would":"…일 것이다, …였을 것이다",
    "oecd":"경제 협력 개발 기구",
    "value":"가치, 중요성, 유용성",
    "political":"정치와 관련된, 정치적인, 정당의, 정파의, 정치에 관심이 있는, 정치적으로 활발한",
    "two":"둘",
    "been":"지금까지 줄곧 …이다 ((계속)), 그때까지 …이었다",
    "why":"왜, 어째서, 무엇 때문에, 이유",
    "tropical":"열대 지방의, 열대의",
    "conservation":"보호, 보존, 관리",
    "too":"너무 (…한), …도 (또한), 그것도",
    "passed":"지나가 버린; (시험에) 합격한; 미불 배당의, 지나가다; 통과하다, 나아가다, 나아가게 하다, 떠나다, 없어지다, 사라지다, 끝나다, 죽다(off), 흐르다, 지나다, 산길, 고갯길; (숲·늪 따위로 통하는) 길.",
    "basic":"기본적인, 기초적인",
    "biggest":"가장 큰",
    "cost-effective":"비용 효율이 높은",
    "hundred":"백",
    "assessment":"평가, 평가 액",
    "gives":"(건네)주다, (선물로) 주다, 제공하다, (…해) 주다",
    "murder":"살인(죄), 살해, 죽을 지경인 것(힘들거나 불쾌한 일을 묘사할 때 씀), 살해하다",
    "the":"그, 예(例)의, 문제의, 특출한, 으뜸가는, 두드러진, 전형적인(따위), …라는 것, …인 것, 그만큼, …하면 그만큼",
    "world":"세계, 지구, 지구 같은 행성",
    "rich":"부유한, 돈 많은, 부자인, 부자들, 부유한 사람들",
    "that":"저, 그, 저 사람, 저이; 저것, …이기 때문에, …이므로, …이라니, …하다니, (…하는, …인) 바의",
    "phenomena":"현상, 경이로운 사람",
    "heritage":"유산",
    "interpretations":"해석, 이해, 설명"
}
    f.write(json.dumps(word))