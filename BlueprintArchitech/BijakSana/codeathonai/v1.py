from sklearn import svm  # contoh
import setting
import pickle
import os
import random
import datetime
from fastai.vision import *
from io import BytesIO
import base64
from binascii import a2b_base64
import string
ascii_uppercase = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'


def model_predict(img_path):
    """
       model_predict will return the preprocessed image
    """

    img = open_image(img_path)
    learn = load_learner('codeathonX/model/')
    pred_class, pred_idx, outputs = learn.predict(img)
    top3 = torch.topk(outputs, k=5)
    return [ascii_uppercase[i] for i in top3[1]]


class learn:
    """docstring"""

    def __init__(self, userid, data_target):
        learn = load_learner('../../../model/')


class predict:
    """docstring"""

    def __init__(self, img):

        imgstr = re.search(r'base64,(.*)', img).group(1)
        output_fname = ''.join(random.choices(
            string.ascii_uppercase + string.digits, k=6))
        output = open(output_fname, 'wb')
        output.write(base64.b64decode(imgstr))
        output.close()
        result = model_predict(output_fname)
        # return
        self.prediction = {
            'result' 			: result,
        }


class learn_and_predict:
    """docstring"""

    def __init__(self, userid, data_target, data_to_predict):
        X = data_target[:-1]
        Y = data_target[-1]
        self.model_fitted = svm.SVC(gamma=0.001).fit(X, Y)

        # return
        self.prediction = {
            'result' 			: list(self.model_fitted.predict(data_to_predict)),
        }
