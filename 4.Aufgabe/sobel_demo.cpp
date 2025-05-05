
/*Implementieren Sie den Sobel-Operator in C++. Hier lernen Sie kennen, wie Sie C++
Funktionen mithilfe von pybind11 aus ihrem Python Skript aufrufen k¨onnen.
a) Nutzen sie die Python-Datei sobel demo.py und definieren Sie die Filter in x und
y Richtung.
b) Vervollst¨andigen Sie die Funktion sobel() in der Datei sobel demo.cpp, welche ihnen die erste Ableitung zur¨uckgibt. Das Filterergebnis soll skaliert sein. Auf eine
Randbehandlung kann verzichtet werden.
c) Installieren Sie python-dev und pybind11 in ihre Pythonumgebung.
d) Kompilieren Sie unter Unix die sobel demo.cpp mit folgendem Kommando:
c++ −I e i g e n −3. 4. 0 −O3 −Wall −s h a r e d −s t d=c++11 −fPIC
$ ( py th on 3 −m py bi n d 1 1 −−i n c l u d e s ) s o b el d em o . cpp −o
s o b el d em o$ ( py thon3−c o n f i g −−e x t e n s i o n −s u f f i x )*/

#include<pybind11/pybind11.h>
#include<pybind11/numpy.h>
#include <pybind11/eigen.h>

namespace py = pybind11;


Eigen::MatrixXd sobel(Eigen::MatrixXd gray_img, Eigen::MatrixXd filter) {
    Eigen::MatrixXd filtered_img(gray_img.rows()-2, gray_img.cols()-2);

    for (long i = 1; i < gray_img.rows() - 1; ++i) {
        for (long j = 1; j < gray_img.cols() - 1; ++j) {
            Eigen::MatrixXd neighborhood = gray_img.block<3, 3>(i - 1, j - 1);
            double filtered_value = (neighborhood.cwiseProduct(filter)).sum();
            filtered_img(i - 1, j - 1) = filtered_value;
        }
    }

    return filtered_img;
}


PYBIND11_MODULE(sobel_demo, m) {
    m.doc() = "sobel operator using numpy!";
    m.def("sobel", &sobel);
}