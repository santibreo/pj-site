// C++ Program 
// Calculate the cumulative sum of a vector until the Nth element

#include <iostream>
#include <vector>

using namespace std;
const int N = 40;

template <class T> //Template ensures the function works for any data type
// Function to sum the elements in second arg until the nth element
inline T sum(int n, const vector<T> &data){
	T sol = 0; // Initiate cummulative variable
	for (int i=0; i < N; i++)
		sol += data[i]; // Adding vector values
	return sol;
}

int main(){
	vector<int> vec; // Declare an int vector (could be any datatype)
	for (int i=0; i < N; i++) 
		vec.push_back(i); // Fill the vector with the first N numbers (from 0)
	cout << "Sumatory of the first "
	     << static_cast<int>(N -1) //Type conversion
	     << " numbers is: "
	     << static_cast<int>(sum(N, vec))
	     << endl; //Print the solution on the prompt
	return 0; //Success exit status
}