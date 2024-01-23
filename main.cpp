#include <cmath>
#include <iostream>
#include "opencv2/opencv.hpp"
#define _USE_MATH_DEFINES
#include <math.h>
#include <fstream>
#include <string>
#include <vector>

double MAX_degree = 360.0;
int  SIZE_lidar = 505;
double tic_deg = MAX_degree/double(SIZE_lidar);
double tic_rad = tic_deg*M_PI/180.0;

std::vector<std::vector<double>> readfile();
int drawlidargraph(std::vector<std::vector<double>> &v);

int main()
{
    cv::Mat canvas = cv::Mat::zeros(500, 500, CV_8UC3);

    std::vector<std::vector<double>> lidar_data;
    //std::vector<double> lidar_data;

    std::cout << "1. PI = " << M_PI << "\n"; // 3.14159
    std::cout << "2. tic_deg = " << tic_deg << "\n"; // 0.712871
    std::cout << "3. tic_rad = " << tic_rad << "\n"; // 0.012442

    lidar_data = readfile();
    //std::cout << lidar_data.size() <<"\n";

    drawlidargraph(lidar_data);

    return 0;
}

int drawlidargraph(std::vector<std::vector<double>> &v){
    for(const auto& data:v){
        cv::Mat canvas = cv::Mat::zeros(1000, 1000, CV_8UC3);

        std::vector<double> x(505);
        std::vector<double> y;

        for(int i=0; i<SIZE_lidar; i++){
            if(data[i] > 0.0){
                x[i] = (data[i] * cos(i * tic_rad));
                y.push_back(data[i] * sin(i * tic_rad));
            }
        }

        for (int j = 0; j < x.size(); j++) {
            cv::circle(canvas, cv::Point(static_cast<int>(x[j] * 100) + 500, static_cast<int>(y[j] * 100) + 500), 2, cv::Scalar(255, 255, 255), -1);
        }

        cv::imshow("Lidar Data", canvas);
        cv::waitKey(10);
    }
    return 0;
}

std::vector<std::vector<double>> readfile(){
    //std::vector<double> data;
    std::vector<std::vector<double>> data;

    std::ifstream file("E:\\Codes\\lidar_algorithms\\lidar.txt");
    
    if (!file.is_open()) {
        std::cerr << "Error opening file." << std::endl;
        return data;
    }
    
    // Parsing lidar file based on ','
    std::string line, token;
    std::getline(file, line);
    std::stringstream ss(line);
    int cnt1 = 0;
    int cnt2 = 0;

    std::vector<double> d;
    while (getline(ss, token, ',')) {
        if(cnt1 < 252500){
            cnt1++;
            if(cnt2 < 504){
                cnt2++;
                d.push_back(std::stod(token));
            }
            else{
                cnt2 = 0;
                d.push_back(std::stod(token));
                data.push_back(d);
                d.clear();
            }
        }
        else{
            break;
        }
	}
    // Separating   
    file.close();

    // std::ofstream writeFile;
    // writeFile.open("output.txt");

    // if(writeFile.is_open()) std::cout<< "writeFile is working...\n";

    // char arr[11] = "BlockDMask";    //"BlockDMask\0"????
    // writeFile.write(arr, 10);

    // std::string str = "is handsome.";
    // writeFile.write(str.c_str(), str.size());

    // writeFile.close();
    
    return data;
}