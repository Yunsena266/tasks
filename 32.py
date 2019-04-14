func=lambda x,y: x*y
print(func(2,5))


colors=['red','orange','white','black'];
sortFunc=map(lambda a: a.casefold(),colors);
print(colors)



def story_edition (words,func):
    for word in words:
        print(func(word))
words=['black','yellow','red'];
story_edition(words, lambda word: word.capitalize()+'!');



