#include<bits/stdc++.h>
using namespace std;



void printMatrixInSpiralForm(vector<vector<int>>& mat)
{
	int row = mat.size();
	int col = mat[0].size();

	int rowBeg = 0 , colBeg = 0 , rowEnd = row - 1, colEnd = col - 1;


	while (rowBeg <= rowEnd && colBeg <= colEnd)
	{
		/* Traverse Right*/
		for (int i = colBeg ; i <= colEnd; i++)
			cout << mat[rowBeg][i] << ' ';
		/*since we are done with the first row ...just increment the rowBeg */
		rowBeg++;



		/* Traverse Down */
		for (int i = rowBeg; i <= rowEnd; i++)
			cout << mat[i][rowEnd] << ' ';
		/*decrement the last col */
		colEnd--;


		if (rowBeg <= rowEnd)
		{
			/* Traverse Left */
			for (int i = colEnd; i >= colBeg; i--)
				cout << mat[rowEnd][i] << ' ';

		}
		rowEnd--;

		if (colBeg <= colEnd)
		{
			/* Traverse Up */
			for (int i = rowEnd ; i >= rowBeg; i--)
				cout << mat[i][colBeg] << ' ';
		}
		colBeg++;
	}
}

void printMatrix(vector<vector<int>>& mat)
{
	int row = mat.size();
	int col = mat[0].size();

	for (int i = 0 ; i < row; i++)
	{
		for (int j = 0 ; j < col ; j++)
		{
			cout << mat[i][j] << '\t';
		}

		cout << endl;
	}

	cout << endl;
}


int main()
{
	vector<vector<int>> mat = { {1, 2, 3, 4},
		{5, 6, 7, 8},
		{9, 10, 11, 12},
		{13, 14, 15, 16}
	};

	printMatrixInSpiralForm(mat);



	return 0;
}