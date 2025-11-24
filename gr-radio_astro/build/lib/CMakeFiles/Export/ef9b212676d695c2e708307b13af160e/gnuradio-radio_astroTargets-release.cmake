#----------------------------------------------------------------
# Generated CMake target import file for configuration "Release".
#----------------------------------------------------------------

# Commands may need to know the format version.
set(CMAKE_IMPORT_FILE_VERSION 1)

# Import target "gnuradio::gnuradio-radio_astro" for configuration "Release"
set_property(TARGET gnuradio::gnuradio-radio_astro APPEND PROPERTY IMPORTED_CONFIGURATIONS RELEASE)
set_target_properties(gnuradio::gnuradio-radio_astro PROPERTIES
  IMPORTED_LOCATION_RELEASE "${_IMPORT_PREFIX}/lib/libgnuradio-radio_astro.so.g1112b05"
  IMPORTED_SONAME_RELEASE "libgnuradio-radio_astro.so.1.0.0git"
  )

list(APPEND _cmake_import_check_targets gnuradio::gnuradio-radio_astro )
list(APPEND _cmake_import_check_files_for_gnuradio::gnuradio-radio_astro "${_IMPORT_PREFIX}/lib/libgnuradio-radio_astro.so.g1112b05" )

# Commands beyond this point should not need to know the version.
set(CMAKE_IMPORT_FILE_VERSION)
