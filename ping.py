tests=[]
tests.append(tests)
def locate_card(cards,query):
    pass
test={
    'input':{
        'cards': [3,1,9,-127],
        'query': -127
    },
    'output':3
}
#result=locate_cards(cards,query)
#print(result)
#result==output
print(locate_card(**test['input']) == test['output'])
print(test)
#from jovian.pythondsa import evaluate_test_case
#for test in tests:   gives the output for all cases
#    print(locate_card(**test['input'])==test['output'])
#evaluate_test_case(locate_card,tests)
def locate_card(cards,query):
    position=0
    print("Cards : ",cards)
    print("Query :",query)
    while True:
        print("Position : ",position)
        if cards[position] == query:
            return position
        position += 1
        if(position == len(cards)):
            return -1
#cards6=tests[6]['input']['cards']
#query6=tests[6]['input']['query']
#locate_cards(cards6,query6)