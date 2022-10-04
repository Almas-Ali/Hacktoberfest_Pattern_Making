#include <iostream>

int main() {
    // Right Triangle Star Pattern for cpp
    // Prompt the user for height
    std::cout << "Height? ";
    
    int height = 0;
    int rowCount = 0;
    std::cin >> height;
    
    // Display start pattern
    if (height > 0) {
        std:: cout << "*\n";
        rowCount ++;
        
        while (rowCount < height) {
            for (int i=0; i < rowCount+1; i++) {
                std:: cout << "*";
            }
            std:: cout << "\n";
            rowCount ++;
        }
    }
    

    return 0;
}