from sklearn import tree
feature = [[120, 5], [110, 5], [185, 12], [163, 12], [93, 5]]
lable = ["ECO CAR / B-SEGMENT", "ECO CAR / B-SEGMENT", "VAN", "VAN", "ECO CAR / B-SEGMENT"]
classifier = tree.DecisionTreeClassifier()
classifier = classifier.fit(feature, lable)
print(classifier,predict([[150,5]]))