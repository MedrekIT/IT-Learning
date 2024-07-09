//
// Created by Daniel Mędrek on 26/06/2024.
//
#include <iostream>

void revArrRec(int t[], int s, int n=0) {
    std::cout << std::endl;
    if (n >= s/2) {
        return;
    }
    int temp = t[n];
    t[n] = t[s-n-1];
    t[s-n-1] = temp;
    return revArrRec(t, s, n+1);
}

int main() {
    int n;
    std::cout << "Enter array size: ";
    std::cin >> n;

    int t[n];

    for (int i = 0; i < n; ++i) {
        std::cout << "Enter " << i+1 << " list element: ";
        std::cin >> t[i];
    }
    revArrRec(t, n);

    std::cout << "Reversed list: ";
    for (int i = 0; i < n; ++i) {
        if (i < n-1) {
            std::cout << t[i] << ", ";
        }
        else {
            std::cout << t[i] << std::endl;
        }
    }
}