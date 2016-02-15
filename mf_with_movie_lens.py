import numpy as np

from load_data import load_ml_1m, load_rating_matrix
from matrix_factorization import MatrixFactorization
from evaluation_metrics import RMSE
#from mf.bayesian_matrix_factorization import BayesianMatrixFactorization


if __name__ == "__main__":

    # load MovieLens data
    num_user, num_item, ratings = load_ml_1m()
    np.random.shuffle(ratings)

    # set feature numbers
    num_feature = 10

    # set max_iterations
    max_iter = 20

    # split data to training & testing
    train_pct = 0.9
    train_size = int(train_pct * len(ratings))
    train = ratings[:train_size]
    validation = ratings[train_size:]

    # models
    rec = MatrixFactorization(num_user, num_item, num_feature, train, validation, max_rating=5, min_rating=1)

    # fitting
    rec.estimate(max_iter)

    # results
    train_preds = rec.predict(train)
    train_rmse = RMSE(validation_preds, np.float16(train[:, 2]))
    validation_preds = rec.predict(validation)
    validation_rmse = RMSE(validation_preds, np.float16(validation[:, 2]))

    print "train RMSE: %.6f, validation RMSE: %.6f " % (train_rmse, validation_rmse)
