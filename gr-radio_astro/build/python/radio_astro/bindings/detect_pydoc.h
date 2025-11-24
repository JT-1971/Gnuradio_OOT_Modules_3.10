/*
 * Copyright 2021 Free Software Foundation, Inc.
 *
 * This file is part of GNU Radio
 *
 * SPDX-License-Identifier: GPL-3.0-or-later
 *
 */
#include "pydoc_macros.h"
#define D(...) DOC(gr,radio_astro, __VA_ARGS__ )
/*
  This file contains placeholders for docstrings for the Python bindings.
  Do not edit! These were automatically extracted during the binding process
  and will be overwritten during the build process
 */

 static const char *__doc_gr_radio_astro_detect = R"doc(Event Detection by comparison of signal to RMS Noise level. event detection: fill a circular buffer with complex samples and search for peaks nsigma above the RMS of the data stream input: complex vector of I/Q samples parameters.

Constructor Specific Documentation:

Return a shared_ptr to a new instance of radio_astro::detect.

To avoid accidental use of raw pointers, radio_astro::detect's constructor is in a private implementation class. radio_astro::detect::make is the public interface for creating new instances.

Args:
    vec_length : 
    dms : 
    f_obs : 
    bw : 
    t_int : 
    nt : )doc";

 static const char *__doc_gr_radio_astro_detect_detect = R"doc()doc";

 static const char *__doc_gr_radio_astro_detect_make = R"doc(Event Detection by comparison of signal to RMS Noise level. event detection: fill a circular buffer with complex samples and search for peaks nsigma above the RMS of the data stream input: complex vector of I/Q samples parameters.

Constructor Specific Documentation:

Return a shared_ptr to a new instance of radio_astro::detect.

To avoid accidental use of raw pointers, radio_astro::detect's constructor is in a private implementation class. radio_astro::detect::make is the public interface for creating new instances.

Args:
    vec_length : 
    dms : 
    f_obs : 
    bw : 
    t_int : 
    nt : )doc";

 static const char *__doc_gr_radio_astro_detect_set_vlen = R"doc()doc";
  
 static const char *__doc_gr_radio_astro_detect_set_dms = R"doc()doc";

 static const char *__doc_gr_radio_astro_detect_set_bw = R"doc()doc";

 static const char *__doc_gr_radio_astro_detect_set_freq = R"doc()doc";

 static const char *__doc_gr_radio_astro_detect_set_dt = R"doc()doc";

 static const char *__doc_gr_radio_astro_detect_set_mode = R"doc()doc";


  
