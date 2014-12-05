
import random 
import sys

def generateModel(text, level):
  words = text.split(' ')
  model = {}
  for i in range(0, len(words) - level):
    fragment  = ''.join(words[i:i+level])
    next_word = words[i+level]
    if fragment not in model:
      model[fragment] = {}
    if next_word not in model[fragment]:
      model[fragment][next_word] = 1
    else:
      model[fragment][next_word] += 1
  return model

def getNextWord(model, fragment):
  words = []
  for word in model[fragment].keys():
    for times in range(0, model[fragment][word]):
      words.append(word)
  return random.choice(words)

def generateText(text, level, length):
  model = generateModel(text, level)
  words = text.split(' ')

  start = random.randint(0, len(words) - 1 - level)
  currentFragment = []
  for i in range(level):
    currentFragment.append(words[start+i])

  output = []
  for i in range(0, length - level):
    output.append(currentFragment[0])
    nextWord = getNextWord(model, ''.join(currentFragment))
    for i in range(1, level):
      currentFragment[i - 1] = currentFragment[i]
    currentFragment[level-1] = nextWord
  output.append(currentFragment[level-1])
  print ' '.join(output)


if __name__ == '__main__':

  if len(sys.argv) != 4:
    print 'usage: python markov.py <filename> <level> <length>'
    sys.exit(1)

  with open(sys.argv[1], 'r') as f:
    text = f.read().replace('\n', ' ')
  generateText(text, int(sys.argv[2]), int(sys.argv[3]))
