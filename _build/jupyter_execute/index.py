#!/usr/bin/env python
# coding: utf-8

# # 寻找人类传播行为的基因
# 
# ![](./images/author.png)
# 

# 
# 二十一世纪是计算社会科学的时代。1998年邓肯·瓦茨关于小世界网络的模型和1999年阿尔伯特·巴拉巴西关于幂律和无标度网络的研究复兴了网络科学。一石激起千层浪，在学术领域产生了深远的影响。对于万维网上的人类行为的研究也形成了一个子领域，被称之为万维网科学(Web Science)；伴随着社交媒体等数字媒体的发展，社会网络分析开始受到前所未有的重视，社交网络上的信息流动网络研究也引起广泛的兴趣；与此同时，机器学习和数据科学取得了突飞猛进的发展，进一步加速了计算化的浪潮；在新闻传播产业当中，数据驱动的新闻生产、计算广告和媒体推荐系统开始成为席卷世界的潮流。面对海量的互联网数据、持续困扰人类的重大社会问题、崭新的理论视角、诱人的物理学模型，在世界大战中发展起来的新闻传播学研究会走向什么地方？这构成了困扰我们的时代问题，而计算传播学正是试图回应这一时代叩问的一种尝试。
# 
# 邓肯·瓦茨2008年在《自然》杂志上发表了题为《一个二十一世纪的科学》的文章。瓦茨认为社会科学才是二十一世纪的科学。社会系统当中充满了海量的异质性个体构成，这些个体之间的互动使得社会过程充满了复杂性。相比于自然科学，社会科学内部的复杂性更高，也更难研究。人类对于自然现象当中的很多规律已经非常了解，但对于社会现象的理解则通常非常有限。面对这些挑战，或许很多人可以做一群鸵鸟，只盯住让自己感觉舒适的领域，当危险来的时候干脆把头埋进沙子里，但是年轻人没有逃避的理由。年轻研究者唯有敢于冒险，才能走出不一样的路来。瓦茨指出网络科学的视角和大规模的互联网数据与实验为社会科学的发展提供了前所未有的理想条件，并乐观地认为“基于因特网的传播数据和互动将会变革我们对于人类群体行为的理解”。
# 
# ## 探索
# 
# “计算传播学”这个词语的提出源于香港城市大学互联网挖掘实验室成员之间在2012年初的一次组会讨论。互联网挖掘实验室由祝建华老师在2000年创建，最初起源于香港互联网使用调查项目。祝建华老师每周都会组织实验室成员进行讨论，讨论的主要内容除了每个人的研究进展之外，还包括文献分享、经验见闻等内容。置身于这样的一个实验室当中，使得我们较早就感受到在互联网人类传播行为的研究领域里来自跨学科的学术创新。这种范式的革新确立的一个标志是2009年大卫·拉泽等人发表在《科学》杂志上的一篇名为《计算社会科学》的文章。以拉泽为首的一群来自社会科学、计算机科学、网络科学等领域的资深研究者们宣告了计算社会科学的诞生。计算社会科学以大规模数据收集和数据分析作为主要的工具，采用网络科学作为主要的研究视角，力图揭示个体和群体行为的模式。
# 
# 2010年我作为博士生进入到香港城市大学互联网挖掘实验室以来，切身感受到了传播学研究者在互联网时代的身份焦虑。2012年1月，我在博客上写了一篇题为《计算传播学：宣言与版图》的短文，试图走一条计算驱动的研究道路，强调了将寻找人类传播行为的可计算基因作为计算传播学的发展使命。在更早一些时候，这篇小文章首先在一个名为《数字媒体阅读报告》的小圈子里流传。2012年2月，合作者林武来实验室交流，分享了关于Python编程基础、数据抓取、Hadoop使用等方面的知识。我们在此期间的一次组会中再次讨论了我们自己期待传播学将走向什么地方这一时代问题，并提出了计算传播（computational communication）的思路，激发了大家的进一步讨论的兴趣。在吴令飞的提议之下，计算传播学谷歌邮件组在2012年2月建立；2012年3月，计算传播学豆瓣小站正式建立；2012年底，吴令飞在多贝网上发布了一个名为计算传播学的系列课程；2014年暑假，我在腾讯实习期间，计算传播网正式建立。在此期间，我和许小可老师进行了一次讨论，我介绍了计算传播学的发展思路。当时，许小可、胡海波和张伦老师在写作一本关于社交网络上的信息传播的书，小可敏锐地觉察到他们所探索的研究范式可以采用计算传播学作为一个理论框架来进行理解，我也加入了这本书的写作。作为第一本计算传播学的图书，《社交网络上的计算传播学》于2015年在科学出版社正式出版。
# 
# 2014年之后，计算传播学开始步入学科建制化的发展阶段。南京大学新闻传播学院计算传播学实验中心经过半年多的筹备在2015年2月成立；2016年1月国际传播学会（ICA）计算方法兴趣小组建立；2016年9月25日第一届计算传播学论坛在南京成功举办，此次会议的主题是“计算传播时代”，旨在让人们认识到基于互联网传播产生的数据和互动性正在变革我们对人类传播行为的认知，传播学研究面临着新的问题与挑战，以人类传播行为的可计算性基础为研究中心的计算传播学为传播学的发展提供了更广阔的空间与可能性；2017年9月14日，第六届全国社会媒体处理大会（SMP2017）在北京举办，张伦和我一起在SMP讲习班介绍了《计算社会科学视角下的计算传播学》，此次会议还设有计算传播学分论坛；2017年9月22-24日，第二届计算传播学论坛暨工作坊在南京大学成功举办。
# 2017年计算传播学工作坊为期一天半，分为两个子题并行进行，分别为“信息传播的网络分析”(Network Approaches to Information Diffusion)和“文本数据处理方法”(Processing Text Data)。前者定位为高级程度，聚焦于计算传播学研究中的一个核心而又困难的题目，以探讨研究设计、理论模型、数据要求、方法选择等问题为主、操作问题为辅，适合已掌握基本方法并有一定研究经验者。后者定位为入门程度，介绍用于文本数据处理的各个步骤上的方法、工具、算法等，含有众多动手操作。这次工作坊“信息传播的网络分析”部分由张子柯和王成军主讲《网络信息传播基础》、许小可讲《网络信息传播实证研究》、胡海波和阮中远讲解《网络信息传播模型》，“文本数据处理方法”部分由张伦主讲《文本分析的基本步骤与方法》、王成军介绍《主题模型》、汪臻真主讲《情感分析》。在酝酿在大数据和人工智能时代，未来的计算社会科学家更需要训练问题意识、培养计算思维、增强数据挖掘和分析的能力，而这正是本书写作的一个重要目的。
# 
# 第二届计算传播学论坛暨工作坊的过程中，许小可、胡海波、张伦和我开始计划写一本《计算传播学导论》书。按照祝建华老师的建议，我们曾对参加了2016年第一届计算传播学论坛的研究者公开征集计算传播学工作坊的题目。经过汇总整理之后的题目包括：计算机模拟/多主体建模、社交媒体数据爬取、传播文本挖掘和主题模型分析、使用深度学习进行传播学研究、社交媒体数据的时间序列分析和空间分析、传播学研究和数据新闻的可视化方法、传播网络分析（社区识别、复杂网络与信息流动）、机器学习、意见形成、Python编程，以及如何教授新闻传播学专业的学生网络分析/数据新闻/编程。我们的想法是每年遴选两个主题组织计算传播学工作坊，系统地整理和组织工作坊教学材料，基于此形成《计算传播学导论》一书的基本材料。
# 
# ## 愿景
# 
# 计算传播学作为一个概念的提出主要源于计算社会科学的发展。直到计算社会科学成为研究热点之后，计算传播作为一个概念才被正式提出。另外一种定义计算传播学的思路是计算传播的产业实践，可以将计算传播定义为数据驱动的、借助于可计算方法所进行的传播过程，而分析计算传播现象的研究领域就是计算传播学。计算传播的应用有很多，例如数据新闻、计算广告、媒体推荐系统等，在过去的几年里，产生了深远的影响。数据新闻风靡全球，重要的国际媒体和国内媒体纷纷采用数据新闻，以开放数据、数据挖掘、可视化的方式提供信息；计算广告备受瞩目，不管是门户网站、搜索引擎，还是社交媒体，纷纷将计算广告当做数据变现的重要渠道，以可计算的方法对广告进行拍卖，实现媒体、内容和用户三方的匹配；媒体推荐系统成为个性化信息获取的重要途径，既包括传统的社交新闻网站，也包括今日头条这种后起之秀，它们纷纷采用协同过滤的方法为用户提供信息，建立了新的信息把关模式。
# 
# 计算传播学将传播学研究置于数据和计算方法的坚固基础上。数据作为一种新的石油，解放了社会科学家对于理论的过度依赖。随着数字媒体的发展，人类社会积累的人类传播行为数据的规模日趋庞大，详尽地记录了社会发展和人类互动的各种细节。运用这些生动的人类传播行为数据，可以从更细的颗粒度、更大的样本规模上让我们捕捉社会的发展。毫无疑问，对于数据的挖掘依赖于人类的计算能力的提高，依赖于跨学科的研究方法和研究视角。我们人类传播行为的基因恰恰隐藏在互动性当中，但这种人类传播行为的互动性本身也使得传播过程充满了复杂性。网络科学为捕捉到纷繁复杂的人类互动提供了一个很好的视角。从数据出发，借助于计算方法和好的理论视角，就可以更好地刻画人类传播行为的模式和法则。需要指出的是，不管是模式还是法则，本身并没有能够回答我们所观察到的社会现实是由何种社会机制构成，因而需要通过建构数学和物理模型的方式来解释社会机制并基于社会机制预测具体的社会现实。社会机制虽然可能非常复杂，但背后的普适性原理却可以非常简单。计算传播学试图从重大的社会问题出发，系统地收集并分析人类传播行为的数据，刻画数据背后的行为模式，探索模式背后的社会机制，试图上升到一般性的原理，达到更好地解释和预测人类传播行为的目的。一个好的理论应当尝试捕捉到这种普适性的原理，基于一般性的原理生成机制，基于因果机制解释行为模式，基于模式预测现实，最终回答重要的社会问题。
# 
# ![](./img/logo/dinosaur.png)
# 
# ## 风格
# 
# 《计算传播基础》（Elements of Computational Communication)书名来源于Thomas M. Cover的名作《信息论基础》（Elements of Information Theory）。
# 
# - 第一，贯彻“凡事应该尽可能简单到不能再简单为止”的原则，采用案例教学的方式“解剖麻雀”，务求将计算的逻辑介绍清楚。
# - 第二，倡导“在干中学”（learning by doing）的方式，强调计算或数据科学实战。本书的设计是为了给新闻传播学院的学生介绍计算传播的编程方法，帮助没有编程基础的同学快速掌握计算方法。
# - 第三，强调直觉式的理解，契合社会科学研究者的需求和特点。但研究者面对定量的研究方法尚且分身乏术的时候，面对计算的方法必然更加畏惧。如何从社会科学研究者的角度出发、面对社会科学研究者介绍计算传播基础构成了一个重要的挑战。本书在内容的遴选方面刻意强化对于这一点的要求。
# - 第四，激发兴趣，为探索者赋能。苏格拉底关于人类应该首先认识自我的强调给笔者提供了很多启发。
# 
# 本书过于强调Python编程和数据科学的方法是教学现实所迫，目前依然存在明显地不足之处：
# 
# - 第一，对于数字时代的调查和实验方法关照不足。针对这一问题，推荐本书读者阅读Bit By Bit一书。在实际的教学过程当中，笔者也在尝试将Bit By Bit一书的内容融入已有的内容体系。
# - 第二，对于因果推断方法的强调不够。基于潜在因果框架和因果图介绍随机对照实验，以及其它模仿实验方法的工具变量方法、倾向值匹配或加权方法、断点回归方法、双重差分方法、面板数据的分析方法。本书未来也将加入相关的内容。
# - 第三，对于理论的重视不足。目前计算社会科学的发展主要是数据和方法驱动的，对于理论的重视不够是通病。然而这一问题并不容易解决，计算作为一种崭新的范式在理论构建方面还需要进一步的积累。但这种转型背后的理论值得重视，本书将尝试以计算中心（the center of calculation）作为主要的理论视角，强化本书的理论取向。
# 
# ## 教学安排
# 
# 根据以上内容开设课程，建议开设72学时课程，每周4学时课程。
# 
# - 第1周介绍计算传播学简介（2学时）、指导学生安装Anaconda Python并学习使用Jupyter Notebook（1学时)、使用Mobirise建立个人网页（1学时）
# - 第2周介绍Python编程基础部分上 （2学时）、作业（2学时）
# - 第3周介绍Python编程基础部分下 （2学时）、作业（1学时）、分组（1学时）
# - 第4周数据收集部分上（2学时）、作业（2学时）
# - 第5周数据收集部分下（2学时）、作业（2学时）
# - 第6周数据清洗部分（2学时）、作业（2学时）
# - 第7周统计部分（2学时）、作业（2学时）
# - 第8周机器学习上（2学时）、作业（2学时）
# - 第9周机器学习下（2学时）、作业（2学时）
# - 第10周神经网络上（2学时）、作业（2学时）
# - 第11周神经网络下（2学时）、作业（2学时）
# - 第12周文本挖掘上（2学时）、作业（2学时）
# - 第13周文本挖掘下（2学时）、作业（2学时）
# - 第14周网络科学上（2学时）、作业（2学时）
# - 第15周网络科学下（2学时）、作业（2学时）
# - 第16周Bit By Bit大数据部分（2学时）、作业（2学时）
# - 第17周Bit By Bit调查部分（2学时）、作业（2学时）
# - 第18周Bit By Bit实验部分（2学时）、作业（2学时）
#  
# 
# ## 致谢
# 
# 首先，我需要感谢周葆华和祝建华两位老师。本书起源于王成军在2016年开始为复旦大学开设的[《计算新闻传播学》](https://github.com/computational-class/cjc)新媒体硕士课程。最初的课程框架由香港城市大学祝建华老师、复旦大学周葆华两位老师和王成军三个人商定，旨在为新闻传播学院的学生提供关于计算传播学应用的基本架构，内容注重计算思维的训练和实战应用，体现了实用性和案例化教学的特点。按照数据分析的流程分为数据收集、数据清洗、统计分析、机器学习（神经网络）、文本挖掘、推荐系统、网络科学、可视化等多个模块。其后，王成军在南京大学开设名为[《大数据挖掘与分析》](https://github.com/computational-class/bigdata)课程，基本上遵循相同的框架。同时，需要感谢参与此课程的所有同学，因为与同学们的互动，本书所使用的案例得以不断更新。
# 
# 
# 其次，我想感谢Anaconda Python和Jupyter项目。本书及其相关课程遵循可计算化的思路，采用Python作为编程工具，所有课程内容，包括文字、图片、代码等，均通过Jupyter Notebook展示。Jupyter Notebook是数据科学和计算社会科学的必备工具，它使得程序运行的结果被非常好地记录下来，确保了数据分析结果更容易被复制出来，利于传播和展示。借助于[RISE](https://computational-class.github.io/ccbook/0_slides.html)，所有的Jupyter Notebook还可以非常方便地在本地以幻灯片的形式展示。为更好地方便教学、交流以及更新课程内容，特将课程相关的Jupyter notebook通过[Jupyter Book](https://github.com/jupyter/jupyter-book)整理为在线图书的形式。我在给学生上课的时候经常鼓吹Jupyter Notebook的高明之处，尤其是支持Markdown的写作体验非常好，因此可以用来写书。但是，我之前从来没有认真尝试过真正这样做。Jupyter Book终于让我的这个愿望成真。综上，笔者非常感谢Jupyter项目：一方面，如果没有Jupyter Notebook就很难有相关的课程；另一方面，如果没有Jupyter Book项目的成熟，将课程内容整理为在线电子图书也是一个巨大的工程。
# 
# 另外，我想感谢Github平台对于本书和相关课程起到了非常重要的作用。为便于教学，课程中使用的所有Jupyter Notebook形式的代码、数据、图片均通过Github完整的记录下来并对所有人开放。借助于nbviewer平台，读者可以非常便利地查看所有的Jupyter Notebook，并在幻灯片和代码两种模式中自由切换。当然，实现这一结果的基础是所有的Jupyter Notebook存储在Github平台上。本书的电子版本也通过[Github Pages](https://github.com/chengjun/mybook)展现。每次更新的结果，均通过Github进行更新。每年开设两次相关课程使得本书所涉及到的内容可以迅速迭代。”苟日新，又日新“。聚沙成塔，集腋成裘，古人诚不我欺也。
# 
# 最后，需要声明的是，本在线书籍中不少应用内容来源于多本其它重要书籍，并非笔者独创。因本书内容驳杂，而个人能力有限，难免存在诸多谬误；对于其中涉及的错误，笔者皆愿意承担。
# 
# 王成军
# 
# 2019年10月11日
# 

# In[ ]:





# 
# ```{toctree}
# :hidden:
# :titlesonly:
# 
# 
# 01-intro2cjc
# 03-python-intro
# 04-crawler-beautifulsoup
# 06-data-cleaning-intro
# 08-01-statistics-thinking
# 09-01-machine-learning-with-sklearn
# 09-11-neural-network-intro
# 10-text-minning-gov-report
# 13-recsys-intro
# 15-network-science-intro
# 19-visualization-with-seaborn
# ```
# 
