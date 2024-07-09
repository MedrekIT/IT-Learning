#include <iostream>

void bubbleSort(int t[], int s) {
    for (int i = 0; i < s-1; ++i) {
        for (int j = i+1; j < s; ++j) {
            if (t[j] < t[i]) {
                int temp = t[j];
                t[j] = t[i];
                t[i] = temp;
            }
        }
    }
}

int binarySearchRec(int x, int t[], int mid, int left, int right) {
    if (t[mid] == x) {
        return mid;
    }
    else {
        if (t[mid] > x) {
            return binarySearchRec(x, t, (mid+left)/2, left, mid);
        }
        else {
            return binarySearchRec(x, t, (mid+right)/2, mid, right);
        }
    }
}

int main() {
    int s, x;
    std::cout << "Enter array size: ";
    std::cin >> s;

    int t[s];

    for (int i = 0; i < s; i++) {
        std::cout << "Enter " << i+1 << " array element: ";
        std::cin >> t[i];
    }

    bubbleSort(t, s);

    std::cout << "Sorted array: ";
    for (int i = 0; i < s; i++) {
        if (i < s-1) {
            std::cout << t[i] << ", ";
        }
        else {
            std::cout << t[i] << std::endl;
        }
    }

    std::cout << "Enter the element you are looking for: ";
    std::cin >> x;

    std::cout << "This is number " << binarySearchRec(x, t, s/2, 0, s - 1) + 1 << " element of an array";
    return 0;
}
