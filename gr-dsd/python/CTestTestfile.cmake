# CMake generated Testfile for 
# Source directory: /home/dr/Code/gr-dsd/python
# Build directory: /home/dr/Code/gr-dsd/python
# 
# This file includes the relevant testing commands required for 
# testing this directory and lists subdirectories to be tested as well.
add_test(qa_dsd_block_ff "/usr/bin/sh" "qa_dsd_block_ff_test.sh")
set_tests_properties(qa_dsd_block_ff PROPERTIES  _BACKTRACE_TRIPLES "/usr/lib/x86_64-linux-gnu/cmake/gnuradio/GrTest.cmake;119;add_test;/home/dr/Code/gr-dsd/python/CMakeLists.txt;34;GR_ADD_TEST;/home/dr/Code/gr-dsd/python/CMakeLists.txt;0;")
subdirs("bindings")
