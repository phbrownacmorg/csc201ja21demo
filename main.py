# Repl to run CSC201 demos in
# Peter Brown <peter.brown@converse.edu>, 2020-01-12

from typing import List

import bmi
import button
import chaos
import chaos_clamped
import chaos_except
import chaos_files
import chaos_format
import chaos_if
import chasethemouse
import chasethemouse_fns
import color_entry
import covid_graph
import covid_graph_coords
import CtoF
import CtoF_entry
import CtoF_fns
import drawline
import draw_triangle
import fact
import fact_fns
import formatdemo
import futureval
import futureval_clamped
import futureval_fns
import futureval_while
import graphicsdemo
import idmaker
import idmaker_files
import lab16
import leapyear
import loop_patterns
import old_macdonald
import old_macdonald_fns
import pounds_to_stone
import quadratic
import quadratic_fns
import rangedemo
import sumlist
import sumlist_fns
import stringdemo
import userdict
import validdate

def main(args:List[str]) -> int:
    return draw_triangle.main(args)

if __name__ == '__main__':
    import sys
    main(sys.argv)