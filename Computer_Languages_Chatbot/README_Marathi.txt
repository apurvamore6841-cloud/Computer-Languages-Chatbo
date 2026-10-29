CODEBUDDY - Computer Languages Chatbot
======================================

हा Python + Flask + HTML + CSS + JavaScript वापरून बनवलेला beginner-friendly chatbot website starter project आहे.

यात समाविष्ट विषय:
- Computer basics: CPU, RAM, ROM, hardware, software, OS, internet, networking
- Programming basics: variables, data types, loops, conditions, functions, arrays/lists, OOP, algorithms, debugging
- Languages: Python, Java, C, C++, C#, JavaScript, TypeScript, PHP, Ruby, Go, Rust, Kotlin, Swift, R, SQL, HTML, CSS, Bash, Dart, Scala, Lua, MATLAB, Perl, Scratch, Assembly
- Web development: frontend, backend, full stack, Flask, Django, React, Node.js, Angular, Vue, API, JSON
- Databases: SQL, MySQL, PostgreSQL, MongoDB
- Tools and careers: VS Code, Git, GitHub, AI, machine learning, data science, cybersecurity, project ideas

महत्त्वाचे:
हा rule-based starter chatbot आहे. तो तयार केलेल्या उत्तरांमधून keywords match करतो; तो स्वतःहून प्रत्येक शक्य प्रश्न समजू शकत नाही आणि सध्या AI API ला जोडलेला नाही. नंतर AI API जोडून वाढवता येईल.

Windows / VS Code मध्ये चालवण्याची पद्धत
-----------------------------------------
1. ZIP extract करा.
2. VS Code उघडा → File → Open Folder → Computer_Languages_Chatbot निवडा.
3. Terminal → New Terminal उघडा.
4. Virtual environment तयार करा:
   python -m venv venv
5. PowerShell मध्ये activate करा:
   .\venv\Scripts\Activate.ps1
   जर execution policy मुळे error आला, तर त्या error चा मजकूर पाठवा. Policy बदलण्याआधी error पाहू.
6. Flask install करा:
   pip install -r requirements.txt
7. Website चालवा:
   python app.py
8. Browser मध्ये ही local address उघडा:
   http://127.0.0.1:5000

Folder structure
----------------
Computer_Languages_Chatbot/
  app.py
  chatbot_data.py
  requirements.txt
  README_Marathi.txt
  templates/
    index.html
  static/
    style.css
    script.js

Troubleshooting
---------------
- 'python is not recognized': Python install आहे का तपासा; installation मध्ये Add Python to PATH निवडलेले असावे.
- 'No module named flask': venv activate करून pip install -r requirements.txt चालवा.
- Website उघडत नसेल: terminal मधील error पाहा आणि http://127.0.0.1:5000 वापरा.
- app.py चालू असताना terminal बंद करू नका.


MARATHI + ENGLISH SUPPORT
-------------------------
Ata chatbot Marathi (देवनागरी), English ani Marathi-English transliteration
(udaa. "Python mhanje kay?") madhil kahi common coding questions samjun gheto.
Python, Java, HTML, CSS, SQL, variables, loops, functions, frontend/backend,
database ani computer basics sathi kahi Marathi answers add kele aahet.

Lakshat theva: ha rule-based chatbot aahe. To pratyek navin/complex prashnala
barobar uttar deil yachi guarantee nahi. Sarva prashnanna natural Marathi
uttare havi astil tar AI language-model API connect karavi lagel.
