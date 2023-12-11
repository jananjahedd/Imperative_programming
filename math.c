#include <stdio.h>
#include <math.h>
#include <stdlib.h>
#include <assert.h>
#include <string.h>

typedef struct __attribute__((packed)) {
	double   *mem; // memory for the cells
	const int rows, cols;
} Matrix;

Matrix newMat(int rows, int cols){
	return (Matrix){
		.rows = rows,
		.cols = cols,
		.mem = calloc(rows*cols, sizeof(*(Matrix){}.mem))
	};
}

Matrix copyMat(Matrix m){
	Matrix new = (Matrix){
		.rows = m.rows,
		.cols = m.cols,
		.mem = calloc(m.rows*m.cols, sizeof *m.mem)
	};
	memcpy(new.mem, m.mem, m.rows*m.cols*sizeof *new.mem);
	return new;
}

void freeMat(Matrix m){
	free(m.mem);
}

void printMat(Matrix m){
	for (int i=0; i<m.rows; i++){
		for (int j=0; j<m.cols; j++){
			printf("% lf%c",
				((double(*)[m.cols])m.mem)[i][j],
				j+1==m.cols ? '\n' : '\t'
			);
		}
	}
	puts("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~");
}

void readMat(Matrix m){
	for (int i=0; i<m.rows; i++){
		for (int j=0; j<m.cols; j++){
			scanf("%lf", &((double(*)[m.cols])m.mem)[i][j]);
		}
	}	
}

// floating point equals
int feq(double a, double b){
	#define EPS 0.00001
	return fabs(a-b) < EPS;
}

int lzCount(Matrix m, int row){
	assert(row < m.rows);
	for (int i = 0; i < m.cols; ++i){
		if (!feq(m.mem[row*m.cols+i], 0)){
			return i;
		}
	}
	return m.cols;
}

void rowSwap(Matrix m, int r1, int r2){
	double tmp[m.cols];
	memcpy(tmp,             m.mem+m.cols*r1, m.cols*sizeof *m.mem);
	memcpy(m.mem+m.cols*r1, m.mem+m.cols*r2, m.cols*sizeof *m.mem);
	memcpy(m.mem+m.cols*r2, tmp,             m.cols*sizeof *m.mem);
}

void rrefMat(Matrix m){
	double (*mat)[m.cols] = (void*)m.mem;
	// gaussian elim
	for (int pcol=0; pcol<m.cols; pcol++){
		printf("trying find pivot row for col %d\n", pcol);
		// pivot column
		// can we find a pivot row for this column?
		int rowFound = 0;
		int prow;
		for (prow=pcol; prow<m.rows; prow++){
			// leading cols are 0?
			// pcol is nonzero?
			if (feq(mat[prow][pcol],0) || lzCount(m, prow) != pcol){
				continue;
			}

			// we have found a pivot row
			rowFound = 1;
			break;
		}
		if (!rowFound){
			continue; // next pivot
		}
		printf("pivot row: r%d\n", prow);

		// normalize pivot row
		double scale = mat[prow][pcol];
		if (!feq(scale, 1)){
			printf("r%d *= 1/%f\n", prow, scale);
			scale = 1.0/scale;
			for (int j=m.cols; j>pcol; j--){
				mat[prow][j-1] *= scale;
			}
		}

		printMat(m);

		// swap row
		// (pcol is the amount of rref rows above)
		if (pcol != prow){
			printf("swap r%d r%d\n", pcol, prow);
			rowSwap(m, pcol, prow);
			printMat(m);
			prow = pcol;
		}

		// subtract pivot row from other rows
		for (int i=0; i<m.rows; i++){
			if (i == prow) continue;
			double factor = mat[i][pcol];
			if (feq(factor, 0)) continue;
			for (int j=m.cols; j>pcol; j--){
				mat[i][j-1] -= factor*mat[prow][j-1];
			}
			printf("r%d -= %f*r%d\n", i, factor, prow);
		}

		printMat(m);
	}
}

int main(void){
	puts("Enter 2 ints nRows nCols");
	int r,c;
	scanf("%d %d", &r, &c);
	printf("Enter %d*%d (=%d) doubles\n", r,c,r*c);
	Matrix m = newMat(r,c);
	readMat(m);
	printMat(m);
	rrefMat(m);
	puts("RREF:");
	printMat(m);
	freeMat(m);
}