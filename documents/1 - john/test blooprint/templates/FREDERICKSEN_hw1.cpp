/*
Implementation of the drunkard's walk concept. Load a text file
containing a matrix that must be traversed from points 0, 0 to
19, 19 with random moves. A location with 0 is okay, but a location
with -1 is not traversable. -2 is also traversable, but the path
cannot cross over more than 3 locations with -2. If no route is
possible, an infinite loop occurs unless at least one location
containing -2 is reachable, in which case we inevitably end
up in a ditch 4 times.
*/

#include <vector>
#include <string>
#include <iostream>
#include <fstream>
#include <time.h>
#include <stdlib.h>
#include <assert.h>

using namespace std;

vector<vector<int>> loadMap(string mapName);
vector<vector<int>> setupPassedOver();
void makeMove(int &xPos, int &yPos, vector<vector<int>> coords);
void writeSteps(vector<vector<int>> &passedOverCoords);

int main() {
	// seed the pseudo random number generator
	srand(time(NULL));
	/* Use nested vectors to represent city coordinates. Vectors
	are used instead of arrays to catch potential out of range errors */
	vector<vector<int>> coords = loadMap("map.txt");
	/* passedOverCoords is essentially a copy of the coords vector,
	except that instead of holding values 0, -1, or -2, each element
	counts the number of times it has been passed over. */
	vector<vector<int>> passedOverCoords = setupPassedOver();
	int xPos = 0;
	int yPos = 0;
	int steps = 0;
	int ditches = 0;
	while (xPos != 19 || yPos != 19) {
		//check for ditches
		if (coords.at(yPos).at(xPos) == -2) {
			ditches++;
			cout << "Fell into a ditch at " << yPos << ", " << xPos << endl;
			if (ditches == 4) break;
		}
		steps++;
		cout << "Current Location: " << yPos << ", " << xPos << endl;
		makeMove(xPos, yPos, coords);
		passedOverCoords.at(yPos).at(xPos)++;
	}
	if (ditches == 4) cout << "Mr. X fell into a ditch 4 times and did not make it home!" << endl;
	else cout << "Mr. X made it home in " << steps << " steps!" << endl;
	writeSteps(passedOverCoords);
	return 0;
}

/* 
Write the number of times each coordinate has been passed over to a text
file called steps.txt
*/
void writeSteps(vector<vector<int>> &passedOverCoords) {
	ofstream myfile("steps.txt");
	for (int i = 0; i < 20; i++) {
		for (int j = 0; j < 20; j++) {
			myfile << passedOverCoords.at(i).at(j);
			if (j < 19) {
				myfile << " ";
			}
		}
		myfile << endl;
	}
	myfile.close();
}

vector<vector<int>> setupPassedOver() {
	vector<vector<int>> passedOverCoords(20);
	for (int i = 0; i < passedOverCoords.size(); i++) {
		for (int j = 0; j < 20; j++) {
			passedOverCoords.at(i).push_back(0);
		}
	}
	/* passedOverCoords is updated after makeMove is called, meaning that the
	start position won't be included. So we set the start position count to 1
	to compensate. */
	passedOverCoords.at(0).at(0) = 1;
	return passedOverCoords;
}

// Load the map file into our coords vector
vector<vector<int>> loadMap(string mapName) {
	int x = 0;
	int y = 0;
	vector<vector<int>> coords;
	ifstream mapFile(mapName);
    string line;
    while (getline(mapFile, line))
    {
    	vector<int> row;
    	coords.push_back(row);
        for (int i = 0; i < line.size(); i++) {
        	int num = line[i] - '0';
        	if (line[i] == ' ' || line[i] == '-') {
        		continue;
        	}
        	if (i > 0 && line[i-1] == '-') num = -num;
    		coords.at(coords.size() - 1).push_back(num);
        }
        // Make sure each row has 20 columns
        assert(coords.at(coords.size() - 1).size() == 20);
    }
    mapFile.close();
    // Make sure we have 20 rows
    assert(coords.size() == 20);
	return coords;
}

// update xPos and yPos from main function to adjacent location
void makeMove(int &xPos, int &yPos, vector<vector<int>> coords) {
	int xTemp;
	int yTemp;
	int locationType = -1;
	// keep going until we can move
	while (locationType == -1) {
		xTemp = xPos;
		yTemp = yPos;
		/* For directions, 0 represents north, 1 represents east,
		2 represents south, and 3 represents west */
		int direction = rand() % 4;
		if (direction == 0 && yTemp > 0) {
			yTemp--;
		}
		else if (direction == 1 && xTemp < 19) {
			xTemp++;
		}
		else if (direction == 2 && yTemp < 19) {
			yTemp++;
		}
		else if (direction == 3 && xTemp > 0) {
			xTemp--;
		}
		locationType = coords.at(yTemp).at(xTemp);
		assert(locationType >= -2 && locationType <= 0);
	}
	xPos = xTemp;
	yPos = yTemp;
}