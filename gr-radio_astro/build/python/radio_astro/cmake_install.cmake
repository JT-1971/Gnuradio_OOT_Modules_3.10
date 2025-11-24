# Install script for directory: /home/dr/Code/gr-radio_astro/python/radio_astro

# Set the install prefix
if(NOT DEFINED CMAKE_INSTALL_PREFIX)
  set(CMAKE_INSTALL_PREFIX "/usr/local")
endif()
string(REGEX REPLACE "/$" "" CMAKE_INSTALL_PREFIX "${CMAKE_INSTALL_PREFIX}")

# Set the install configuration name.
if(NOT DEFINED CMAKE_INSTALL_CONFIG_NAME)
  if(BUILD_TYPE)
    string(REGEX REPLACE "^[^A-Za-z0-9_]+" ""
           CMAKE_INSTALL_CONFIG_NAME "${BUILD_TYPE}")
  else()
    set(CMAKE_INSTALL_CONFIG_NAME "Release")
  endif()
  message(STATUS "Install configuration: \"${CMAKE_INSTALL_CONFIG_NAME}\"")
endif()

# Set the component getting installed.
if(NOT CMAKE_INSTALL_COMPONENT)
  if(COMPONENT)
    message(STATUS "Install component: \"${COMPONENT}\"")
    set(CMAKE_INSTALL_COMPONENT "${COMPONENT}")
  else()
    set(CMAKE_INSTALL_COMPONENT)
  endif()
endif()

# Install shared libraries without execute permission?
if(NOT DEFINED CMAKE_INSTALL_SO_NO_EXE)
  set(CMAKE_INSTALL_SO_NO_EXE "1")
endif()

# Is this installation the result of a crosscompile?
if(NOT DEFINED CMAKE_CROSSCOMPILING)
  set(CMAKE_CROSSCOMPILING "FALSE")
endif()

# Set default install directory permissions.
if(NOT DEFINED CMAKE_OBJDUMP)
  set(CMAKE_OBJDUMP "/usr/bin/objdump")
endif()

if(CMAKE_INSTALL_COMPONENT STREQUAL "Unspecified" OR NOT CMAKE_INSTALL_COMPONENT)
  file(INSTALL DESTINATION "${CMAKE_INSTALL_PREFIX}/lib/python3.12/dist-packages/gnuradio/radio_astro" TYPE FILE FILES
    "/home/dr/Code/gr-radio_astro/python/radio_astro/__init__.py"
    "/home/dr/Code/gr-radio_astro/python/radio_astro/systemp_calibration.py"
    "/home/dr/Code/gr-radio_astro/python/radio_astro/chart_recorder.py"
    "/home/dr/Code/gr-radio_astro/python/radio_astro/correlate.py"
    "/home/dr/Code/gr-radio_astro/python/radio_astro/csv_filesink.py"
    "/home/dr/Code/gr-radio_astro/python/radio_astro/hdf5_sink.py"
    "/home/dr/Code/gr-radio_astro/python/radio_astro/radioastronomy.py"
    "/home/dr/Code/gr-radio_astro/python/radio_astro/jdutil.py"
    "/home/dr/Code/gr-radio_astro/python/radio_astro/angles.py"
    "/home/dr/Code/gr-radio_astro/python/radio_astro/ra_ascii_sink.py"
    "/home/dr/Code/gr-radio_astro/python/radio_astro/ra_event_log.py"
    "/home/dr/Code/gr-radio_astro/python/radio_astro/ra_event_sink.py"
    "/home/dr/Code/gr-radio_astro/python/radio_astro/ra_integrate.py"
    "/home/dr/Code/gr-radio_astro/python/radio_astro/ra_vave.py"
    "/home/dr/Code/gr-radio_astro/python/radio_astro/ra_vmedian.py"
    "/home/dr/Code/gr-radio_astro/python/radio_astro/filters.py"
    "/home/dr/Code/gr-radio_astro/python/radio_astro/powerSpectrum.py"
    "/home/dr/Code/gr-radio_astro/python/radio_astro/integration.py"
    "/home/dr/Code/gr-radio_astro/python/radio_astro/vector_moving_average.py"
    "/home/dr/Code/gr-radio_astro/python/radio_astro/png_print_spectrum.py"
    )
endif()

if(NOT CMAKE_INSTALL_LOCAL_ONLY)
  # Include the install script for each subdirectory.
  include("/home/dr/Code/gr-radio_astro/build/python/radio_astro/bindings/cmake_install.cmake")

endif()

