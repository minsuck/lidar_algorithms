cmake_minimum_required(VERSION 3.22)

project(HelloCV)

set(CMAKE_CXX_STANDARD 20)
set(CMAKE_CXX_STANDARD_REQUIRED ON)
set(CMAKE_CXX_EXTENSIONS OFF)

include(CTest)
enable_testing()

find_package( OpenCV REQUIRED )
include_directories( ${OpenCV_INCLUDE_DIRS} )

set(CPACK_PROJECT_NAME ${PROJECT_NAME})
set(CPACK_PROJECT_VERSION ${PROJECT_VERSION})

add_executable(HelloCV main.cpp)

target_link_libraries(HelloCV ${OpenCV_LIBS})

#target_compile_options(program PUBLIC -Wall -Werror)