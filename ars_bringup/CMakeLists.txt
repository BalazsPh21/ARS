cmake_minimum_required(VERSION 3.5)

project(ars_bringup)

find_package(ament_cmake REQUIRED)
find_package(ars_description REQUIRED)

# Install project launch files
install(
  DIRECTORY
    launch
    config
    maps
  DESTINATION share/${PROJECT_NAME}/
)

if(BUILD_TESTING)
  find_package(ament_lint_auto REQUIRED)
  ament_lint_auto_find_test_dependencies()
endif()

ament_package()