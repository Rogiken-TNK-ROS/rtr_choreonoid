
option(BUILD_RTR_MODEL "Building the Rogiken+/TNK-ROS Model files" ON)
if(NOT BUILD_RTR_MODEL)
  return()
endif()

install(DIRECTORY
  model
  project
  DESTINATION ${CNOID_SHARE_SUBDIR}/rtr_models)
