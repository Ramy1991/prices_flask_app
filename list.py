import langid

lang = langid.classify("")
print(lang[0])
# ('en', -54.41310358047485)