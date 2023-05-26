#include <iostream>
#include <complex>
#include <vector>
#include <cmath>
#include <fstream>
#include <chrono>

using namespace std;

vector<vector<int>> compute_mandelbrot(int N_max, double some_threshold, int nx, int ny) {
    vector<vector<int>> mandelbrot_set(nx, vector<int>(ny, 0));

    // A grid of c-values
    vector<double> x(nx);
    vector<double> y(ny);

    for (int i = 0; i < nx; i++) {
        x[i] = -2.0 + i * (3.0 / (nx - 1));
    }

    for (int i = 0; i < ny; i++) {
        y[i] = -1.5 + i * (3.0 / (ny - 1));
    }

    for (int i = 0; i < nx; i++) {
        for (int j = 0; j < ny; j++) {
            complex<double> c(x[i], y[j]);
            complex<double> z(0, 0);

            // Mandelbrot iteration
            int k = 0;
            while (k < N_max && abs(z) < some_threshold) {
                z = z * z + c;
                k++;
            }

            if (k == N_max) {
                mandelbrot_set[i][j] = 1;
            }
        }
    }

    return mandelbrot_set;
}

int main() {
    int N_max = 500;
    double some_threshold = 500.0;
    // int nx = 5601;
    // int ny = 5401;
    int nx = 601;
    int ny = 401;

    std::chrono::steady_clock::time_point begin = std::chrono::steady_clock::now();

    vector<vector<int>> mandelbrot_set = compute_mandelbrot(N_max, some_threshold, nx, ny);

    std::chrono::steady_clock::time_point end = std::chrono::steady_clock::now();
    std::cout << "Elapsed time: (sec) = " << (std::chrono::duration_cast<std::chrono::microseconds>(end - begin).count())/1000000.0 <<std::endl;

    ofstream outfile("mandelbrot_set.txt");
    for (int i = 0; i < nx; i++) {
        for (int j = 0; j < ny; j++) {
            outfile << mandelbrot_set[i][j] << " ";
        }
        outfile << endl;
    }
    outfile.close();

    return 0;
}

