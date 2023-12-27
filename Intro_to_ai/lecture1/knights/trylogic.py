from logic import *

harry = Symbol("harry")
rain = Symbol("rain")
dumbledore = Symbol("dumbledore")

knowledge = And(
    Or(harry, dumbledore),
    Implication(Not(rain), harry),
    Not(And(harry, dumbledore)))
print(model_check(knowledge, rain))
print(model_check(knowledge, dumbledore))
print(model_check(knowledge, harry))
print(model_check(knowledge, knowledge))

print(knowledge.formula())
