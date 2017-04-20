from prob3 import generate, closed_form

print('======= CLOSED FORM=======')
print('=====OUTPUT ~ [2, -1]=====')
train_set, values = generate((-1, 1), 10000, 0.1)
print(closed_form(train_set, values))