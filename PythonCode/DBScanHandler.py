#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      ShiroRaven
#
# Created:     08/11/2013
# Copyright:   (c) ShiroRaven 2013
# Licence:     <your licence>
#-------------------------------------------------------------------------------
#!/usr/bin/env python

from DBSCAN2 import dbScanner as DB
import time

def main():
	# get articles in format
	# number - Title|keyword1:keyword2

	#create DBSCAN
	# TODO - handle iterative clustering for old points
	# Solution? Add all points in first, then iterate through while clustering

	#dbscan = DB(2,0.9,'Jaccard')
	dbscan = DB(2,0.9,'bla')

	with open('DBSCAN-mid.txt','r') as f:
		#take apart line
		for line in f:
			if (len(line) > 1):
				parts = line.split("|")
				title = parts[0]
				wordSet = parts[1].split(":")
				#print(title+"\n")
				#print(title + str(wordSet))
				#print("\n\n")
				if (len(wordSet) > 2):
					dbscan.AddArticle(title, wordSet)

	print("\nStarted Clustering all points...\n\n")
	startTime = time.time()
	dbscan.ClusterAllPoints()
	endTime = time.time()

	print("Time elapsed = " + str(endTime - startTime) + " seconds")

    #print("\n"+str(dbscan.ReturnClusters()))

	dic = {}
	dic = dbscan.ReturnClusters()

	for cluster in dic.keys():
	    print (str(cluster)+" : "+str(len(dic[cluster])))


	print("\n\nDONE!")


if __name__ == '__main__':
    main()
