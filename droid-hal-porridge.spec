# These and other macros are documented in dhd/droid-hal-device.inc

%define device porridge
%define vendor wileyfox

%define vendor_pretty Wileyfox
%define device_pretty Spark

%define installable_zip 1

#For OTA
%define enable_kernel_update 1

%include rpm/dhd/droid-hal-device.inc
