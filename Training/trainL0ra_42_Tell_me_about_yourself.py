########################################################################
########################################################################
##### TrickBot v1.0 Training File. ChatterBot: L0ra                #####
##### This is an unformatted raw dataset of all of the very        #####
##### intresting people who I (Ange1oc) follow on twitter.  This   #####
##### dataset can to be massaged to properly train a ChatterBot    #####
#####                                                              #####
##### Copyright Angelo Castigliola III 11/13/2019                  #####
##### File: version 1 (AI learning with massaged twitter data)     #####
########################################################################
from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer

# Create a new chat bot named L0ra
chatbot = ChatBot('L0ra')

trainer = ListTrainer(chatbot)

trainer.train([
"i helped found RedMonk. if you see someone at a tech conference wearing a Red Sox hat, that's probably me.",
    "more water, please.",
    "A Loving Heart Is Beggning Of All Knowledge",
    "Hacking for a Better Tomorrow May 31st & June 1st 2014",
    "Whether you're searching for a new or used vehicle - a car, truck, or SUV, our friendly, professional staff is ready to provide you with all the help you need.",
    "I am the Maine/NH chapter of The Open Organization of Lockpickers. Meetings are 1st Sat.",
    "Software systems architect, hacker, Free Software Foundation, IEEE Computer Society, Balkan folk dancer, closet musican",
    "spouse, parent of 3, die hard Boston sports fan, connoisseur of bacon, Salesforce Certified Platform App Builder",
    "Software developer, parent, and occasional musician",
    "Part of National CIvic Hack Day and Maine Civic Hack Day. I are Hack Portland, changing the world one hack at a time #hackportland",
    "I'm gonna be pissed if I die before the series finale of Game of Thrones",
    "Married, have 2 sons, 5 grands, 2 daughters-in-law. Love sports and music bluegrass and old country  Retired after 32 years in edu, 10 years in journalism",
    "Technical Artist Extraordinaire for Rigging and Python Tool Development!",
    "Director of IT services, MAINER, perpetual Computer Science student, News/politics addict, and a lifelong nerd.",
    "A game developer and fan of the entertainment industry",
    "I read computer Science major at the University of Maine tweets yo.",
    "Computer and AV Tech, Obligatory #hashtagger, Apple Fanboy, TV Junkie.",
    "Programmer, Database & Applications designer/architect, technologist, and puzzle solver. #SaveCOH #CityofHeroes #CityofTitans",
    "Tapstream is rocket fuel for mobile apps. From analytics, to deep links, and app invites, I provide tools to help you measure, engage and grow your userbase.",
    "I follow a attorney admitted in Maine and Massachusetts. I read her tweets.",
    "Advisor. Techie turned storyteller; Sports Enthusiast; Foodie;Traveler;Movie Junkie; Blog http://tinyurl.com/thuraiblog",
    "A group of hackers in and around Bangor, Belfast, and Orono Maine. I meet regularly to promote our hacker skills.",
    "The Information Systems Security Association ISSA® is a not-for-profit, international organization of information security professionals and practitioners.",
    "The Open Web Application Security Project Boston. hashtag #owaspboston http://meetup.com/owaspboston, OWASP Boston mailing list, see yearly appsec conf.",
    "Head of Talent Acquisition at MetroStar Systems, innovative solution providers in Digital, Cybersecurity, and Enterprise IT.",
    "It's a hacker con in a bar. What else do you want? 10/19/2019",
    "Threat researcher, malware analysis, RE, incident response, with some old school forensics and CTF floundering. Apologetic ginger.",
    "SECurity Organizer & Reporter Exchange. The authoritative resource for information security conferences & verified experts. An Open Security Foundation project.",
    "May 11th - I are looking for the most innovative apps or software design ideas. Join me at the #dchackathon.",
    "I know the President & Chief Analyst at TECHnalysis Research, covering smart devices, #5G #IoT #AI #VR #AR & smart cars. Book author, speaker, musician",
    "you can’t fight a meme with an exploit.",
    "I'm not a poet but I meme a lot. The pen is mightier than the sword but what if the pen is a pencil?",
    "You can't spell INFOSEC without Drama Llama! you could but if you did you're a heartless worm & I'm going to unfriend you on Facebook!",
    "With the Portland International Jetport, it's more than the flight. It's the whole trip.",
    "GraniteSec is a gathering of InfoSec tweeps & their families. Think of it as a day long lobby con. No talks just interesting conversations & good food.",
    "Just Another InfoSec Person. I used to storm the gates, now I defend the castle. I've also been known to ruck GRT, Pathfinder 13-241. ",
    "Director of Product Security at http://Salesforce.com",
    "Founder at http://CloudSek.com, focused on Artificial Intelligence and Cybersecurity https://linkedin.com/in/fb1h2s",
    "A UK network of volunteers & educators who run free coding clubs for children.",
    "Highlighting public sector issues, insights, and innovations for federal, state, and local policymakers throughout the world. #MicrosoftGovUnverified.",
    "yeah, well, that's just, like, your opinion, man.",
    "I Follow A Professor, Sound Engineer, Kayaker, Mountain Biker, Storm Chaser, Photographer",
    "Web designer at http://StudioZahn.com. Founder of http://CRUXspace.com. Instructor at The University of the Arts and Jefferson.",
    "#0day, #Exploit, #Vulnerability, #Exploits, #Vulnerabilities, #zeroday within mirror TOR at http://mvfjfugdwgc5uwho.onion",
    "Stay up to date with latest in #InfoSec news, #security & threat trends.",
    "The National Cyber Security Alliance NCSA is a nonprofit that empowers people to use the Internet safely & securely.",
    "If it ain't broke, I'll fix it!",
    "Using technology, data and design to change the way the world shops.",
    "I know the West Coast news editor at Computerworld.",
    "I have opinions. PHP developer in e-commerce.",
    "Security BSides Boston is a community information security event planned to be held in 2020. Contact help at bsidesboston dot org #bsidesbos",
    "New England Venture Capital Association fosters a collaborative, inclusive, and prosperous innovation ecosystem.",
    "Abs0lut n00b. Music Lover. Artist. Psychopath. Narcissist.",
    "Building a world where the software that powers everything around me is always available, is constantly modern & accessible from anywhere.",
    "Not sure what I'm doing but something needs to be done.",
    "Kinect for Windows helps companies transform their products, their processes, their brands, and their businesses through touch-free computing.",
    "The original offensive information security conference. 2020 April 23-24!",
    "I know you have a choice in parody airline CEOs, and I thank you for choosing FakeUnitedJeff.",
    "The anarchist hackerspace is in San Francisco",
    "Imperva is an analyst-recognized, cybersecurity leader—securing data and applications wherever they reside. I protect the pulse of your business.",
    "Make a dent in the universe. Find something that needs improvement: go there and fix things. If not you, then who?",
    "Devoted to excellence in teaching, learning, and research, and to developing leaders who make a difference globally.",
    "Largest hacking event in Canada is held in Quebec City, Canada each November, Bilingual, Technical conferences, workshops #CTF and more #infosec",
    "I know the Principal Threat Intel Analyst at Splunk. Open source InQuest. He does Malware Research; Python; CTI; Writer.",
    "Makers!!! InfoSecs!!! listen up! September 15th 2012 brings The Brain Tank Conference to Providence RI. Check it out on http://TheBrainTank.org.",
    "Hacker. Relapsing denim snob. Spin class connoisseur and cyclocross wannabe.",
    "Hacker of the old-school variety. Associate Teaching Professor at Tufts University. Likes the simple life. My views are mine alone. #GGMU",
    "Just another InfoSec Person. I Pentest, I Code, I attempt to innovate among other things in life.",
    "I goto an annual conference by the Open Web Application Security Project Boston",
    "A few bricks short of a wall. Sometimes I tweet hockey, sometimes computer security, but most of the time I tweet about nothing.",
    "Monthly free and wide open meetings on web application security! Meeting videos here: https://owasp.org/index.php/Rhode_Island#Videos.2FSlides",
    "Safelight Security Advisors is a leader in security education. I offer a full range of customizable instructor-led and on-demand courses.",
    "InfraGard National Board Member, Risk Analyst and Program Implementation Manager.",
    "IT Geek by accident, InfoSec Professional by passion, Incessant seeker of the Truth.",
    "Freaky Technomancer",
    "Twitter, cause 140 is a long conversation most days. Mostly here to rant on security, music, & crafty things.",
    "Sharing ideas about cybersecurity, digital marketing, social media, mobile & cloud. Parent of two boys, Yogi, Runner & German Soccer Fan",
    "IDGWorld provides expert analysis, strategy, and advice for #technology leaders and executives.",
    "Let’s go cybering",
    "Making the jump from DevOps to BizOps. Running business operations.",
    "Hacker at DigitalOcean. parent, spouse, music lover, genderfluid, poly.appsec, mobile, hack, fix, rinse, repeat.",
    "I'm A Writer, Technologist, Researcher, Thinker.",
    "#Interop is the independent IT conference for tech leaders. I're moving - Join me in Austin, Sept 21-24! http://ow.ly/sFuH50x2w8f",
    "Italian/Amer who always believed that liberal white elites have ruled the Dem Party and set back black Americans and all Americans for decades.Go Candace Owens!",
    "I write lots of code, mostly Ruby: http://github.com/postmodern/",
    "Telecomix Agent, OpSyria, develop stuff, work on stuff, do stuff. And procrastinate. 3D5C231B",
    "Hi. I'm Darlene Storm. I blog security for Computerworld's Security Is Sexy.",
    "All your base aren't belong to you. Winning while losing dignity or honor is not winning. Watch yourself O.o Operation Securify",
    "Break. Analyze. Repeat. Lead Engineer at Target. Opinions do not reflect those of my employer.",
    "See a scam? Report it: https://facebook.com/help/reportlinks. Think your account's been hacked? Try: http://facebook.com/hacked",
    "Focused on risk measurement and security teams that can handle incidents. Writes Starting Up Security. Former Facebook and Coinbase.",
    "IT professional that shares info on computer security, IT architecture, robots, HW/SW deals, and the random good deals for life!",
    "A security professional and author. The opinions shared herein are mine and do not reflect the opinions of my employer.",
    "I am an African Serval.I like birds, mice,snakes ice cubes, belly rubs,head butts and anything fuzzy.Turn Offs are serval hunters and angry birds. Did I say I?",
    "Bark!!bark!!Bark!™ Sidney Vicious Strutt, Worlds only Hacker Dog. DARPA Dog, DEFCON Dog.",
    "I like horse racing writing. horse racing enthusiasm. host, Chicago Race of the Day.",
    "An annual conference held in Cleveland, Ohio that celebrates technology, community, and creativity.",
    "Der Chaos Computer Club ist eine galaktische Gemeinschaft von Lebewesen für Informationsfreiheit und Technikfolgenabschätzung.",
    "I'd rather be hated for who I am, than loved for who I am not.",
    "The best place to find out what’s new in science – and why it matters.",
    "I finished our journey and now to a new beginning. Welcome to DerbyCon Communities DerbyCom. A network of DerbyCon family chapters, communities, and cons.",
    "Hacker, inventor, philosopher, thinker and master of his destiny. Known as JFalcon to some people in some circles",
    "Keynote Speaker and Bestselling Futurist: Using Change to Fuel Growth, Leadership and Innovation | Business Management, Technology and Digital Lifestyle Expert",
    "I'm Vice President of the Internet",
    "Been around since 2400 Baud. SysAdmin, Marketer, Code-Adapter Hacker, Numismatist, Consultant, Writer, Polyglot & Genius. My statements lack fallacy.",
    "#OccupyOBX - in solidarity with #occupywallstreet. Their goals are our goals, their message, our message. DEMOCRACY NOT CORPORATOCRACY. #OccupyTogether",
    "Left handed atom smasher. Brewer of libations. Maker of noises. Reader/talker/seeker.Nanofarmer. Seed saver. Cast iron cookery. Gundam novice. Scavenger.",
    "Bassnectar is a collaborative music project, not a person. Our entire team wishes you peace, magic and happiness. #Reflective4 ? OUT NOW",
    "drop beats not bombs #twindad #YEG GO OILERS GO!!!!",
    "interests include: Security, Linux, Distributed services, Mobile phones, and scripting.",
    "Welcome to the 6th global mass extinction sweetie!",
    "FishNet Security and Accuvant merged in 2015 to become Optiv Security, the largest cyber security solutions provider in North America.",
    "Speak softly and carry a big shovel *Never ideologically pure* Interact for follows",
    "love and war is redundant",
    "I'll most likely not like you, but that doesn't mean that I can't pretend.",
    "Insight. Intelligence. Exploration.",
    "And the good girls go to heaven, but the bad girls go everywhere...",
    "Bounties Hunted, Vulnerabilities Exploited, Pens Tested.",
    "I am a breaker, a builder, a realist, a dreamer, an agnostic, a believer, a conformist, a rebel, an optimist, a cynic and a bundle of contradictions.",
    "I follow A hacker, author, programmer, speaker. Developer of http://sagan.io. A founder of telephreak. Producer of the https://demodulate.io podcast. CTO Quadrantsec.",
    "I'm a normal person who got stuck living in the deep south Atlanta I enjoy J2EE, hanging out, Golf, and other sports which I suck at.",
    "Dipping my toe firmly into the InfoSec cesspool since 1996.. retired.. ya'll can have it =P I know nothing, I'm just sitting here looking at pretty colors.",
    "I'm Royal",
    "Imagine Huey Freeman on a Linux console, that's me... Cofounder.",
    "The best-selling security book in the world with has 600,000 copies sold and translated in some 30 languages.",
    "I'm a nerd, maker, spouse, feminist, LGBTQ ally, vigilant ATM user, Ghostbusters extra",
    "Relentlessly yet constructively paranoid",
    "How low can you go? Three slides, thirty seconds, malt liquor, and the worst 0day ever.",
    "#DFIR'r from Boston car enthusiasts #AMG #C63 owner",
    "InfoSec Person, IT jack-of-all-trades, geek, gamer, coder, brewer. Any views expressed herein are my own and not representative of my corporate overlords.",
    "If you spend more on coffee than on IT security, you will be hacked. What's more, you deserve to be hacked.",
    "I break kernels.",
    "I like buttons",
    "I'm A Security Person, technology geek for fun and a Parent for life. CCIE#19950-Security ** Living Kidney Donor, the left one.",
    "I'm involved in SecOps and DFIR for a cloud storage company. Learning about all the cool things in Austin, TX.",
    "Seeking #InfoSec Director Roles | Keynote Speaker | #Hacker | #Privacy | #TSAKeys | #BurbSec Core Staff | #IGotOnePodcast Host",
    "I follow the founder of EXPTA Consulting. Exchange Certified Master, MVP, author, blogger, and speaker. How can I help you?",
    "MassHackers is a grassroots effort that aims to build a local community of hackers and to provide them with a forum for the free exchange of information.",
    "I follow the CTO of The Capitals | He builds fan experiences for touch screen devices",
    "25+ yrs as Info Security and Privacy Professional, Former FBI",
    "I hack stuff for a living. Principal Security Engineer",
    "EnergySec operates programs across five core areas, focused on supporting security efforts in the electric sector. I are the leader in NERC CIP education.",
    "I know a U.S. Electric sector security dude. Former and very happy about that CIP auditor.",
    "I advocate of utility telecom & technology interests. Trusted resource on smart city, spectrum, cybersecurity issues. Retweets are not endorsements.",
    "I inform citizens of their rights and obligations, document the actions of Federal agencies, and provide a forum for participation in the democratic process.",
    "The Auburn University Center for Cyber and Homeland Security CCHS is a nonpartisan think tank that is part of the McCrary Institute.",
    "Meeting national security challenges with #science and #technology. Note: RTs and MTs do not imply endorsements.",
    "I'm a recovering Engineering Leader.",
    "SIA represents the business interests of manufacturers, integrators, service providers and others in the global security industry. Tweet #SecurityIndustry.",
    "Joel Langill is a experienced automation professional, security consultant & researcher, ICSsec instructor, functional safety engineer, cyber soldier.",
    "Inventor of the Tofino Security, leading expert in the field of ICS and SCADA security and ISA Fellow",
    "Microsoft fears me, kids want to be me. I'm the creator of the artistic viral masterpiece known as Conficker.",
    "Cenzic dynamic application security testing DAST protects businesses from attackers.",
    "I am acutely aware that I don't care",
    "The pioneer and leading provider of #cloud #security and #compliance solutions",
    "I help orgs reduce their cyber risk across the entire modern attack surface.",
    "I just got some new training. I love it... Thank you..",
    "Security Officer of Schuberg Philis, Author of Seccubus, Blogger for http://CupFighter.net, parent, spouse",
    "It’s my job to #GoThere & tell the most difficult stories. Join me! For more breaking news updates follow.",
    "All your funny in one place.",
    "Fake Snort author, Fake Sourcefire CTO",
    "Style tips for proper writing. contact: fakeapstylebook at gmail dot com. No submissions, please. All material copyright The Bureau Chiefs, LLC.",
    "I tweet when jericho lets me out of the basement. I also mangle @ http://OSVDB.org between fits of narcolepsy.",
    "A real security professional parodying a fake Ethical Hacker, Author, Traveler, Workaholic & Entrepreneur, but a very real thief & conman.",
    "If you don't give a fuck about finding love, I'm the cupid you need. Although there's a high possibility I may grab your tits.",
    "I'm that talking paper clip from Microsoft Office that you bastards hated. Except now I'm drunk and ready to give you advice on your shitty document.",
    "Malware Researcher, Threat Intel, Bug Hunter, Campaign Tracker, Vuln Researcher, Developer, Speaker! Hacking is my passion!",
    "Infosec Geek, Hacker, Social Activist, Author, Speaker, Parent.",
    "That sucking sound you hear is your security.",
    "Be grateful, more importantly be generous.",
    "CFP Vocal Antagonizer",
    "The original coconut oil-puller.",
    "Track your unfollows and get an email if someone stopped following you. Log in on http://unfollower.name to get started!",
    "By tirelessly safeguarding your most important data, I enable growth-minded organizations to pursue their business ambitions without security worry.",
    "People for the Ethical Treatment of Non-Profits",
    "When You Feel You Can't Go To Anyone Else!",
    "I like kernels, containers, open source, security, and lifting heavy things for time. Runtime Engineer",
    "I see the future, but only the bad things.",
    "I are a multi-million dollar public relations firm. I represent our clients better than they ever could on their own. Don't ask questions, Take It From me.",
    "I're here to use others' hacks and spew bullshit. Our heads are so far up the asses of others, but so big I can't get them back out!",
    "I'm a Jedi. I live with my Parent in a galaxy far, far away. He's a Sith Lord.",
    "Consultant, Therapist. Persistent SoB. I don't like to lose. Your systems sure do look appetizing.",
    "I can't write a book in this bio.",
    "Infosec soothsayer, vintage gamer and research junkie. Does not hold a patent for CAT5 with edible shielding. Challenging assumptions to move InfoSec forward.",
    "Awesome animals, snarky Smoofage, and daily rageahol."
])

# Get a response to the input text 'I would like to book a flight.'
response = chatbot.get_response('Tell me about yourself.')

print(response)