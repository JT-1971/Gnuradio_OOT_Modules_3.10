#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#
# SPDX-License-Identifier: GPL-3.0
#
# GNU Radio Python Flow Graph
# Title: DAB Measurement tool
# Author: Serge G
# Description: Constellation+MER+Spectrum (all blocks are extracted)
# GNU Radio version: 3.10.9.2

from PyQt5 import Qt
from gnuradio import qtgui
from gnuradio import analog
from gnuradio import blocks
from gnuradio import fft
from gnuradio.fft import window
from gnuradio import gr
from gnuradio.filter import firdes
import sys
import signal
from PyQt5 import Qt
from argparse import ArgumentParser
from gnuradio.eng_arg import eng_float, intx
from gnuradio import eng_notation
import gnuradio.dab as dab
import osmosdr
import time
import sip



class dab_whole_graph(gr.top_block, Qt.QWidget):

    def __init__(self):
        gr.top_block.__init__(self, "DAB Measurement tool", catch_exceptions=True)
        Qt.QWidget.__init__(self)
        self.setWindowTitle("DAB Measurement tool")
        qtgui.util.check_set_qss()
        try:
            self.setWindowIcon(Qt.QIcon.fromTheme('gnuradio-grc'))
        except BaseException as exc:
            print(f"Qt GUI: Could not set Icon: {str(exc)}", file=sys.stderr)
        self.top_scroll_layout = Qt.QVBoxLayout()
        self.setLayout(self.top_scroll_layout)
        self.top_scroll = Qt.QScrollArea()
        self.top_scroll.setFrameStyle(Qt.QFrame.NoFrame)
        self.top_scroll_layout.addWidget(self.top_scroll)
        self.top_scroll.setWidgetResizable(True)
        self.top_widget = Qt.QWidget()
        self.top_scroll.setWidget(self.top_widget)
        self.top_layout = Qt.QVBoxLayout(self.top_widget)
        self.top_grid_layout = Qt.QGridLayout()
        self.top_layout.addLayout(self.top_grid_layout)

        self.settings = Qt.QSettings("GNU Radio", "dab_whole_graph")

        try:
            geometry = self.settings.value("geometry")
            if geometry:
                self.restoreGeometry(geometry)
        except BaseException as exc:
            print(f"Qt GUI: Could not restore geometry: {str(exc)}", file=sys.stderr)

        ##################################################
        # Variables
        ##################################################
        self.symbols_per_frame__ = symbols_per_frame__ = [76, 76, 153, 76]
        self.symbols_for_magnitude_equalization__ = symbols_for_magnitude_equalization__ = [6,6,12,6]
        self.symbols_for_ffs_estimation__ = symbols_for_ffs_estimation__ = [8,8,16,8]
        self.symbol_length__ = symbol_length__ = [2552, 638, 319, 1276]
        self.samp_rate = samp_rate = 2048000
        self.num_carriers__ = num_carriers__ = [1536, 384, 192, 768]
        self.ns_length__ = ns_length__ = [2656, 664, 345, 1328]
        self.frame_length__ = frame_length__ = [196608, 49152, 49152, 98304]
        self.fft_length__ = fft_length__ = [2048, 512, 256, 1024]
        self.dab_mode = dab_mode = 1
        self.cp_length__ = cp_length__ = [504, 126, 63, 252]
        self.cp_gap__ = cp_gap__ = [252, 63, 31, 124]

        ##################################################
        # Blocks
        ##################################################

        self.rtlsdr_source_0 = osmosdr.source(
            args="numchan=" + str(1) + " " + ''
        )
        self.rtlsdr_source_0.set_time_unknown_pps(osmosdr.time_spec_t())
        self.rtlsdr_source_0.set_sample_rate(samp_rate)
        self.rtlsdr_source_0.set_center_freq(206.35e6, 0)
        self.rtlsdr_source_0.set_freq_corr(68, 0)
        self.rtlsdr_source_0.set_dc_offset_mode(0, 0)
        self.rtlsdr_source_0.set_iq_balance_mode(0, 0)
        self.rtlsdr_source_0.set_gain_mode(False, 0)
        self.rtlsdr_source_0.set_gain(30, 0)
        self.rtlsdr_source_0.set_if_gain(20, 0)
        self.rtlsdr_source_0.set_bb_gain(20, 0)
        self.rtlsdr_source_0.set_antenna('', 0)
        self.rtlsdr_source_0.set_bandwidth(0, 0)
        self.qtgui_time_sink_x_0 = qtgui.time_sink_c(
            1024, #size
            1200000, #samp_rate
            "I/Q Display", #name
            1, #number of inputs
            None # parent
        )
        self.qtgui_time_sink_x_0.set_update_time(0.10)
        self.qtgui_time_sink_x_0.set_y_axis(-1, 1)

        self.qtgui_time_sink_x_0.set_y_label('Amplitude', "")

        self.qtgui_time_sink_x_0.enable_tags(True)
        self.qtgui_time_sink_x_0.set_trigger_mode(qtgui.TRIG_MODE_NORM, qtgui.TRIG_SLOPE_POS, 0.0, 0, 0, "")
        self.qtgui_time_sink_x_0.enable_autoscale(False)
        self.qtgui_time_sink_x_0.enable_grid(False)
        self.qtgui_time_sink_x_0.enable_axis_labels(True)
        self.qtgui_time_sink_x_0.enable_control_panel(False)
        self.qtgui_time_sink_x_0.enable_stem_plot(False)


        labels = ['I/Q', 'Signal 2', 'Signal 3', 'Signal 4', 'Signal 5',
            'Signal 6', 'Signal 7', 'Signal 8', 'Signal 9', 'Signal 10']
        widths = [1, 1, 1, 1, 1,
            1, 1, 1, 1, 1]
        colors = ['blue', 'red', 'green', 'black', 'cyan',
            'magenta', 'yellow', 'dark red', 'dark green', 'dark blue']
        alphas = [1.0, 1.0, 1.0, 1.0, 1.0,
            1.0, 1.0, 1.0, 1.0, 1.0]
        styles = [1, 1, 1, 1, 1,
            1, 1, 1, 1, 1]
        markers = [-1, -1, -1, -1, -1,
            -1, -1, -1, -1, -1]


        for i in range(2):
            if len(labels[i]) == 0:
                if (i % 2 == 0):
                    self.qtgui_time_sink_x_0.set_line_label(i, "Re{{Data {0}}}".format(i/2))
                else:
                    self.qtgui_time_sink_x_0.set_line_label(i, "Im{{Data {0}}}".format(i/2))
            else:
                self.qtgui_time_sink_x_0.set_line_label(i, labels[i])
            self.qtgui_time_sink_x_0.set_line_width(i, widths[i])
            self.qtgui_time_sink_x_0.set_line_color(i, colors[i])
            self.qtgui_time_sink_x_0.set_line_style(i, styles[i])
            self.qtgui_time_sink_x_0.set_line_marker(i, markers[i])
            self.qtgui_time_sink_x_0.set_line_alpha(i, alphas[i])

        self._qtgui_time_sink_x_0_win = sip.wrapinstance(self.qtgui_time_sink_x_0.qwidget(), Qt.QWidget)
        self.top_layout.addWidget(self._qtgui_time_sink_x_0_win)
        self.qtgui_freq_sink_x_0 = qtgui.freq_sink_c(
            1024, #size
            window.WIN_BLACKMAN_hARRIS, #wintype
            0, #fc
            samp_rate, #bw
            "Input Spectrum", #name
            1,
            None # parent
        )
        self.qtgui_freq_sink_x_0.set_update_time(0.10)
        self.qtgui_freq_sink_x_0.set_y_axis((-140), 10)
        self.qtgui_freq_sink_x_0.set_y_label('Relative Gain', 'dB')
        self.qtgui_freq_sink_x_0.set_trigger_mode(qtgui.TRIG_MODE_FREE, 0.0, 0, "")
        self.qtgui_freq_sink_x_0.enable_autoscale(False)
        self.qtgui_freq_sink_x_0.enable_grid(False)
        self.qtgui_freq_sink_x_0.set_fft_average(1.0)
        self.qtgui_freq_sink_x_0.enable_axis_labels(True)
        self.qtgui_freq_sink_x_0.enable_control_panel(False)
        self.qtgui_freq_sink_x_0.set_fft_window_normalized(False)



        labels = ['', '', '', '', '',
            '', '', '', '', '']
        widths = [1, 1, 1, 1, 1,
            1, 1, 1, 1, 1]
        colors = ["blue", "red", "green", "black", "cyan",
            "magenta", "yellow", "dark red", "dark green", "dark blue"]
        alphas = [1.0, 1.0, 1.0, 1.0, 1.0,
            1.0, 1.0, 1.0, 1.0, 1.0]

        for i in range(1):
            if len(labels[i]) == 0:
                self.qtgui_freq_sink_x_0.set_line_label(i, "Data {0}".format(i))
            else:
                self.qtgui_freq_sink_x_0.set_line_label(i, labels[i])
            self.qtgui_freq_sink_x_0.set_line_width(i, widths[i])
            self.qtgui_freq_sink_x_0.set_line_color(i, colors[i])
            self.qtgui_freq_sink_x_0.set_line_alpha(i, alphas[i])

        self._qtgui_freq_sink_x_0_win = sip.wrapinstance(self.qtgui_freq_sink_x_0.qwidget(), Qt.QWidget)
        self.top_layout.addWidget(self._qtgui_freq_sink_x_0_win)
        self.fft_vxx_0 = fft.fft_vcc((fft_length__[dab_mode-1]), True, [], True, 4)
        self.dab_ofdm_sampler_0 = dab.ofdm_sampler((fft_length__[dab_mode-1]), (cp_length__[dab_mode-1]), (symbols_per_frame__[dab_mode-1]), (cp_gap__[dab_mode-1]))
        self.dab_ofdm_remove_first_symbol_vcc_0 = dab.ofdm_remove_first_symbol_vcc((num_carriers__[dab_mode-1]))
        self.dab_ofdm_ffe_all_in_one_0 = dab.ofdm_ffe_all_in_one((fft_length__[dab_mode-1]+cp_length__[dab_mode-1]), (fft_length__[dab_mode-1]), (symbols_for_ffs_estimation__[dab_mode-1]), 0.5, samp_rate)
        self.dab_ofdm_coarse_frequency_correct_0 = dab.ofdm_coarse_frequency_correct((fft_length__[dab_mode-1]), (num_carriers__[dab_mode-1]), (cp_length__[dab_mode-1]))
        self.dab_moving_sum_ff_0 = dab.moving_sum_ff((ns_length__[dab_mode-1]))
        self.dab_diff_phasor_vcc_0 = dab.diff_phasor_vcc((num_carriers__[dab_mode-1]))
        self.dab_control_stream_to_tag_cc_0 = dab.control_stream_to_tag_cc("dab_sync", 1)
        self.blocks_vector_to_stream_0 = blocks.vector_to_stream(gr.sizeof_gr_complex*1, 1536)
        self.blocks_peak_detector_xb_0_0 = blocks.peak_detector_fb(0.6, 0.7, 10, 0.0001)
        self.blocks_multiply_xx_0 = blocks.multiply_vcc(1)
        self.blocks_multiply_const_vxx_0 = blocks.multiply_const_ff((-1))
        self.blocks_delay_0 = blocks.delay(gr.sizeof_gr_complex*1, ((fft_length__[dab_mode-1]+cp_length__[dab_mode-1])*symbols_for_ffs_estimation__[dab_mode-1]))
        self.blocks_delay_0.set_min_output_buffer(4096)
        self.blocks_complex_to_mag_squared_0 = blocks.complex_to_mag_squared(1)
        self.analog_frequency_modulator_fc_0 = analog.frequency_modulator_fc(1)


        ##################################################
        # Connections
        ##################################################
        self.connect((self.analog_frequency_modulator_fc_0, 0), (self.blocks_multiply_xx_0, 0))
        self.connect((self.blocks_complex_to_mag_squared_0, 0), (self.dab_moving_sum_ff_0, 0))
        self.connect((self.blocks_delay_0, 0), (self.blocks_multiply_xx_0, 1))
        self.connect((self.blocks_multiply_const_vxx_0, 0), (self.blocks_peak_detector_xb_0_0, 0))
        self.connect((self.blocks_multiply_xx_0, 0), (self.dab_ofdm_sampler_0, 0))
        self.connect((self.blocks_peak_detector_xb_0_0, 0), (self.dab_control_stream_to_tag_cc_0, 1))
        self.connect((self.blocks_vector_to_stream_0, 0), (self.qtgui_time_sink_x_0, 0))
        self.connect((self.dab_control_stream_to_tag_cc_0, 0), (self.blocks_delay_0, 0))
        self.connect((self.dab_control_stream_to_tag_cc_0, 0), (self.dab_ofdm_ffe_all_in_one_0, 0))
        self.connect((self.dab_diff_phasor_vcc_0, 0), (self.dab_ofdm_remove_first_symbol_vcc_0, 0))
        self.connect((self.dab_moving_sum_ff_0, 0), (self.blocks_multiply_const_vxx_0, 0))
        self.connect((self.dab_ofdm_coarse_frequency_correct_0, 0), (self.dab_diff_phasor_vcc_0, 0))
        self.connect((self.dab_ofdm_ffe_all_in_one_0, 0), (self.analog_frequency_modulator_fc_0, 0))
        self.connect((self.dab_ofdm_remove_first_symbol_vcc_0, 0), (self.blocks_vector_to_stream_0, 0))
        self.connect((self.dab_ofdm_sampler_0, 0), (self.fft_vxx_0, 0))
        self.connect((self.fft_vxx_0, 0), (self.dab_ofdm_coarse_frequency_correct_0, 0))
        self.connect((self.rtlsdr_source_0, 0), (self.blocks_complex_to_mag_squared_0, 0))
        self.connect((self.rtlsdr_source_0, 0), (self.dab_control_stream_to_tag_cc_0, 0))
        self.connect((self.rtlsdr_source_0, 0), (self.qtgui_freq_sink_x_0, 0))


    def closeEvent(self, event):
        self.settings = Qt.QSettings("GNU Radio", "dab_whole_graph")
        self.settings.setValue("geometry", self.saveGeometry())
        self.stop()
        self.wait()

        event.accept()

    def get_symbols_per_frame__(self):
        return self.symbols_per_frame__

    def set_symbols_per_frame__(self, symbols_per_frame__):
        self.symbols_per_frame__ = symbols_per_frame__

    def get_symbols_for_magnitude_equalization__(self):
        return self.symbols_for_magnitude_equalization__

    def set_symbols_for_magnitude_equalization__(self, symbols_for_magnitude_equalization__):
        self.symbols_for_magnitude_equalization__ = symbols_for_magnitude_equalization__

    def get_symbols_for_ffs_estimation__(self):
        return self.symbols_for_ffs_estimation__

    def set_symbols_for_ffs_estimation__(self, symbols_for_ffs_estimation__):
        self.symbols_for_ffs_estimation__ = symbols_for_ffs_estimation__
        self.blocks_delay_0.set_dly(int(((self.fft_length__[self.dab_mode-1]+self.cp_length__[self.dab_mode-1])*self.symbols_for_ffs_estimation__[self.dab_mode-1])))

    def get_symbol_length__(self):
        return self.symbol_length__

    def set_symbol_length__(self, symbol_length__):
        self.symbol_length__ = symbol_length__

    def get_samp_rate(self):
        return self.samp_rate

    def set_samp_rate(self, samp_rate):
        self.samp_rate = samp_rate
        self.qtgui_freq_sink_x_0.set_frequency_range(0, self.samp_rate)
        self.rtlsdr_source_0.set_sample_rate(self.samp_rate)

    def get_num_carriers__(self):
        return self.num_carriers__

    def set_num_carriers__(self, num_carriers__):
        self.num_carriers__ = num_carriers__

    def get_ns_length__(self):
        return self.ns_length__

    def set_ns_length__(self, ns_length__):
        self.ns_length__ = ns_length__

    def get_frame_length__(self):
        return self.frame_length__

    def set_frame_length__(self, frame_length__):
        self.frame_length__ = frame_length__

    def get_fft_length__(self):
        return self.fft_length__

    def set_fft_length__(self, fft_length__):
        self.fft_length__ = fft_length__
        self.blocks_delay_0.set_dly(int(((self.fft_length__[self.dab_mode-1]+self.cp_length__[self.dab_mode-1])*self.symbols_for_ffs_estimation__[self.dab_mode-1])))

    def get_dab_mode(self):
        return self.dab_mode

    def set_dab_mode(self, dab_mode):
        self.dab_mode = dab_mode
        self.blocks_delay_0.set_dly(int(((self.fft_length__[self.dab_mode-1]+self.cp_length__[self.dab_mode-1])*self.symbols_for_ffs_estimation__[self.dab_mode-1])))

    def get_cp_length__(self):
        return self.cp_length__

    def set_cp_length__(self, cp_length__):
        self.cp_length__ = cp_length__
        self.blocks_delay_0.set_dly(int(((self.fft_length__[self.dab_mode-1]+self.cp_length__[self.dab_mode-1])*self.symbols_for_ffs_estimation__[self.dab_mode-1])))

    def get_cp_gap__(self):
        return self.cp_gap__

    def set_cp_gap__(self, cp_gap__):
        self.cp_gap__ = cp_gap__




def main(top_block_cls=dab_whole_graph, options=None):

    qapp = Qt.QApplication(sys.argv)

    tb = top_block_cls()

    tb.start()

    tb.show()

    def sig_handler(sig=None, frame=None):
        tb.stop()
        tb.wait()

        Qt.QApplication.quit()

    signal.signal(signal.SIGINT, sig_handler)
    signal.signal(signal.SIGTERM, sig_handler)

    timer = Qt.QTimer()
    timer.start(500)
    timer.timeout.connect(lambda: None)

    qapp.exec_()

if __name__ == '__main__':
    main()
