from sentence_transformers import SentenceTransformer

model = SentenceTransformer('all-MiniLM-L6-v2')

sentence1 = "XUV700 has a mileage of 18 kmpl"
sentence2 = "Scorpio-N has a mileage of 15 kmpl"
sentence3 = "The weather today is sunny."

embedding1 = model.encode(sentence1)
embedding2 = model.encode(sentence2)
embedding3 = model.encode(sentence3)

print("Length of embedding vector:", len(embedding1))
print()
print("Sentence 1:", sentence1)
print("First 5 numbers of embedding1:", embedding1[:5])
print()
print("Sentence 2:", sentence2)
print("First 5 numbers of embedding2:", embedding2[:5])
print()
print("Sentence 3:", sentence3)
print("First 5 numbers of embedding3:", embedding3[:5])