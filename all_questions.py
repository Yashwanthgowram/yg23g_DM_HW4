# Add import files
import pickle



# -----------------------------------------------------------
def question1():
    answers = {}

    # string "yes" or "no"
    answers["(a)"] = "no"
    answers["(b)"] = "no"
    answers["(c)"] = "yes"
    answers["(d)"] = "yes"

    # explain-string: explanation in english prose
    answers["(a) explain"] = "Mutual exclusivity among rules implies that no single instance can satisfy more than one rule. However, within this rule set, certain conditions overlap. For instance, an individual with low income and single marital status satisfies both rule 2 (Single Marital Status → DB = Yes) and rule 3 (Low Annual Income → DB = Yes). Therefore, the rules lack mutual exclusivity."
    answers["(b) explain"] = "Exhaustive rule sets cover all potential combinations of attributes. However, this particular rule set does not meet this criterion, as it lacks explicit coverage of certain conditions. For instance, a married person with a high income and current employment status does not fit into any of the stated rules. Consequently, the rule set is considered non-exhaustive."
    answers["(c) explain"] = "In cases where rules do not demonstrate mutual exclusivity, the sequence of evaluation plays a crucial role in determining outcomes. Without mutual exclusivity, establishing an order becomes necessary to resolve potential conflicts. However, the lack of specified priorities within the given rules may introduce ambiguity."
    answers["(d) explain"] = "A default class is necessary for a non-exhaustive rule set to handle cases that do not match any of the rules. Since this rule set is not exhaustive, a default class would be needed to cover all possible cases."

    return answers


# -----------------------------------------------------------
"""
def question2():
    answers = {}

    # string "yes" or "no"
    answers["(a)"] = None
    answers["(b)"] = None
    answers["(c)"] = None
    answers["(d)"] = None

    # explain_string: explanation in english prose
    answers["(a) explain"] = None
    answers["(b) explain"] = None
    answers["(c) explain"] = None
    answers["(d) explain"] = None

    return answers
"""
# -----------------------------------------------------------
def question3():
    answers = {}

    # string "yes" or "no"
    answers["(a)"] = "yes"
    answers["(b)"] = "no"
    answers["(c)"] = "no"

    # explain-string: explanation in english prose
    answers["(a) example"] = "the rules are defined by unique combinations of attributes, implying mutual exclusivity."
    answers["(b) example"] = "without clear criteria for what constitutes an aerial or aquatic creature, it is uncertain if all potential vertebrate types are covered. Hence, the rules likely lack exhaustiveness."
    answers["(c) example"] = "If the rules are mutually exclusive and exhaustive, then the ordering of the rules should not matter, as each input will only trigger one rule."

    return answers
# -----------------------------------------------------------
def question7():
    answers = {}

    # bool: True/False
    answers["(a)"] = True
    answers["(b)"] = True
    answers["(c)"] = False
    answers["(d)"] = False

    # explain_string: explanation in english prose
    answers["(a) explain"] = "In the backpropagation process, the gradients at layer k+1 are utilized to compute the gradients at layer k by applying the chain rule of calculus repeatedly."
    answers["(b) explain"] = "During the forward pass of an Artificial Neural Network (ANN), the activations at each layer are determined by the activations and weights of the preceding layer, incorporating the transition from the k-th to the k+1-th layer."
    answers["(c) explain"] = "When facing the vanishing gradient problem, gradients diminish to a point where they obstruct learning in the early layers of deep networks. This stands apart from instances of zero training error and high test error, which signal overfitting"
    answers["(d) explain"] = "Perfect classification of training instances does not mean gradients are zero, as the gradients reflect how much a change in weights would alter the loss, which could still be positive even if the loss is decreasing and the classification is currently perfect"

    return answers

# -----------------------------------------------------------
def question8():
    answers = {}

    # float
    answers["(a) P(X_1=1)"] = 0.65
    answers["(a) P(X_2=1)"] = 0.41
    answers["(a) P(X_1=1,X_2=1)"] = 0.28

    # string: "dependent" or "independent"
    answers["(a) Relationship between X_1 and X_2"] = "independent"

    # string: "yes" or "no"
    answers["(b) X_1 and X_2 conditionally independent given the class?"] = "yes"

    # float
    answers["(c) P(X_1=1 | +)"] = 0.8
    answers["(c) P(X_1=1 | -)"] = 0.5
    answers["(c) P(X_2=1 | +)"] = 0.5
    answers["(c) P(X_2=1 | -)"] = 0.32
    answers["(c) P(X_3=1 | +)"] = 0.4
    answers["(c) P(X_3=1 | -)"] = 0.16

    # For each row give the class predicted by the model after training using Naive Bayes
    # String: either '+' or '-'
    answers["(d) Row 1"] = '+'
    answers["(d) Row 2"] = '-'
    answers["(d) Row 3"] = '-'
    answers["(d) Row 4"] = '-'

    # float between 0 and 1
    answers["(d) Training error rate"] = 0.5

    return answers

# --------------------------------------------------------
def question9():
    answers = {}

    # int
    answers["(a) K"] = 5
    answers["(b) K"] = 50

    # explain_string
    answers["(a) explain"] = "Choosing a smaller K value, such as 5, is beneficial for well-separated data as it minimizes the influence of noise on classification, while still capturing the local structure of the data"
    answers["(b) explain"] = "For intermixed data, a larger K value of 50, is preferred to reduce the impact of overlap and noise by considering a broader neighborhood for classification"

    return answers

# --------------------------------------------------------
def question10():
    answers = {}

    # float
    answers["(a) P(A=1|+)"] = 0.6
    answers["(a) P(B=1|+)"] = 0.4
    answers["(a) P(C=1|+)"] = 0.8
    answers["(a) P(A=1|-)"] = 0.4
    answers["(a) P(B=1|-)"] = 0.4
    answers["(a) P(C=1|-)"] = 0.2

    # type: explanatory string
    answers["(a) P(A=1|+) explain your answer"] = "With A occurring as 1 in 3 out of 5 positive instances, the P(A=1∣+) value is established as 0.6 or 60%."
  
    # type: float
    # note: R is the sample (A=1,B=1,C=1)
    answers["(b) P(+|R)"] = 0.857 
    answers["(b) P(R|+)"] = 0.192
    answers["(b) P(R|-)"] = 0.032

    # string, '+' or '-'
    answers["(b) class label"] = '+'

    # explain_string
    answers["(b) Explain your reasoning"] = "The test sample R is inclined to belong to the positive class ('+') with a posterior probability of 0.857, primarily influenced by its greater likelihood under the positive class P(R∣+)=0.192) in comparison to P(R∣−)=0.032) under the negative class"
  
    # float
    answers["(c) P(A=1)"] = 0.5
    answers["(c) P(B=1)"] = 0.4
    answers["(c) P(A=1,B=1)"] = 0.2

    # type: string, 'yes' or 'no'
    answers["(c) A independent of B?"] = 'yes'
  
    # type: float
    answers["(d) P(A=1)"] = 0.5
    answers["(d) P(B=0)"] = 0.6
    answers["(d) P(A=1,B=0)"] = 0.3

    # type: string: 'yes' or 'no'
    answers["(d) A independent of B?"] = "yes"
  
    # type: float
    answers["(e) P(A=1,B=1|+)"] = 0.2
    answers["(e) P(A=1|+)"] = 0.6
    answers["(e) P(B=1|+)"] = 0.4

    # type: string: 'yes' or 'no'
    answers["(e) A independent of B given class +?"] = "no"

    # type: explanatory string
    answers["(e) A and B conditionally independent given class +, explain"] =  "A and B are not conditionally independent for the class '+', because their joint probability is different from the expected probability if they were independent"
  
    return answers
# --------------------------------------------------------
if __name__ == '__main__':
    answers_dict = {}
    answers_dict['question1'] = question1()
    answers_dict['question2'] = question2()
    answers_dict['question3'] = question3()
    answers_dict['question4'] = question4()
    answers_dict['question7'] = question7()
    answers_dict['question8'] = question8()
    answers_dict['question9'] = question9()
    answers_dict['question10'] = question10()

    with open('answers.pkl', 'wb') as f:
        pickle.dump(answers_dict, f)
