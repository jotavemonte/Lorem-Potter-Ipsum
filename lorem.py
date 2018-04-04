import numpy as np

def lorem_generator(paragraphs_number):
    """This function aims to build a lorem generator for the DinofauroFexBot"""
    conectives_list =   ['do','vah','ki','in','pro','stra','gma','tri','tong','ne','et','me','tos','bahs','noni','male'] #Aleatórios
    words_list      =   ['avada','kedavra','lumus','maximus','accio','aguamenti','alarte','ascendare','alohomora','aparecium','apparate',
                         'aqua','eructo','ascendio','avis','avifors','arresto','momentum','arania','exumai','baubillious','bombarda','maxima','brackium','emendo',
                         'calvario','cantis','carpe','retractum','cave','inimicum','cistem','aperio','colloportus','colloshoo','colovaria','cofundo','ventus','duo','vara',
                         'verto','verdimillious']
                     #Source: http://harrypotter.wikia.com/wiki/List_of_spells (Inseridas manualmente)
    #pontuation = ",.!?"
    #rr stands for repeat rule (after x events will ocur, where x is the number designated for each variable)
    numberof_paragraphs = range(paragraphs_number)
    conectives_rr       = 3 #Could variate randomly. It will be analised later
    lorem               = ""
    len_conectives      = len(conectives_list)
    len_words           = len(words_list)
    for i in numberof_paragraphs:
        conective_flag      = 1
        paragraphslen_rr    = np.random.randint(80,150)
        for j in range(paragraphslen_rr):
            comma_rr = np.random.randint(4,15)
            if conective_flag == 3:
                lorem += conectives_list[np.random.randint(0,len_conectives)] + " "
		conective_flag = 1
            lorem = lorem + words_list[np.random.randint(0,len_words)] + " "
            conective_flag += 1
        lorem += ".\n\n"
    return lorem

print(lorem_generator(3))
