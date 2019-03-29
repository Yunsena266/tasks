# Enter a sentence consisting of words and punctuation marks. Delete marks and leave only words.
sen=(input("write the sentence",).split());
punctuation=['.','.',':','!','?',';','/','-'];
i=0;
for a in sen:
    if a[-1] in punctuation:
        sen[i]=a[:-1];
        a=sen[i];
    if a[0] in punctuation:
        sen[i]=a[1:];
        a=sen[i];
    i=i+1;
print(sen);




