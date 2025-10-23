**Tamil to English Transliteration**

A simple **Python** project that transliterates **Tamil text into English** — preserving pronunciation, not meaning.
It converts Tamil Unicode characters into their equivalent Romanized English representation.

--------------------------------------------------------------------------------------------

📘 What’s the Difference?

Translation → Converts meaning (Tamil → English)

Example: “நான் வீட்டுக்கு போகிறேன்” → “I am going home.”

Transliteration → Converts sounds/letters

Example: “நான் வீட்டுக்கு போகிறேன்” → “naan veettukku pogiren”

This project performs transliteration, not translation.

--------------------------------------------------------------------------------------------

⚙️ How It Works

The system uses two Python files:

  File	                                                                         Purpose
tamil_unicode_map.py	            Contains a dictionary (charmap) that maps Tamil Unicode characters to English equivalents.
ta_eng.py	                        The main engine that reads Tamil text, converts it using the charmap, and outputs transliterated text.

----------------------------------------------------------------------------------------------
🧠 Flow

Tamil text is read from input.txt.

Each Tamil character is identified and mapped using tamil_unicode_map.py.

The logic in ta_eng.py handles pulli, dependent vowels, and compound characters.

Final transliteration is written to output.csv.

----------------------------------------------------------------------------------------------

📂 Project Structure

tamil-transliteration/
│
├── ta_eng.py               # Main transliteration logic
├── tamil_unicode_map.py    # Tamil → English character mapping
├── input.txt               # Input Tamil text file
└── output.csv              # Output file (generated automatically)

----------------------------------------------------------------------------------------------


🚀 How to Run

1️⃣ Clone the Repository

git clone https://github.com/<your-username>/tamil-transliteration.git
cd tamil-transliteration

2️⃣ Add Tamil Text

Put your Tamil sentences in input.txt, one per line.

Example:

நான் வீட்டுக்கு போகிறேன்
இது ஒரு சோதனை

3️⃣ Run the Script

python ta_eng.py

4️⃣ Check the Output

Open output.csv — you’ll see both Tamil and English transliterations side by side.

Example:

Tamil Text	                              English Transliteration

நான் வீட்டுக்கு போகிறேன்	              naan veettukku pogiren
இது ஒரு சோதனை	                    idhu oru sothanai

----------------------------------------------------------------------------------------------

🧩 Example Code Snippet

from tamil_unicode_map import charmap
from ta_eng import TamilTransliterator

t = TamilTransliterator(charmap)
text = "தமிழ்"
print(t.transliterate(text))   # Output: tamizh

----------------------------------------------------------------------------------------------

🛠 Requirements

Python 3.x

No external libraries required (uses only built-in modules)

----------------------------------------------------------------------------------------------

📜 License

This project is open-source under the MIT License — feel free to use, modify, and share.

----------------------------------------------------------------------------------------------

💡 Author

Rahul Vanchivel
Software Developer | Tech Enthusiast

✨ "Code what you speak — speak what you code." ✨
