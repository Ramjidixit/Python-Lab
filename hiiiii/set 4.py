#1
a=input("Enter thw comma separated words:")
words=[word for word in a.split(",")]
print(",".join(sorted(list(set(words)))))