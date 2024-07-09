#include <iostream>

int main() {
    int x, y=1;

    std::cout << "Enter a number you want to get factorial of: ";
    std::cin >> x;

    for (int i = 1; i < x+1; ++i) {
        y*=i;
    }
    std::cout << x << " factorial is " << y;
    return 0;
}
