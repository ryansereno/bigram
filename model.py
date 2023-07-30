import torch 

with open('names.txt', 'r') as file:
    words = file.read().splitlines()

#initialize a dictionary
b = {}

for w in words:
  #add a start and end token to every workd
  chars = ['<Start>'] + list(w) + ['<End>']
  for char1, char2 in zip(chars, chars[1:]):
    bigram = (char1, char2)
    b[bigram] = b.get(bigram, 0) + 1

sorted(b.items(), key = lambda kv: -kv[1])

N = torch.zeros((27,27), dtype=torch.int32)

#get alpha sorted list of all chars in dataset
chars = sorted(list(set(''.join(words))))

#create dictionary, where key is the char, and val is the index (0-26)
stoi = {s:i+1 for i,s in enumerate(chars)}

#Add start and end tokens to dictionary
stoi['.'] =0 

#also create index:string dictionary copy, for graphing purposes
itos = {i:s for s,i in stoi.items()}

#iterate over every word in dataset
for w in words:

 #add start and end token to the string 
  chars = ['.'] + list(w) + ['.']

  #iterate over chars of word, paring with next char, using a zip object
  for char1, char2 in zip(chars, chars[1:]):

    #get index of chars from the dictionary
    ix1 = stoi[char1]
    ix2 = stoi[char2]

    #using the two char indexes, increment the count of that combination in the matrix
    N[ix1, ix2] += 1

g = torch.Generator().manual_seed(2147483647)

#normalize all rows in the matrix, turning them into probabilities
#normalization makes the sum of the row == 1, making them probabilities, not counts
P = N.float()

#use in-place operations when possible; they don't require allocating new memory
#this creates a new vector
#P = P/P.sum(1, keepdim=True)

#this only updates the existing vector in memory
P /= P.sum(1, keepdim=True)

for i in range(10):
  out = []
  ix = 0
  while True:
    p = P[ix]
    ix = torch.multinomial(p, num_samples=1, replacement=True).item()
    out.append(itos[ix])
    if ix == 0:
      break

  print(''.join(out))
