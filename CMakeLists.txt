if(NOT ENABLE_GUI)
  return()
endif()

option(BUILD_RTR_PROJECTS "Building the Rogiken+/TNK-ROS project files" ON)
if(NOT BUILD_RTR_PROJECTS)
  return()
endif()

if(UNIX)
  add_custom_target(
    symlink_to_RTR_PROJECTS ALL
    COMMAND ${CMAKE_COMMAND} -E create_symlink
    ${CMAKE_CURRENT_SOURCE_DIR} ${CNOID_BINARY_SHARE_DIR}/rtr_projects)
endif()

install(DIRECTORY
  script
  DESTINATION ${CNOID_SHARE_SUBDIR}/rtr_projects)

if(NOT ENABLE_GUI)
  return()
endif()
