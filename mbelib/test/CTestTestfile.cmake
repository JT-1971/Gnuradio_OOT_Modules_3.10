# CMake generated Testfile for 
# Source directory: /home/dr/Code/mbelib/test
# Build directory: /home/dr/Code/mbelib/test
# 
# This file includes the relevant testing commands required for 
# testing this directory and lists subdirectories to be tested as well.
add_test(gtest "mbetest")
set_tests_properties(gtest PROPERTIES  _BACKTRACE_TRIPLES "/home/dr/Code/mbelib/test/CMakeLists.txt;19;add_test;/home/dr/Code/mbelib/test/CMakeLists.txt;0;")
subdirs("gtest")
subdirs("gmock")
