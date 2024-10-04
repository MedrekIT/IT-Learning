cmake_minimum_required(VERSION 3.28)
project(test)

set(CMAKE_CXX_STANDARD 17)

find_package(SDL2 REQUIRED COMPONENTS SDL2)
find_package(SDL2_ttf REQUIRED)
find_package(SDL2_mixer REQUIRED)

add_executable(test main.cpp)

target_link_libraries(test PRIVATE SDL2::SDL2)
target_link_libraries(test PRIVATE SDL2_ttf::SDL2_ttf)
target_link_libraries(test PRIVATE SDL2_mixer::SDL2_mixer)