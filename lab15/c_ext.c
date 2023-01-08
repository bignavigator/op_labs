#define PY_SSIZE_T_CLEAN
#include <math.h>
#include <python3.10/Python.h>
#define N 100000000U

static inline double func_f(double x) {
    return exp(-2*x)-x;
}


static double func_g(double x) {
    return sqrt(x)+1/exp(x);
}


static double func_a_ij(double i, double j) {
    return fabs(func_f(i) + func_g(j));
}

static PyObject *py_integrate(PyObject *self, PyObject *args)
{
    double m, n;
    if (PyArg_ParseTuple(args, "dd", &m, &n))
    {
        double min_value = 10.0;
        double max_value = 0.0;
        for (int i=1; i <= m; i++) {
            for (int j=1; j <= n; j++) {
                min_value = fmin(min_value, func_a_ij(i, j));
                max_value = fmax(max_value, func_a_ij(i, j));
            }
    }
    double result = ((min_value+1)/(max_value+1))-1;
    return Py_BuildValue("d", result);
    }
    Py_RETURN_NONE;
}

static PyMethodDef c_ext_methods[] = {
        {"integrate", py_integrate, METH_VARARGS, "Function for numerical integration with c"},
        {NULL, NULL, 0, NULL} // sentinel
};

static struct PyModuleDef c_ext = {
        PyModuleDef_HEAD_INIT,
        "c_ext",
        "Example C module",
        -1, // no additional memory reqiurements
        c_ext_methods
};

PyMODINIT_FUNC PyInit_c_ext(void)
{
    return PyModule_Create(&c_ext);
}