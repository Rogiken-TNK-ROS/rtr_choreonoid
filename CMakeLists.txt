
option(BUILD_RTR_PROJECTS "Building the Rogiken+/TNK-ROS project files" ON)
if(NOT BUILD_RTR_PROJECTS)
  return()
endif()

install(DIRECTORY
  script
