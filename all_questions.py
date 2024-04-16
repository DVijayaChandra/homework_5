import pytest
from all_questions import *
import pickle



#-----------------------------------------------------------
def question1():
    answers = {}

    # type: float
    # Calculate the probability.
    answers['(a)'] = 0.0288

    # type: float
    # Calculate the probability.
    answers['(b)'] = 0.002

    # type: float
    # Calculate the probability.
    answers['(c)'] = 0.0080
    return answers


#-----------------------------------------------------------
def question2():
    answers = {}

    # type: bool
    answers['(a) A'] = True

    # type: bool
    answers['(a) B'] = False

    # type: bool
    answers['(a) C'] = False

    # type: bool
    answers['(a) D'] = True

    # type: bool
    answers['(b) A'] = True

    # type: bool
    answers['(b) B'] = False

    # type: bool
    answers['(b) C'] = True

    # type: bool
    answers['(b) D'] = False

    # type: eval_float
    # The formulas should only use the variable 'p'. The formulas should be
    # a valid Python expression. Use the functions in the math module as
    # required.
    answers['(c) Weight update'] = '0.5 * math.log((1 - p) / p)'

    # type: float
    # the answer should be correct to 3 significant digits
    answers['(d) Weight influence'] = 1.528
    return answers


#-----------------------------------------------------------
def question3():
    answers = {}

    # type: string
    answers['Agree?'] = 'no'

    # type: explain_string
    answers['Explain'] = 'Alans method of predicting stock market movements by flipping a coin and relying on the majority outcome lacks effectiveness as an application of ensemble methods. Ensemble methods entail aggregating predictions from numerous independent classifiers trained on data, whereas a coin flip lacks any training or learning process. Consequently, Alans approach is fundamentally flawed and improbable to yield meaningful predictions for the stock market.'
    return answers


#-----------------------------------------------------------
def question4():
    answers = {}

    # type: bool
    answers['(a) e=0.5, independent'] = False

    # type: bool
    answers['(b), independent'] = True

    # type: bool
    answers['(c) identical'] = False
    return answers


#-----------------------------------------------------------
def question5():
    answers = {}

    # type: string
    # choices: ['i', 'ii', 'iii', 'iv']
    answers['(a)'] = 'iii'

    # type: string
    # choices: ['i', 'ii', 'iii', 'iv']
    answers['(b)'] = 'i'

    # type: string
    # choices: ['i', 'ii', 'iii', 'iv']
    answers['(c)'] = 'ii'

    # type: string
    # choices: ['i', 'ii', 'iii', 'iv']
    answers['(d)'] = 'iv'
    return answers


#-----------------------------------------------------------
def question6():
    answers = {}

    # type: eval_float
    answers['(a) C1-TPR'] = "p"

    # type: eval_float
    answers['(a) C2-TPR'] = "2*p"

    # type: eval_float
    answers['(a) C1-FPR'] = "p"

    # type: eval_float
    answers['(a) C2-FPR'] = "2*p"

    # type: string
    # Hint: The random guess line in an ROC curve corresponds to TPR=FPR.
    # choices: ['yes', 'no']
    answers['(b) C2 better classifier than C1?'] = "no"

    # type: explain_string
    answers['(b) C2 better classifier than C1? Explain'] = "Similarly, the independent classifiers work like the random nature when two conditions, true positive rate (TPR) and false positive rate (FPR), come to be revealed as equals. For C2 to have greater efficiency with the preference to the positive class, the accuracy cannot be only quantified by the value from TPR and FPR rise or fall, even if both of those two indicator values moved in the same direction. Through this, we will come up with outcomes that is same as the random process."

    # type: string
    # choices: ['TPR/FPR', 'precision/recall']
    answers['(c) Which metric?'] = "TPR/FPR"

    # type: explain_string
    answers['(c) explain'] = "TPR and FPR show the ability of good to predict and its overall power on class performance whether positive or negative. For this reason, it is the case that C1 and C2 whose false positive and true positive rates are equal have ROC performance similar to such a random guess as a basis for comparison. While precision and recall make true negatives irrelevant when evaluating algorithms which make random guesses for each class respectively, they can give incomplete and often misleading perspective."
    return answers


#-----------------------------------------------------------
def question7():
    answers = {}

    # type: string
    # choices: ['C1', 'C2', 'None']
    answers['(i) Best classifier?'] = "C2"

    # type: explain_string
    answers['(i) Best classifier, explain'] = "C2 was thus the most appropriate choice, based on his relatively high recall/TPR and F1-measure performance compared to C1. This assumption appears that C2 recognizes more positive cases than that of a more balanced precisions and recall depiction."

    # type: string
    # choices: ['TPR-FPR', 'precision-recall-F1-Measure']
    answers['(ii) appropriate metric pair'] = "precision-recall-F1-Measure"

    # type: explain_string
    answers['(ii) appropriate metric pair, explain'] = "Precision, recall, and F1-measure can serve as a reasonable framework as they show the overall performance of a classifier mainly in the datasets with imbalanced situation that the positive instances are less often than negative ones"

    # type: string
    # choices: ['C1', 'C2', 'C3']
    answers['(iii) preferred classifier?'] = "C3"

    # type: explain_string
    answers['(iii) best classifier, explain'] = "C2 dominates over the others because of accuracy and the ability to compromise with the precision and recall apparently, reaching the highest F1-measure. Even while it displays the best precision, C3 shoulders this burden at the expense of recall and therefore underscores that this model is unfit for scenarios where detecting all positive cases are the ingredients of the situation."
    return answers


#-----------------------------------------------------------
def question8():
    answers = {}

    # type: eval_float
    answers['(a) precision for C0'] = '(p*100)/(p*1000)'

    # type: eval_float
    answers['(a) recall for C0'] = 'P'#0.5

    # type: eval_float
    answers['(b) F-measure of C0'] =  '(0.2 * P) / (0.1 + P)'#0.16666

    # type: string
    # choices: ['yes', 'no', 'unknown']
    answers['C1 better than random?'] = 'no'

    # type: float
    # What is the range of p for which C1 is better than random?  What is
    # "?" in the expression "p > ?"

    answers['p-range'] = 0.3#0.3
    return answers


#-----------------------------------------------------------
def question9():
    answers = {}

    # type: dict[string,float]
    # keys: ['recall', 'precision', 'F-measure', 'accuracy']
    answers['(i) metrics'] =  {
        'recall': 0.533,
        'precision': 0.6154,
        'F-measure': 0.5689,
        'accuracy': 0.8800
    }

    # type: string
    # choices: ['recall', 'precision', 'F-measure', 'accuracy']
    answers['(i) best metric?'] = 'F-measure'

    # type: string
    # choices: ['recall', 'precision', 'F-measure', 'accuracy']
    answers['(i) worst metric?'] = 'Accuracy'

    # type: explain_string
    answers['(ii) Explain your choices of best and worst metrics'] = "In this instance, the meaningful metric is F-measure that provides a balance between precision and recall that is especially appreciated for imbalanced classes, examples of which are weather prediction and other areas with a dominant kind of outcome. However, accuracy shows to be the least proper indicator that is easily inflated by many true negatives that does not mean the minor class predicting is effective enough."
    return answers


#-----------------------------------------------------------
def question10():
    answers = {}

    # type: string
    # choices: ['T1', 'T2']
    answers['(a) better test based on F-measure?'] = "T1"

    # type: string
    # choices: ['T1', 'T2']
    answers['(b) better test based on TPR/FPR?'] = "T2"

    # type: string
    # choices: ['F1', 'TPR/FPR']
    answers['(c) Which evaluation measure to use between the two tests?'] = "F1"

    # type: explain_string
    answers['(c) Which evaluation measure? Explain'] = "The reason for the choice of the F1-Score is in the fact that it is able to provide a more fair evaluation of a test's precision thanks to the combination of both precision and recall. This, consequently, makes it suitable to be used in clinical trials where the impact of generating false positives and false negatives is critical."

    # type: explain_string
    answers['(d) Example scenario where you would reverse choise in (c)'] = "In instances where accuracy maintaining and finding true cases is prioritized, like in case of early screening for a very dangerous disease, metrics TPR (True Positive Rate) and FPR (False Positive Rate) could be preferred over the F1-Score. This preference is due to their focus on sensitivity perpendicular to precision, which gives preference to TP over FP."
    return answers
#-----------------------------------------------------------
if __name__ == '__main__':
    answers_dict = {}
    answers_dict['question1'] = question1()
    answers_dict['question2'] = question2()
    answers_dict['question3'] = question3()
    answers_dict['question4'] = question4()
    answers_dict['question5'] = question5()
    answers_dict['question6'] = question6()
    answers_dict['question7'] = question7()
    answers_dict['question8'] = question8()
    answers_dict['question9'] = question9()
    answers_dict['question10'] = question10()

    with open('answers.pkl', 'wb') as f:
        pickle.dump(answers_dict, f)
