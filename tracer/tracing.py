import os, sys, hunter

from .code-coverage_testing.input_code_files.input_data import input_data

hunter.trace(module= input_data, action=hunter.CallPrinter)