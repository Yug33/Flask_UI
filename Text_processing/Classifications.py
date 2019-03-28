import pickle
def naive_bayes(training_data, y_train, input_data):
    from sklearn.naive_bayes import MultinomialNB
    print("NaiveBayes")
    # --------
    try:
        filename="naive_bayes"
        loaded_model = pickle.load(open(filename, 'rb'))
        print("loaded from model")
        predictions_nb=loaded_model.predict(input_data)
    except:
        naive_bayes = MultinomialNB()
        naive_bayes.fit(training_data, y_train)
        pickle.dump(naive_bayes, open(filename, 'wb'))
        predictions_nb = naive_bayes.predict(input_data)
    # --------
    return predictions_nb


def svm(training_data, y_train, input_data):
    print("SVM")
    from sklearn.svm import SVC
    try:
        filename="SVM"
        loaded_model = pickle.load(open(filename, 'rb'))
        print("loaded from model")
        predictions_sv=loaded_model.predict(input_data)
    except:
        svclassifier = SVC(kernel='linear')
        svclassifier.fit(training_data, y_train)
        pickle.dump(naive_bayes, open(filename, 'wb'))
        predictions_sv = svclassifier.predict(input_data)
    return predictions_sv


def random_forest(training_data, y_train, input_data):
    print("rf")
    from sklearn.ensemble import RandomForestRegressor
    try:
        filename = "random_forest"
        loaded_model = pickle.load(open(filename, 'rb'))
        print("loaded from model")
        y_pred = loaded_model.predict(input_data)
    except:
        regressor = RandomForestRegressor(n_estimators=2, random_state=0)
        regressor.fit(training_data, y_train)
        pickle.dump(naive_bayes, open(filename, 'wb'))
        y_pred = regressor.predict(input_data)
    return y_pred

def decision_tree(training_data, y_train, input_data):
    print("decision tree")
    from sklearn.tree import tree
    try:
        filename = "decision_tree"
        loaded_model = pickle.load(open(filename, 'rb'))
        print("loaded from model")
        y_pred = loaded_model.predict(input_data)
    except:
        regressor = tree.DecisionTreeClassifier()
        regressor.fit(training_data, y_train)
        y_pred = regressor.predict(input_data)
    return y_pred
