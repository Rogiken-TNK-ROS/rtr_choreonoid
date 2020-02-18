cmake_minimum_required(VERSION 3.5.0)
project(rtr_choreonoid_models)

add_compile_options(-std=c++17)

find_package(catkin REQUIRED COMPONENTS
  choreonoid
  )

option(BUILD_RTR_MODEL "Building the Rogiken+/TNK-ROS Model files" ON)
if(NOT BUILD_RTR_MODEL)
  return()
endif()

install(DIRECTORY
  model
  project
  DESTINATION ${CHOREONOID_SHARE_SUBDIR}/rtr_choreonoid_models)
