#include <stdio.h>
#include <math.h>


double func_f(double x) {
    return exp(-2*x)-x;
}


double func_g(double x) {
    return sqrt(x)+1/exp(x);
}


double func_a_ij(double i, double j) {
    return fabs(func_f(i) + func_g(j));
}


double func_n_a(double m, double n) {
    double min_value = 10.0;
    double max_value = 0.0;
    for (int i=1; i <= m; i++) {
        for (int j=1; j <= n; j++) {
            min_value = fmin(min_value, func_a_ij(i, j));
            max_value = fmax(max_value, func_a_ij(i, j));
        }
    }
    return ((min_value+1)/(max_value+1))-1;
}


int main() {
    printf("%lf", func_n_a(10, 10));
    return 0;
}