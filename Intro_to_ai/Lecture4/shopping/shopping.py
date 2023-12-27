import csv
import sys

from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier

TEST_SIZE = 0.4


def main():
    # Check command-line arguments
    if len(sys.argv) != 2:
        sys.exit("Usage: python shopping.py data")

    # Load data from spreadsheet and split into train and test sets
    evidence, labels = load_data(sys.argv[1])
    X_train, X_test, y_train, y_test = train_test_split(
        evidence, labels, test_size=TEST_SIZE
    )

    # Train model and make predictions
    model = train_model(X_train, y_train)
    predictions = model.predict(X_test)
    sensitivity, specificity = evaluate(y_test, predictions)

    # Print results
    print(f"Correct: {(y_test == predictions).sum()}")
    print(f"Incorrect: {(y_test != predictions).sum()}")
    print(f"True Positive Rate: {100 * sensitivity:.2f}%")
    print(f"True Negative Rate: {100 * specificity:.2f}%")


def load_data(filename):
    """
    Load shopping data from a CSV file `filename` and convert into a list of
    evidence lists and a list of labels. Return a tuple (evidence, labels).

    evidence should be a list of lists, where each list contains the
    following values, in order:
        - Administrative, an integer
        - Administrative_Duration, a floating point number
        - Informational, an integer
        - Informational_Duration, a floating point number
        - ProductRelated, an integer
        - ProductRelated_Duration, a floating point number
        - BounceRates, a floating point number
        - ExitRates, a floating point number
        - PageValues, a floating point number
        - SpecialDay, a floating point number
        - Month, an index from 0 (January) to 11 (December)
        - OperatingSystems, an integer
        - Browser, an integer
        - Region, an integer
        - TrafficType, an integer
        - VisitorType, an integer 0 (not returning) or 1 (returning)
        - Weekend, an integer 0 (if false) or 1 (if true)

    labels should be the corresponding list of labels, where each label
    is 1 if Revenue is true, and 0 otherwise.
    """

    with open(filename) as file:
        reader = csv.DictReader(file)
        final_evedience = []
        final_label = []
        month_dict = {
            "Jan": 0,
            "Feb": 1,
            "Mar": 2,
            "Apr": 3,
            "May": 4,
            "June": 5,
            "July": 6,
            "Aug": 7,
            "Sep": 8,
            "Oct": 9,
            "Nov": 10,
            "Dec": 11,
        }

        for row in reader:
            evedience = [
                row["Administrative"],
                row["Administrative_Duration"],
                row["Informational"],
                row["Informational_Duration"],
                row["ProductRelated"],
                row["ProductRelated_Duration"],
                row["BounceRates"],
                row["ExitRates"],
                row["PageValues"],
                row["SpecialDay"],
                row["OperatingSystems"],
                row["Browser"],
                row["Region"],
                row["TrafficType"],
            ]

            for month in month_dict:
                if row["Month"] == month_dict:
                    evedience.insert(month_dict[month], 10)

            if row["VisitorType"] == "Returning_Visitor":
                evedience.append(1)
            else:
                evedience.append(0)

            if row["Weekend"] == "TRUE":
                evedience.append(1)
            else:
                evedience.append(0)

            if row["Revenue"] == "TRUE":
                final_label.append(1)
            else:
                final_label.append(0)

            final_evedience.append(evedience)

    return (final_evedience, final_label)

    raise NotImplementedError


def train_model(evidence, labels):
    """
    Given a list of evidence lists and a list of labels, return a
    fitted k-nearest neighbor model (k=1) trained on the data.
    """

    model = KNeighborsClassifier(n_neighbors=1)
    X_traning = [evidence[i] for i in range(len(evidence))]
    Y_traiing = [labels[j] for j in range(len(labels))]
    model.fit(X_traning, Y_traiing)
    return model

    raise NotImplementedError


def evaluate(labels, predictions):
    """
    Given a list of actual labels and a list of predicted labels,
    return a tuple (sensitivity, specificity).

    Assume each label is either a 1 (positive) or 0 (negative).

    `sensitivity` should be a floating-point value from 0 to 1
    representing the "true positive rate": the proportion of
    actual positive labels that were accurately identified.

    `specificity` should be a floating-point value from 0 to 1
    representing the "true negative rate": the proportion of
    actual negative labels that were accurately identified.
    """

    users_go_through_label = 0
    users_not_go_through_label = 0
    users_go_through_predict = 0
    users_not_go_through_predict = 0
    for i in labels:
        if i == 1:
            users_go_through_label += 1
        elif i == 0:
            users_not_go_through_label += 1

    for i in predictions:
        if i == 1:
            users_go_through_predict += 1
        elif i == 0:
            users_not_go_through_predict += 1
    print(len(predictions), len(labels))
    print(users_not_go_through_predict, users_not_go_through_label)

    sensitivity = users_go_through_predict / users_go_through_label

    specificity = users_not_go_through_label / users_not_go_through_predict

    return (sensitivity, specificity)

    raise NotImplementedError


if __name__ == "__main__":
    main()
