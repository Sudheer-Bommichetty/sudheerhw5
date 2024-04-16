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
    answers['Explain'] = 'Alans approach of predicting stock market movements by flipping a coin and using the majority outcome is not an effective application of ensemble methods. Ensemble methods involve combining predictions from multiple independent classifiers trained on data, whereas a coin flip does not involve any training or learning process. Therefore, Alans approach is fundamentally flawed and is unlikely to provide meaningful predictions for the stock market.'
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
    answers['(b) C2 better classifier than C1? Explain'] = "Both classifiers operate similarly to random guessing when the true positive rate (TPR) equals the false positive rate (FPR). Boosting the likelihood of predicting the positive class doesn't improve the effectiveness of C2, as it raises both TPR and FPR equally, resulting in performance comparable to random chance."

    # type: string
    # choices: ['TPR/FPR', 'precision/recall']
    answers['(c) Which metric?'] = "TPR/FPR"

    # type: explain_string
    answers['(c) explain'] = "TPR and FPR evaluate the positive predictions and their overall influence on performance across both classes. Given that C1 and C2 share identical TPR and FPR values, they exhibit equivalent performance relative to the random guess baseline on an ROC curve. Precision and recall, which disregard true negatives, provide less informative insights when assessing classifiers that produce random predictions for imbalanced classes."
    return answers


#-----------------------------------------------------------
def question7():
    answers = {}

    # type: string
    # choices: ['C1', 'C2', 'None']
    answers['(i) Best classifier?'] = "C2"

    # type: explain_string
    answers['(i) Best classifier, explain'] = "C2 emerges as the superior classifier due to its significantly elevated recall/TPR and F1-measure compared to C1. This suggests that C2 accurately detects a greater number of positive instances while achieving a more favorable balance between precision and recall."

    # type: string
    # choices: ['TPR-FPR', 'precision-recall-F1-Measure']
    answers['(ii) appropriate metric pair'] = "precision-recall-F1-Measure"

    # type: explain_string
    answers['(ii) appropriate metric pair, explain'] = "Precision, recall, and F1-measure serve as suitable metrics as they offer a comprehensive assessment of a classifier's performance, particularly crucial in scenarios with imbalanced datasets where positive instances are significantly less common than negatives."

    # type: string
    # choices: ['C1', 'C2', 'C3']
    answers['(iii) preferred classifier?'] = "C3"

    # type: explain_string
    answers['(iii) best classifier, explain'] = "C2 is favored due to its ability to strike a balance between precision and recall, evident from its highest F1-measure among the classifiers. Although C3 exhibits the highest precision, it does so at the cost of recall, rendering it less preferable for situations where capturing all positive instances is crucial."
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
    answers['(ii) Explain your choices of best and worst metrics'] = "The optimal metric in this scenario is the F-measure, as it offers an equilibrium between precision and recall, which holds particular importance in contexts characterized by imbalanced classes, like weather prediction where one outcome might prevail. Conversely, accuracy proves to be the least suitable metric since it can be inflated by a multitude of true negatives, which doesn't necessarily reflect effective predictive capabilities for the minority class."
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
    answers['(c) Which evaluation measure? Explain'] = "The selection of the F1-Score is motivated by its ability to offer a more equitable assessment of a test's precision, amalgamating both precision and recall. This makes it particularly apt for assessing clinical tests, where the implications of false positives and false negatives are substantial."

    # type: explain_string
    answers['(d) Example scenario where you would reverse choise in (c)'] = "In situations where prioritizing the identification of true cases is paramount, such as in early screening for a highly hazardous disease, metrics like TPR (True Positive Rate) and FPR (False Positive Rate) could be favored over the F1-Score. This preference is due to their emphasis on the ratio of true positives to false positives, placing greater importance on sensitivity rather than precision."
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
