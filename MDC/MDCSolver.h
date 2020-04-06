//
//  MDCSolver.h
//  MDC
//
//  Created by Guilherme Albertini on 28/03/20.
//  Copyright © 2020 Guilherme Albertini. All rights reserved.
//

#ifndef MDCSolver_h
#define MDCSolver_h

#include <iostream>
#include <cstdio>
#include <time.h>
#include <chrono>
#include <random>
#include <iomanip>

static class MDCSolver
{

private:
public:

    //Empty constructor
    MDCSolver(){}

    //Solve MDC for content and return de MDC
    int GetMDC(const int a, const int b){
        
        int a_ = a;
        int b_ = b;
        
        //Try to solve MDC
        try
        {
            if (a_ < b_)
                throw std::runtime_error("MDCSolver A must be higher than B.");
        
            int left = 1;
            
            while(left != 0)
            {
                left = a_ % b_;
                a_ = b_;
                b_ = left;
            }
            
        } catch (std::runtime_error & e)
        {
            throw e;
        }
        
        return a_;
    }
    
    //Solve MDC recurssively for content and return de MDC
    int GetMDCRecursive(const int a, const int b){
        
        int a_ = a;
        int b_ = b;
        
        //Try to solve MDC
        try
        {
            if (a_ < b_)
                throw std::runtime_error("MDCSolver A must be higher than B.");
            
            if (b_ == 0)
                return a_;
            
            return GetMDCRecursive(b_, a_ % b_);
        } catch (std::runtime_error & e)
        {
            throw e;
        }
    }
    
    void EvaluateSolver(){
        
        int i = 0;
        std::chrono::time_point<std::chrono::steady_clock> tStart;
        std::random_device rd;
        std::mt19937 eng(rd());
        std::uniform_int_distribution<int> randGcd(1000000, 9000000);
        std::cout.setf(std::ios::fixed);
        
        int a = (int)randGcd(eng);
        int b = (int)randGcd(eng);
        
        std::cout<<"Iteration;Type;A;B;MDC;Time(s)"<<std::endl;
        
        while (i < 30)
        {
            
            if(a<b)
                continue;
            
            MDCSolver solver = MDCSolver();
            
            tStart = std::chrono::high_resolution_clock::now();
            std::cout<< i+1 <<";Iterative;"<<a<<";"<<b<<";"<<solver.GetMDC(a, b)<<";"<< std::chrono::duration_cast<std::chrono::microseconds>
                                                            (std::chrono::high_resolution_clock::now() - tStart).count() <<std::endl;
            
            tStart = std::chrono::high_resolution_clock::now();
            std::cout<< i+1 <<";Recursive;"<<a<<";"<<b<<";"<<solver.GetMDCRecursive(a, b)<<";"<< std::chrono::duration_cast<std::chrono::microseconds>
                                                            (std::chrono::high_resolution_clock::now() - tStart).count() <<std::endl;
            
            i++;
        }
    }
    
};

#endif /* MDCSolver_h */
