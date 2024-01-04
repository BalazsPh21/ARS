cmake_minimum_required(VERSION 3.5)

project(ars_description)

find_package(ament_cmake REQUIRED)

if(BUILD_TESTING)
  find_package(ament_lint_auto REQUIRED)
  ament_lint_auto_find_test_dependencies()
endif()

install(
  DIRECTORY
    models/
  DESTINATION share/${PROJECT_NAME}/models
)

install(
  DIRECTORY
    urdf/
  DESTINATION share/${PROJECT_NAME}/urdf
)

install(
  DIRECTORY
    config/
  DESTINATION share/${PROJECT_NAME}/config
)

ament_package()