"""
Beginner-friendly educational chatbot.
Contains curated explanations and keyword matching for computer basics,
programming languages, web development, databases, tools, and careers.
This is a rule-based chatbot, not a live AI model.
"""

TOPICS = {
    "python": "Python is a beginner-friendly, high-level programming language. It is used for automation, web development, data analysis, AI/ML, and scripting. Example: print('Hello, world!')",
    "javascript": "JavaScript makes websites interactive. It can run in browsers and on servers with Node.js. Example: console.log('Hello, world!');",
    "java": "Java is a class-based, object-oriented language used in enterprise apps, Android development, and backend systems. Example: System.out.println(\"Hello, world!\");",
    "c++": "C++ is a compiled language often used for games, performance-heavy software, embedded systems, and competitive programming.",
    "c language": "C is a procedural language used for operating systems, embedded software, and learning memory and low-level concepts.",
    " c ": "C is a procedural language used for systems and embedded programming. It is a useful language for learning core programming concepts.",
    "c#": "C# (C-sharp) is commonly used with .NET for Windows apps, web backends, and Unity game development.",
    "php": "PHP is a server-side scripting language often used for websites and web applications.",
    "typescript": "TypeScript adds static types to JavaScript and is widely used for larger web applications.",
    "ruby": "Ruby is a general-purpose language known for readable syntax and the Ruby on Rails web framework.",
    "go language": "Go (Golang) is a compiled language designed for simple, efficient services and cloud infrastructure.",
    "golang": "Go (Golang) is a compiled language designed for simple, efficient services and cloud infrastructure.",
    "rust": "Rust focuses on memory safety and performance. It is used in systems programming and command-line tools.",
    "kotlin": "Kotlin is used for Android apps and JVM-based applications.",
    "swift": "Swift is Apple's language for iOS, macOS, watchOS, and other Apple-platform apps.",
    "r language": "R is used for statistics, data analysis, and data visualization.",
    "sql": "SQL (Structured Query Language) is used to create, read, update, and delete data in relational databases. Example: SELECT * FROM students;",
    "html": "HTML structures web pages. It is a markup language, not a programming language. Example: <h1>Hello</h1>",
    "css": "CSS styles web pages: colors, layout, spacing, fonts, and responsive design. Example: body { font-family: Arial; }",
    "bash": "Bash is a command-line shell and scripting language used to automate tasks on Linux and macOS.",
    "scratch": "Scratch is a visual, block-based programming environment that helps beginners learn programming concepts.",
    "assembly": "Assembly language provides low-level instructions closely related to a processor's instruction set.",
    "matlab": "MATLAB is used for numerical computing, engineering, simulations, and data visualization.",
    "dart": "Dart is used with Flutter to build apps for mobile, web, and desktop.",
    "scala": "Scala combines object-oriented and functional programming and runs on the JVM.",
    "perl": "Perl is a scripting language historically used for text processing, automation, and system administration.",
    "lua": "Lua is a lightweight scripting language often embedded in games and applications.",
    "objective-c": "Objective-C is an older Apple-platform language still found in some legacy iOS and macOS projects.",
    "programming language": "A programming language lets people write instructions a computer can execute. Examples include Python, Java, C, C++, JavaScript, and C#.",
    "language": "Popular computer languages include Python, Java, C, C++, C#, JavaScript, TypeScript, PHP, Go, Rust, Swift, Kotlin, Ruby, R, and SQL. Ask about one language for details.",
    "variable": "A variable is a named place to store a value. Python example: age = 20",
    "data type": "A data type describes a value, such as int (whole number), float (decimal), str (text), bool (True/False), list, tuple, set, and dict in Python.",
    "datatype": "A data type describes a value, such as int, float, str, bool, list, tuple, set, and dict in Python.",
    "loop": "A loop repeats instructions. Python example: for i in range(3): print(i)",
    "for loop": "A for loop repeats over a sequence or range. Example: for i in range(5): print(i)",
    "while loop": "A while loop repeats as long as its condition is True. Example: while count < 5: count += 1",
    "if else": "if/else runs different code depending on a condition. Example: if age >= 18: print('Adult') else: print('Minor')",
    "function": "A function is a reusable block of code. Python example: def greet(): print('Hello')",
    "array": "An array stores multiple values in an indexed collection. Exact behavior depends on the language; Python commonly uses lists.",
    "list": "A Python list is an ordered, changeable collection. Example: fruits = ['apple', 'mango']",
    "tuple": "A Python tuple is an ordered collection that cannot be changed after creation. Example: point = (2, 3)",
    "dictionary": "A Python dictionary stores key-value pairs. Example: student = {'name': 'Asha', 'age': 20}",
    "oops": "OOP means Object-Oriented Programming. Its common concepts are classes, objects, inheritance, encapsulation, abstraction, and polymorphism.",
    "oop": "Object-Oriented Programming organizes code using classes and objects. Key concepts include inheritance, encapsulation, abstraction, and polymorphism.",
    "class": "A class is a blueprint for creating objects. It defines attributes and methods.",
    "object": "An object is an instance of a class, with its own data and behavior.",
    "algorithm": "An algorithm is a finite set of clear steps used to solve a problem.",
    "debugging": "Debugging means finding and fixing errors in a program.",
    "error": "A syntax error breaks language grammar; a runtime error occurs while running; a logic error means the program runs but gives the wrong result.",
    "compiler": "A compiler translates source code into another form, often machine code, before execution.",
    "interpreter": "An interpreter executes or evaluates source code, often step by step.",
    "ide": "An IDE (Integrated Development Environment) combines tools such as a code editor, run/debug tools, and project management.",
    "vs code": "Visual Studio Code is a code editor. You can write code in it and run it using language runtimes or extensions.",
    "flask": "Flask is a lightweight Python web framework. It can create routes, receive requests, and return web pages or JSON.",
    "django": "Django is a batteries-included Python web framework with routing, templates, ORM, authentication features, and an admin interface.",
    "react": "React is a JavaScript library for building user interfaces from reusable components.",
    "node": "Node.js runs JavaScript outside the browser, often for servers and developer tools.",
    "node.js": "Node.js runs JavaScript outside the browser, often for servers and developer tools.",
    "angular": "Angular is a TypeScript-based framework for building web applications.",
    "vue": "Vue is a JavaScript framework for building user interfaces.",
    "database": "A database stores and organizes information so it can be searched and updated. Examples include SQLite, MySQL, PostgreSQL, and MongoDB.",
    "mysql": "MySQL is a relational database that uses SQL.",
    "postgresql": "PostgreSQL is an open-source relational database known for strong SQL support and advanced features.",
    "mongodb": "MongoDB is a document-oriented NoSQL database that stores records in BSON-like documents.",
    "api": "An API is a defined way for software systems to communicate. A web API often exchanges data using HTTP and JSON.",
    "json": "JSON is a text format for structured data using objects, arrays, strings, numbers, booleans, and null.",
    "git": "Git is a version control system that tracks code changes and helps developers collaborate.",
    "github": "GitHub hosts Git repositories and supports collaboration through issues, pull requests, and project tools.",
    "frontend": "Frontend is the part users see and interact with. Common web technologies are HTML, CSS, and JavaScript.",
    "backend": "Backend handles server-side logic, data storage, authentication, and APIs. Common choices include Python/Flask, Django, Node.js, Java, and PHP.",
    "full stack": "Full-stack development includes both frontend and backend work, often plus database and deployment.",
    "website": "A website commonly uses HTML for structure, CSS for styling, JavaScript for interaction, a backend for server logic, and a database when data needs to persist.",
    "ai": "Artificial Intelligence (AI) is the field of building systems that perform tasks associated with human intelligence, such as language understanding or image recognition.",
    "machine learning": "Machine Learning (ML) lets systems learn patterns from data. Common uses include predictions, recommendations, and classification.",
    "data science": "Data science combines statistics, programming, and domain knowledge to analyze data and communicate insights.",
    "cyber security": "Cybersecurity protects systems, networks, and data. Learn networking, operating systems, secure coding, and ethical/legal practice.",
    "networking": "Computer networking connects devices so they can communicate. Key concepts include IP addresses, DNS, routers, TCP/IP, and HTTP.",
    "operating system": "An operating system manages computer hardware and software resources. Examples include Windows, Linux, macOS, Android, and iOS.",
    "hardware": "Hardware means the physical parts of a computer, such as CPU, RAM, storage, motherboard, keyboard, and monitor.",
    "software": "Software is programs and instructions that tell a computer what to do. Examples include operating systems, browsers, and apps.",
    "cpu": "CPU stands for Central Processing Unit. It executes instructions and performs calculations.",
    "ram": "RAM is temporary working memory used by running programs. Its contents are normally lost when power is off.",
    "rom": "ROM is non-volatile memory used to store data that should remain available without power.",
    "internet": "The internet is a global network of connected networks that communicate using standard protocols.",
    "http": "HTTP is a protocol used to transfer web resources between clients and servers. HTTPS adds encryption using TLS.",
    "career": "Computer career options include web developer, Python developer, software engineer, data analyst, QA tester, database developer, cloud engineer, and cybersecurity analyst. Choose based on your interests and practice projects.",
    "project": "Beginner project ideas: calculator, quiz app, to-do list, student management system, voting system, portfolio website, and chatbot. Build one, test it, and document it on GitHub.",
    "help": "Try asking: What is Python? Explain HTML. What is a variable? Explain loops. What is SQL? What is frontend/backend? What is AI? Ask about a language or computer basic.",
}

GREETINGS = {
    "hi": "Hi! Welcome to Computer Languages Chatbot. Ask me about programming languages, coding basics, web development, databases, AI, or computer fundamentals.",
    "hello": "Hello! I can help you learn computer languages and basic computer concepts. What would you like to know?",
    "hey": "Hey! Ask me a coding or computer question.",
    "thanks": "You're welcome! Keep practicing and building small projects.",
    "thank you": "You're welcome! Keep practicing and building small projects.",
    "bye": "Goodbye! Keep learning and coding. See you next time!",
}


# Marathi and Marathi-in-English (transliteration) support.
# These aliases map common Marathi questions to existing topic keys.
MARATHI_ALIASES = {
    "पायथन": "python", "पायथॉन": "python", "python म्हणजे काय": "python",
    "python mhanje kay": "python", "python kay ahe": "python", "python kasa shikaycha": "python",
    "जावा": "java", "java म्हणजे काय": "java", "java mhanje kay": "java",
    "सी भाषा": "c language", "सी प्लस प्लस": "c++", "जावास्क्रिप्ट": "javascript",
    "एचटीएमएल": "html", "html म्हणजे काय": "html", "html mhanje kay": "html",
    "सीएसएस": "css", "css म्हणजे काय": "css", "css mhanje kay": "css",
    "एसक्यूएल": "sql", "sql म्हणजे काय": "sql", "sql mhanje kay": "sql",
    "व्हेरिएबल": "variable", "variable म्हणजे काय": "variable", "variable mhanje kay": "variable",
    "डेटा टाइप": "data type", "डेटा टाइप म्हणजे काय": "data type", "data type mhanje kay": "data type",
    "लूप": "loop", "loop म्हणजे काय": "loop", "loop mhanje kay": "loop",
    "फंक्शन": "function", "function म्हणजे काय": "function", "function mhanje kay": "function",
    "लिस्ट": "list", "डिक्शनरी": "dictionary", "क्लास": "class", "ऑब्जेक्ट": "object",
    "ओओपी": "oop", "ओप्स": "oops", "अल्गोरिदम": "algorithm", "डीबगिंग": "debugging",
    "फ्रंटएंड": "frontend", "बॅकएंड": "backend", "वेबसाइट": "website",
    "डेटाबेस": "database", "एपीआय": "api", "गिटहब": "github", "गिट": "git",
    "एआय": "ai", "मशीन लर्निंग": "machine learning", "सायबर सिक्युरिटी": "cyber security",
    "कॉम्प्युटर म्हणजे काय": "computer", "संगणक": "computer", "हार्डवेअर": "hardware",
    "सॉफ्टवेअर": "software", "सीपीयू": "cpu", "रॅम": "ram", "इंटरनेट": "internet",
    "मला मदत कर": "help", "मदत": "help", "तुझे नाव काय": "your name",
}

MARATHI_ANSWERS = {
    "python": "Python ही शिकायला सोपी आणि लोकप्रिय programming language आहे. तिचा वापर web development, automation, data analysis आणि AI/ML साठी होतो. उदाहरण: print('Hello')",
    "javascript": "JavaScript चा वापर वेबसाइट interactive बनवण्यासाठी होतो. उदाहरणार्थ, button click केल्यावर काही action करणे.",
    "java": "Java ही object-oriented programming language आहे. तिचा वापर मोठ्या software systems, backend आणि Android development मध्ये होतो.",
    "c++": "C++ ही वेगवान programming language आहे. तिचा वापर games, system software आणि competitive programming मध्ये होतो.",
    "c language": "C ही programming language operating systems, embedded systems आणि programming चे मूलभूत concepts शिकण्यासाठी वापरली जाते.",
    "html": "HTML ही markup language आहे. ती website चा structure तयार करते—उदा. heading, paragraph, image आणि link.",
    "css": "CSS चा वापर website सुंदर दिसण्यासाठी होतो. रंग, font, spacing आणि layout CSS ने ठरवतात.",
    "sql": "SQL चा वापर database मधील data साठवणे, शोधणे, बदलणे आणि delete करण्यासाठी होतो. उदाहरण: SELECT * FROM students;",
    "variable": "Variable म्हणजे value साठवण्यासाठी वापरलेले नाव. Python उदाहरण: age = 20. येथे age या variable मध्ये 20 साठवले आहे.",
    "data type": "Data type म्हणजे value कोणत्या प्रकारची आहे हे. उदाहरणे: int म्हणजे पूर्णांक, float म्हणजे दशांश संख्या, str म्हणजे text आणि bool म्हणजे True/False.",
    "loop": "Loop म्हणजे एकच code पुन्हा पुन्हा चालवणे. उदाहरणार्थ, 1 ते 5 पर्यंत संख्या print करणे.",
    "for loop": "For loop चा वापर sequence किंवा range मधील प्रत्येक item साठी code चालवण्यासाठी होतो.",
    "while loop": "While loop condition True असेपर्यंत code पुन्हा चालवतो. Condition कधी false होईल याची काळजी घ्यावी.",
    "function": "Function म्हणजे पुन्हा वापरता येणारा code चा भाग. त्यामुळे code व्यवस्थित आणि reusable होतो.",
    "list": "Python मधील list मध्ये अनेक values क्रमाने साठवता येतात. उदाहरण: fruits = ['apple', 'mango']",
    "dictionary": "Python dictionary मध्ये key-value pairs असतात. उदाहरण: student = {'name': 'Asha', 'age': 20}",
    "oop": "OOP म्हणजे Object-Oriented Programming. यात class आणि object वापरून code organize करतात. मुख्य concepts: inheritance, encapsulation, abstraction आणि polymorphism.",
    "class": "Class म्हणजे objects तयार करण्यासाठीचा blueprint किंवा आराखडा.",
    "object": "Object म्हणजे class चा instance. त्यात data आणि त्या data वर काम करणाऱ्या methods असू शकतात.",
    "algorithm": "Algorithm म्हणजे एखादी समस्या सोडवण्यासाठी दिलेल्या स्पष्ट, क्रमवार steps.",
    "debugging": "Debugging म्हणजे program मधील चुका शोधून त्या दुरुस्त करणे.",
    "frontend": "Frontend म्हणजे website चा user ला दिसणारा आणि वापरता येणारा भाग. HTML, CSS आणि JavaScript वापरले जातात.",
    "backend": "Backend म्हणजे server वर चालणारा भाग. तो logic, database आणि API requests हाताळतो. Python + Flask हा एक पर्याय आहे.",
    "website": "Website तयार करताना HTML structure साठी, CSS design साठी, JavaScript interaction साठी आणि गरजेनुसार Python/Flask backend साठी वापरता येते.",
    "database": "Database म्हणजे माहिती व्यवस्थित साठवण्याची जागा. उदाहरणे: MySQL, SQLite, PostgreSQL आणि MongoDB.",
    "api": "API म्हणजे दोन software systems ना एकमेकांशी संवाद साधण्यासाठी असलेला नियमबद्ध मार्ग.",
    "github": "GitHub ही code projects online ठेवण्यासाठी आणि इतरांसोबत collaborate करण्यासाठीची platform आहे.",
    "ai": "AI म्हणजे Artificial Intelligence. संगणकाला शिकणे, भाषा समजणे किंवा image ओळखणे यांसारखी कामे करण्यास सक्षम करणारे तंत्रज्ञान.",
    "machine learning": "Machine Learning मध्ये computer data मधील patterns शिकतो आणि त्यावरून prediction किंवा classification करतो.",
    "hardware": "Hardware म्हणजे संगणकाचे physical parts—उदा. keyboard, monitor, CPU, RAM आणि motherboard.",
    "software": "Software म्हणजे संगणकाला काय करायचे ते सांगणारे programs आणि instructions.",
    "cpu": "CPU म्हणजे Central Processing Unit. तो instructions execute करतो आणि calculations करतो.",
    "ram": "RAM ही computer ची temporary working memory आहे. वीज बंद झाल्यावर तिच्यातील data साधारणपणे टिकत नाही.",
    "internet": "Internet हे जगभरातील computers आणि networks जोडणारे मोठे network आहे.",
    "help": "तू असे प्रश्न विचारू शकतेस: Python म्हणजे काय? Loop काय असतो? HTML आणि CSS मध्ये काय फरक आहे? Variable म्हणजे काय? Frontend आणि Backend काय आहेत? एखाद्या language चे नाव लिहूनही विचारू शकतेस.",
}

MARATHI_GREETINGS = {
    "नमस्कार": "नमस्कार! 😊 मी CodeBuddy आहे. तू मला Marathi, English किंवा Marathi-English मध्ये computer languages आणि coding बद्दल प्रश्न विचारू शकतेस.",
    "हाय": "हाय! 😊 Python, Java, HTML, CSS, coding basics किंवा computer बद्दल काहीही विचार.",
    "hello": "Hello! 😊 तू Marathi, English किंवा Marathi-English मध्ये प्रश्न विचारू शकतेस.",
    "hi": "Hi! 😊 तू Marathi, English किंवा Marathi-English मध्ये प्रश्न विचारू शकतेस.",
    "धन्यवाद": "तुझं स्वागत आहे! 😊 Coding चा सराव करत राहा.",
    "थँक यू": "तुझं स्वागत आहे! 😊 आणखी काही शिकायचं असेल तर विचार.",
    "बाय": "बाय! 😊 शिकत राहा आणि छोटे projects बनवत राहा.",
}

def _marathi_topic_key(user_text: str):
    lowered = user_text.lower().strip()
    # Longer aliases first to avoid matching a short phrase too early.
    for alias in sorted(MARATHI_ALIASES, key=len, reverse=True):
        if alias.lower() in lowered:
            return MARATHI_ALIASES[alias]
    # Common Roman-Marathi question wording.
    roman_aliases = {
        "mhanje kay": None,
        "kay ahe": None,
        "samjaun sang": None,
        "samjhavun sang": None,
        "sang na": None,
        "marathi madhe": None,
    }
    cleaned = lowered
    for phrase in roman_aliases:
        cleaned = cleaned.replace(phrase, " ")
    for key in sorted(TOPICS, key=len, reverse=True):
        if key.strip() and key in cleaned:
            return key
    return None

def _looks_marathi(user_text: str) -> bool:
    devanagari = any("\u0900" <= ch <= "\u097f" for ch in user_text)
    roman = any(phrase in user_text.lower() for phrase in [
        "mhanje", "kay ahe", "samja", "sang", "mala", "marathi", "kas", "kasa", "kashi", "kaay"
    ])
    return devanagari or roman


def get_reply(message: str) -> str:
    user_text = message.strip()
    lowered = user_text.lower()

    # Marathi greetings first.
    for greeting, reply in MARATHI_GREETINGS.items():
        if lowered == greeting.lower():
            return reply

    # Map Marathi/Marathi-English wording to a known topic.
    marathi_mode = _looks_marathi(user_text)
    mapped_key = _marathi_topic_key(user_text)
    if mapped_key:
        if marathi_mode and mapped_key in MARATHI_ANSWERS:
            return MARATHI_ANSWERS[mapped_key]
        if mapped_key in TOPICS:
            return TOPICS[mapped_key]
        if mapped_key == "your name":
            return "माझं नाव CodeBuddy आहे! मी computer languages आणि coding basics शिकायला मदत करतो."

    # Existing English behavior.
    if lowered in GREETINGS:
        return GREETINGS[lowered]

    # Match longer topic phrases before shorter ones.
    for key in sorted(TOPICS.keys(), key=len, reverse=True):
        if key.strip() and key in lowered:
            return TOPICS[key]

    if any(word in lowered for word in ["who are you", "your name", "what can you do"]):
        return "I'm CodeBuddy, a beginner-friendly rule-based learning assistant. You can ask in Marathi, English, or Marathi-English about programming languages, coding basics, web development, databases, and computer fundamentals."
    if any(word in lowered for word in ["what is", "explain", "meaning", "define", "tell me about"]):
        if marathi_mode:
            return "मला त्या विषयाचं तयार उत्तर अजून माहित नाही. Python, Java, HTML, CSS, SQL, variable, loop, function, database किंवा computer basics बद्दल विचारून बघ."
        return "I don't have a prepared explanation for that exact topic yet. Try asking about Python, Java, C/C++, JavaScript, HTML, CSS, SQL, variables, loops, functions, OOP, databases, AI, or computer basics."
    if marathi_mode:
        return "माफ कर, हा प्रश्न मला अजून नीट समजला नाही. 😊 Python, Java, HTML, CSS, SQL, variable, loop किंवा computer basics बद्दल विचारून बघ. हा starter chatbot prepared answers वापरतो; तो पूर्ण AI chatbot नाही."
    return "I'm not sure about that exact question yet. Try asking about a computer language or basic topic. Type 'help' to see examples. This starter version uses prepared answers; it is not connected to an AI service."
