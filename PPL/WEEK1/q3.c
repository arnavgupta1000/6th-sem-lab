#include<stdio.h>
#include<mpi.h>
#include<math.h>
int main(int argc,char * argv[]){
	int rank,size;
	MPI_Init(&argc,&argv);
	MPI_Comm_rank(MPI_COMM_WORLD,&rank);
	MPI_Comm_size(MPI_COMM_WORLD,&size);
	int a=10,b=5,ans;
	switch(rank){
	case 0:
		ans=a+b;
		printf("process %d addition %d \n",rank,ans);
		break;
	case 1:
		ans=a-b;
		printf("Process %d subtraction %d \n",rank,ans);
		break;
	case 2:
		ans=a*b;
		printf("Process %d MULTIPLY %d \n",rank,ans);
		break;
	case 3:
		ans=a/b;
		printf("Process %d divide %d \n",rank,ans);
		break;
	case 4:
		printf("Error");
		
	}
	MPI_Finalize();
	return 0;

}
