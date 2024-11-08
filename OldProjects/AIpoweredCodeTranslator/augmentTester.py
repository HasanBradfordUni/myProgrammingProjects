import nlpaug.augmenter.word as naw
import nlpaug.augmenter.char as nac

with open("Code.txt", "r") as file:
    data = file.readlines()
    print(data)

lowercaseWords = []

for line in data:
    for word in line.split():
        if word.islower():
            lowercaseWords.append(word)
    aug = naw.SynonymAug(aug_src='wordnet', name='Synonym_Aug', aug_min=1, aug_max=100, aug_p=0.3,stopwords=lowercaseWords,
                         lang='eng', tokenizer=None, reverse_tokenizer=None, force_reload=False, verbose=0)
    augmented_text = aug.augment(line)
    print("Original:")
    print(line)
    print("Augmented Text:")
    print(augmented_text)
    print("-" * 50)