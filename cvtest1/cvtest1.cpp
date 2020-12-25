/*
    https://www.murtazahassan.com/courses/opencv-cpp-course/lesson/windows/

    VC++ Directories
    1. Add Build Directories: D:\opencv\build\include
    2. Add Library Directories: D:\opencv\build\x64\vc15\lib
Linker Input
    3. Add Linker input: opencv_world451d.lib (opencv 4.5.1)
       d for debug without d for release

*/

#include <opencv2/imgcodecs.hpp>
#include <opencv2/highgui.hpp>
#include <opencv2/imgproc.hpp>
#include <iostream>

using namespace cv;
using namespace std;


/////////////////  Images  //////////////////////

int main() {
    string path = "Resources/lambo.png";
    Mat img = imread(path);
    imshow("Image", img);
    waitKey(0);
    return 0;
}



