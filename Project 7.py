#In this program we are creating a pig latin translator.
#The programs gets user input and prints out the output in pig latin.

#Get user input
user = input('Enter your two names: ').lower().strip()
print() #add space
words = user.split()
newwords =[]#to store the converted words

for word in words:
  #check if word starts with a vowel and add yay at the end.
  if word[0] in 'aeiou':
    newwords.append(word+'yay')
  else:
    #check for words that do not start in a vowel
    vowelpos=0 #checking the position of first vowel
    for letter in word:
      if letter not in 'aeiou':
        vowelpos += 1
      else:
        break
      #slice consonants and vowels and add ay at the end
      cons = word[:vowelpos]
      vowels = word[vowelpos:]
      combined = vowels+cons+'ay'
      newwords.append(combined)

#join the new words

result = ' '.join(newwords)

print(f'Your name in pig latin is : {result}!')
