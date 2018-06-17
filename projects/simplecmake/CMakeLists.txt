
cmake_minimum_required(VERSION 3.8)

set(CMAKE_CXX_STANDARD 17)
set(CMAKE_CXX_STANDARD_REQUIRED ON)

set (PROJECT_NAME "hello_boost_with_cmake" CXX)

project(${PROJECT_NAME})

set(SOURCE hello-vsc.cpp)

add_executable(${PROJECT_NAME} ${SOURCE})
