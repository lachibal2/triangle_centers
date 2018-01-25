#program for graphing/showing triangle centers
#made by: Lachi Balabanski
import matplotlib.pyplot as plot
import numpy as np
import argparse
import math

try:
    #parsing terminal arguments
    p = argparse.ArgumentParser()
    p.add_argument('-p1','--point1',required=True,help='triangle point one', type=str)
    p.add_argument('-p2','--point2',required=True,help='triangle point one', type=str)
    p.add_argument('-p3','--point3',required=True,help='triangle point one', type=str)
    p.add_argument('-s','--show',required=False, help='show triangle and center',type=bool)
    p.add_argument('-t','--type',required=True,help='triangle center type: circumcenter, centroid',choices=['circ','cent'])
    args = p.parse_args()
    #defining show, if it is not defined
    if args.show:
        show = args.show
    else:
        show = False
    #defining parsed arguments
    point1 = args.point1
    point2 = args.point2
    point3 = args.point3
    center = args.type
    #parse point strings to tuples

    temp1, temp2, temp3 = point1.split(','), point2.split(','), point3.split(',')
    for i in range(len(temp1)):
        if '~' in temp1[i]:
            temp1[i] = temp1[i].replace('~','-')
    for i in range(len(temp2)):
        if '~' in temp2[i]:
            temp2[i] = temp2[i].replace('~','-')
    for i in range(len(temp3)):
        if '~' in temp3[i]:
            temp3[i] = temp3[i].replace('~','-')
                    
    point1 = (int(temp1[0]), int(temp1[1]))
    point2 = (int(temp2[0]), int(temp2[1]))
    point3 = (int(temp3[0]), int(temp3[1]))
    def getLine(p1, p2):
        """
        p1 is a tuple of the first point
        p2 is a tuple of the second point
        returns a tuple of the slope and y-intercept of the line going throug both points
        """
        try:
            slope = float((p1[1] - p2[1]) / (p1[0] - p2[0]))
            yint = float((-1 * (p1[0])) * slope + p1[1])
            return (slope, yint)
        except ZeroDivisionError:
            print('Divided by Zero Error.')
    def getIntersection(line1, line2):
        """
        line1 is a tuple of m and b of the line in the form y=mx+b
        line2 is a tuple of m and b of the line in the form y=mx+b
        returns a tuple of the points of the intersection of the two lines
        """
        slope1, slope2 = line1[0], line2[0]
        yint1, yint2 = line1[1], line2[1]
        matA = np.matrix(str(-1 * slope1) + ' 1;' + str(-1 * slope2) + ' 1')
        matB = np.matrix(str(yint1) + '; ' + str(yint2))
        invA = matA.getI()
        resultant = invA * matB
        return (resultant[0,0], resultant[1,0])
    def getMidpoint(p1, p2):
        """
        p1 is a tuple of the first point
        p2 is a tuple of the second point
        returns the midpoint, in tuple form, of p1 and p2
        """
        return(((p1[0] + p2[0]) / 2), ((p1[1] + p2[1]) / 2))
    def perpSlope(slope):
        #takes slope(float) and returns the slope of a line perpendicular to it
        return (slope * -1) ** -1
    def distance(p1, p2):
        """
        p1 is a tuple of ...
        p2 is a tuple of ...
        returns float of distance between p1 and p2
        """
        return(float(math.sqrt((p1[0] + p2[0]) ** 2 + (p1[1] + p2[1]) ** 2)))
    def lineFromSlope(slope, point):
        """
        slope is a float of slope
        point is a tuple of ...
        returns tuple of slope and y intercept
        """
        return (slope, ((slope * (-1 * point[0])) +  point[1]))
    if center == 'circ':
        mid1 = getMidpoint(point1, point2)
        mid2 = getMidpoint(point2, point3)
        line1 = getLine(point1, point2)
        line2 = getLine(point2, point3)
        perp1 = perpSlope(line1[0])
        perp2 = perpSlope(line2[0])
        perpbi1 = lineFromSlope(perp1, mid1)
        perpbi2 = lineFromSlope(perp2, mid2)
        circumcent = getIntersection(perpbi1, perpbi2)
        radius = distance(circumcent, point1)
        xList = [point1[0], point2[0], point3[0], point1[0]]
        yList = [point1[1], point2[1], point3[1], point1[1]]
        plot.plot(xList, yList)
        plot.scatter(circumcent[0], circumcent[1])
        print('====================')
        print('circumcenter: (' + str(circumcent[0]) + ', ' + str(circumcent[1]) + ')')
        print('circumcircle radius: %f' % (radius))
        print('====================')
        if show == True:
            plot.show()
    if center == 'cent':
        mid1 = getMidpoint(point1, point2)
        mid2 = getMidpoint(point2, point3)
        line1 = getLine(mid1, point3)
        line2 = getLine(mid2, point1)
        centroid = getIntersection(line1, line2)
        xList = [point1[0], point2[0], point3[0], point1[0]]
        yList = [point1[1], point2[1], point3[1], point1[1]]
        plot.plot(xList, yList)
        plot.scatter(centroid[0], centroid[1])
        print('====================')
        print('centroid: (%f, %f)' % (centroid[0], centroid[1]))
        print('====================')
        if show == True:
            plot.show()
except ModuleNotFoundError:
    print('Missing Modules. Modules used in this file: matplotlib, numpy, and argparse')

finally:
    print("Thank you for using Lachi Balabanski's triangle program") 
