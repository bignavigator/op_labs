#define PY_SSIZE_T_CLEAN
#include "Python.h"
#include <math.h>
#define N 100000000U

static inline double f(double x)
{
    return x <= 1.0 ? cos(x + x * x * x) : exp(-x * x) - x * x + 2.0 * x;
}

static double integrate(double a, double b)
{
    const double h = (b - a) / N;
    const double h2 = h * 0.5;
    double s = 0.0;
    for (register size_t i = 0; i < N; i++)
        s += f(a + i * h + h2);
    return s * h;
}

static long int sum_array(size_t n, int a[n])
{
    register long int s = 0;
    for (register size_t i = 0; i < n; i++)
        s += a[i];
    return s;
}

static PyObject *py_integrate(PyObject *self, PyObject *args)
{
    double a, b;
    if (PyArg_ParseTuple(args, "dd", &a, &b))
    {
        double result = integrate(a, b);
        return Py_BuildValue("d", result);
    }
    Py_RETURN_NONE;
}

static PyObject *py_sum_sequence(PyObject *self, PyObject *args)
{
    if (PyTuple_Size(args) != 1)
    {
        PyErr_SetString(PyExc_TypeError, "wrong number of arguments");
        Py_RETURN_NONE;
    }
    PyObject *sequence = NULL;
    if (!PyArg_ParseTuple(args, "O", &sequence))
    {
        PyErr_SetString(PyExc_TypeError, "argument parsing failed");
        Py_RETURN_NONE;
    }
    sequence = PySequence_Fast(sequence, "argument must be iterable");
    if (!sequence)
    {
        PyErr_SetString(PyExc_TypeError, "all items must be integers");
        Py_RETURN_NONE;
    }
    size_t seq_len = PySequence_Fast_GET_SIZE(sequence);
    int *array = malloc(seq_len * sizeof(int));
    if (!array)
    {
        Py_DECREF(sequence);
        return PyErr_NoMemory();
    }
    for (size_t i = 0; i < seq_len; i++)
    {
        PyObject *item = PySequence_Fast_GET_ITEM(sequence, i);
        if (!item)
        {
            Py_DECREF(sequence);
            free(array);
            PyErr_SetString(PyExc_ValueError, "failed to get sequence item");
            Py_RETURN_NONE;
        }
        PyObject *litem = PyNumber_Long(item);
        if (!litem)
        {
            Py_DECREF(sequence);
            free(array);
            PyErr_SetString(PyExc_TypeError, "all items must be integers");
            Py_RETURN_NONE;
        }
        array[i] = (int)PyLong_AsLong(litem);
        Py_DECREF(litem);
    }
    Py_DECREF(sequence);
    long int result = sum_array(seq_len, array);
    free(array);
    return Py_BuildValue("l", result);
}

static PyMethodDef mymodule_methods[] = {
        {"integrate", py_integrate, METH_VARARGS, "Function for numerical integration with c"},
        {"sum_sequence", py_sum_sequence, METH_VARARGS, "Function for counting int array sum with c"},
        {NULL, NULL, 0, NULL} // sentinel
};

static struct PyModuleDef mymodule = {
        PyModuleDef_HEAD_INIT,
        "my_module",
        "Example C module",
        -1, // no additional memory reqiurements
        mymodule_methods
};

PyMODINIT_FUNC PyInit_my_module(void)
{
    return PyModule_Create(&mymodule);
}