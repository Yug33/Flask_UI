import pickle
import string

import pandas as pd
def training_models(filename):
    """
    Used for the classification of the sentences
    :parameter ranked_text (list)
    """

    print("training data")
    news_df = pd.read_csv(filename, sep=",")
    news_df['CATEGORY'] = news_df.CATEGORY.map({'b': 1, 't': 2, 'e': 3, 'm': 4, 'p': 5, 's': 6})
    news_df['TITLE'] = news_df.TITLE.map(
        lambda x: x.lower().translate(str.maketrans('', '', string.punctuation))
    )
    from sklearn.model_selection import train_test_split

    X_train, X_test, y_train, y_test = train_test_split(
        news_df['TITLE'],
        news_df['CATEGORY'],
        random_state=1
    )
    from sklearn.feature_extraction.text import CountVectorizer

    count_vector = CountVectorizer(stop_words='english')
    training_data = count_vector.fit_transform(X_train)
    testing_data = count_vector.transform(X_test)

    from Kratos import Classifications

    result = Classifications.decision_tree(training_data, y_train, testing_data,y_test)
    return result

def model_analysis(filename,testing_data,y_test):
    loaded_model = pickle.load(open(filename, 'rb'))
    predictions_nb = loaded_model.predict(testing_data)

    from sklearn.metrics import confusion_matrix

    cnf_matrix = confusion_matrix(y_test, predictions_nb)
    print(cnf_matrix)

    from sklearn.metrics import accuracy_score, recall_score, precision_score, f1_score

    print("Model Analysis")
    print("Accuracy score: ", accuracy_score(y_test, predictions_nb))
    print("Recall score: ", recall_score(y_test, predictions_nb, average='weighted'))
    print("Precision score: ", precision_score(y_test, predictions_nb, average='weighted'))
    print("F1 score: ", f1_score(y_test, predictions_nb, average='weighted'))



def naive_bayes(training_data, y_train, input_data,y_test):
    from sklearn.naive_bayes import MultinomialNB
    print("NaiveBayes")

    filename = "naive_bayes.pkl"
    naive_bayes = MultinomialNB()
    naive_bayes.fit(training_data, y_train)
    pickle.dump(naive_bayes, open(filename, 'wb'))
    model_analysis(filename,input_data,y_test)


def svm(training_data, y_train, input_data,y_test):
    print("SVM")
    from sklearn.svm import SVC
    filename = "SVM.pkl"
    print("trainning SVM")

    svclassifier = SVC(kernel='linear')
    svclassifier.fit(training_data, y_train)
    pickle.dump(naive_bayes, open(filename, 'wb'))
    model_analysis(filename, input_data, y_test)


def random_forest(training_data, y_train, input_data,y_test):
    print("rf")
    from sklearn.ensemble import RandomForestRegressor
    filename = "random_forest.pkl"

    regressor = RandomForestRegressor(n_estimators=2, random_state=0)
    regressor.fit(training_data, y_train)
    pickle.dump(naive_bayes, open(filename, 'wb'))
    model_analysis(filename, input_data, y_test)

def decision_tree(training_data, y_train, input_data,y_test):
    print("decision tree")
    from sklearn.tree import tree
    filename = "decision_tree.pkl"

    print("Training Decison tree")
    regressor = tree.DecisionTreeClassifier()
    regressor.fit(training_data, y_train)
    pickle.dump(regressor, open(filename, 'wb'))

    print("Trained Decison tree")
    model_analysis(filename, input_data, y_test)