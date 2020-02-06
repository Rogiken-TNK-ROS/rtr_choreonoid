cmake_minimum_required(VERSION 3.5.0)
project(rtr_projects)

add_compile_options(-std=c++17)

find_package(catkin REQUIRED COMPONENTS
  choreonoid
  )

option(BUILD_RTR_PROJECTS "Building the Rogiken+/TNK-ROS project files" ON)
if(NOT BUILD_RTR_PROJECTS)
  return()
endif()

install(DIRECTORY
  project
  script
  DESTINATION ${CHOREONOID_SHARE_SUBDIR}/rtr_projects)
