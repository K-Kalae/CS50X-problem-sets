text = input("Text: ").lower()
num_sentences = 0
print(text.split())
for z in text:
    if z in [".","?", "!"]:
        num_sentences+=1
num_words = 0
num_letters = 0
text_letters = text.strip()
for ch in text:
    if ch.isalpha():
        num_letters+=1
for p in text.split():
    num_words+=1

L = float((num_letters * 100)/(num_words))
S= float((num_sentences * 100)/(num_words))
grade = round(0.0588 * L - 0.296 * S - 15.8)


if grade > 16:
    print("Grade 16+")
elif grade < 1:
    print("Before Grade 1")
else:
    print(f"Grade {grade}")
