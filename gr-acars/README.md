# Adding support for libacars

## Compile libacars

``libacars`` is cloned as a submodule of gr-acars from https://github.com/szpajder/libacars/
but must be compiled and installed manually if it is to be used:

```
cd libacars
mkdir build
cd build
cmake ../
make
sudo make install
```

Since the default installation directory is ``/usr/local/lib``, an execution error when
running gr-acars using libacars might be solved by ``export LD_LIBRARY_PATH=/usr/local/lib``
prior to launching the GNU Radio Python script.

## Activate libacars support

Edit ``lib/CMakeLists.txt`` and uncomment

```
target_link_libraries(gnuradio-acars gnuradio::gnuradio-runtime gnuradio::gnuradio-fft acars-2)
```
and comment the next line
```
target_link_libraries(gnuradio-acars gnuradio::gnuradio-runtime gnuradio::gnuradio-fft)
```

Edit ``lib/acars_impl.cc`` and uncomment
```
#define LIBACARS
```

An example of result including ADS-C decoding by libacars-2:
```
Sat Aug 23 16:56:12 2025

2b 2a 16 16 01 32 2e 47 2d 53 54 42 44 15 42 36 32 
00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 
+*2.G-STBDB62F13ABA0127/QUKAXBA.ADS.G-STBD07224CA02017088BB4A51DD475&.?

Aircraft=.G-STBD
STX
Seq. No=46 31 33 41 F13A
Flight=BA0127
/QUKAXBA.ADS.G-STBD07224CA02017088BB4A51DD475ETX
label: B6
message: /QUKAXBA.ADS.G-STBD07224CA02017088BB4A51DD475 &.?5
Sublabel:  MFI: 
Decoded message:
ADS-C message:
 Basic report:
  Lat: 48.2334137
  Lon: 5.6407928
  Alt: 35000 ft
  Time: 3369.250 sec past hour (:56:09.250)
  Position accuracy: <0.25 nm
  NAV unit redundancy: OK
  TCAS: OK
```
