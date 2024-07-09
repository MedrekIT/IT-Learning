#include <iostream>

void decimalToBinary(int x) {
    if (x > 0) {
        decimalToBinary(x/2);
        std::cout << x%2;
    }
}

int main() {
    int x;
    std::cout << "Enter a decimal number: ";
    std::cin >> x;

    std::cout << "Number " << x << " is ";
    decimalToBinary(x);
    std::cout << " in binary code";
    return 0;
}
