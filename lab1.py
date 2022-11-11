from transformers import pipeline

pipe = pipeline("question-answering")

context = r"""
Pink Floyd was a rock band formed in London in 1965.
The Beatles was a pop band formed in Liverpool.
The reason there are no dinosaurs is that they are extinct.
The ratio between men and women is 10:1.
There are 400 men here.
There are 40 women here.
"""
print(pipe(question="When was Pink Floyd formed?", context=context))
print(pipe(question="Where was Pink Floyd formed?", context=context))
print(pipe(question="Why are there no dinosaurs?", context=context))
print(pipe(question="What is Pink Floyd?", context=context))
print(pipe(question="What is Beatles?", context=context))
print(pipe(question="Who were formed in Liverpool?", context=context))
print(pipe(question="What is the ratio between men and women?", context=context))
print(pipe(question="How many men are there?", context=context))
print(pipe(question="How many are men?", context=context))
print(pipe(question="How many are women?", context=context))
