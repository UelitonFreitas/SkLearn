from sklearn import svm
from sklearn import preprocessing
from sklearn.cross_validation import KFold
from sklearn.grid_search import GridSearchCV
from sklearn.metrics import classification_report
from sklearn.svm import SVC
from sklearn.metrics import precision_score
from sklearn.metrics import recall_score
from sklearn.metrics import f1_score
from sklearn.multiclass import OneVsOneClassifier
from sklearn.svm import SVC
from sklearn.grid_search import GridSearchCV, RandomizedSearchCV
from sklearn.svm import LinearSVC
from scipy import *
from numpy  import *

from sklearn import cross_validation

import ReadArff as Rd
import OneXAll as OXALL


def main():
    """Main do programa"""
    
    arffReader = Rd.ReadArff('fish_Dic64.arff')
    
    #Conjuntos de treinamento e testes
    X_train = X_test = y_train = y_test = None
    
    X = arffReader.get_data_frame()
    yt = arffReader.get_classes()
    
    classes_map = arffReader.get_classes_map()
    y = arffReader.get_classes()
    data = arffReader.get_data_frame()
    
    oxall = OXALL.OneXAll(data, y, classes_map)
    oxall.transform_ovall()
    
    
   # 
   # for class_index in range(len(classes_map)):    
   #     ds = oxall.get_one_x_all_of_class(class_index)
   #     
   #     #Os dados precisam ser do tipo array.
   #     X = array(ds['features'])
   #     y = array(ds['class'])
   #     
   #     #Metodo de validacao cruzada com 10 folders embaralhando as amostras
   #     kfold =  cross_validation.KFold(len(y), n_folds=10,shuffle=True)
   #     
   #     print "Cross Validation with 10 folds: Class: ",class_index," ....."
   #     
   #     #Divite o conjunto de treinamento em conjunto de teste
   #     #fornecidos pela validacao cruzada.
   #     #X_train contem as amostras de treinamento e X_test as amostras de teste
   #     #y_train contem as classes das amostras de treinamento e y_test de classe
   #     for train_index,test_index in kfold:
   #         X_train, X_test = X[train_index], X[test_index]
   #         y_train, y_test = y[train_index], y[test_index]
   # 
   #         ## Set the parameters by cross-validation
   #         parameters = {'C': [1, 10, 100, 1000], 'kernel': ['linear']}
   #          
   #         svm = SVC()
   #         # run randomized search
   #         n_iter_search = 10
   #          
   #         
   #         scores = [
   #             ('precision', precision_score),
   #             ('recall', recall_score),
   #         ]
   #         
   #         for score_name, score_func in scores:
   #             print "# Tuning hyper-parameters for %s" % score_name
   #             print
   #      
   #             clf = RandomizedSearchCV(svm, param_distributions=parameters,n_iter=n_iter_search,n_jobs=4)
   #             clf.fit(X_train, y_train)
   #             
   #             print "Best parameters set found on development set:"
   #             print
   #             print clf.best_estimator_
   #             print
   #             print "Grid scores on development set:"
   #             print
   #             for params, mean_score, scores in clf.grid_scores_:
   #                 print "%0.3f (+/-%0.03f) for %r" % (
   #                     mean_score, scores.std() / 2, params)
   #             print
   #             
   #             print "Detailed classification report:"
   #             print
   #             print "The model is trained on the full development set."
   #             print "The scores are computed on the full evaluation set."
   #             print
   #             y_true, y_pred = y_test, clf.predict(X_test)
   #             print classification_report(y_true, y_pred)
   #             print
   #             
   #             print
   #             print clf.score(X_test,y_test)
   ##     


    arffReader.split_arff_one_x_all()
    #print arffReader.get_data_frame()
    #print arffReader.get_scaled_data()
    #print arffReader.get_meta()
    #print arffReader.get_classes()
    

if __name__ == '__main__':
    main()
