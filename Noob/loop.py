externo = ['in0','a','in1']
interno = ['in0','in1', 'in2']

def loop_break(externo, interno):
    
    for ext in range(len(externo)):
        for inter in range(len(interno)):
            if externo[ext] == interno[inter]:
                print(externo[ext] + ' = ' + interno[inter] + '  break')
                break
            else:
                print('diferente')   

def loop_return(externo, interno):
    
    for ext in range(len(externo)):
        for inter in range(len(interno)):
            if externo[ext] == interno[inter]:
                print(externo[ext] + ' = ' + interno[inter] + '  return')
                return
            else:
                print('diferente_return')   

loop_break(externo, interno)

loop_return(externo, interno)