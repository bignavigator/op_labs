#include <stdio.h>
#include <math.h>


double func_f(double x) {
    return exp(e, -2*x)-x;
}


double func_g(double x) {
    return sqrt(x)+1/exp(e, x);
}


double func_a_ij(double i, double j) {
    return fabs(func_f(i) + func_g(j));
}


double func_n_a(double m, double n) {
    float min_value = ("inf");
    float max_value = ("-inf");
    for (i=1, i <= m, i++) {
        for (j=1, i <= n, j++) {
            min_value = min(min_value, func_a_ij(i, j));
            max_value = max(max_value, func_a_ij(i, j));
        }
    }
    return ((min_value+1)/(max_value+1))-1
}


int main() {
    print("%lf", func_n_a(10, 10));
    return 0;
}