
option(BUILD_RTR_PROJECTS "Building the Rogiken+/TNK-ROS project files" ON)
if(NOT BUILD_RTR_PROJECTS)
  return()
endif()

install(DIRECTORY
  script
  DESTINATION ${CNOID_SHARE_SUBDIR}/rtr_projects)

if(NOT ENABLE_GUI)
  return()
endif()
