__author__ = 'Jorge Paredes'

import pandas as pd
import zipfile
import os




class DataPreparation:
    def __init__(self):
        self.X = []  # Dataset attributes
        self.cBin = []  # Binary Class Output classifier
        self.fClasses = []  # Frequency of Classes
        self.dictFreq = {}  # map labels with their respective quantity
        self.dictLabels = []  # map labels with integers
        self.train_instances = 'Disable'  # Only get a value when train and test are separate files

        # self.bool_categories = [0,0,0,1,0,....,0] # Seria xvr implementar a ver cuales serian categoricos

    def info_data(self):
        info = [self.X, self.cBin, self.fClasses, self.dictFreq, self.dictLabels]
        if self.train_instances != 'Disable':
            info.append(self.train_instances)
        return info

    def read_data(self,data):
        self.X, self.cBin, self.fClasses, self.dictFreq, self.dictLabels = self.calculate_parameters(data)

    def read_1file(self, file_path):
        data = pd.read_csv(file_path)
        self.X, self.cBin, self.fClasses, self.dictFreq, self.dictLabels = self.calculate_parameters(data)

    def read_1cv(self, zipFilePath, file_train, file_test):
        with zipfile.ZipFile(zipFilePath, 'r') as z:
            train = pd.read_csv(z.open(file_train))
            test = pd.read_csv(z.open(file_test))
        # With pd.merge we can lost instances if we have repetitive instances in train and test
        data = train.append(test, ignore_index=True)
        self.X, self.cBin, self.fClasses, self.dictFreq, self.dictLabels = self.calculate_parameters(data)
        self.train_instances = train.shape[0]

    def read_folder(self, folder_path):
        files_folder = os.listdir(folder_path)
        datas = []
        for i in files_folder:
            datas.append(self.read_1file(i))
        return datas

    def calculate_parameters(self,data):
        X = data.iloc[:, 0:-1].values  # attributes
        output_class = data.iloc[:, -1]  # output class
        binarized_output_class = pd.get_dummies(output_class)
        cBin = binarized_output_class.values  # binary output class

        real_labels = binarized_output_class.columns.values.tolist()
        int_labels = range(1, len(real_labels) + 1)
        dict_labels = dict(zip(int_labels, real_labels))
        dict_freq = dict(output_class.value_counts())  # labels - quantity

        # Adding information to assist in making decisions: [freq_classes, priority]
        temp = [dict_freq[dict_labels[x]] for x in int_labels]
        freq_classes = [1. * x / sum(temp) for x in temp]
        return X, cBin, freq_classes, dict_freq, dict_labels

def main():
    print ('Module 1 <<DataPreparation>>\n=============')
    L = DataPreparation()
    filezip_name = "D:\\Jorg\Projects\\autoFIS\\test\\datas" + '\\' + 'saheart-10-fold_csv.zip'
    print (filezip_name)
    L.read_1cv(filezip_name, 'saheart-10-7tra.csv', 'saheart-10-7tst.csv')
    print (L.fClasses)


if __name__ == '__main__':
    main()