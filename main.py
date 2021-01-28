# Repl to run CSC201 demos in
# Peter Brown <peter.brown@converse.edu>, 2020-01-12

from typing import List

import bmi
import button
import chaos
import chaos_clamped
import chaos_files
import chaos_format
import chasethemouse
import chasethemouse_fns
import color_entry
import covid_graph
import covid_graph_coords
import CtoF
import CtoF_entry
import CtoF_fns
import drawline
import formatdemo
import graphicsdemo
import fact
import fact_fns
import futureval
import futureval_clamped
import futureval_fns
import idmaker
import idmaker_files
import leapyear
import old_macdonald
import old_macdonald_fns
import pounds_to_stone
import quadratic
import quadratic_fns
import rangedemo
import sumlist
import sumlist_fns
import stringdemo
import validdate

def main(args:List[str]) -> int:
    return validdate.main(args)

if __name__ == '__main__':
    import sys
    main(sys.argv)