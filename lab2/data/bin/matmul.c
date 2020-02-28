#include <stdlib.h>
typedef float real_t;
typedef real_t* arr_t;
#if VERSION == 0
arr_t matmul_basic(const arr_t A, const arr_t B, const int M, const int N, const int K) {
    arr_t C = (arr_t) malloc(M * N * sizeof(real_t)); 
    for( int m = 0; m < M; ++m ) {
        for( int n = 0; n < N; ++n ) {
            for( int k = 0; k < K; ++k ) {
                C[ m * M + n ] += A[ m * M + k ] * B[ k * K + n ];
            }
        }
    }
  return C;
}
#elif VERSION == 1
arr_t matmul_basic(const arr_t A, const arr_t B, const int M, const int N, const int K) {
    arr_t C = (arr_t) malloc(M * N * sizeof(real_t)); 
    for( int m = 0; m < M; ++m ) {
        for( int k = 0; k < K; ++k ) {
            real_t _a = A[m * M + k];
            for( int n = 0; n < N; ++n ) {
                C[ m * M + n ] += _a * B[ k * K + n ];
            }
        }
    }
  return C;
}
#endif

int main() { 
    const int N = 128;
    arr_t A = (arr_t) malloc(N * N * sizeof(real_t)); 
    arr_t B = (arr_t) malloc(N * N * sizeof(real_t)); 
    arr_t C = matmul_basic(A, B, N, N, N);
    return 0;
}

