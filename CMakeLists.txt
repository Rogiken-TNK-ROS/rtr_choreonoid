if(NOT ENABLE_GUI)
  return()
endif()

option(BUILD_RTR_MODEL "Building the Rogiken+/TNK-ROS Model files" ON)
if(NOT BUILD_RTR_MODEL)
  return()
endif()

if(UNIX)
  add_custom_target(
    symlink_to_RTR_MODEL ALL
    COMMAND ${CMAKE_COMMAND} -E create_symlink
    ${CMAKE_CURRENT_SOURCE_DIR} ${CNOID_BINARY_SHARE_DIR}/rtr_models)
endif()

install(DIRECTORY
  model
  project
  DESTINATION ${CNOID_SHARE_SUBDIR}/rtr_models)
