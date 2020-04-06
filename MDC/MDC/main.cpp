//
//  main.cpp
//  MDC
//
//  Created by Guilherme Albertini on 28/03/20.
//  Copyright © 2020 Guilherme Albertini. All rights reserved.
//

#include <iostream>
#include "MDCSolver.h"
#include <vector>
int main(int argc, const char * argv[]) {
    try {
        
        MDCSolver solver = MDCSolver();
        
        //std::cout << solver.GetMDC(15, 5) << std::endl;
        //std::cout << solver.GetMDCRecursive(12, 9) << std::endl;
        
        solver.EvaluateSolver();
        
    } catch (std::runtime_error & e) {
        std::cout<<e.what()<<std::endl;
    }
    
    return 0;
}
