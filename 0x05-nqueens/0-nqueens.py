#include <iostream>
#include <vector>

using namespace std;

int numSolutions=0;

//Uses recursion to count how many solutions there are for
//placing n queens on an nxn chess board
bool isSafe(vector<vector<int>>board, int row, int col){
            //checks column for queens
                for(int i=0; i<row; i++){
                            if(board[i][col]==1){
                                            return false;
                                                    }
                                }
                    
                    //checks right diagonal for queens(\)
                        for(int i=row, x=col; i>= 0 && x>=0; i--, x--){
                                    if(board[i][x]==1){
                                                    return false;
                                                            }
                                        }
                            
                            //checks left diagonal for queens(/)
                                for(int i=row, x=col; i>= 0 && x>=0; i--, x++){
                                            if(board[i][x]==1){
                                                            return false;
                                                                    }
                                                }
                                    
                                    //returns true once all conditions are met for queen to be safe
                                        return true;
                                        }



void nQueensSolution(vector<vector<int>>board, int row, int n){
            //base case, adds to number of solutions if queens are placed successfully
                if(row==n){
                            numSolutions++;
                                    return;
                                        }
                    
                    //places a queen in the square if it is safe
                        for(int i=0; i<n; i++){
                                    if(isSafe(board, row, i)==true){
                                                    board[row][i]=1;
                                                                
                                                                //recurring function to move onto next row to find solution
                                                                            nQueensSolution(board, row+1, n);
                                                                                        
                                                                                        //backtrack to try the other squares in current row
                                                                                                    board[row][i]=0;
                                                                                                            }
                                        }
                            
                        }

int nQueens(int n)
{
            //Implement int nQueens(int n)
                //Feel free to implement any recursive helper functions
                    vector<vector<int>>board(n, vector<int>(n));
                        int row=0;
                            nQueensSolution(board, row, n);
                                return numSolutions;
                                }

int main()
{
            cout << "1: " << nQueens(1) << endl;
                numSolutions=0;
                    cout << "2: " << nQueens(2) << endl;
                        numSolutions=0;
                            cout << "3: " << nQueens(3) << endl;
                                numSolutions=0;
                                    cout << "4: " << nQueens(4) << endl;
                                        numSolutions=0;
                                            cout << "5: " << nQueens(5) << endl;
                                                numSolutions=0;
                                                    cout << "6: " << nQueens(6) << endl;
                                                        numSolutions=0;
                                                            cout << "7: " << nQueens(7) << endl;
                                                                numSolutions=0;
                                                                    cout << "8: " << nQueens(8) << endl;
                                                                        numSolutions=0;
                                                                            cout << "9: " << nQueens(9) << endl;
                                                                                numSolutions=0;
                                                                                    cout << "10: " << nQueens(10) << endl;
                                                                                        numSolutions=0;
                                                                                            cout << "11: " << nQueens(11) << endl;
                                                                                                numSolutions=0;
                                                                                                    cout << "12: " << nQueens(12) << endl;
                                                                                                        return 0;
                                                                                                        }
