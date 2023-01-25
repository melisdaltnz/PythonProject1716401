import os
import numpy as np
import matplotlib.pyplot as plt
import random

data = np.array([])

class GetDataClass:

    def loadDataFromFile():
        try:
            global data
            fileDir = input("please give a file directory:")
            fileName = input("please input the file name:")
            filePath = fileDir + "\\" + fileName     
            data = np.loadtxt(filePath, dtype=int)
           
        except ValueError:
            print("please clean your data.. you have non numeric values!")

        return data

    def loadDataFromSameDir():
        try:
            global data
            fileDir = input("please give a file directory:")
            for filename in os.scandir(fileDir):
                if filename.is_file():
                    content = np.loadtxt(filename.path, dtype=int)
                    data = np.append(data,content)
        except ValueError:
            print("please clean your data.. you have non numeric values!")

        return data

    def validateData():
        print("validations are checked while you are loading data")


    def generateArray():
        # creating an empty list
        lst = []

        # number of elements as input
        n = int(input("Enter number of elements of your array : "))

        # iterating till the range
        for i in range(0, n):
            ele = int(input("Enter a array value : "))

            lst.append(ele) # adding the element

        global data
        data = np.array(lst)


class CalculatorClass:
    def convertUnit():
        num = int(input("Enter a number: "))
        selection = int(input("Please select a conversion:\n"
        "1.g to kg\n"
        "2.F to C\n"
        "3.cm to m\n"
        "4.kg to g\n"
        "5.C to K\n"
        "6.m to cm\n"))

        if selection == 1:
            return num / 1000

        elif selection == 2:
            return (num - 32) / 1.800

        elif selection == 3:
            return num / 100
        
        elif selection == 4:
            return num * 1000
        
        elif selection == 5:
            return num + 273
        
        elif selection == 6:
            return num * 100

        else:
            return "invalid selection"

    def calculateMean():
        selection = int(input("do you want to generate a new array? Otherwise, existed data will be used.\n"
            "1.Yes\n"
            "2.No\n"))

        if selection == 1:
            GetDataClass.generateArray()

        if data.size == 0:
            selection = int(input("you did not upload data.. do you want to generate array?\n"
            "1.Yes\n"
            "2.No\n"))
            if selection == 1:
                GetDataClass.generateArray()

            else:
                return "please first upload data"

        return "mean: {}".format(np.mean(data))

    def calculateVariance():
        selection = int(input("do you want to generate a new array? Otherwise, existed data will be used.\n"
            "1.Yes\n"
            "2.No\n"))

        if selection == 1:
            GetDataClass.generateArray()

        if data.size == 0:
            selection = int(input("you did not upload data.. do you want to generate array?\n"
            "1.Yes\n"
            "2.No\n"))
            if selection == 1:
                GetDataClass.generateArray()
            
            else:
                return "please first upload data"

        return "variance: {} ".format(np.var(data))

    def calculateMax():
        selection = int(input("do you want to generate a new array? Otherwise, existed data will be used.\n"
            "1.Yes\n"
            "2.No\n"))

        if selection == 1:
            GetDataClass.generateArray()

        if data.size == 0:
            selection = int(input("you did not upload data.. do you want to generate array?\n"
            "1.Yes\n"
            "2.No\n"))
            if selection == 1:
                GetDataClass.generateArray()
            
            else:
                return "please first upload data"
        
        maxVal =  np.max(data)
        indexMaxVal = np.where(data == maxVal)

        return "value: {} index: {}".format(maxVal, indexMaxVal[0][0])

    def calculateMin():
        selection = int(input("do you want to generate a new array? Otherwise, existed data will be used.\n"
            "1.Yes\n"
            "2.No\n"))

        if selection == 1:
            GetDataClass.generateArray()

        if data.size == 0:
            selection = int(input("you did not upload data.. do you want to generate array?\n"
            "1.Yes\n"
            "2.No\n"))
            if selection == 1:
                GetDataClass.generateArray()
            
            else:
                return "please first upload data"

        minVal =  np.min(data)
        indexMinVal = np.where(data == minVal)

        return "value: {} index: {}".format(minVal, indexMinVal[0][0])

class PlotAndSimulateClass:
    dimension = ""
    x_axis = []
    y_axis = []
    x_label = ""
    y_label = ""

    def provideData():
        PlotAndSimulateClass.dimension = int(input("please provide a dimension size: \n"))
        dimension = PlotAndSimulateClass.dimension

        for i in range(0, dimension):
            ele = int(input("Enter x-axis value : "))
         
            PlotAndSimulateClass.x_axis.append(ele) # adding the element
        
        
        for i in range(0, dimension):
            ele = int(input("Enter y-axis value : "))
          
            PlotAndSimulateClass.y_axis.append(ele) # adding the element
        
        PlotAndSimulateClass.x_label = input("please enter x-axis label: \n")
        PlotAndSimulateClass.y_label = input("please enter y-axis label: \n")

    def plotNormalData():     
        selection = int(input("do you want to generate a random dataset? Otherwise, you need to enter a dataset.\n"
            "1.Yes\n"
            "2.No\n"))
        if selection == 2:
            PlotAndSimulateClass.provideData()

            plt.plot(PlotAndSimulateClass.x_axis, PlotAndSimulateClass.y_axis)
            plt.xlabel(PlotAndSimulateClass.x_label)
            plt.ylabel(PlotAndSimulateClass.y_label)
        
        plt.show()
        if selection == 1:
            xs = [random.randint(0, 10) for _ in range(100)]
            ys = [random.randint(0, 10) for _ in range(100)]
            plt.plot(xs, ys)
            plt.xlabel(PlotAndSimulateClass.x_label)
            plt.ylabel(PlotAndSimulateClass.y_label)
            plt.title("Random plot")
            plt.show()
            
    def plotScatteredData():
        selection = int(input("do you want to generate a random dataset? Otherwise, existed data will be used.\n"
            "1.Yes\n"
            "2.No\n"))
        if selection == 2:
            PlotAndSimulateClass.provideData()

            plt.scatter(PlotAndSimulateClass.x_axis, PlotAndSimulateClass.y_axis)
            plt.xlabel(PlotAndSimulateClass.x_label)
            plt.ylabel(PlotAndSimulateClass.y_label)
        
            plt.show()
        if selection == 1:
             xs = [random.randint(0, 10) for _ in range(100)]
             ys = [random.randint(0, 10) for _ in range(100)]
             plt.scatter(xs, ys)
             plt.xlabel(PlotAndSimulateClass.x_label)
             plt.ylabel(PlotAndSimulateClass.y_label)
             plt.title("Random plot")
             plt.show()
    def plotData():
        selection = int(input("How do you want to plot your data?\n"
        "1.Normal\n"
        "2.Scattered\n"))

        if selection == 1:
            PlotAndSimulateClass.plotNormalData()
        
        elif selection == 2:
            PlotAndSimulateClass.plotScatteredData()
        
        else:
            return "invalid selection"
        
print("Welcome to MelCulator! In that program you can find the mean values, varience and min-max values of your datasets and draw a plot. You can enter your own dataset or you can choose a file. Also you can make unit conversiton. Have fun!")
    
while True:

    selection = int(input("please select one of the following functions:\n"
    "1.loadDataFromFile()\n"
    "2.loadDataFromSameDir()\n"
    "3.validateData()\n"
    "4.convertUnit()\n"
    "5.calculateMean()\n"
    "6.calculateVariance()\n"
    "7.calculateMax()\n"
    "8.calculateMin()\n"
    "9.plotData()\n"))


    if selection == 1:
        print("your data is: ",GetDataClass.loadDataFromFile())

    elif selection == 2:
       print("your data is: ",GetDataClass.loadDataFromSameDir())

    elif selection == 3:
       GetDataClass.validateData()

    elif selection == 4:
        print(CalculatorClass.convertUnit())

    elif selection == 5:
        print(CalculatorClass.calculateMean())

    elif selection == 6:
        print(CalculatorClass.calculateVariance())

    elif selection == 7:
        print(CalculatorClass.calculateMax())

    elif selection == 8:
        print(CalculatorClass.calculateMin())
    
    elif selection == 9:
        PlotAndSimulateClass.plotData()

    selectionContinue = int(input("do you want to process any other function?:\n"
    "1.yes\n"
    "2.no\n"))

    if selectionContinue == 2:
        print("terminating the software . . .")
        break